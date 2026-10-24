-- =============================================================================
--  mudanca_mascara v2 — rótulos de cobertura e de mudança para treino de IA
--  SQL plain · PostgreSQL 18 + PostGIS 3 · SRID único do projeto: 32723
--
--  Criar (banco vazio):
--    createdb -U postgres mudanca_mascara
--    psql -U postgres -d mudanca_mascara -f db/mudanca_mascara.sql
--
--  Esquemas
--    dominio    vocabulários controlados, taxonomia de classes e de alterações
--    catalogo   sensores, grades, produtos, imagens (com QC) e AOI; rasters ficam fora
--    rotulo     máscaras de cobertura (tarefa → sessão → anotação), séries temporais,
--               eventos de mudança, controles estáveis, amostragem e proveniência
--    treino     divisão espaço-temporal, datasets congelados, entrada da máscara raster
--    auditoria  histórico de alterações e utilitários
--
--  Duas referências complementares (docs/banco_mascara.md):
--    1. Cobertura por data: tarefa (recorte de UMA imagem) particionada em anotações.
--       Em série, a sessão é propagada para o mês seguinte e só o que mudou é editado.
--    2. Mudança: evento com tipo, de→para, estágio e mês de início, desenhado olhando a
--       série; controles estáveis medem falso alarme e deriva de cor.
--
--  Convenções: tabelas no singular; PK "id" identity; FK "<entidade>_id"; prefixos
--  vw_ (visão), fn_ (função), tg_ (gatilho), ix_ (índice), ck_/uq_/fk_ (restrições).
--  Testes: db/testes.sql
-- =============================================================================

\set ON_ERROR_STOP on
SET client_encoding = 'UTF8';
SET client_min_messages = warning;

BEGIN;

CREATE EXTENSION IF NOT EXISTS postgis;

CREATE SCHEMA dominio;
CREATE SCHEMA catalogo;
CREATE SCHEMA rotulo;
CREATE SCHEMA treino;
CREATE SCHEMA auditoria;

COMMENT ON SCHEMA dominio   IS 'Vocabulários controlados, taxonomia de classes e de alterações';
COMMENT ON SCHEMA catalogo  IS 'Sensores, grades, produtos, imagens com QC e AOI. Os rasters ficam fora do banco';
COMMENT ON SCHEMA rotulo    IS 'Cobertura por data, séries, eventos de mudança, controles estáveis, amostragem e proveniência';
COMMENT ON SCHEMA treino    IS 'Divisão espaço-temporal, datasets congelados e entrada da máscara raster';
COMMENT ON SCHEMA auditoria IS 'Histórico de alterações e funções utilitárias';


-- =============================================================================
-- AUDITORIA E UTILITÁRIOS
-- =============================================================================

CREATE TABLE auditoria.registro (
    id           bigint GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_registro PRIMARY KEY,
    momento      timestamptz NOT NULL DEFAULT clock_timestamp(),
    usuario      text        NOT NULL,
    tabela       text        NOT NULL,
    operacao     text        NOT NULL CONSTRAINT ck_registro_operacao CHECK (operacao IN ('INSERT', 'UPDATE', 'DELETE')),
    registro_id  text,
    antes        jsonb,
    depois       jsonb
);
COMMENT ON TABLE  auditoria.registro IS 'Uma linha por alteração nas tabelas auditadas';
COMMENT ON COLUMN auditoria.registro.usuario IS 'app.usuario da sessão, se definido; senão, o usuário do banco';
CREATE INDEX ix_registro_tabela_id ON auditoria.registro (tabela, registro_id);
CREATE INDEX ix_registro_momento   ON auditoria.registro (momento);

-- Quem está operando: SET app.usuario = 'apelido' ou o login do banco.
CREATE FUNCTION auditoria.fn_usuario() RETURNS text
LANGUAGE sql STABLE AS $$
    SELECT coalesce(nullif(current_setting('app.usuario', true), ''), current_user::text)
$$;

CREATE FUNCTION auditoria.fn_registrar() RETURNS trigger
LANGUAGE plpgsql AS $$
DECLARE
    v_antes  jsonb := CASE WHEN TG_OP <> 'INSERT' THEN to_jsonb(OLD) END;
    v_depois jsonb := CASE WHEN TG_OP <> 'DELETE' THEN to_jsonb(NEW) END;
BEGIN
    IF TG_OP = 'UPDATE' AND v_antes = v_depois THEN
        RETURN NULL;
    END IF;
    INSERT INTO auditoria.registro (usuario, tabela, operacao, registro_id, antes, depois)
    VALUES (auditoria.fn_usuario(), TG_TABLE_SCHEMA || '.' || TG_TABLE_NAME, TG_OP,
            coalesce(v_depois ->> 'id', v_antes ->> 'id'), v_antes, v_depois);
    RETURN NULL;
END $$;

CREATE FUNCTION auditoria.fn_tocar_atualizado_em() RETURNS trigger
LANGUAGE plpgsql AS $$
BEGIN
    NEW.atualizado_em := now();
    RETURN NEW;
END $$;

-- Polígono limpo para máscara: válido, só partes de área, MultiPolygon.
CREATE FUNCTION auditoria.fn_multipoligono(p geometry) RETURNS geometry
LANGUAGE sql IMMUTABLE STRICT PARALLEL SAFE AS $$
    SELECT ST_Multi(ST_CollectionExtract(ST_MakeValid(p), 3))
$$;

-- Diferença em meses entre duas datas (b - a).
CREATE FUNCTION auditoria.fn_meses(a date, b date) RETURNS integer
LANGUAGE sql IMMUTABLE STRICT PARALLEL SAFE AS $$
    SELECT ((extract(year FROM b) - extract(year FROM a)) * 12 + extract(month FROM b) - extract(month FROM a))::int
$$;


-- =============================================================================
-- DOMÍNIO
-- =============================================================================

-- Tabelas de código simples: (codigo, nome, descricao, ordem).
CREATE TABLE dominio.status_sessao (
    codigo text PRIMARY KEY, nome text NOT NULL, descricao text, ordem smallint NOT NULL);
COMMENT ON TABLE dominio.status_sessao IS 'Estados da sessão de rotulagem; transições impostas por rotulo.tg_sessao_estado';
INSERT INTO dominio.status_sessao VALUES
    ('em_andamento', 'Em andamento', 'rotulador desenhando; única fase em que anotações podem mudar', 1),
    ('enviada',      'Enviada',      'rotulador terminou; tarefa sem lacunas; aguarda revisão',        2),
    ('aprovada',     'Aprovada',     'revisada e aceita; é a referência da tarefa',                    3),
    ('rejeitada',    'Rejeitada',    'revisada e recusada; pode ser reaberta',                         4);

CREATE TABLE dominio.status_revisao (
    codigo text PRIMARY KEY, nome text NOT NULL, descricao text, ordem smallint NOT NULL);
COMMENT ON TABLE dominio.status_revisao IS 'Revisão de eventos e controles (mesmo domínio de status_revisao em configs/esquema_vetor.yaml)';
INSERT INTO dominio.status_revisao VALUES
    ('nao_revisado', 'Não revisado', 'registrado pelo intérprete, sem revisão', 1),
    ('confirmado',   'Confirmado',   'revisor concorda; entra em dataset',       2),
    ('rejeitado',    'Rejeitado',    'revisor discorda; fica fora de tudo',      3);

CREATE TABLE dominio.papel_conjunto (
    codigo text PRIMARY KEY, nome text NOT NULL, descricao text, ordem smallint NOT NULL,
    regime text NOT NULL CONSTRAINT ck_papel_regime CHECK (regime IN ('ajuste', 'shift_espacial', 'shift_temporal', 'shift_espaco_tempo')),
    usa_no_ajuste boolean NOT NULL);
COMMENT ON TABLE  dominio.papel_conjunto IS 'Conjunto de uso. Os três testes medem os regimes de Vincent 2024 (espacial, temporal e ambos)';
COMMENT ON COLUMN dominio.papel_conjunto.ordem IS 'Na folga entre blocos, o conjunto de ordem menor cede a área (o teste nunca perde área)';
INSERT INTO dominio.papel_conjunto VALUES
    ('treino',             'Treino',                  'ajuste dos pesos',                                          1, 'ajuste',             true),
    ('validacao',          'Validação',               'hiperparâmetros, limiar e parada antecipada',               2, 'ajuste',             true),
    ('teste',              'Teste espacial',          'blocos de teste, período anterior à reserva temporal',      3, 'shift_espacial',     false),
    ('teste_temporal',     'Teste temporal',          'blocos de treino/validação no período reservado',           4, 'shift_temporal',     false),
    ('teste_espaco_tempo', 'Teste espaço-temporal',   'blocos de teste no período reservado',                      5, 'shift_espaco_tempo', false);

CREATE TABLE dominio.origem_anotacao (codigo text PRIMARY KEY, nome text NOT NULL, descricao text);
INSERT INTO dominio.origem_anotacao VALUES
    ('manual',            'Manual',               'desenhada por uma pessoa'),
    ('pre_rotulo_modelo', 'Pré-rótulo',           'gerada por ferramenta ou modelo (exige processamento) e conferida por uma pessoa'),
    ('propagada',         'Propagada',            'copiada da sessão da data anterior da mesma série'),
    ('importado',         'Importado',            'trazida de base externa');

CREATE TABLE dominio.nivel_certeza (
    codigo text PRIMARY KEY, nome text NOT NULL,
    peso real NOT NULL CONSTRAINT ck_nivel_certeza_peso CHECK (peso > 0 AND peso <= 1),
    descricao text);
COMMENT ON TABLE  dominio.nivel_certeza IS 'Certeza do intérprete. Equivale a certa / provavel / duvidosa da skill rotulagem-referencia';
COMMENT ON COLUMN dominio.nivel_certeza.peso IS 'Peso sugerido para a perda por pixel no treino';
INSERT INTO dominio.nivel_certeza VALUES
    ('alta',  'Alta (certa)',      1.0, 'evidente na imagem'),
    ('media', 'Média (provável)',  0.7, 'provável; conferida em imagem de apoio ou contexto'),
    ('baixa', 'Baixa (duvidosa)',  0.4, 'incerta; candidata a revisão ou a "indeterminado"');

CREATE TABLE dominio.funcao_pessoa (codigo text PRIMARY KEY, nome text NOT NULL);
INSERT INTO dominio.funcao_pessoa VALUES ('rotulador', 'Rotulador'), ('revisor', 'Revisor'), ('curador', 'Curador');

CREATE TABLE dominio.status_qc (codigo text PRIMARY KEY, nome text NOT NULL, descricao text, aceita_rotulo boolean NOT NULL);
COMMENT ON TABLE dominio.status_qc IS 'Resultado do QC da imagem (skill inventario-dados)';
INSERT INTO dominio.status_qc VALUES
    ('pendente',  'Pendente',  'QC ainda não rodou',                                   true),
    ('aprovada',  'Aprovada',  'grade, alfa e radiometria conferidos',                 true),
    ('restrita',  'Restrita',  'usável com ressalvas (nuvem parcial, deslocamento)',   true),
    ('reprovada', 'Reprovada', 'fora da grade, corrompida ou sem observação útil',     false);

CREATE TABLE dominio.regime_processamento (codigo text PRIMARY KEY, nome text NOT NULL, descricao text);
COMMENT ON TABLE dominio.regime_processamento IS 'Regime de processamento do produto. A Planet mudou nitidez e super-resolução em 2022 (Glazer 2025, p. 2–3); o mês exato vem do QC de nitidez';
INSERT INTO dominio.regime_processamento VALUES
    ('planet_antes_mudanca_2022',  'Planet antes da mudança de 2022',  'antes do salto de nitidez detectado no QC'),
    ('planet_depois_mudanca_2022', 'Planet depois da mudança de 2022', 'depois do salto de nitidez detectado no QC'),
    ('nao_se_aplica',              'Não se aplica',                    'produto sem esse regime (CBERS, cena única)');

CREATE TABLE dominio.modo_selecao (
    codigo text PRIMARY KEY, nome text NOT NULL, descricao text, probabilistico boolean NOT NULL);
COMMENT ON TABLE dominio.modo_selecao IS 'Como a tarefa foi escolhida. Só modos probabilísticos sustentam estimativa de área com IC (Olofsson 2014)';
INSERT INTO dominio.modo_selecao VALUES
    ('conveniencia',       'Conveniência',         'escolhida pelo rotulador (locais conhecidos, exemplos)',     false),
    ('sistematica_bloco',  'Sistemática por bloco','um recorte por bloco da divisão',                            false),
    ('aleatoria',          'Aleatória simples',    'sorteio com probabilidade conhecida',                        true),
    ('estratificada',      'Estratificada',        'sorteio dentro de um estrato com probabilidade conhecida',   true),
    ('aprendizado_ativo',  'Aprendizado ativo',    'escolhida pela incerteza de um modelo (ciclo registrado)',   false);

CREATE TABLE dominio.condicao_rotulagem (codigo text PRIMARY KEY, nome text NOT NULL, descricao text);
COMMENT ON TABLE dominio.condicao_rotulagem IS 'Condição da sessão, para medir o ganho de tempo da pré-anotação (EXP6)';
INSERT INTO dominio.condicao_rotulagem VALUES
    ('manual',              'Manual',                 'desenho do zero no QGIS'),
    ('pre_anotacao_sam',    'Pré-anotação SamGeo',    'parte de máscaras do SamGeo/GeoAI'),
    ('pre_anotacao_geosam', 'Pré-anotação Geo-SAM',   'parte de máscaras do Geo-SAM pré-codificado'),
    ('pre_anotacao_modelo', 'Pré-anotação de modelo', 'parte da previsão de um modelo do pipeline'),
    ('propagada',           'Propagada',              'parte da sessão aprovada da data anterior da série');

CREATE TABLE dominio.ferramenta (codigo text PRIMARY KEY, nome text NOT NULL, licenca text);
INSERT INTO dominio.ferramenta VALUES
    ('samgeo',          'SamGeo / GeoAI',            'MIT'),
    ('geo_sam',         'Geo-SAM',                   'MIT'),
    ('deepness',        'Deepness (ONNX)',           NULL),
    ('iamap',           'IAMAP',                     'GPL-3.0'),
    ('k_textures',      'k-textures',                NULL),
    ('pipeline_mudanca','Pipeline src/mudanca',      NULL),
    ('outra',           'Outra',                     NULL);

CREATE TABLE dominio.estagio (codigo text PRIMARY KEY, nome text NOT NULL, descricao text, ordem smallint NOT NULL);
INSERT INTO dominio.estagio VALUES
    ('novo',         'Novo',          'primeira detecção do evento',             1),
    ('em_expansao',  'Em expansão',   'evento existente que cresceu',            2),
    ('consolidado',  'Consolidado',   'evento completo e estável',               3),
    ('revertido',    'Revertido',     'rebrota, demolição ou reversão',          4);

CREATE TABLE dominio.papel_evidencia (codigo text PRIMARY KEY, nome text NOT NULL, descricao text);
INSERT INTO dominio.papel_evidencia VALUES
    ('antes',       'Antes',       'última imagem sem a mudança'),
    ('inicio',      'Início',      'primeira imagem com a mudança visível'),
    ('completo',    'Completo',    'imagem em que o evento está completo'),
    ('confirmacao', 'Confirmação', 'imagem independente que confirma (ex.: CBERS 2 m)');

CREATE TABLE dominio.tipo_superficie_estavel (codigo text PRIMARY KEY, nome text NOT NULL, descricao text);
INSERT INTO dominio.tipo_superficie_estavel VALUES
    ('telhado_antigo',  'Telhado antigo',  'edificação presente em toda a série'),
    ('asfalto',         'Asfalto',         'via pavimentada presente em toda a série'),
    ('mata_fechada',    'Mata fechada',    'dossel contínuo sem alteração'),
    ('agua',            'Água',            'superfície d''água permanente'),
    ('solo_compactado', 'Solo compactado', 'solo exposto sem alteração'),
    ('outra',           'Outra',           'descrever na observação');

-- Taxonomia de cobertura --------------------------------------------------------

CREATE TABLE dominio.taxonomia (
    id                  integer GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_taxonomia PRIMARY KEY,
    codigo              text     NOT NULL,
    versao              smallint NOT NULL CONSTRAINT ck_taxonomia_versao CHECK (versao > 0),
    nome                text     NOT NULL,
    descricao           text,
    valor_nao_rotulado  smallint NOT NULL DEFAULT 0 CONSTRAINT ck_taxonomia_nao_rotulado CHECK (valor_nao_rotulado BETWEEN 0 AND 255),
    vigente             boolean  NOT NULL DEFAULT false,
    criada_em           timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT uq_taxonomia_codigo_versao UNIQUE (codigo, versao)
);
COMMENT ON TABLE  dominio.taxonomia IS 'Conjunto versionado de classes. Mudou classe ou valor de pixel → nova versão';
COMMENT ON COLUMN dominio.taxonomia.valor_nao_rotulado IS 'Pixel fora das tarefas, sem dado (alfa 0) ou fora da AOI: ignorado no treino';
CREATE UNIQUE INDEX uq_taxonomia_vigente ON dominio.taxonomia (codigo) WHERE vigente;

CREATE TABLE dominio.classe (
    id                  integer GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_classe PRIMARY KEY,
    taxonomia_id        integer  NOT NULL,
    codigo              text     NOT NULL CONSTRAINT ck_classe_codigo CHECK (codigo ~ '^[a-z][a-z0-9_]*$'),
    nome                text     NOT NULL,
    classe_pai_id       integer,
    nivel               smallint NOT NULL CONSTRAINT ck_classe_nivel CHECK (nivel BETWEEN 1 AND 3),
    tipo                text     NOT NULL CONSTRAINT ck_classe_tipo CHECK (tipo IN ('cobertura', 'exclusao')),
    valor_raster        smallint CONSTRAINT ck_classe_valor CHECK (valor_raster BETWEEN 1 AND 255),
    ignorar_no_treino   boolean  NOT NULL DEFAULT false,
    cor_hex             char(7)  NOT NULL CONSTRAINT ck_classe_cor CHECK (cor_hex ~ '^#[0-9A-F]{6}$'),
    ordem               smallint NOT NULL,
    descricao           text,
    criterio_rotulagem  text,
    area_minima_m2      real CONSTRAINT ck_classe_area_minima CHECK (area_minima_m2 >= 0),
    CONSTRAINT uq_classe_taxonomia_id     UNIQUE (taxonomia_id, id),
    CONSTRAINT uq_classe_taxonomia_codigo UNIQUE (taxonomia_id, codigo),
    CONSTRAINT uq_classe_taxonomia_valor  UNIQUE (taxonomia_id, valor_raster),
    CONSTRAINT fk_classe_taxonomia FOREIGN KEY (taxonomia_id) REFERENCES dominio.taxonomia (id),
    CONSTRAINT fk_classe_pai FOREIGN KEY (taxonomia_id, classe_pai_id) REFERENCES dominio.classe (taxonomia_id, id),
    CONSTRAINT ck_classe_raiz CHECK ((nivel = 1) = (classe_pai_id IS NULL)),
    CONSTRAINT ck_classe_exclusao_ignorada CHECK (tipo <> 'exclusao' OR ignorar_no_treino)
);
COMMENT ON TABLE  dominio.classe IS 'Árvore de classes por taxonomia. Só folhas (valor_raster não nulo) recebem anotação';
COMMENT ON COLUMN dominio.classe.valor_raster IS 'Valor do pixel na máscara. Nulo = classe agregadora';
COMMENT ON COLUMN dominio.classe.tipo IS 'cobertura = classe a aprender; exclusao = pixel sem informação de cobertura';
COMMENT ON COLUMN dominio.classe.ignorar_no_treino IS 'Pixel entra como ignore_index na perda e fica fora das métricas';
COMMENT ON COLUMN dominio.classe.criterio_rotulagem IS 'Regra de decisão para o rotulador (guia de anotação; proposta inicial)';
COMMENT ON COLUMN dominio.classe.area_minima_m2 IS 'Menor objeto que vale a pena desenhar; abaixo disso, absorver no entorno';
CREATE INDEX ix_classe_pai ON dominio.classe (classe_pai_id);

CREATE FUNCTION dominio.fn_validar_classe() RETURNS trigger
LANGUAGE plpgsql AS $$
DECLARE
    v_pai dominio.classe;
BEGIN
    IF NEW.classe_pai_id IS NOT NULL THEN
        SELECT * INTO v_pai FROM dominio.classe WHERE id = NEW.classe_pai_id;
        IF NEW.nivel <> v_pai.nivel + 1 THEN
            RAISE EXCEPTION 'Classe %: nível % incompatível com o pai % (nível %)', NEW.codigo, NEW.nivel, v_pai.codigo, v_pai.nivel;
        END IF;
        IF NEW.tipo <> v_pai.tipo THEN
            RAISE EXCEPTION 'Classe %: tipo % diferente do pai % (%)', NEW.codigo, NEW.tipo, v_pai.codigo, v_pai.tipo;
        END IF;
        IF v_pai.valor_raster IS NOT NULL THEN
            RAISE EXCEPTION 'Classe %: o pai % é folha (tem valor_raster) e não pode ter filhas', NEW.codigo, v_pai.codigo;
        END IF;
    END IF;
    RETURN NEW;
END $$;
CREATE TRIGGER tg_classe_validar BEFORE INSERT OR UPDATE ON dominio.classe
    FOR EACH ROW EXECUTE FUNCTION dominio.fn_validar_classe();

INSERT INTO dominio.taxonomia (codigo, versao, nome, descricao, vigente) VALUES
    ('cobertura', 1, 'Cobertura terrestre v1',
     'Classes de cobertura para a AOI Jardim Interlagos com Planet ~4,5 m RGB. Enxuta de propósito (lacuna L10).', true);

WITH t AS (SELECT id FROM dominio.taxonomia WHERE codigo = 'cobertura' AND versao = 1)
INSERT INTO dominio.classe (taxonomia_id, codigo, nome, nivel, tipo, ignorar_no_treino, cor_hex, ordem, descricao)
SELECT t.id, v.codigo, v.nome, 1, v.tipo, v.tipo = 'exclusao', v.cor, v.ordem, v.descricao
  FROM t, (VALUES
    ('vegetacao',    'Vegetação',          'cobertura', '#2E7D32', 10, 'cobertura vegetal viva'),
    ('construido',   'Construído',         'cobertura', '#C62828', 20, 'estruturas e edificações'),
    ('viario',       'Sistema viário',     'cobertura', '#616161', 30, 'ruas, estradas e caminhos'),
    ('solo',         'Solo',               'cobertura', '#D7A86E', 40, 'superfície sem cobertura vegetal nem construção'),
    ('hidrografia',  'Hidrografia',        'cobertura', '#1E88E5', 50, 'corpos d''água'),
    ('exclusao',     'Sem informação',     'exclusao',  '#9E9E9E', 90, 'pixels onde a cobertura não é visível ou não é confiável')
  ) AS v (codigo, nome, tipo, cor, ordem, descricao);

WITH t AS (SELECT id FROM dominio.taxonomia WHERE codigo = 'cobertura' AND versao = 1)
INSERT INTO dominio.classe (taxonomia_id, codigo, nome, classe_pai_id, nivel, tipo, valor_raster,
                            ignorar_no_treino, cor_hex, ordem, descricao, criterio_rotulagem, area_minima_m2)
SELECT t.id, v.codigo, v.nome, p.id, 2, p.tipo, v.valor, p.tipo = 'exclusao', v.cor, v.ordem, v.descricao, v.criterio, v.area_min
  FROM t
  JOIN (VALUES
    ('vegetacao_arborea',  'vegetacao',   1,   'Vegetação densa',      '#1B5E20', 11,
     'árvores, mata, restinga arbórea, mangue',
     'Dossel contínuo com textura rugosa e sombra própria. Árvore isolada só se a copa ocupa ~2×2 px ou mais; menor que isso, use a classe do entorno.', 80),
    ('vegetacao_rasteira', 'vegetacao',   2,   'Vegetação rasteira',   '#9CCC65', 12,
     'pasto, campo, gramado, vegetação baixa, brejo vegetado',
     'Verde liso, sem sombra de copa. Lote com capim entre casas é rasteira. Na dúvida entre rasteira e solo, decida pela cor dominante do polígono.', 40),
    ('edificacao',         'construido',  4,   'Construção',           '#C62828', 21,
     'telhados e estruturas fechadas',
     'Contorne o telhado inteiro. Casas coladas podem formar um polígono. Obra com laje ou telhado visível já é construção; terraplenagem sem estrutura é solo exposto.', 20),
    ('via_pavimentada',    'viario',      5,   'Rua pavimentada',      '#424242', 31,
     'asfalto, concreto, calçamento',
     'Leito cinza contínuo. Inclua calçada quando não separável. Mantenha a continuidade sob copas parciais só se o leito for visível dos dois lados.', 20),
    ('via_terra',          'viario',      6,   'Rua de terra',         '#8D6E63', 32,
     'estrada e rua de terra',
     'Faixa linear de terra com continuidade de rede. Clareira ou lote de terra sem forma de via é solo exposto.', 20),
    ('solo_exposto',       'solo',        3,   'Solo exposto',         '#D7A86E', 41,
     'terra sem cobertura, aterro, areia, movimentação de terra, canteiro de obra sem estrutura',
     'Superfície clara ou avermelhada sem vegetação nem telhado. Areia de praia e margem de lagoa seca também entram aqui.', 40),
    ('agua',               'hidrografia', 7,   'Massa d''água',        '#1E88E5', 51,
     'lagoa, canal, represa',
     'Superfície d''água aberta. Brejo com vegetação emergente é vegetação rasteira.', 40),
    ('nuvem',              'exclusao',    251, 'Nuvem',                '#FFFFFF', 91,
     'nuvem ou névoa que impede ver o solo',
     'Use só onde a cobertura não é distinguível. Névoa leve com solo visível: classifique a cobertura.', NULL),
    ('sombra',             'exclusao',    252, 'Sombra de nuvem',      '#000000', 92,
     'sombra de nuvem ou de relevo',
     'Sombra de edificação não é exclusão: faz parte da construção ou do entorno.', NULL),
    ('sem_dado',           'exclusao',    253, 'Sem dado',             '#FF00FF', 93,
     'alfa 0 no raster',
     'O pipeline queima o alfa 0 automaticamente como valor_nao_rotulado; desenhe só se o alfa falhar.', NULL),
    ('borda_mosaico',      'exclusao',    254, 'Borda de mosaico',     '#FFEB3B', 94,
     'costura entre cenas com cor ou geometria inconsistente',
     'Faixa onde a costura deforma objetos ou muda a cor abruptamente.', NULL),
    ('indeterminado',      'exclusao',    255, 'Indeterminado',        '#9E9E9E', 95,
     'o rotulador não consegue decidir',
     'Melhor que um rótulo errado: o pixel fica fora do treino e da avaliação.', NULL)
  ) AS v (codigo, pai, valor, nome, cor, ordem, descricao, criterio, area_min) ON true
  JOIN dominio.classe p ON p.taxonomia_id = t.id AND p.codigo = v.pai;

CREATE VIEW dominio.vw_classe AS
WITH RECURSIVE arvore AS (
    SELECT c.id, c.id AS raiz_id, c.codigo::text AS caminho
      FROM dominio.classe c WHERE c.classe_pai_id IS NULL
    UNION ALL
    SELECT f.id, a.raiz_id, a.caminho || ' / ' || f.codigo
      FROM dominio.classe f JOIN arvore a ON f.classe_pai_id = a.id
)
SELECT c.id, t.codigo AS taxonomia, t.versao AS taxonomia_versao, c.taxonomia_id,
       c.codigo, c.nome, c.nivel, c.tipo, c.valor_raster,
       (c.valor_raster IS NOT NULL) AS atribuivel, c.ignorar_no_treino, c.cor_hex,
       r.codigo AS macro_codigo, r.nome AS macro_nome, a.caminho,
       c.descricao, c.criterio_rotulagem, c.area_minima_m2, c.ordem
  FROM dominio.classe c
  JOIN dominio.taxonomia t ON t.id = c.taxonomia_id
  JOIN arvore a ON a.id = c.id
  JOIN dominio.classe r ON r.id = a.raiz_id
 ORDER BY t.codigo, t.versao, c.ordem;
COMMENT ON VIEW dominio.vw_classe IS 'Classes com macroclasse e caminho; atribuivel = pode receber anotação';

-- Taxonomia de alterações (configs/classes.yaml: tipo_alteracao) --------------

CREATE TABLE dominio.tipo_alteracao (
    codigo               text PRIMARY KEY,
    nome                 text     NOT NULL,
    descricao            text,
    restringe_transicao  boolean  NOT NULL DEFAULT true,
    ordem                smallint NOT NULL
);
COMMENT ON TABLE  dominio.tipo_alteracao IS 'Tipos de mudança. Com restringe_transicao, de→para precisa estar em transicao_permitida';

INSERT INTO dominio.tipo_alteracao (codigo, nome, descricao, restringe_transicao, ordem) VALUES
    ('supressao_vegetacao_arborea',  'Supressão de vegetação densa',    NULL, true,  1),
    ('supressao_vegetacao_rasteira', 'Supressão de vegetação rasteira', NULL, true,  2),
    ('inicio_construcao',            'Início de construção',
     'terraplenagem, fundação e canteiro; ainda sem telhado reconhecível; a classe final só é conhecida meses depois', true, 3),
    ('edificacao_nova',              'Edificação nova',                 NULL, true,  4),
    ('abertura_via',                 'Abertura de via',                 NULL, true,  5),
    ('ampliacao_via',                'Ampliação de via',                NULL, true,  6),
    ('solo_exposto_movimentacao',    'Solo exposto / movimentação',     NULL, true,  7),
    ('mineracao',                    'Mineração',                       'provavelmente ausente nesta AOI; mantido para outras áreas', true, 8),
    ('outra',                        'Outra',                           'descrever na observação', false, 9);

CREATE TABLE dominio.transicao_permitida (
    taxonomia_id          integer NOT NULL,
    tipo_alteracao_codigo text    NOT NULL REFERENCES dominio.tipo_alteracao (codigo),
    classe_de_id          integer NOT NULL,
    classe_para_id        integer NOT NULL,
    CONSTRAINT pk_transicao_permitida PRIMARY KEY (taxonomia_id, tipo_alteracao_codigo, classe_de_id, classe_para_id),
    CONSTRAINT fk_transicao_de   FOREIGN KEY (taxonomia_id, classe_de_id)   REFERENCES dominio.classe (taxonomia_id, id),
    CONSTRAINT fk_transicao_para FOREIGN KEY (taxonomia_id, classe_para_id) REFERENCES dominio.classe (taxonomia_id, id)
);
COMMENT ON TABLE dominio.transicao_permitida IS 'de→para aceitos por tipo de alteração e taxonomia (configs/classes.yaml)';
CREATE INDEX ix_transicao_de_para ON dominio.transicao_permitida (classe_de_id, classe_para_id);

INSERT INTO dominio.transicao_permitida (taxonomia_id, tipo_alteracao_codigo, classe_de_id, classe_para_id)
SELECT t.id, r.tipo, cd.id, cp.id
  FROM dominio.taxonomia t
 CROSS JOIN (VALUES
    ('supressao_vegetacao_arborea',  ARRAY['vegetacao_arborea'], ARRAY['solo_exposto', 'edificacao', 'via_terra', 'via_pavimentada', 'vegetacao_rasteira']),
    ('supressao_vegetacao_rasteira', ARRAY['vegetacao_rasteira'], ARRAY['solo_exposto', 'edificacao', 'via_terra', 'via_pavimentada']),
    ('inicio_construcao',            ARRAY['vegetacao_arborea', 'vegetacao_rasteira', 'solo_exposto'], ARRAY['solo_exposto']),
    ('edificacao_nova',              ARRAY['vegetacao_arborea', 'vegetacao_rasteira', 'solo_exposto'], ARRAY['edificacao']),
    ('abertura_via',                 ARRAY['vegetacao_arborea', 'vegetacao_rasteira', 'solo_exposto'], ARRAY['via_terra', 'via_pavimentada']),
    ('ampliacao_via',                ARRAY['via_terra'], ARRAY['via_pavimentada']),
    ('solo_exposto_movimentacao',    ARRAY['vegetacao_arborea', 'vegetacao_rasteira'], ARRAY['solo_exposto']),
    ('mineracao',                    ARRAY['vegetacao_arborea', 'vegetacao_rasteira', 'solo_exposto'], ARRAY['solo_exposto'])
  ) AS r (tipo, de, para)
 CROSS JOIN LATERAL unnest(r.de) AS d (codigo)
 CROSS JOIN LATERAL unnest(r.para) AS p (codigo)
  JOIN dominio.classe cd ON cd.taxonomia_id = t.id AND cd.codigo = d.codigo
  JOIN dominio.classe cp ON cp.taxonomia_id = t.id AND cp.codigo = p.codigo
 WHERE t.codigo = 'cobertura' AND t.versao = 1;


-- =============================================================================
-- CATÁLOGO
-- =============================================================================

CREATE TABLE catalogo.sensor (codigo text PRIMARY KEY, nome text NOT NULL, operador text);
INSERT INTO catalogo.sensor VALUES
    ('planetscope', 'PlanetScope (Dove)', 'Planet Labs'),
    ('sentinel2',   'Sentinel-2 MSI',     'ESA / Copernicus'),
    ('cbers4a_wpm', 'CBERS-4A WPM',       'INPE / CAST');

CREATE TABLE catalogo.grade (
    id          integer GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_grade PRIMARY KEY,
    codigo      text   NOT NULL CONSTRAINT uq_grade_codigo UNIQUE,
    origem_x    double precision NOT NULL,
    origem_y    double precision NOT NULL,
    pixel_x     double precision NOT NULL CONSTRAINT ck_grade_pixel_x CHECK (pixel_x > 0),
    pixel_y     double precision NOT NULL CONSTRAINT ck_grade_pixel_y CHECK (pixel_y < 0),
    largura     integer NOT NULL CONSTRAINT ck_grade_largura CHECK (largura > 0),
    altura      integer NOT NULL CONSTRAINT ck_grade_altura CHECK (altura > 0),
    area_pixel_m2 double precision GENERATED ALWAYS AS (pixel_x * -pixel_y) STORED,
    geom        geometry(Polygon, 32723) GENERATED ALWAYS AS (
                    ST_MakeEnvelope(origem_x, origem_y + altura * pixel_y,
                                    origem_x + largura * pixel_x, origem_y, 32723)) STORED
);
COMMENT ON TABLE  catalogo.grade IS 'Grade raster (afim sem rotação + tamanho). A máscara é gerada nesta grade, alinhada à imagem';
COMMENT ON COLUMN catalogo.grade.origem_x IS 'Canto superior esquerdo (GDAL GeoTransform[0])';
COMMENT ON COLUMN catalogo.grade.origem_y IS 'Canto superior esquerdo (GDAL GeoTransform[3])';
CREATE INDEX ix_grade_geom ON catalogo.grade USING gist (geom);

-- Lidas dos GeoTIFFs com gdalinfo em 2026-10-24.
INSERT INTO catalogo.grade (codigo, origem_x, origem_y, pixel_x, pixel_y, largura, altura) VALUES
    ('planet_4m5_jardim_interlagos', 726219.0, 7462777.5, 4.5, -4.5,  659,  725),
    ('planet_3m_jardim_interlagos',  726219.0, 7462776.0, 3.0, -3.0,  988, 1087),
    ('cbers_2m_jardim_interlagos',   726220.0, 7462776.0, 2.0, -2.0, 1482, 1631);

CREATE TABLE catalogo.produto (
    codigo          text PRIMARY KEY,
    nome            text     NOT NULL,
    sensor_codigo   text     NOT NULL REFERENCES catalogo.sensor (codigo),
    grade_id        integer  NOT NULL REFERENCES catalogo.grade (id),
    pasta           text     NOT NULL,
    bandas          text[]   NOT NULL,
    tipo_dado       text     NOT NULL,
    banda_alfa      smallint,
    uso             text     NOT NULL CONSTRAINT ck_produto_uso CHECK (uso IN ('serie_principal', 'serie_candidata', 'apoio_rotulagem', 'teste_inferencia')),
    descricao       text
);
COMMENT ON TABLE  catalogo.produto IS 'Família de imagens (configs/pipeline.yaml: dados.fontes). Todas as imagens de um produto compartilham a grade';
COMMENT ON COLUMN catalogo.produto.pasta IS 'Relativa à raiz de dados (configs/pipeline.yaml: dados.raiz)';
COMMENT ON COLUMN catalogo.produto.banda_alfa IS 'Índice (1-based) da banda alfa; nulo se não houver';

INSERT INTO catalogo.produto (codigo, nome, sensor_codigo, grade_id, pasta, bandas, tipo_dado, banda_alfa, uso, descricao)
SELECT v.codigo, v.nome, v.sensor, g.id, v.pasta, v.bandas, 'uint8', v.alfa, v.uso, v.descricao
  FROM (VALUES
    ('global_monthly',    'Planet basemap global mensal (visual)', 'planetscope', 'planet_4m5_jardim_interlagos',
     'data/planet_basemaps/global_monthly',            ARRAY['R','G','B','A'], 4::smallint, 'serie_principal',
     'Mosaico visual mensal; nativo 4,777 m reamostrado'),
    ('medres_normalized', 'Planet basemap normalizado (medres)',    'planetscope', 'planet_4m5_jardim_interlagos',
     'data/planet_basemaps/medres_normalized',         ARRAY['R','G','B','A'], 4::smallint, 'serie_candidata',
     'Candidato a radiometria mais estável'),
    ('sentinel2_8b',      'Planet basemap Sentinel-2 normalizado',  'sentinel2',   'planet_4m5_jardim_interlagos',
     'data/planet_basemaps/sentinel2_8b',              ARRAY['R','G','B','A'], 4::smallint, 'apoio_rotulagem',
     'Só 2026-08 e 2026-09'),
    ('psscene',           'Mosaico PSScene',                        'planetscope', 'planet_3m_jardim_interlagos',
     'data/planet_psscene/mosaico_2026-10-23/mosaico', ARRAY['R','G','B','A'], 4::smallint, 'teste_inferencia',
     'Imagem nova de teste; datas por pixel em *_datas.tif'),
    ('cbers_wpm',         'CBERS-4A WPM fundida 2 m (PCA)',         'cbers4a_wpm', 'cbers_2m_jardim_interlagos',
     'CBERS/wpm_fused_2m',                             ARRAY['R','G','B'],     NULL,         'apoio_rotulagem',
     'Não é Planet; serve para confirmar classes e eventos na rotulagem')
  ) AS v (codigo, nome, sensor, grade, pasta, bandas, alfa, uso, descricao)
  JOIN catalogo.grade g ON g.codigo = v.grade;

CREATE TABLE catalogo.imagem (
    id                     integer GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_imagem PRIMARY KEY,
    produto_codigo         text NOT NULL REFERENCES catalogo.produto (codigo),
    arquivo                text NOT NULL,
    data_inicio            date NOT NULL,
    data_fim               date NOT NULL,
    data_referencia        date NOT NULL,
    mes_referencia         text GENERATED ALWAYS AS (
                               extract(year FROM data_referencia)::int::text || '-' ||
                               lpad(extract(month FROM data_referencia)::int::text, 2, '0')) STORED,
    sha256                 char(64) CONSTRAINT ck_imagem_sha256 CHECK (sha256 ~ '^[0-9a-f]{64}$'),
    ativa                  boolean NOT NULL DEFAULT true,
    -- QC (skill inventario-dados)
    qc_status_codigo       text NOT NULL DEFAULT 'pendente' REFERENCES dominio.status_qc (codigo),
    regime_processamento_codigo text REFERENCES dominio.regime_processamento (codigo),
    pct_valido             real CONSTRAINT ck_imagem_pct_valido CHECK (pct_valido BETWEEN 0 AND 100),
    pct_nuvem_estimada     real CONSTRAINT ck_imagem_pct_nuvem  CHECK (pct_nuvem_estimada BETWEEN 0 AND 100),
    deslocamento_px        real CONSTRAINT ck_imagem_deslocamento CHECK (deslocamento_px >= 0),
    nitidez                real,
    estabilidade_cor       jsonb,
    qc_em                  timestamptz,
    qc_observacao          text,
    observacao             text,
    criado_em              timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT uq_imagem_produto_arquivo UNIQUE (produto_codigo, arquivo),
    CONSTRAINT ck_imagem_periodo CHECK (data_fim >= data_inicio),
    CONSTRAINT ck_imagem_referencia CHECK (data_referencia BETWEEN data_inicio AND data_fim)
);
COMMENT ON TABLE  catalogo.imagem IS 'Um raster com seu QC. A anotação herda daqui a data do que foi classificado';
COMMENT ON COLUMN catalogo.imagem.data_referencia IS 'Data atribuída ao conteúdo (mosaico mensal: dia 1 do mês; o composto mistura datas)';
COMMENT ON COLUMN catalogo.imagem.sha256 IS 'Hash do arquivo (inventário). Obrigatório para a imagem entrar em dataset congelado';
COMMENT ON COLUMN catalogo.imagem.deslocamento_px IS 'Deslocamento estimado contra a referência da série em alvos estáveis; > 1 px pede máscara (Etten 2021)';
COMMENT ON COLUMN catalogo.imagem.nitidez IS 'Variância do laplaciano; salto brusco indica mudança de processamento';
COMMENT ON COLUMN catalogo.imagem.estabilidade_cor IS 'Média e desvio de R, G, B e Hue nas áreas estáveis, ex.: {"r": 92.1, "hue": 0.31}';
CREATE INDEX ix_imagem_data    ON catalogo.imagem (data_referencia);
CREATE INDEX ix_imagem_produto ON catalogo.imagem (produto_codigo);

-- global_monthly: 81 meses, 2020-01 a 2026-09
INSERT INTO catalogo.imagem (produto_codigo, arquivo, data_inicio, data_fim, data_referencia)
SELECT 'global_monthly', format('global_monthly_%s_mosaic.tif', to_char(m, 'YYYY_MM')),
       m::date, (m + interval '1 month - 1 day')::date, m::date
  FROM generate_series('2020-01-01'::date, '2026-09-01'::date, interval '1 month') AS m;

-- medres_normalized: 1 trimestre (2020-06 a 2020-08) + 73 meses (2020-09 a 2026-09)
INSERT INTO catalogo.imagem (produto_codigo, arquivo, data_inicio, data_fim, data_referencia) VALUES
    ('medres_normalized', 'planet_medres_normalized_analytic_2020-06_2020-08_mosaic.tif', '2020-06-01', '2020-08-31', '2020-07-01');
INSERT INTO catalogo.imagem (produto_codigo, arquivo, data_inicio, data_fim, data_referencia)
SELECT 'medres_normalized', format('planet_medres_normalized_analytic_%s_mosaic.tif', to_char(m, 'YYYY-MM')),
       m::date, (m + interval '1 month - 1 day')::date, m::date
  FROM generate_series('2020-09-01'::date, '2026-09-01'::date, interval '1 month') AS m;

-- sentinel2_8b: 2026-08 e 2026-09
INSERT INTO catalogo.imagem (produto_codigo, arquivo, data_inicio, data_fim, data_referencia)
SELECT 'sentinel2_8b', format('br_pf_monthly_sen2_normalized_analytic_8b_sr_%s_mosaic.tif', to_char(m, 'YYYY_MM')),
       m::date, (m + interval '1 month - 1 day')::date, m::date
  FROM generate_series('2026-08-01'::date, '2026-09-01'::date, interval '1 month') AS m;

-- psscene: uma cena, 2026-10-09
INSERT INTO catalogo.imagem (produto_codigo, arquivo, data_inicio, data_fim, data_referencia, regime_processamento_codigo, observacao) VALUES
    ('psscene', 'mosaico_mosaico_2026-10-23_rgb.tif', '2026-10-09', '2026-10-09', '2026-10-09', 'nao_se_aplica',
     'datas por pixel em mosaico_mosaico_2026-10-23_datas.tif');

-- cbers_wpm: 21 datas, 2023-04 a 2026-10 (data no início do nome)
INSERT INTO catalogo.imagem (produto_codigo, arquivo, data_inicio, data_fim, data_referencia, regime_processamento_codigo)
SELECT 'cbers_wpm', a, left(a, 10)::date, left(a, 10)::date, left(a, 10)::date, 'nao_se_aplica'
  FROM unnest(ARRAY[
    '2023-04-11_CBERS4A_WPM_PCA_RGB321_20230411_198_142.tif', '2023-06-12_CBERS4A_WPM_PCA_RGB321_20230612_198_142.tif',
    '2023-09-13_CBERS4A_WPM_PCA_RGB321_20230913_198_142.tif', '2023-11-14_CBERS4A_WPM_PCA_RGB321_20231114_198_142.tif',
    '2023-12-15_CBERS4A_WPM_PCA_RGB321_20231215_198_142.tif', '2024-01-15_CBERS4A_WPM_PCA_RGB321_20240115_198_142.tif',
    '2024-04-17_CBERS4A_WPM_PCA_RGB321_20240417_198_142.tif', '2024-04-22_CBERS4A_WPM_PCA_RGB321_20240422_197_142.tif',
    '2024-05-18_CBERS4A_WPM_PCA_RGB321_20240518_198_142.tif', '2024-08-19_CBERS4A_WPM_PCA_RGB321_20240819_198_142.tif',
    '2025-01-21_CBERS4A_WPM_PCA_RGB321_20250121_198_142.tif', '2025-05-25_CBERS4A_WPM_PCA_RGB321_20250525_198_142.tif',
    '2025-06-25_CBERS4A_WPM_PCA_RGB321_20250625_198_142.tif', '2025-07-26_CBERS4A_WPM_PCA_RGB321_20250726_198_142.tif',
    '2025-10-27_CBERS4A_WPM_PCA_RGB321_20251027_198_142.tif', '2026-01-02_CBERS4A_WPM_PCA_RGB321_20260102_197_142.tif',
    '2026-01-28_CBERS4A_WPM_PCA_RGB321_20260128_198_142.tif', '2026-03-31_CBERS4A_WPM_PCA_RGB321_20260331_198_142.tif',
    '2026-08-07_CBERS4A_WPM_PCA_RGB321_20260807_197_142.tif', '2026-09-02_CBERS4A_WPM_PCA_RGB321_20260902_198_142.tif',
    '2026-10-08_CBERS4A_WPM_PCA_RGB321_20261008_197_142.tif']) AS a;

CREATE TABLE catalogo.aoi (
    id          integer GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_aoi PRIMARY KEY,
    codigo      text NOT NULL CONSTRAINT uq_aoi_codigo UNIQUE,
    nome        text NOT NULL,
    geom        geometry(MultiPolygon, 32723) NOT NULL,
    fonte       text,
    observacao  text
);
COMMENT ON TABLE catalogo.aoi IS 'Áreas de interesse. A grade cobre a AOI + 100 m';
CREATE INDEX ix_aoi_geom ON catalogo.aoi USING gist (geom);

INSERT INTO catalogo.aoi (codigo, nome, geom, fonte, observacao) VALUES
    ('jardim_interlagos', 'Jardim Interlagos, Maricá/RJ',
     auditoria.fn_multipoligono(ST_Transform(ST_SetSRID(ST_GeomFromGeoJSON('{"type":"Polygon","coordinates":[[[-42.77037681,-22.94891664],[-42.77030259,-22.94895405],[-42.77013204,-22.94807396],[-42.76987196,-22.94782301],[-42.76978796,-22.94757697],[-42.76970698,-22.94708702],[-42.76980103,-22.94676204],[-42.76998398,-22.94635399],[-42.77017099,-22.94570402],[-42.77009897,-22.94472096],[-42.76998664,-22.94382764],[-42.7700357,-22.94358688],[-42.77006096,-22.94289301],[-42.76992614,-22.94243793],[-42.76960096,-22.94216339],[-42.76937703,-22.94206382],[-42.76882304,-22.94192199],[-42.76864797,-22.941838],[-42.76803299,-22.94158503],[-42.767422,-22.94125004],[-42.76730171,-22.94119009],[-42.76672069,-22.94127242],[-42.76615588,-22.94090861],[-42.76603838,-22.94076091],[-42.76602201,-22.94065701],[-42.76611404,-22.940413],[-42.766296,-22.94008899],[-42.76664881,-22.93968111],[-42.76679476,-22.93944868],[-42.76710599,-22.93903798],[-42.76719696,-22.93887603],[-42.76737804,-22.93855201],[-42.76773901,-22.93806502],[-42.76819103,-22.93750104],[-42.76830292,-22.93735688],[-42.76842416,-22.93720894],[-42.7686564,-22.93686047],[-42.76883727,-22.93664831],[-42.76898699,-22.93645707],[-42.76933574,-22.93602898],[-42.76958052,-22.93571102],[-42.76974585,-22.93549864],[-42.76992025,-22.93529129],[-42.77026508,-22.93495005],[-42.77051318,-22.93471698],[-42.7707293,-22.93453901],[-42.77093983,-22.93443089],[-42.77125734,-22.93429959],[-42.77176918,-22.93419655],[-42.77190115,-22.93413827],[-42.77203311,-22.93407999],[-42.77216508,-22.9340218],[-42.77229704,-22.93396352],[-42.77242911,-22.93390525],[-42.77256107,-22.93384697],[-42.77269304,-22.93378878],[-42.772825,-22.9337305],[-42.77295697,-22.93367222],[-42.77308893,-22.93361394],[-42.773221,-22.93355575],[-42.77335296,-22.93349747],[-42.77348493,-22.93343919],[-42.77370723,-22.93334679],[-42.77377444,-22.93332885],[-42.77403477,-22.93320553],[-42.77416494,-22.93314387],[-42.7742951,-22.93308221],[-42.77442527,-22.93302055],[-42.77455544,-22.93295889],[-42.7746856,-22.93289723],[-42.77481577,-22.93283557],[-42.77494593,-22.93277391],[-42.7750761,-22.93271225],[-42.77520626,-22.93265059],[-42.77533643,-22.93258893],[-42.77538454,-22.9325636],[-42.77544656,-22.93244255],[-42.77548641,-22.93235788],[-42.77552628,-22.93222763],[-42.7755676,-22.93210201],[-42.77559561,-22.93194197],[-42.77557673,-22.93180427],[-42.77559064,-22.93166947],[-42.77561847,-22.93139987],[-42.77582527,-22.93078407],[-42.77600466,-22.9305377],[-42.77608458,-22.93042431],[-42.7761645,-22.93031091],[-42.776244,-22.93019727],[-42.7763288,-22.93008696],[-42.7764136,-22.92997665],[-42.77649807,-22.9298643],[-42.7765832,-22.92975603],[-42.77666799,-22.92964572],[-42.7767473,-22.92953681],[-42.7768321,-22.9294265],[-42.7769169,-22.92931619],[-42.7770017,-22.92920588],[-42.7770865,-22.92909557],[-42.7771713,-22.92898526],[-42.7772561,-22.92887495],[-42.77734089,-22.92876464],[-42.77757803,-22.92847809],[-42.77772635,-22.92859525],[-42.7778376,-22.92868311],[-42.77786348,-22.9287324],[-42.77806971,-22.92886947],[-42.77829001,-22.92901001],[-42.77855913,-22.9291905],[-42.7788343,-22.92943326],[-42.7790385,-22.92963981],[-42.77939369,-22.93005098],[-42.77942713,-22.93000898],[-42.77939369,-22.93005098],[-42.77922297,-22.93029943],[-42.77917925,-22.93059664],[-42.77924049,-22.93074149],[-42.7792964,-22.93079037],[-42.77935298,-22.9308619],[-42.77935669,-22.93096289],[-42.77945696,-22.93121104],[-42.779597,-22.93153393],[-42.77968116,-22.9317275],[-42.7797614,-22.93194775],[-42.77983833,-22.93214208],[-42.7799463,-22.93234655],[-42.78002453,-22.93246152],[-42.78014467,-22.93261979],[-42.78033545,-22.93291579],[-42.7805296,-22.93310464],[-42.78064326,-22.93333183],[-42.78064157,-22.93343533],[-42.78078957,-22.93382693],[-42.78084975,-22.93390649],[-42.78090915,-22.93426277],[-42.78106716,-22.93451172],[-42.78117542,-22.93461331],[-42.78127464,-22.93481226],[-42.78130049,-22.93494031],[-42.78131233,-22.93512855],[-42.78125757,-22.93528803],[-42.78113273,-22.9355175],[-42.78087992,-22.93574129],[-42.7805245,-22.93607386],[-42.78045858,-22.93623168],[-42.78032886,-22.9365329],[-42.78026151,-22.93677827],[-42.78021101,-22.93701912],[-42.78015044,-22.937306],[-42.7801331,-22.93756975],[-42.78013576,-22.93772076],[-42.78018501,-22.93789918],[-42.78027656,-22.93799708],[-42.78043099,-22.93812347],[-42.78045693,-22.93813246],[-42.78057018,-22.93815648],[-42.78092288,-22.93823388],[-42.78092635,-22.93824946],[-42.78117678,-22.93831508],[-42.78119024,-22.93828939],[-42.78139058,-22.93834223],[-42.78143833,-22.93832715],[-42.78148408,-22.93837783],[-42.78182321,-22.93848782],[-42.78197609,-22.93845178],[-42.7821645,-22.93855104],[-42.78232194,-22.93860673],[-42.78254924,-22.93872034],[-42.78276546,-22.93881287],[-42.78305015,-22.93891995],[-42.78316245,-22.93900261],[-42.7833035,-22.93914952],[-42.78351741,-22.93925561],[-42.78377409,-22.9393955],[-42.7838446,-22.93952762],[-42.78393924,-22.93976469],[-42.78399993,-22.94015657],[-42.78408925,-22.94062024],[-42.78419587,-22.94116568],[-42.78427911,-22.94166032],[-42.78443591,-22.94207015],[-42.78462697,-22.9424645],[-42.78480846,-22.94276036],[-42.78502603,-22.94298534],[-42.78570359,-22.94333622],[-42.78606311,-22.9434534],[-42.78619412,-22.94361699],[-42.7865054,-22.94383701],[-42.78650834,-22.94388537],[-42.78684397,-22.94418295],[-42.78706119,-22.94422912],[-42.78718819,-22.94421018],[-42.78728158,-22.94406655],[-42.78743276,-22.94404968],[-42.78753739,-22.94414604],[-42.7877544,-22.94439192],[-42.78843207,-22.94453596],[-42.78877419,-22.94442016],[-42.78905603,-22.94427397],[-42.78913681,-22.94411808],[-42.7892442,-22.94392978],[-42.78943863,-22.94374506],[-42.78958151,-22.94366595],[-42.78979943,-22.94366899],[-42.79000805,-22.9436719],[-42.79004772,-22.943724],[-42.79022959,-22.94376794],[-42.79034645,-22.94379891],[-42.79049737,-22.94391316],[-42.7906488,-22.94408199],[-42.79081982,-22.94433457],[-42.79092124,-22.9445137],[-42.79112228,-22.94475376],[-42.79128125,-22.94494577],[-42.79140416,-22.94529365],[-42.79138268,-22.94569819],[-42.79131652,-22.94587154],[-42.79114818,-22.94614182],[-42.79106202,-22.94641411],[-42.79092178,-22.9467896],[-42.79076775,-22.94744076],[-42.79073096,-22.94797082],[-42.79073599,-22.94823489],[-42.79079321,-22.94849731],[-42.79093998,-22.94886688],[-42.79114717,-22.94918725],[-42.79132861,-22.94937268],[-42.7915044,-22.94953301],[-42.79171542,-22.94973265],[-42.79196534,-22.94981722],[-42.79220295,-22.94987057],[-42.79235568,-22.94975882],[-42.79242666,-22.94974772],[-42.79258661,-22.94964987],[-42.7927136,-22.94951706],[-42.79278502,-22.94959375],[-42.79274704,-22.94986757],[-42.79268854,-22.95027181],[-42.79255513,-22.95045631],[-42.79239286,-22.95058173],[-42.79197914,-22.95058805],[-42.79150689,-22.95035544],[-42.79129727,-22.95029903],[-42.79066532,-22.95034868],[-42.79042544,-22.95043506],[-42.79021859,-22.95066684],[-42.79024374,-22.95072413],[-42.79023876,-22.95080171],[-42.79006518,-22.95083466],[-42.789869,-22.95109765],[-42.78986914,-22.95120398],[-42.78972125,-22.95124678],[-42.78965607,-22.95135975],[-42.78953519,-22.95157548],[-42.78939285,-22.95173569],[-42.78935329,-22.95199137],[-42.78924096,-22.9522538],[-42.78913663,-22.952597],[-42.78914066,-22.95326654],[-42.78926483,-22.95363622],[-42.78963378,-22.95420689],[-42.79001841,-22.954616],[-42.79018056,-22.95472697],[-42.79021641,-22.95469986],[-42.79023335,-22.95457414],[-42.79021195,-22.95451517],[-42.79024399,-22.95449319],[-42.79034444,-22.95450279],[-42.7904955,-22.95458016],[-42.7906792,-22.95474147],[-42.79086457,-22.95491487],[-42.79094319,-22.95523604],[-42.79083817,-22.9555072],[-42.7907214,-22.95569882],[-42.79057946,-22.95584869],[-42.79037268,-22.95596141],[-42.79008076,-22.95606756],[-42.78974848,-22.95624906],[-42.78901787,-22.95626303],[-42.78851502,-22.95619217],[-42.78813909,-22.95605062],[-42.78801177,-22.95597465],[-42.78781909,-22.95579251],[-42.78757806,-22.95564852],[-42.78722607,-22.95529507],[-42.78695529,-22.9550178],[-42.78681436,-22.95486227],[-42.78668971,-22.9547363],[-42.78640532,-22.95469295],[-42.78636974,-22.95453454],[-42.78652285,-22.95417286],[-42.78649655,-22.95403668],[-42.78647829,-22.95353184],[-42.78639009,-22.95306918],[-42.78616294,-22.95250837],[-42.7852102,-22.95222768],[-42.78516279,-22.95201198],[-42.78521216,-22.95198249],[-42.78526665,-22.95201343],[-42.78552455,-22.95193592],[-42.7856058,-22.95187151],[-42.78558075,-22.95175209],[-42.78543094,-22.9517276],[-42.78536654,-22.95167954],[-42.78523389,-22.95157017],[-42.78502003,-22.95144457],[-42.78485289,-22.95132717],[-42.78458795,-22.95138383],[-42.78444503,-22.95140447],[-42.7843638,-22.95151463],[-42.78421744,-22.95162199],[-42.78404473,-22.95184593],[-42.78403347,-22.95206812],[-42.78309481,-22.95217383],[-42.78278897,-22.95211486],[-42.7825476,-22.95205301],[-42.78229829,-22.95197784],[-42.78208492,-22.95186946],[-42.78191646,-22.95183315],[-42.78174994,-22.95180253],[-42.78166842,-22.95180516],[-42.78151749,-22.95181814],[-42.78144621,-22.95181714],[-42.781336,-22.95183069],[-42.78124051,-22.95181615],[-42.78119444,-22.95176835],[-42.78115831,-22.95173577],[-42.78110771,-22.9517162],[-42.78106405,-22.9516458],[-42.78101302,-22.95149499],[-42.780929,-22.95124896],[-42.78084796,-22.95108085],[-42.78075224,-22.95098287],[-42.78044138,-22.9507372],[-42.78033295,-22.95056203],[-42.78023897,-22.95034003],[-42.78009271,-22.95018141],[-42.77993064,-22.95003437],[-42.7798037,-22.94994959],[-42.77974927,-22.94979038],[-42.77964907,-22.94965722],[-42.77951806,-22.9495237],[-42.77937078,-22.94930125],[-42.77925461,-22.94918079],[-42.77915611,-22.94909357],[-42.77903253,-22.94897764],[-42.77876151,-22.94877437],[-42.7786115,-22.94869714],[-42.77842792,-22.94858894],[-42.77823608,-22.94848816],[-42.77801609,-22.94836436],[-42.77770674,-22.94827161],[-42.77682587,-22.94823875],[-42.77655267,-22.94813117],[-42.77636422,-22.94810259],[-42.77617392,-22.94803202],[-42.77594431,-22.94787412],[-42.77556311,-22.94780087],[-42.77514101,-22.94783079],[-42.77493981,-22.9477261],[-42.77465948,-22.94755618],[-42.77432627,-22.94750623],[-42.77346028,-22.9474356],[-42.77313345,-22.94741569],[-42.77290215,-22.94736151],[-42.77273311,-22.94736102],[-42.77263708,-22.94739528],[-42.77251983,-22.94746554],[-42.77218888,-22.94727793],[-42.772037,-22.94748871],[-42.77184358,-22.9476086],[-42.77168832,-22.94762151],[-42.77178443,-22.94773792],[-42.77181571,-22.94806634],[-42.77155133,-22.94816637],[-42.77144215,-22.94838129],[-42.77121924,-22.94856112],[-42.77108135,-22.94877234],[-42.77066713,-22.94889267],[-42.77054576,-22.94892278],[-42.77048686,-22.94891252],[-42.77037681,-22.94891664]]]}'), 4326), 32723)),
     'Jardim_Interlagos.geojson',
     'Geometria reconstituída por diferença entre distritos e bairros; exige confirmação cadastral. A original tem autointerseção, corrigida com ST_MakeValid');

CREATE VIEW catalogo.vw_imagem AS
SELECT i.id, i.produto_codigo, p.uso, p.sensor_codigo, i.arquivo,
       p.pasta || '/' || i.arquivo AS caminho_relativo,
       i.data_inicio, i.data_fim, i.data_referencia, i.mes_referencia, i.ativa,
       i.qc_status_codigo, i.regime_processamento_codigo, i.pct_valido, i.pct_nuvem_estimada, i.deslocamento_px,
       (i.sha256 IS NOT NULL) AS tem_hash,
       g.id AS grade_id, g.codigo AS grade, g.pixel_x AS resolucao_m, g.largura, g.altura,
       g.geom
  FROM catalogo.imagem i
  JOIN catalogo.produto p ON p.codigo = i.produto_codigo
  JOIN catalogo.grade g   ON g.id = p.grade_id;
COMMENT ON VIEW catalogo.vw_imagem IS 'Imagem com caminho, grade, QC e extensão (chave: id)';


-- =============================================================================
-- ROTULAGEM — estrutura
-- =============================================================================

CREATE TABLE rotulo.pessoa (
    id             integer GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_pessoa PRIMARY KEY,
    apelido        text NOT NULL CONSTRAINT uq_pessoa_apelido UNIQUE CONSTRAINT ck_pessoa_apelido CHECK (apelido ~ '^[a-z][a-z0-9_.]*$'),
    nome           text NOT NULL,
    funcao_codigo  text NOT NULL REFERENCES dominio.funcao_pessoa (codigo),
    ativa          boolean NOT NULL DEFAULT true,
    criado_em      timestamptz NOT NULL DEFAULT now()
);
COMMENT ON TABLE  rotulo.pessoa IS 'Quem rotula e revisa';
COMMENT ON COLUMN rotulo.pessoa.apelido IS 'Igual ao login do banco ou ao app.usuario: é o que filtra as visões de trabalho cego';

CREATE TABLE rotulo.campanha (
    id                integer GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_campanha PRIMARY KEY,
    codigo            text    NOT NULL CONSTRAINT uq_campanha_codigo UNIQUE,
    nome              text    NOT NULL,
    taxonomia_id      integer NOT NULL REFERENCES dominio.taxonomia (id),
    aoi_id            integer NOT NULL REFERENCES catalogo.aoi (id),
    objetivo          text,
    tolerancia_lacuna_px real NOT NULL DEFAULT 1 CONSTRAINT ck_campanha_tolerancia CHECK (tolerancia_lacuna_px >= 0),
    ativa             boolean NOT NULL DEFAULT true,
    criado_em         timestamptz NOT NULL DEFAULT now()
);
COMMENT ON TABLE  rotulo.campanha IS 'Esforço de rotulagem com taxonomia fixa. Trocar de taxonomia = nova campanha';
COMMENT ON COLUMN rotulo.campanha.tolerancia_lacuna_px IS 'Área máxima sem classe, em pixels da grade, aceita no envio da sessão';

INSERT INTO rotulo.campanha (codigo, nome, taxonomia_id, aoi_id, objetivo)
SELECT 'cobertura_referencia_v1', 'Referência de cobertura e mudança v1', t.id, a.id,
       'Máscaras de cobertura por data, eventos de mudança e controles estáveis para treinar e avaliar detectores'
  FROM dominio.taxonomia t, catalogo.aoi a
 WHERE t.codigo = 'cobertura' AND t.versao = 1 AND a.codigo = 'jardim_interlagos';

-- Proveniência de qualquer processamento que gere rótulos (D20; Febrita 2025).
CREATE TABLE rotulo.processamento (
    id                 integer GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_processamento PRIMARY KEY,
    ferramenta_codigo  text NOT NULL REFERENCES dominio.ferramenta (codigo),
    versao_ferramenta  text,
    modelo_ref         text,
    parametros         jsonb NOT NULL DEFAULT '{}',
    run_id             text,
    executado_em       timestamptz NOT NULL DEFAULT now(),
    observacao         text
);
COMMENT ON TABLE  rotulo.processamento IS 'Execução de ferramenta ou modelo que gerou pré-rótulos ou incertezas';
COMMENT ON COLUMN rotulo.processamento.parametros IS 'Todos os parâmetros: resolução de processamento, sobreposição, pontos de prompt, limiar, remoção de segmentos...';
COMMENT ON COLUMN rotulo.processamento.run_id IS 'run_id do registro de experimentos (runs/.../run.json), quando houver';

-- Aprendizado ativo (Masolele 2024; Carter 2024).
CREATE TABLE rotulo.ciclo_aprendizado (
    id                 integer GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_ciclo PRIMARY KEY,
    campanha_id        integer  NOT NULL REFERENCES rotulo.campanha (id),
    numero             smallint NOT NULL CONSTRAINT ck_ciclo_numero CHECK (numero > 0),
    processamento_id   integer  NOT NULL REFERENCES rotulo.processamento (id),
    criterio           text     NOT NULL DEFAULT 'entropia',
    limiar             real,
    fracao_aleatoria   real CONSTRAINT ck_ciclo_fracao CHECK (fracao_aleatoria BETWEEN 0 AND 1),
    criado_em          timestamptz NOT NULL DEFAULT now(),
    observacao         text,
    CONSTRAINT uq_ciclo_campanha_numero UNIQUE (campanha_id, numero)
);
COMMENT ON TABLE  rotulo.ciclo_aprendizado IS 'Ciclo de seleção por incerteza; o modelo e seus parâmetros ficam em processamento';
COMMENT ON COLUMN rotulo.ciclo_aprendizado.fracao_aleatoria IS 'Fração dos recortes do ciclo sorteada ao acaso para não enviesar';

-- Plano amostral para avaliação independente (Olofsson 2014; Zhang 2023, p. 7).
CREATE TABLE rotulo.plano_amostral (
    id           integer GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_plano PRIMARY KEY,
    campanha_id  integer NOT NULL REFERENCES rotulo.campanha (id),
    codigo       text    NOT NULL CONSTRAINT uq_plano_codigo UNIQUE,
    uso          text    NOT NULL CONSTRAINT ck_plano_uso CHECK (uso IN ('avaliacao_independente', 'treino')),
    semente      integer NOT NULL,
    descricao    text,
    criado_em    timestamptz NOT NULL DEFAULT now()
);
COMMENT ON TABLE  rotulo.plano_amostral IS 'Desenho amostral. Tarefas de plano avaliacao_independente nunca entram em dataset de treino';

CREATE TABLE rotulo.estrato (
    id          integer GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_estrato PRIMARY KEY,
    plano_id    integer NOT NULL REFERENCES rotulo.plano_amostral (id),
    codigo      text    NOT NULL,
    descricao   text,
    geom        geometry(MultiPolygon, 32723) NOT NULL,
    area_m2     double precision GENERATED ALWAYS AS (ST_Area(geom)) STORED,
    n_alvo      integer CONSTRAINT ck_estrato_n CHECK (n_alvo > 0),
    CONSTRAINT uq_estrato_plano_codigo UNIQUE (plano_id, codigo)
);
COMMENT ON TABLE rotulo.estrato IS 'Estrato do plano (ex.: mudança do mapa por mês, estável). area_m2 é o N_h do estimador';
CREATE INDEX ix_estrato_geom ON rotulo.estrato USING gist (geom);

-- Série: a mesma área rotulada em várias datas do mesmo produto (Etten 2021; Toker 2022).
CREATE TABLE rotulo.serie (
    id              integer GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_serie PRIMARY KEY,
    campanha_id     integer NOT NULL REFERENCES rotulo.campanha (id),
    produto_codigo  text    NOT NULL REFERENCES catalogo.produto (codigo),
    geom            geometry(Polygon, 32723) NOT NULL,
    observacao      text,
    criado_em       timestamptz NOT NULL DEFAULT now()
);
COMMENT ON TABLE rotulo.serie IS 'Recorte fixo rotulado ao longo do tempo: rotula a 1ª data, propaga e edita só onde muda';
CREATE INDEX ix_serie_geom ON rotulo.serie USING gist (geom);

-- Objeto físico com identidade persistente entre datas (SCOT exige rastreio; Etten 2021).
CREATE TABLE rotulo.objeto (
    id           bigint GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_objeto PRIMARY KEY,
    campanha_id  integer NOT NULL REFERENCES rotulo.campanha (id),
    observacao   text,
    criado_em    timestamptz NOT NULL DEFAULT now()
);
COMMENT ON TABLE rotulo.objeto IS 'Identidade de um objeto (ex.: uma edificação) ao longo da série; anotações e eventos apontam para cá';


-- =============================================================================
-- ROTULAGEM — cobertura por data
-- =============================================================================

CREATE TABLE rotulo.tarefa (
    id                   integer GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_tarefa PRIMARY KEY,
    campanha_id          integer NOT NULL REFERENCES rotulo.campanha (id),
    imagem_id            integer NOT NULL REFERENCES catalogo.imagem (id),
    data_referencia      date    NOT NULL,
    geom                 geometry(Polygon, 32723) NOT NULL,
    area_m2              double precision GENERATED ALWAYS AS (ST_Area(geom)) STORED,
    serie_id             integer REFERENCES rotulo.serie (id),
    modo_selecao_codigo  text    NOT NULL DEFAULT 'conveniencia' REFERENCES dominio.modo_selecao (codigo),
    estrato_id           integer REFERENCES rotulo.estrato (id),
    prob_inclusao        double precision CONSTRAINT ck_tarefa_prob CHECK (prob_inclusao > 0 AND prob_inclusao <= 1),
    ciclo_id             integer REFERENCES rotulo.ciclo_aprendizado (id),
    incerteza            real,
    prioridade           smallint NOT NULL DEFAULT 3 CONSTRAINT ck_tarefa_prioridade CHECK (prioridade BETWEEN 1 AND 5),
    motivo               text,
    descartada           boolean NOT NULL DEFAULT false,
    observacao           text,
    criado_em            timestamptz NOT NULL DEFAULT now(),
    atualizado_em        timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT uq_tarefa_serie_imagem UNIQUE (serie_id, imagem_id),
    CONSTRAINT ck_tarefa_ativo_ciclo CHECK (modo_selecao_codigo <> 'aprendizado_ativo' OR ciclo_id IS NOT NULL),
    CONSTRAINT ck_tarefa_prob_obrigatoria CHECK (modo_selecao_codigo NOT IN ('aleatoria', 'estratificada') OR prob_inclusao IS NOT NULL),
    CONSTRAINT ck_tarefa_estrato CHECK (modo_selecao_codigo <> 'estratificada' OR estrato_id IS NOT NULL)
);
COMMENT ON TABLE  rotulo.tarefa IS 'Recorte de UMA imagem a ser classificado por completo. Unidade de trabalho, revisão e amostra';
COMMENT ON COLUMN rotulo.tarefa.data_referencia IS 'Copiada da imagem (não editável): data do que é classificado';
COMMENT ON COLUMN rotulo.tarefa.modo_selecao_codigo IS 'Como a tarefa foi escolhida; define se serve a estimativas com IC';
COMMENT ON COLUMN rotulo.tarefa.prob_inclusao IS 'Probabilidade de inclusão no sorteio (peso = 1/prob_inclusao)';
COMMENT ON COLUMN rotulo.tarefa.incerteza IS 'Incerteza do modelo no recorte (ex.: entropia média), no aprendizado ativo';
CREATE INDEX ix_tarefa_geom     ON rotulo.tarefa USING gist (geom);
CREATE INDEX ix_tarefa_campanha ON rotulo.tarefa (campanha_id);
CREATE INDEX ix_tarefa_imagem   ON rotulo.tarefa (imagem_id);
CREATE INDEX ix_tarefa_data     ON rotulo.tarefa (data_referencia);
CREATE INDEX ix_tarefa_serie    ON rotulo.tarefa (serie_id);
CREATE INDEX ix_tarefa_estrato  ON rotulo.tarefa (estrato_id);

CREATE TABLE rotulo.sessao (
    id                 integer GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_sessao PRIMARY KEY,
    tarefa_id          integer NOT NULL REFERENCES rotulo.tarefa (id),
    pessoa_id          integer NOT NULL REFERENCES rotulo.pessoa (id),
    status_codigo      text    NOT NULL DEFAULT 'em_andamento' REFERENCES dominio.status_sessao (codigo),
    condicao_codigo    text    NOT NULL DEFAULT 'manual' REFERENCES dominio.condicao_rotulagem (codigo),
    sessao_origem_id   integer REFERENCES rotulo.sessao (id),
    tempo_ativo_s      integer CONSTRAINT ck_sessao_tempo CHECK (tempo_ativo_s >= 0),
    iniciada_em        timestamptz NOT NULL DEFAULT now(),
    enviada_em         timestamptz,
    revisor_id         integer REFERENCES rotulo.pessoa (id),
    revisada_em        timestamptz,
    comentario_revisao text,
    atualizado_em      timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT uq_sessao_tarefa_pessoa UNIQUE (tarefa_id, pessoa_id),
    CONSTRAINT ck_sessao_revisor_diferente CHECK (revisor_id IS NULL OR revisor_id <> pessoa_id),
    CONSTRAINT ck_sessao_propagada CHECK ((condicao_codigo = 'propagada') = (sessao_origem_id IS NOT NULL))
);
COMMENT ON TABLE  rotulo.sessao IS 'Passada de uma pessoa sobre uma tarefa. Duas sessões na mesma tarefa medem concordância; só uma é aprovada';
COMMENT ON COLUMN rotulo.sessao.condicao_codigo IS 'Condição de trabalho (manual, pré-anotação, propagada) para medir ganho de tempo';
COMMENT ON COLUMN rotulo.sessao.tempo_ativo_s IS 'Tempo efetivo de trabalho informado pelo rotulador (sem pausas)';
CREATE UNIQUE INDEX uq_sessao_aprovada_por_tarefa ON rotulo.sessao (tarefa_id) WHERE status_codigo = 'aprovada';
CREATE INDEX ix_sessao_pessoa ON rotulo.sessao (pessoa_id);
CREATE INDEX ix_sessao_status ON rotulo.sessao (status_codigo);

CREATE TABLE rotulo.anotacao (
    id                  integer GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_anotacao PRIMARY KEY,
    sessao_id           integer NOT NULL REFERENCES rotulo.sessao (id) ON DELETE CASCADE,
    tarefa_id           integer NOT NULL REFERENCES rotulo.tarefa (id),
    data_referencia     date    NOT NULL,
    classe_id           integer NOT NULL REFERENCES dominio.classe (id),
    geom                geometry(MultiPolygon, 32723) NOT NULL,
    area_m2             double precision GENERATED ALWAYS AS (ST_Area(geom)) STORED,
    certeza_codigo      text NOT NULL DEFAULT 'alta'   REFERENCES dominio.nivel_certeza (codigo),
    origem_codigo       text NOT NULL DEFAULT 'manual' REFERENCES dominio.origem_anotacao (codigo),
    processamento_id    integer REFERENCES rotulo.processamento (id),
    anotacao_origem_id  integer REFERENCES rotulo.anotacao (id) ON DELETE SET NULL,
    editada             boolean NOT NULL DEFAULT false,
    objeto_id           bigint REFERENCES rotulo.objeto (id),
    imagem_apoio_id     integer REFERENCES catalogo.imagem (id),
    observacao          text,
    criado_em           timestamptz NOT NULL DEFAULT now(),
    atualizado_em       timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT ck_anotacao_pre_rotulo CHECK (origem_codigo <> 'pre_rotulo_modelo' OR processamento_id IS NOT NULL)
);
COMMENT ON TABLE  rotulo.anotacao IS 'Polígono de cobertura. As anotações de uma sessão particionam a tarefa: sem sobreposição e, no envio, sem lacunas';
COMMENT ON COLUMN rotulo.anotacao.data_referencia IS 'Data do que foi classificado; copiada da imagem da tarefa (não editável)';
COMMENT ON COLUMN rotulo.anotacao.geom IS 'Recortada automaticamente ao limite da tarefa e corrigida se inválida';
COMMENT ON COLUMN rotulo.anotacao.processamento_id IS 'Ferramenta/modelo que gerou o pré-rótulo';
COMMENT ON COLUMN rotulo.anotacao.anotacao_origem_id IS 'Anotação da data anterior de onde esta foi propagada';
COMMENT ON COLUMN rotulo.anotacao.editada IS 'true se uma pessoa alterou classe ou geometria de um pré-rótulo ou de uma propagação';
COMMENT ON COLUMN rotulo.anotacao.objeto_id IS 'Identidade persistente do objeto entre datas (ex.: edificação)';
CREATE INDEX ix_anotacao_geom    ON rotulo.anotacao USING gist (geom);
CREATE INDEX ix_anotacao_sessao  ON rotulo.anotacao (sessao_id);
CREATE INDEX ix_anotacao_tarefa  ON rotulo.anotacao (tarefa_id);
CREATE INDEX ix_anotacao_classe  ON rotulo.anotacao (classe_id);
CREATE INDEX ix_anotacao_data    ON rotulo.anotacao (data_referencia);
CREATE INDEX ix_anotacao_objeto  ON rotulo.anotacao (objeto_id);

-- Regras da tarefa ------------------------------------------------------------

CREATE FUNCTION rotulo.fn_validar_tarefa() RETURNS trigger
LANGUAGE plpgsql AS $$
DECLARE
    v_img    record;
    v_serie  rotulo.serie;
    v_conf   integer;
    v_estrato geometry;
BEGIN
    IF TG_OP = 'UPDATE' AND (NEW.imagem_id <> OLD.imagem_id OR NEW.campanha_id <> OLD.campanha_id
                             OR NOT ST_Equals(NEW.geom, OLD.geom) OR NEW.serie_id IS DISTINCT FROM OLD.serie_id)
       AND EXISTS (SELECT 1 FROM rotulo.sessao s WHERE s.tarefa_id = NEW.id) THEN
        RAISE EXCEPTION 'Tarefa %: imagem, campanha, série e recorte não mudam depois que há sessões; crie outra tarefa', NEW.id;
    END IF;

    SELECT i.data_referencia, i.ativa, i.produto_codigo, q.aceita_rotulo, i.qc_status_codigo, g.geom AS extensao INTO v_img
      FROM catalogo.imagem i
      JOIN catalogo.produto p  ON p.codigo = i.produto_codigo
      JOIN catalogo.grade g    ON g.id = p.grade_id
      JOIN dominio.status_qc q ON q.codigo = i.qc_status_codigo
     WHERE i.id = NEW.imagem_id;

    IF TG_OP = 'INSERT' AND NOT v_img.ativa THEN
        RAISE EXCEPTION 'Imagem % está inativa', NEW.imagem_id;
    END IF;
    IF TG_OP = 'INSERT' AND NOT v_img.aceita_rotulo THEN
        RAISE EXCEPTION 'Imagem % tem QC %; não recebe tarefas', NEW.imagem_id, v_img.qc_status_codigo;
    END IF;

    IF NEW.serie_id IS NOT NULL THEN
        SELECT * INTO v_serie FROM rotulo.serie WHERE id = NEW.serie_id;
        IF v_serie.produto_codigo <> v_img.produto_codigo OR v_serie.campanha_id <> NEW.campanha_id THEN
            RAISE EXCEPTION 'Tarefa da série % precisa ser do produto % e da mesma campanha', NEW.serie_id, v_serie.produto_codigo;
        END IF;
        NEW.geom := v_serie.geom;
    END IF;

    NEW.data_referencia := v_img.data_referencia;
    NEW.geom := ST_MakeValid(NEW.geom);

    IF NOT ST_CoveredBy(NEW.geom, v_img.extensao) THEN
        RAISE EXCEPTION 'Tarefa fora da extensão da imagem %', NEW.imagem_id;
    END IF;

    IF NEW.estrato_id IS NOT NULL THEN
        SELECT geom INTO v_estrato FROM rotulo.estrato WHERE id = NEW.estrato_id;
        IF NOT ST_Intersects(ST_Centroid(NEW.geom), v_estrato) THEN
            RAISE EXCEPTION 'Tarefa fora do estrato %', NEW.estrato_id;
        END IF;
    END IF;

    IF NOT NEW.descartada THEN
        SELECT t.id INTO v_conf
          FROM rotulo.tarefa t
         WHERE t.campanha_id = NEW.campanha_id AND t.imagem_id = NEW.imagem_id
           AND t.id <> coalesce(NEW.id, -1) AND NOT t.descartada
           AND t.geom && NEW.geom
           AND ST_Area(ST_Intersection(t.geom, NEW.geom)) > 0.01
         LIMIT 1;
        IF v_conf IS NOT NULL THEN
            RAISE EXCEPTION 'Tarefa sobrepõe a tarefa % na mesma imagem e campanha', v_conf;
        END IF;
    END IF;
    RETURN NEW;
END $$;

CREATE TRIGGER tg_tarefa_validar BEFORE INSERT OR UPDATE ON rotulo.tarefa
    FOR EACH ROW EXECUTE FUNCTION rotulo.fn_validar_tarefa();
CREATE TRIGGER tg_tarefa_atualizado_em BEFORE UPDATE ON rotulo.tarefa
    FOR EACH ROW EXECUTE FUNCTION auditoria.fn_tocar_atualizado_em();

CREATE FUNCTION rotulo.fn_lacuna(p_sessao_id integer) RETURNS geometry
LANGUAGE sql STABLE AS $$
    SELECT auditoria.fn_multipoligono(
               ST_Difference(t.geom, coalesce(
                   (SELECT ST_Union(a.geom) FROM rotulo.anotacao a WHERE a.sessao_id = s.id),
                   ST_SetSRID('POLYGON EMPTY'::geometry, 32723))))
      FROM rotulo.sessao s
      JOIN rotulo.tarefa t ON t.id = s.tarefa_id
     WHERE s.id = p_sessao_id
$$;

-- Máquina de estados da sessão ---------------------------------------------------
--   em_andamento → enviada              (sem lacuna acima da tolerância)
--   enviada      → aprovada | rejeitada (revisor obrigatório e diferente do rotulador)
--   enviada | rejeitada | aprovada → em_andamento  (aprovada só se fora de dataset congelado)
CREATE FUNCTION rotulo.fn_estado_sessao() RETURNS trigger
LANGUAGE plpgsql AS $$
DECLARE
    v_de      text := CASE WHEN TG_OP = 'UPDATE' THEN OLD.status_codigo END;
    v_para    text := NEW.status_codigo;
    v_lacuna  double precision;
    v_tol     double precision;
BEGIN
    IF TG_OP = 'INSERT' THEN
        IF NEW.status_codigo <> 'em_andamento' THEN
            RAISE EXCEPTION 'Sessão nasce em_andamento';
        END IF;
        IF (SELECT descartada FROM rotulo.tarefa WHERE id = NEW.tarefa_id) THEN
            RAISE EXCEPTION 'Tarefa % está descartada', NEW.tarefa_id;
        END IF;
        RETURN NEW;
    END IF;

    IF NEW.tarefa_id <> OLD.tarefa_id OR NEW.pessoa_id <> OLD.pessoa_id
       OR NEW.sessao_origem_id IS DISTINCT FROM OLD.sessao_origem_id THEN
        RAISE EXCEPTION 'Tarefa, pessoa e origem da sessão não mudam';
    END IF;
    IF v_de = v_para THEN
        RETURN NEW;
    END IF;

    IF v_de = 'em_andamento' AND v_para = 'enviada' THEN
        SELECT coalesce(ST_Area(rotulo.fn_lacuna(NEW.id)), 0), c.tolerancia_lacuna_px * g.area_pixel_m2
          INTO v_lacuna, v_tol
          FROM rotulo.tarefa t
          JOIN rotulo.campanha c  ON c.id = t.campanha_id
          JOIN catalogo.imagem i  ON i.id = t.imagem_id
          JOIN catalogo.produto p ON p.codigo = i.produto_codigo
          JOIN catalogo.grade g   ON g.id = p.grade_id
         WHERE t.id = NEW.tarefa_id;
        IF v_lacuna > v_tol THEN
            RAISE EXCEPTION 'Sessão %: % m² da tarefa sem classe (tolerância % m²)', NEW.id, round(v_lacuna::numeric, 1), round(v_tol::numeric, 1)
                  USING HINT = 'Veja rotulo.vw_lacuna; use a classe "indeterminado" onde não for possível decidir';
        END IF;
        NEW.enviada_em := now();

    ELSIF v_de = 'enviada' AND v_para IN ('aprovada', 'rejeitada') THEN
        IF NEW.revisor_id IS NULL THEN
            RAISE EXCEPTION 'Informe revisor_id para aprovar ou rejeitar';
        END IF;
        NEW.revisada_em := now();

    ELSIF v_para = 'em_andamento' AND v_de IN ('enviada', 'rejeitada', 'aprovada') THEN
        IF v_de = 'aprovada' AND EXISTS (
               SELECT 1 FROM treino.dataset_amostra da
                 JOIN treino.dataset d ON d.id = da.dataset_id
                WHERE da.sessao_id = NEW.id AND d.congelado_em IS NOT NULL) THEN
            RAISE EXCEPTION 'Sessão % é referência de dataset congelado; crie nova sessão em vez de reabrir', NEW.id;
        END IF;
        NEW.enviada_em  := NULL;
        NEW.revisada_em := NULL;
        NEW.revisor_id  := NULL;

    ELSE
        RAISE EXCEPTION 'Transição de sessão inválida: % → %', v_de, v_para;
    END IF;
    RETURN NEW;
END $$;

CREATE TRIGGER tg_sessao_estado BEFORE INSERT OR UPDATE ON rotulo.sessao
    FOR EACH ROW EXECUTE FUNCTION rotulo.fn_estado_sessao();
CREATE TRIGGER tg_sessao_atualizado_em BEFORE UPDATE ON rotulo.sessao
    FOR EACH ROW EXECUTE FUNCTION auditoria.fn_tocar_atualizado_em();

-- Regras da anotação ----------------------------------------------------------
CREATE FUNCTION rotulo.fn_validar_anotacao() RETURNS trigger
LANGUAGE plpgsql AS $$
DECLARE
    v_ctx     record;
    v_classe  dominio.classe;
    v_conf    integer;
    v_sessao  integer := CASE WHEN TG_OP = 'DELETE' THEN OLD.sessao_id ELSE NEW.sessao_id END;
BEGIN
    SELECT s.status_codigo, t.id AS tarefa_id, t.geom AS tarefa_geom, t.data_referencia,
           c.id AS campanha_id, c.taxonomia_id, g.area_pixel_m2
      INTO v_ctx
      FROM rotulo.sessao s
      JOIN rotulo.tarefa t    ON t.id = s.tarefa_id
      JOIN rotulo.campanha c  ON c.id = t.campanha_id
      JOIN catalogo.imagem i  ON i.id = t.imagem_id
      JOIN catalogo.produto p ON p.codigo = i.produto_codigo
      JOIN catalogo.grade g   ON g.id = p.grade_id
     WHERE s.id = v_sessao;

    IF v_ctx.status_codigo <> 'em_andamento' THEN
        RAISE EXCEPTION 'Sessão % está %; anotações só mudam com a sessão em_andamento', v_sessao, v_ctx.status_codigo;
    END IF;
    IF TG_OP = 'DELETE' THEN
        RETURN OLD;
    END IF;
    IF TG_OP = 'UPDATE' AND (NEW.sessao_id <> OLD.sessao_id OR NEW.origem_codigo <> OLD.origem_codigo
                             OR NEW.anotacao_origem_id IS DISTINCT FROM OLD.anotacao_origem_id) THEN
        RAISE EXCEPTION 'Sessão, origem e anotação de origem não mudam';
    END IF;
    IF NEW.origem_codigo = 'propagada' AND NEW.anotacao_origem_id IS NULL THEN
        RAISE EXCEPTION 'Anotação propagada precisa de anotacao_origem_id (use rotulo.fn_propagar_sessao)';
    END IF;

    SELECT * INTO v_classe FROM dominio.classe WHERE id = NEW.classe_id;
    IF v_classe.taxonomia_id <> v_ctx.taxonomia_id THEN
        RAISE EXCEPTION 'Classe % não pertence à taxonomia da campanha', v_classe.codigo;
    END IF;
    IF v_classe.valor_raster IS NULL THEN
        RAISE EXCEPTION 'Classe % é agregadora; use uma classe folha', v_classe.codigo
              USING HINT = 'SELECT codigo FROM dominio.vw_classe WHERE atribuivel';
    END IF;
    IF NEW.objeto_id IS NOT NULL AND (SELECT campanha_id FROM rotulo.objeto WHERE id = NEW.objeto_id) <> v_ctx.campanha_id THEN
        RAISE EXCEPTION 'Objeto % é de outra campanha', NEW.objeto_id;
    END IF;

    NEW.tarefa_id       := v_ctx.tarefa_id;
    NEW.data_referencia := v_ctx.data_referencia;
    NEW.geom := auditoria.fn_multipoligono(ST_Intersection(ST_MakeValid(NEW.geom), v_ctx.tarefa_geom));

    IF ST_IsEmpty(NEW.geom) OR ST_Area(NEW.geom) < 0.25 * v_ctx.area_pixel_m2 THEN
        RAISE EXCEPTION 'Anotação fora da tarefa ou menor que 1/4 de pixel após o recorte';
    END IF;

    IF TG_OP = 'UPDATE' AND NEW.origem_codigo IN ('pre_rotulo_modelo', 'propagada')
       AND (NEW.classe_id <> OLD.classe_id OR NOT ST_Equals(NEW.geom, OLD.geom)) THEN
        NEW.editada := true;
    END IF;

    SELECT a.id INTO v_conf
      FROM rotulo.anotacao a
     WHERE a.sessao_id = NEW.sessao_id
       AND a.id <> coalesce(NEW.id, -1)
       AND a.geom && NEW.geom
       AND ST_Area(ST_Intersection(a.geom, NEW.geom)) > 0.01
     LIMIT 1;
    IF v_conf IS NOT NULL THEN
        RAISE EXCEPTION 'Anotação sobrepõe a anotação % da mesma sessão', v_conf
              USING HINT = 'No QGIS ative "Evitar sobreposição", ou chame rotulo.fn_abrir_espaco(sessao_id, geom)';
    END IF;
    RETURN NEW;
END $$;

CREATE TRIGGER tg_anotacao_validar BEFORE INSERT OR UPDATE OR DELETE ON rotulo.anotacao
    FOR EACH ROW EXECUTE FUNCTION rotulo.fn_validar_anotacao();
CREATE TRIGGER tg_anotacao_atualizado_em BEFORE UPDATE ON rotulo.anotacao
    FOR EACH ROW EXECUTE FUNCTION auditoria.fn_tocar_atualizado_em();

-- Operações da cobertura ---------------------------------------------------------

CREATE FUNCTION rotulo.fn_pessoa(p_apelido text) RETURNS integer
LANGUAGE plpgsql STABLE AS $$
DECLARE
    v_id integer;
BEGIN
    SELECT id INTO v_id FROM rotulo.pessoa WHERE apelido = p_apelido AND ativa;
    IF v_id IS NULL THEN
        RAISE EXCEPTION 'Pessoa % não encontrada ou inativa', p_apelido;
    END IF;
    RETURN v_id;
END $$;

CREATE FUNCTION rotulo.fn_iniciar_sessao(p_tarefa_id integer, p_apelido text, p_condicao text DEFAULT 'manual')
RETURNS integer LANGUAGE plpgsql AS $$
DECLARE
    v_id integer;
BEGIN
    INSERT INTO rotulo.sessao (tarefa_id, pessoa_id, condicao_codigo)
    VALUES (p_tarefa_id, rotulo.fn_pessoa(p_apelido), p_condicao) RETURNING id INTO v_id;
    RETURN v_id;
END $$;
COMMENT ON FUNCTION rotulo.fn_iniciar_sessao IS 'Abre uma sessão da pessoa na tarefa e devolve o id (use como sessao_id no QGIS)';

CREATE FUNCTION rotulo.fn_enviar_sessao(p_sessao_id integer, p_tempo_ativo_s integer DEFAULT NULL) RETURNS void
LANGUAGE sql AS $$
    UPDATE rotulo.sessao SET status_codigo = 'enviada', tempo_ativo_s = coalesce(p_tempo_ativo_s, tempo_ativo_s)
     WHERE id = p_sessao_id
$$;

CREATE FUNCTION rotulo.fn_revisar_sessao(p_sessao_id integer, p_revisor text, p_aprovar boolean, p_comentario text DEFAULT NULL)
RETURNS void LANGUAGE sql AS $$
    UPDATE rotulo.sessao
       SET status_codigo = CASE WHEN p_aprovar THEN 'aprovada' ELSE 'rejeitada' END,
           revisor_id = rotulo.fn_pessoa(p_revisor), comentario_revisao = p_comentario
     WHERE id = p_sessao_id
$$;

CREATE FUNCTION rotulo.fn_reabrir_sessao(p_sessao_id integer) RETURNS void
LANGUAGE sql AS $$
    UPDATE rotulo.sessao SET status_codigo = 'em_andamento' WHERE id = p_sessao_id
$$;

CREATE FUNCTION rotulo.fn_abrir_espaco(p_sessao_id integer, p_geom geometry) RETURNS integer
LANGUAGE plpgsql AS $$
DECLARE
    n_del integer;
    n_upd integer;
BEGIN
    DELETE FROM rotulo.anotacao a
     WHERE a.sessao_id = p_sessao_id AND ST_CoveredBy(a.geom, p_geom);
    GET DIAGNOSTICS n_del = ROW_COUNT;
    UPDATE rotulo.anotacao a
       SET geom = auditoria.fn_multipoligono(ST_Difference(a.geom, p_geom))
     WHERE a.sessao_id = p_sessao_id AND a.geom && p_geom
       AND ST_Area(ST_Intersection(a.geom, p_geom)) > 0.01;
    GET DIAGNOSTICS n_upd = ROW_COUNT;
    RETURN n_del + n_upd;
END $$;
COMMENT ON FUNCTION rotulo.fn_abrir_espaco IS 'Desenhar por cima: subtrai p_geom das anotações da sessão (a nova vence)';

-- Séries: criar e propagar -----------------------------------------------------

CREATE FUNCTION rotulo.fn_criar_serie(p_campanha_id integer, p_produto text, p_geom geometry,
                                      p_data_inicio date, p_data_fim date) RETURNS integer
LANGUAGE plpgsql AS $$
DECLARE
    v_serie integer;
BEGIN
    INSERT INTO rotulo.serie (campanha_id, produto_codigo, geom)
    VALUES (p_campanha_id, p_produto, ST_MakeValid(p_geom)) RETURNING id INTO v_serie;

    INSERT INTO rotulo.tarefa (campanha_id, imagem_id, data_referencia, geom, serie_id, modo_selecao_codigo, motivo)
    SELECT p_campanha_id, i.id, i.data_referencia, p_geom, v_serie, 'conveniencia', format('série %s', v_serie)
      FROM catalogo.imagem i
      JOIN dominio.status_qc q ON q.codigo = i.qc_status_codigo
     WHERE i.produto_codigo = p_produto AND i.ativa AND q.aceita_rotulo
       AND i.data_referencia BETWEEN p_data_inicio AND p_data_fim
     ORDER BY i.data_referencia;
    RETURN v_serie;
END $$;
COMMENT ON FUNCTION rotulo.fn_criar_serie IS 'Cria a série e uma tarefa por imagem do produto no período (QC aceito)';

-- Copia as anotações de uma sessão para uma tarefa de outra data da mesma série.
-- O rotulador edita só o que mudou; anotacao.editada registra o que foi alterado.
CREATE FUNCTION rotulo.fn_propagar_sessao(p_sessao_origem_id integer, p_tarefa_destino_id integer, p_apelido text)
RETURNS integer LANGUAGE plpgsql AS $$
DECLARE
    v_orig   record;
    v_serie  integer;
    v_nova   integer;
BEGIN
    SELECT s.status_codigo, t.serie_id, t.id AS tarefa_id INTO v_orig
      FROM rotulo.sessao s JOIN rotulo.tarefa t ON t.id = s.tarefa_id WHERE s.id = p_sessao_origem_id;
    SELECT serie_id INTO v_serie FROM rotulo.tarefa WHERE id = p_tarefa_destino_id;

    IF v_orig.serie_id IS NULL OR v_serie IS DISTINCT FROM v_orig.serie_id THEN
        RAISE EXCEPTION 'Origem e destino precisam ser tarefas da mesma série';
    END IF;
    IF v_orig.tarefa_id = p_tarefa_destino_id THEN
        RAISE EXCEPTION 'Destino igual à origem';
    END IF;
    IF v_orig.status_codigo NOT IN ('enviada', 'aprovada') THEN
        RAISE EXCEPTION 'Só se propaga sessão enviada ou aprovada (origem está %)', v_orig.status_codigo;
    END IF;

    INSERT INTO rotulo.sessao (tarefa_id, pessoa_id, condicao_codigo, sessao_origem_id)
    VALUES (p_tarefa_destino_id, rotulo.fn_pessoa(p_apelido), 'propagada', p_sessao_origem_id)
    RETURNING id INTO v_nova;

    INSERT INTO rotulo.anotacao (sessao_id, tarefa_id, data_referencia, classe_id, geom, certeza_codigo,
                                 origem_codigo, anotacao_origem_id, objeto_id)
    SELECT v_nova, p_tarefa_destino_id, '-infinity', a.classe_id, a.geom, a.certeza_codigo,
           'propagada', a.id, a.objeto_id
      FROM rotulo.anotacao a WHERE a.sessao_id = p_sessao_origem_id
     ORDER BY a.id;
    RETURN v_nova;
END $$;


-- =============================================================================
-- ROTULAGEM — mudança: eventos e controles estáveis
-- =============================================================================

CREATE TABLE rotulo.evento (
    id                     integer GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_evento PRIMARY KEY,
    campanha_id            integer NOT NULL REFERENCES rotulo.campanha (id),
    pessoa_id              integer NOT NULL REFERENCES rotulo.pessoa (id),
    tipo_alteracao_codigo  text    NOT NULL REFERENCES dominio.tipo_alteracao (codigo),
    classe_de_id           integer NOT NULL REFERENCES dominio.classe (id),
    classe_para_id         integer NOT NULL REFERENCES dominio.classe (id),
    estagio_codigo         text    NOT NULL DEFAULT 'novo' REFERENCES dominio.estagio (codigo),
    mes_inicio             date    NOT NULL,
    mes_inicio_min         date    NOT NULL,
    mes_inicio_max         date    NOT NULL,
    mes_visivel_completo   date,
    certeza_codigo         text    NOT NULL DEFAULT 'alta' REFERENCES dominio.nivel_certeza (codigo),
    objeto_id              bigint  REFERENCES rotulo.objeto (id),
    geom                   geometry(MultiPolygon, 32723) NOT NULL,
    area_m2                double precision GENERATED ALWAYS AS (ST_Area(geom)) STORED,
    modo_selecao_codigo    text    NOT NULL DEFAULT 'conveniencia' REFERENCES dominio.modo_selecao (codigo),
    status_revisao_codigo  text    NOT NULL DEFAULT 'nao_revisado' REFERENCES dominio.status_revisao (codigo),
    revisor_id             integer REFERENCES rotulo.pessoa (id),
    revisada_em            timestamptz,
    comentario_revisao     text,
    observacao             text,
    criado_em              timestamptz NOT NULL DEFAULT now(),
    atualizado_em          timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT ck_evento_meses_dia1 CHECK (extract(day FROM mes_inicio) = 1 AND extract(day FROM mes_inicio_min) = 1
                                           AND extract(day FROM mes_inicio_max) = 1
                                           AND (mes_visivel_completo IS NULL OR extract(day FROM mes_visivel_completo) = 1)),
    CONSTRAINT ck_evento_intervalo CHECK (mes_inicio_min <= mes_inicio AND mes_inicio <= mes_inicio_max),
    CONSTRAINT ck_evento_completo CHECK (mes_visivel_completo IS NULL OR mes_visivel_completo >= mes_inicio),
    CONSTRAINT ck_evento_revisor_diferente CHECK (revisor_id IS NULL OR revisor_id <> pessoa_id)
);
COMMENT ON TABLE  rotulo.evento IS 'Mudança real observada na série (referencia_eventos da skill rotulagem-referencia)';
COMMENT ON COLUMN rotulo.evento.mes_inicio IS 'Primeiro mês em que a mudança é visível (dia 1). O mês anterior é o último sem a mudança';
COMMENT ON COLUMN rotulo.evento.mes_inicio_min IS 'Intervalo possível do início quando há meses nublados ou com cor discrepante';
COMMENT ON COLUMN rotulo.evento.mes_visivel_completo IS 'Mês em que a obra/supressão termina (opcional)';
COMMENT ON COLUMN rotulo.evento.geom IS 'Extensão visível no último mês em que o evento está completo';
COMMENT ON COLUMN rotulo.evento.modo_selecao_codigo IS 'Como o local foi achado (estratos da skill: candidatos do baseline, aleatório, conhecido)';
CREATE INDEX ix_evento_geom      ON rotulo.evento USING gist (geom);
CREATE INDEX ix_evento_campanha  ON rotulo.evento (campanha_id);
CREATE INDEX ix_evento_inicio    ON rotulo.evento (mes_inicio);

CREATE TABLE rotulo.evento_evidencia (
    evento_id      integer NOT NULL REFERENCES rotulo.evento (id) ON DELETE CASCADE,
    imagem_id      integer NOT NULL REFERENCES catalogo.imagem (id),
    papel_codigo   text    NOT NULL REFERENCES dominio.papel_evidencia (codigo),
    observacao     text,
    CONSTRAINT pk_evento_evidencia PRIMARY KEY (evento_id, imagem_id, papel_codigo)
);
COMMENT ON TABLE rotulo.evento_evidencia IS 'Imagens que sustentam o evento: última sem mudança, primeira com mudança, completa e confirmação';

CREATE TABLE rotulo.controle_estavel (
    id                          integer GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_controle PRIMARY KEY,
    campanha_id                 integer NOT NULL REFERENCES rotulo.campanha (id),
    pessoa_id                   integer NOT NULL REFERENCES rotulo.pessoa (id),
    tipo_superficie_codigo      text    NOT NULL REFERENCES dominio.tipo_superficie_estavel (codigo),
    classe_id                   integer NOT NULL REFERENCES dominio.classe (id),
    periodo_inicio              date    NOT NULL,
    periodo_fim                 date    NOT NULL,
    imagem_inicio_id            integer NOT NULL REFERENCES catalogo.imagem (id),
    imagem_fim_id               integer NOT NULL REFERENCES catalogo.imagem (id),
    geom                        geometry(MultiPolygon, 32723) NOT NULL,
    area_m2                     double precision GENERATED ALWAYS AS (ST_Area(geom)) STORED,
    status_revisao_codigo       text    NOT NULL DEFAULT 'nao_revisado' REFERENCES dominio.status_revisao (codigo),
    revisor_id                  integer REFERENCES rotulo.pessoa (id),
    revisada_em                 timestamptz,
    observacao                  text,
    criado_em                   timestamptz NOT NULL DEFAULT now(),
    atualizado_em               timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT ck_controle_periodo CHECK (periodo_fim > periodo_inicio),
    CONSTRAINT ck_controle_revisor_diferente CHECK (revisor_id IS NULL OR revisor_id <> pessoa_id)
);
COMMENT ON TABLE  rotulo.controle_estavel IS 'Área que NÃO muda no período: mede falso alarme por km²·mês e deriva de cor';
COMMENT ON COLUMN rotulo.controle_estavel.imagem_inicio_id IS 'Imagem do início do período em que a estabilidade foi conferida';
CREATE INDEX ix_controle_geom ON rotulo.controle_estavel USING gist (geom);

-- Regras comuns de evento e controle ----------------------------------------------
CREATE FUNCTION rotulo.fn_validar_evento() RETURNS trigger
LANGUAGE plpgsql AS $$
DECLARE
    v_tax     integer;
    v_ext     geometry;
    v_de      dominio.classe;
    v_para    dominio.classe;
    v_restr   boolean;
    v_conf    integer;
BEGIN
    SELECT c.taxonomia_id, ST_Expand(ST_Envelope(a.geom), 100) INTO v_tax, v_ext
      FROM rotulo.campanha c JOIN catalogo.aoi a ON a.id = c.aoi_id WHERE c.id = NEW.campanha_id;
    SELECT * INTO v_de   FROM dominio.classe WHERE id = NEW.classe_de_id;
    SELECT * INTO v_para FROM dominio.classe WHERE id = NEW.classe_para_id;

    IF v_de.taxonomia_id <> v_tax OR v_para.taxonomia_id <> v_tax
       OR v_de.tipo <> 'cobertura' OR v_para.tipo <> 'cobertura'
       OR v_de.valor_raster IS NULL OR v_para.valor_raster IS NULL THEN
        RAISE EXCEPTION 'Evento: de e para precisam ser classes folha de cobertura da taxonomia da campanha';
    END IF;

    SELECT restringe_transicao INTO v_restr FROM dominio.tipo_alteracao WHERE codigo = NEW.tipo_alteracao_codigo;
    IF v_restr AND NOT EXISTS (
           SELECT 1 FROM dominio.transicao_permitida tp
            WHERE tp.taxonomia_id = v_tax AND tp.tipo_alteracao_codigo = NEW.tipo_alteracao_codigo
              AND tp.classe_de_id = NEW.classe_de_id AND tp.classe_para_id = NEW.classe_para_id) THEN
        RAISE EXCEPTION 'Transição % → % não é permitida para %', v_de.codigo, v_para.codigo, NEW.tipo_alteracao_codigo;
    END IF;
    IF NEW.classe_de_id = NEW.classe_para_id AND NEW.estagio_codigo <> 'em_expansao' AND NOT v_restr THEN
        RAISE EXCEPTION 'classe_de igual a classe_para só em estágio em_expansao ou em transição permitida';
    END IF;

    IF NEW.status_revisao_codigo <> 'nao_revisado' AND NEW.revisor_id IS NULL THEN
        RAISE EXCEPTION 'Informe revisor_id para confirmar ou rejeitar';
    END IF;
    IF TG_OP = 'INSERT' OR NEW.status_revisao_codigo IS DISTINCT FROM OLD.status_revisao_codigo THEN
        NEW.revisada_em := CASE WHEN NEW.status_revisao_codigo = 'nao_revisado' THEN NULL ELSE now() END;
    END IF;

    NEW.geom := auditoria.fn_multipoligono(NEW.geom);
    IF ST_IsEmpty(NEW.geom) OR NOT ST_CoveredBy(NEW.geom, v_ext) THEN
        RAISE EXCEPTION 'Evento vazio ou fora da área da campanha';
    END IF;

    IF NEW.status_revisao_codigo <> 'rejeitado' THEN
        SELECT ce.id INTO v_conf
          FROM rotulo.controle_estavel ce
         WHERE ce.campanha_id = NEW.campanha_id AND ce.status_revisao_codigo <> 'rejeitado'
           AND NEW.mes_inicio BETWEEN ce.periodo_inicio AND ce.periodo_fim
           AND ce.geom && NEW.geom AND ST_Area(ST_Intersection(ce.geom, NEW.geom)) > 0.01
         LIMIT 1;
        IF v_conf IS NOT NULL THEN
            RAISE EXCEPTION 'Evento cai no controle estável % ativo no período', v_conf
                  USING HINT = 'Se a mudança é real, rejeite ou reduza o controle antes de registrar o evento';
        END IF;
    END IF;
    RETURN NEW;
END $$;

CREATE TRIGGER tg_evento_validar BEFORE INSERT OR UPDATE ON rotulo.evento
    FOR EACH ROW EXECUTE FUNCTION rotulo.fn_validar_evento();
CREATE TRIGGER tg_evento_atualizado_em BEFORE UPDATE ON rotulo.evento
    FOR EACH ROW EXECUTE FUNCTION auditoria.fn_tocar_atualizado_em();

CREATE FUNCTION rotulo.fn_validar_evidencia() RETURNS trigger
LANGUAGE plpgsql AS $$
DECLARE
    v_ev   rotulo.evento;
    v_mes  date;
BEGIN
    SELECT * INTO v_ev FROM rotulo.evento WHERE id = NEW.evento_id;
    SELECT date_trunc('month', data_referencia)::date INTO v_mes FROM catalogo.imagem WHERE id = NEW.imagem_id;
    IF NEW.papel_codigo = 'antes' AND v_mes >= v_ev.mes_inicio_min THEN
        RAISE EXCEPTION 'Evidência "antes" (%) precisa ser anterior ao início mais cedo possível (%)', v_mes, v_ev.mes_inicio_min;
    ELSIF NEW.papel_codigo = 'inicio' AND v_mes NOT BETWEEN v_ev.mes_inicio_min AND v_ev.mes_inicio_max THEN
        RAISE EXCEPTION 'Evidência "inicio" (%) fora do intervalo do início (% a %)', v_mes, v_ev.mes_inicio_min, v_ev.mes_inicio_max;
    ELSIF NEW.papel_codigo IN ('completo', 'confirmacao') AND v_mes < v_ev.mes_inicio_min THEN
        RAISE EXCEPTION 'Evidência "%" (%) anterior ao início do evento', NEW.papel_codigo, v_mes;
    END IF;
    RETURN NEW;
END $$;
CREATE TRIGGER tg_evidencia_validar BEFORE INSERT OR UPDATE ON rotulo.evento_evidencia
    FOR EACH ROW EXECUTE FUNCTION rotulo.fn_validar_evidencia();

CREATE FUNCTION rotulo.fn_validar_controle() RETURNS trigger
LANGUAGE plpgsql AS $$
DECLARE
    v_tax     integer;
    v_ext     geometry;
    v_classe  dominio.classe;
    v_ini     date;
    v_fim     date;
    v_conf    integer;
BEGIN
    SELECT c.taxonomia_id, ST_Expand(ST_Envelope(a.geom), 100) INTO v_tax, v_ext
      FROM rotulo.campanha c JOIN catalogo.aoi a ON a.id = c.aoi_id WHERE c.id = NEW.campanha_id;
    SELECT * INTO v_classe FROM dominio.classe WHERE id = NEW.classe_id;
    IF v_classe.taxonomia_id <> v_tax OR v_classe.tipo <> 'cobertura' OR v_classe.valor_raster IS NULL THEN
        RAISE EXCEPTION 'Controle: classe precisa ser folha de cobertura da taxonomia da campanha';
    END IF;

    SELECT data_referencia INTO v_ini FROM catalogo.imagem WHERE id = NEW.imagem_inicio_id;
    SELECT data_referencia INTO v_fim FROM catalogo.imagem WHERE id = NEW.imagem_fim_id;
    IF v_ini > NEW.periodo_inicio + 31 OR v_fim < NEW.periodo_fim - 31 THEN
        RAISE EXCEPTION 'Controle: as imagens de conferência precisam estar nas pontas do período (± 1 mês)';
    END IF;

    IF NEW.status_revisao_codigo <> 'nao_revisado' AND NEW.revisor_id IS NULL THEN
        RAISE EXCEPTION 'Informe revisor_id para confirmar ou rejeitar';
    END IF;
    IF TG_OP = 'INSERT' OR NEW.status_revisao_codigo IS DISTINCT FROM OLD.status_revisao_codigo THEN
        NEW.revisada_em := CASE WHEN NEW.status_revisao_codigo = 'nao_revisado' THEN NULL ELSE now() END;
    END IF;

    NEW.geom := auditoria.fn_multipoligono(NEW.geom);
    IF ST_IsEmpty(NEW.geom) OR NOT ST_CoveredBy(NEW.geom, v_ext) THEN
        RAISE EXCEPTION 'Controle vazio ou fora da área da campanha';
    END IF;

    IF NEW.status_revisao_codigo <> 'rejeitado' THEN
        SELECT e.id INTO v_conf
          FROM rotulo.evento e
         WHERE e.campanha_id = NEW.campanha_id AND e.status_revisao_codigo <> 'rejeitado'
           AND e.mes_inicio BETWEEN NEW.periodo_inicio AND NEW.periodo_fim
           AND e.geom && NEW.geom AND ST_Area(ST_Intersection(e.geom, NEW.geom)) > 0.01
         LIMIT 1;
        IF v_conf IS NOT NULL THEN
            RAISE EXCEPTION 'Controle estável sobrepõe o evento % no período', v_conf;
        END IF;
    END IF;
    RETURN NEW;
END $$;

CREATE TRIGGER tg_controle_validar BEFORE INSERT OR UPDATE ON rotulo.controle_estavel
    FOR EACH ROW EXECUTE FUNCTION rotulo.fn_validar_controle();
CREATE TRIGGER tg_controle_atualizado_em BEFORE UPDATE ON rotulo.controle_estavel
    FOR EACH ROW EXECUTE FUNCTION auditoria.fn_tocar_atualizado_em();

CREATE FUNCTION rotulo.fn_revisar_evento(p_evento_id integer, p_revisor text, p_confirmar boolean, p_comentario text DEFAULT NULL)
RETURNS void LANGUAGE sql AS $$
    UPDATE rotulo.evento
       SET status_revisao_codigo = CASE WHEN p_confirmar THEN 'confirmado' ELSE 'rejeitado' END,
           revisor_id = rotulo.fn_pessoa(p_revisor), comentario_revisao = p_comentario
     WHERE id = p_evento_id
$$;

CREATE FUNCTION rotulo.fn_revisar_controle(p_controle_id integer, p_revisor text, p_confirmar boolean)
RETURNS void LANGUAGE sql AS $$
    UPDATE rotulo.controle_estavel
       SET status_revisao_codigo = CASE WHEN p_confirmar THEN 'confirmado' ELSE 'rejeitado' END,
           revisor_id = rotulo.fn_pessoa(p_revisor)
     WHERE id = p_controle_id
$$;

-- Sorteio de pontos (células de 1 pixel) num estrato, para avaliação independente.
CREATE FUNCTION rotulo.fn_sortear_pontos(p_estrato_id integer, p_imagem_id integer, p_n integer) RETURNS integer
LANGUAGE plpgsql AS $$
DECLARE
    v_e     record;
    v_g     catalogo.grade;
    v_total integer;
    n       integer;
BEGIN
    SELECT e.geom, e.codigo, pl.semente, pl.campanha_id, pl.codigo AS plano INTO v_e
      FROM rotulo.estrato e JOIN rotulo.plano_amostral pl ON pl.id = e.plano_id WHERE e.id = p_estrato_id;
    SELECT g.* INTO v_g
      FROM catalogo.imagem i JOIN catalogo.produto p ON p.codigo = i.produto_codigo JOIN catalogo.grade g ON g.id = p.grade_id
     WHERE i.id = p_imagem_id;

    CREATE TEMP TABLE IF NOT EXISTS pg_temp.celula_sorteio (c int, l int, geom geometry) ON COMMIT DROP;
    TRUNCATE pg_temp.celula_sorteio;
    INSERT INTO pg_temp.celula_sorteio
    SELECT c, l, cel
      FROM generate_series(greatest(0, floor((ST_XMin(v_e.geom) - v_g.origem_x) / v_g.pixel_x)::int),
                           least(v_g.largura - 1, ceil((ST_XMax(v_e.geom) - v_g.origem_x) / v_g.pixel_x)::int - 1)) AS c,
           generate_series(greatest(0, floor((v_g.origem_y - ST_YMax(v_e.geom)) / -v_g.pixel_y)::int),
                           least(v_g.altura - 1, ceil((v_g.origem_y - ST_YMin(v_e.geom)) / -v_g.pixel_y)::int - 1)) AS l
     CROSS JOIN LATERAL (SELECT ST_MakeEnvelope(v_g.origem_x + c * v_g.pixel_x, v_g.origem_y + (l + 1) * v_g.pixel_y,
                                                v_g.origem_x + (c + 1) * v_g.pixel_x, v_g.origem_y + l * v_g.pixel_y, 32723) AS cel) x
     WHERE ST_CoveredBy(cel, v_e.geom)
       AND NOT EXISTS (SELECT 1 FROM rotulo.tarefa t
                        WHERE t.imagem_id = p_imagem_id AND t.campanha_id = v_e.campanha_id AND NOT t.descartada
                          AND t.geom && cel AND ST_Area(ST_Intersection(t.geom, cel)) > 0.01);
    SELECT count(*) INTO v_total FROM pg_temp.celula_sorteio;
    IF v_total < p_n THEN
        RAISE EXCEPTION 'Estrato % tem % células livres; pedido %', v_e.codigo, v_total, p_n;
    END IF;

    INSERT INTO rotulo.tarefa (campanha_id, imagem_id, data_referencia, geom, modo_selecao_codigo, estrato_id, prob_inclusao, motivo)
    SELECT v_e.campanha_id, p_imagem_id, '-infinity', cs.geom, 'estratificada', p_estrato_id, p_n::double precision / v_total,
           format('plano %s, estrato %s, célula (%s,%s)', v_e.plano, v_e.codigo, cs.c, cs.l)
      FROM pg_temp.celula_sorteio cs
     ORDER BY md5(v_e.semente || ':' || p_estrato_id || ':' || cs.c || ':' || cs.l)
     LIMIT p_n;
    GET DIAGNOSTICS n = ROW_COUNT;
    RETURN n;
END $$;
COMMENT ON FUNCTION rotulo.fn_sortear_pontos IS 'Sorteia n células de pixel livres no estrato (semente do plano) e cria tarefas com prob_inclusao = n / células livres';

-- Visões da rotulagem ------------------------------------------------------------

CREATE VIEW rotulo.vw_tarefa AS
SELECT t.id, t.campanha_id, c.codigo AS campanha, t.imagem_id, i.produto_codigo, i.arquivo,
       t.data_referencia, i.mes_referencia, t.serie_id, t.modo_selecao_codigo, t.estrato_id, t.prob_inclusao,
       t.ciclo_id, t.incerteza, t.prioridade, t.motivo, t.descartada,
       CASE WHEN t.descartada                              THEN 'descartada'
            WHEN bool_or(s.status_codigo = 'aprovada')     THEN 'aprovada'
            WHEN bool_or(s.status_codigo = 'enviada')      THEN 'em_revisao'
            WHEN bool_or(s.status_codigo = 'em_andamento') THEN 'em_rotulagem'
            WHEN count(s.id) > 0                           THEN 'rejeitada'
            ELSE 'aberta' END                              AS situacao,
       max(s.id) FILTER (WHERE s.status_codigo = 'aprovada') AS sessao_referencia_id,
       count(s.id)                                         AS n_sessoes,
       t.area_m2, t.geom
  FROM rotulo.tarefa t
  JOIN rotulo.campanha c ON c.id = t.campanha_id
  JOIN catalogo.imagem i ON i.id = t.imagem_id
  LEFT JOIN rotulo.sessao s ON s.tarefa_id = t.id
 GROUP BY t.id, c.codigo, i.produto_codigo, i.arquivo, i.mes_referencia;
COMMENT ON VIEW rotulo.vw_tarefa IS 'Tarefa com situação derivada das sessões e a sessão de referência (chave: id)';

CREATE VIEW rotulo.vw_anotacao AS
SELECT a.id, a.sessao_id, a.tarefa_id, s.status_codigo AS status_sessao, p.apelido AS rotulador,
       t.imagem_id, i.produto_codigo, a.data_referencia, i.mes_referencia, t.serie_id, a.objeto_id,
       a.classe_id, k.codigo AS classe, k.nome AS classe_nome, r.codigo AS macroclasse,
       k.tipo, k.valor_raster, k.cor_hex, a.certeza_codigo, a.origem_codigo, a.editada,
       a.area_m2, a.geom
  FROM rotulo.anotacao a
  JOIN rotulo.sessao s   ON s.id = a.sessao_id
  JOIN rotulo.pessoa p   ON p.id = s.pessoa_id
  JOIN rotulo.tarefa t   ON t.id = a.tarefa_id
  JOIN catalogo.imagem i ON i.id = t.imagem_id
  JOIN dominio.classe k  ON k.id = a.classe_id
  JOIN dominio.classe r  ON r.id = k.classe_pai_id;
COMMENT ON VIEW rotulo.vw_anotacao IS 'Todas as anotações (revisão e curadoria; NÃO usar para rotular em dupla: use vw_minha_anotacao)';

-- Trabalho cego: cada pessoa vê e edita só as próprias anotações (atualizável no QGIS).
CREATE VIEW rotulo.vw_minha_anotacao AS
SELECT a.*
  FROM rotulo.anotacao a
 WHERE a.sessao_id IN (SELECT s.id FROM rotulo.sessao s JOIN rotulo.pessoa p ON p.id = s.pessoa_id
                        WHERE p.apelido = auditoria.fn_usuario())
  WITH LOCAL CHECK OPTION;
COMMENT ON VIEW rotulo.vw_minha_anotacao IS 'Camada de edição do rotulador: só as sessões do usuário corrente (login ou app.usuario). Garante rotulagem cega';

CREATE VIEW rotulo.vw_lacuna AS
SELECT s.id, s.tarefa_id, s.status_codigo, l.geom, ST_Area(l.geom) AS area_m2
  FROM rotulo.sessao s
 CROSS JOIN LATERAL (SELECT rotulo.fn_lacuna(s.id) AS geom) l
 WHERE s.status_codigo = 'em_andamento' AND NOT ST_IsEmpty(l.geom);
COMMENT ON VIEW rotulo.vw_lacuna IS 'O que falta classificar em cada sessão em andamento (chave: id = sessao_id)';

CREATE VIEW rotulo.vw_concordancia AS
WITH sessoes AS (
    SELECT s.id, s.tarefa_id FROM rotulo.sessao s
     WHERE s.status_codigo IN ('enviada', 'aprovada', 'rejeitada') AND s.condicao_codigo <> 'propagada'
), pares AS (
    SELECT a.tarefa_id, a.id AS sessao_a, b.id AS sessao_b
      FROM sessoes a JOIN sessoes b ON b.tarefa_id = a.tarefa_id AND b.id > a.id
), por_classe AS (
    SELECT sessao_id, classe_id, ST_Union(geom) AS geom
      FROM rotulo.anotacao WHERE sessao_id IN (SELECT id FROM sessoes)
     GROUP BY sessao_id, classe_id
), cruzado AS (
    SELECT p.tarefa_id, p.sessao_a, p.sessao_b, k.classe_id,
           coalesce(ST_Area(ST_Intersection(ca.geom, cb.geom)), 0) AS inter_m2,
           coalesce(ST_Area(ca.geom), 0) + coalesce(ST_Area(cb.geom), 0)
             - coalesce(ST_Area(ST_Intersection(ca.geom, cb.geom)), 0) AS uniao_m2
      FROM pares p
     CROSS JOIN LATERAL (SELECT classe_id FROM por_classe WHERE sessao_id IN (p.sessao_a, p.sessao_b) GROUP BY classe_id) k
      LEFT JOIN por_classe ca ON ca.sessao_id = p.sessao_a AND ca.classe_id = k.classe_id
      LEFT JOIN por_classe cb ON cb.sessao_id = p.sessao_b AND cb.classe_id = k.classe_id
)
SELECT row_number() OVER (ORDER BY x.tarefa_id, x.sessao_a, x.sessao_b, x.classe_id) AS id,
       x.tarefa_id, x.sessao_a, x.sessao_b, c.codigo AS classe,
       round((x.inter_m2 / nullif(x.uniao_m2, 0))::numeric, 3) AS iou,
       round((sum(x.inter_m2) OVER (PARTITION BY x.tarefa_id, x.sessao_a, x.sessao_b) / t.area_m2)::numeric, 3) AS acordo_global
  FROM cruzado x
  JOIN dominio.classe c ON c.id = x.classe_id
  JOIN rotulo.tarefa t  ON t.id = x.tarefa_id;
COMMENT ON VIEW rotulo.vw_concordancia IS 'Concordância de cobertura entre sessões independentes (não propagadas) da mesma tarefa';

-- Concordância de eventos: pares de intérpretes diferentes com IoU >= 0,25 (critério do SpaceNet 7).
CREATE VIEW rotulo.vw_concordancia_evento AS
SELECT row_number() OVER (ORDER BY a.id, b.id) AS id,
       a.campanha_id, a.id AS evento_a, b.id AS evento_b, pa.apelido AS interprete_a, pb.apelido AS interprete_b,
       round(x.iou::numeric, 3) AS iou,
       a.tipo_alteracao_codigo = b.tipo_alteracao_codigo AS mesmo_tipo,
       (a.classe_de_id, a.classe_para_id) = (b.classe_de_id, b.classe_para_id) AS mesma_transicao,
       abs(auditoria.fn_meses(a.mes_inicio, b.mes_inicio)) AS dif_mes_inicio,
       abs(auditoria.fn_meses(a.mes_inicio, b.mes_inicio)) <= 1 AS mes_concorda
  FROM rotulo.evento a
  JOIN rotulo.evento b ON b.campanha_id = a.campanha_id AND b.id > a.id AND b.pessoa_id <> a.pessoa_id AND b.geom && a.geom
  JOIN rotulo.pessoa pa ON pa.id = a.pessoa_id
  JOIN rotulo.pessoa pb ON pb.id = b.pessoa_id
 CROSS JOIN LATERAL (SELECT ST_Area(ST_Intersection(a.geom, b.geom)) / nullif(ST_Area(ST_Union(a.geom, b.geom)), 0) AS iou) x
 WHERE x.iou >= 0.25
   AND a.status_revisao_codigo <> 'rejeitado' AND b.status_revisao_codigo <> 'rejeitado';
COMMENT ON VIEW rotulo.vw_concordancia_evento IS 'Acordo de existência (IoU ≥ 0,25), de tipo e de mês de início (± 1) entre intérpretes';

-- Mudança derivada da série de máscaras: datas aprovadas consecutivas com classe diferente.
CREATE VIEW rotulo.vw_mudanca_derivada AS
WITH ref AS (
    SELECT t.serie_id, t.data_referencia, s.id AS sessao_id,
           lag(s.id)              OVER w AS sessao_antes,
           lag(t.data_referencia) OVER w AS data_antes
      FROM rotulo.tarefa t
      JOIN rotulo.sessao s ON s.tarefa_id = t.id AND s.status_codigo = 'aprovada'
     WHERE t.serie_id IS NOT NULL AND NOT t.descartada
    WINDOW w AS (PARTITION BY t.serie_id ORDER BY t.data_referencia)
)
SELECT row_number() OVER (ORDER BY r.serie_id, r.data_referencia, a.id, b.id) AS id,
       r.serie_id, r.data_antes, r.data_referencia AS data_depois,
       a.objeto_id, cd.codigo AS classe_de, cp.codigo AS classe_para,
       (SELECT array_agg(DISTINCT tp.tipo_alteracao_codigo ORDER BY tp.tipo_alteracao_codigo)
          FROM dominio.transicao_permitida tp
         WHERE tp.classe_de_id = a.classe_id AND tp.classe_para_id = b.classe_id) AS tipos_candidatos,
       ST_Area(g.geom) AS area_m2, g.geom
  FROM ref r
  JOIN rotulo.anotacao a ON a.sessao_id = r.sessao_antes
  JOIN rotulo.anotacao b ON b.sessao_id = r.sessao_id AND b.geom && a.geom AND b.classe_id <> a.classe_id
  JOIN dominio.classe cd ON cd.id = a.classe_id AND cd.tipo = 'cobertura'
  JOIN dominio.classe cp ON cp.id = b.classe_id AND cp.tipo = 'cobertura'
 CROSS JOIN LATERAL (SELECT auditoria.fn_multipoligono(ST_Intersection(a.geom, b.geom)) AS geom) g
 WHERE r.sessao_antes IS NOT NULL AND ST_Area(g.geom) > 0.01;
COMMENT ON VIEW rotulo.vw_mudanca_derivada IS 'Pós-classificação da série rotulada: onde a classe mudou entre datas aprovadas consecutivas';

-- Amostra de avaliação: classe de referência e peso de cada ponto sorteado.
CREATE VIEW rotulo.vw_amostra_avaliacao AS
SELECT t.id AS tarefa_id, pl.codigo AS plano, e.codigo AS estrato, e.area_m2 AS area_estrato_m2, e.n_alvo,
       t.prob_inclusao, 1 / t.prob_inclusao AS peso, t.data_referencia, t.imagem_id,
       vt.situacao, ref.classe AS classe_referencia, ref.certeza_codigo, t.geom
  FROM rotulo.tarefa t
  JOIN rotulo.estrato e         ON e.id = t.estrato_id
  JOIN rotulo.plano_amostral pl ON pl.id = e.plano_id
  JOIN rotulo.vw_tarefa vt      ON vt.id = t.id
  LEFT JOIN LATERAL (
        SELECT k.codigo AS classe, a.certeza_codigo FROM rotulo.anotacao a JOIN dominio.classe k ON k.id = a.classe_id
         WHERE a.sessao_id = vt.sessao_referencia_id ORDER BY a.area_m2 DESC LIMIT 1) ref ON true
 WHERE pl.uso = 'avaliacao_independente';
COMMENT ON VIEW rotulo.vw_amostra_avaliacao IS 'Pontos da avaliação independente com estrato e peso, para o estimador estratificado (Olofsson 2014)';

CREATE VIEW rotulo.vw_progresso AS
SELECT t.campanha, t.produto_codigo, t.modo_selecao_codigo, t.situacao, count(*) AS n_tarefas,
       round((sum(t.area_m2) / 10000)::numeric, 2) AS area_ha
  FROM rotulo.vw_tarefa t
 GROUP BY t.campanha, t.produto_codigo, t.modo_selecao_codigo, t.situacao
 ORDER BY 1, 2, 3, 4;


-- =============================================================================
-- TREINO
-- =============================================================================

CREATE TABLE treino.divisao (
    id                     integer GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_divisao PRIMARY KEY,
    codigo                 text    NOT NULL CONSTRAINT uq_divisao_codigo UNIQUE,
    grade_id               integer NOT NULL REFERENCES catalogo.grade (id),
    tamanho_bloco_m        real    NOT NULL CONSTRAINT ck_divisao_bloco CHECK (tamanho_bloco_m > 0),
    folga_m                real    NOT NULL DEFAULT 0 CONSTRAINT ck_divisao_folga CHECK (folga_m >= 0),
    semente                integer NOT NULL,
    prop_treino            numeric(4,3) NOT NULL,
    prop_validacao         numeric(4,3) NOT NULL,
    prop_teste             numeric(4,3) NOT NULL,
    teste_temporal_inicio  date,
    teste_temporal_fim     date,
    descricao              text,
    limitacao              text,
    criado_em              timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT ck_divisao_proporcoes CHECK (prop_treino + prop_validacao + prop_teste = 1
                                            AND least(prop_treino, prop_validacao, prop_teste) >= 0),
    CONSTRAINT ck_divisao_folga_bloco CHECK (folga_m < tamanho_bloco_m),
    CONSTRAINT ck_divisao_periodo CHECK ((teste_temporal_inicio IS NULL) = (teste_temporal_fim IS NULL)
                                         AND (teste_temporal_fim IS NULL OR teste_temporal_fim >= teste_temporal_inicio))
);
COMMENT ON TABLE  treino.divisao IS 'Divisão espaço-temporal: blocos (espaço) + período reservado (tempo). Nunca por pixel nem por recorte aleatório';
COMMENT ON COLUMN treino.divisao.folga_m IS 'Distância mínima entre áreas úteis de conjuntos diferentes; quem cede é o conjunto de menor ordem';
COMMENT ON COLUMN treino.divisao.teste_temporal_inicio IS 'Período reservado (configs/pipeline.yaml: divisao.periodo_teste_final): nunca entra no ajuste';
COMMENT ON COLUMN treino.divisao.limitacao IS 'O que esta divisão não garante (registrar no relatório)';

CREATE TABLE treino.bloco (
    id           integer GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_bloco PRIMARY KEY,
    divisao_id   integer  NOT NULL REFERENCES treino.divisao (id) ON DELETE CASCADE,
    linha        smallint NOT NULL,
    coluna       smallint NOT NULL,
    papel_codigo text     NOT NULL REFERENCES dominio.papel_conjunto (codigo),
    geom         geometry(Polygon, 32723) NOT NULL,
    geom_util    geometry(MultiPolygon, 32723),
    CONSTRAINT uq_bloco_posicao UNIQUE (divisao_id, linha, coluna),
    CONSTRAINT ck_bloco_papel_espacial CHECK (papel_codigo IN ('treino', 'validacao', 'teste'))
);
COMMENT ON TABLE  treino.bloco IS 'Célula da divisão com seu conjunto espacial';
COMMENT ON COLUMN treino.bloco.geom_util IS 'Bloco menos a folga voltada para blocos de outro conjunto (só o conjunto de menor ordem cede)';
CREATE INDEX ix_bloco_geom      ON treino.bloco USING gist (geom);
CREATE INDEX ix_bloco_geom_util ON treino.bloco USING gist (geom_util);

CREATE FUNCTION treino.fn_gerar_blocos(p_divisao_id integer) RETURNS integer
LANGUAGE plpgsql AS $$
DECLARE
    d treino.divisao;
    n integer;
BEGIN
    SELECT * INTO d FROM treino.divisao WHERE id = p_divisao_id;
    IF EXISTS (SELECT 1 FROM treino.bloco WHERE divisao_id = p_divisao_id) THEN
        RAISE EXCEPTION 'Divisão % já tem blocos', d.codigo;
    END IF;

    WITH celula AS (
        SELECT l, c,
               ST_Intersection(g.geom, ST_MakeEnvelope(
                   g.origem_x + c * d.tamanho_bloco_m, g.origem_y - (l + 1) * d.tamanho_bloco_m,
                   g.origem_x + (c + 1) * d.tamanho_bloco_m, g.origem_y - l * d.tamanho_bloco_m, 32723)) AS geom
          FROM catalogo.grade g,
               generate_series(0, ceil(g.largura * g.pixel_x / d.tamanho_bloco_m)::int - 1) AS c,
               generate_series(0, ceil(g.altura * -g.pixel_y / d.tamanho_bloco_m)::int - 1) AS l
         WHERE g.id = d.grade_id
    ), sorteio AS (
        SELECT celula.*,
               row_number() OVER (ORDER BY md5(d.semente || ':' || l || ':' || c)) AS ordem,
               count(*) OVER () AS total
          FROM celula
    )
    INSERT INTO treino.bloco (divisao_id, linha, coluna, papel_codigo, geom)
    SELECT d.id, l, c,
           CASE WHEN ordem <= round(total * d.prop_treino) THEN 'treino'
                WHEN ordem <= round(total * (d.prop_treino + d.prop_validacao)) THEN 'validacao'
                ELSE 'teste' END,
           geom
      FROM sorteio;
    GET DIAGNOSTICS n = ROW_COUNT;

    -- Folga só onde há vizinho de outro conjunto; cede o conjunto de menor ordem (o teste não perde área).
    UPDATE treino.bloco b
       SET geom_util = CASE WHEN ST_IsEmpty(x.util) THEN NULL ELSE auditoria.fn_multipoligono(x.util) END
      FROM (SELECT b2.id,
                   ST_Difference(b2.geom, coalesce(
                       (SELECT ST_Union(ST_Buffer(nb.geom, d.folga_m, 'join=mitre'))
                          FROM treino.bloco nb
                          JOIN dominio.papel_conjunto pn ON pn.codigo = nb.papel_codigo
                         WHERE nb.divisao_id = b2.divisao_id AND pn.ordem > p2.ordem
                           AND ST_DWithin(nb.geom, b2.geom, d.folga_m)),
                       ST_SetSRID('POLYGON EMPTY'::geometry, 32723))) AS util
              FROM treino.bloco b2
              JOIN dominio.papel_conjunto p2 ON p2.codigo = b2.papel_codigo
             WHERE b2.divisao_id = d.id) x
     WHERE x.id = b.id;
    RETURN n;
END $$;

-- Conjunto de uma geometria numa data:
--   exigir_contido = true  → precisa caber num bloco útil (tarefas);
--   exigir_contido = false → bloco de maior sobreposição, sinalizando se cruza (eventos, controles).
-- Se a data cai no período reservado: teste_temporal (treino/validação) ou teste_espaco_tempo (teste).
CREATE FUNCTION treino.fn_conjunto(p_divisao_id integer, p_geom geometry, p_data date, p_exigir_contido boolean,
                                   OUT bloco_id integer, OUT papel text, OUT cruza_bloco boolean)
LANGUAGE plpgsql STABLE AS $$
DECLARE
    d treino.divisao;
BEGIN
    SELECT * INTO d FROM treino.divisao WHERE id = p_divisao_id;
    IF p_exigir_contido THEN
        SELECT b.id, b.papel_codigo INTO bloco_id, papel
          FROM treino.bloco b
         WHERE b.divisao_id = d.id AND b.geom_util && p_geom AND ST_CoveredBy(p_geom, b.geom_util)
         LIMIT 1;
        cruza_bloco := bloco_id IS NULL;
    ELSE
        SELECT b.id, b.papel_codigo, count(*) OVER () > 1 INTO bloco_id, papel, cruza_bloco
          FROM treino.bloco b
         WHERE b.divisao_id = d.id AND b.geom && p_geom AND ST_Area(ST_Intersection(b.geom, p_geom)) > 0.01
         ORDER BY ST_Area(ST_Intersection(b.geom, p_geom)) DESC
         LIMIT 1;
    END IF;
    IF papel IS NOT NULL AND p_data IS NOT NULL AND d.teste_temporal_inicio IS NOT NULL
       AND p_data BETWEEN d.teste_temporal_inicio AND d.teste_temporal_fim THEN
        papel := CASE WHEN papel = 'teste' THEN 'teste_espaco_tempo' ELSE 'teste_temporal' END;
    END IF;
END $$;

CREATE FUNCTION treino.fn_criar_tarefas_por_bloco(p_campanha_id integer, p_imagem_id integer, p_divisao_id integer,
                                                  p_papeis text[] DEFAULT ARRAY['treino', 'validacao', 'teste'])
RETURNS integer LANGUAGE plpgsql AS $$
DECLARE
    n integer;
BEGIN
    INSERT INTO rotulo.tarefa (campanha_id, imagem_id, data_referencia, geom, modo_selecao_codigo, motivo)
    SELECT p_campanha_id, p_imagem_id, '-infinity', parte.geom, 'sistematica_bloco',
           format('bloco %s (%s,%s) da divisão %s', b.id, b.linha, b.coluna, d.codigo)
      FROM treino.bloco b
      JOIN treino.divisao d   ON d.id = b.divisao_id
      JOIN catalogo.imagem i  ON i.id = p_imagem_id
      JOIN catalogo.produto p ON p.codigo = i.produto_codigo
      JOIN catalogo.grade g   ON g.id = p.grade_id
     CROSS JOIN LATERAL ST_Dump(ST_Intersection(b.geom_util, g.geom)) AS parte
     WHERE b.divisao_id = p_divisao_id AND b.geom_util IS NOT NULL
       AND b.papel_codigo = ANY (p_papeis)
       AND ST_Area(parte.geom) > 0
     ORDER BY b.linha, b.coluna;
    GET DIAGNOSTICS n = ROW_COUNT;
    RETURN n;
END $$;
COMMENT ON FUNCTION treino.fn_criar_tarefas_por_bloco IS 'Uma tarefa por parte de bloco útil (data_referencia vem do gatilho)';

-- Divisão padrão (configs/pipeline.yaml: divisao).
INSERT INTO treino.divisao (codigo, grade_id, tamanho_bloco_m, folga_m, semente, prop_treino, prop_validacao, prop_teste,
                            teste_temporal_inicio, teste_temporal_fim, descricao, limitacao)
SELECT 'blocos_600m_s42', g.id, 600, 100, 42, 0.6, 0.2, 0.2, '2026-01-01', '2026-09-30',
       'Blocos de 600 m, folga de 100 m, semente 42; período reservado 2026-01 a 2026-09',
       'Blocos e folga menores que os 1,6 km / 0,4 km de Zaraza-Aguilera 2022, porque a AOI tem ~3 km: '
       'há autocorrelação espacial residual entre conjuntos. Uma só AOI: não mede generalização para outras áreas (roteiro, fase 8)'
  FROM catalogo.grade g WHERE g.codigo = 'planet_4m5_jardim_interlagos';
SELECT treino.fn_gerar_blocos(id) FROM treino.divisao WHERE codigo = 'blocos_600m_s42';

CREATE VIEW treino.vw_divisao_resumo AS
SELECT d.codigo AS divisao, b.papel_codigo, count(*) AS n_blocos,
       round((sum(ST_Area(b.geom)) / 1e6)::numeric, 3) AS area_km2,
       round((sum(coalesce(ST_Area(b.geom_util), 0)) / 1e6)::numeric, 3) AS area_util_km2,
       round((100 * sum(coalesce(ST_Area(b.geom_util), 0)) / sum(ST_Area(b.geom)))::numeric, 1) AS pct_util
  FROM treino.bloco b JOIN treino.divisao d ON d.id = b.divisao_id
 GROUP BY d.codigo, b.papel_codigo
 ORDER BY 1, 2;
COMMENT ON VIEW treino.vw_divisao_resumo IS 'Blocos e área útil por conjunto (custo da folga)';

CREATE VIEW treino.vw_tarefa_conjunto AS
SELECT row_number() OVER (ORDER BY d.id, t.id) AS id,
       d.id AS divisao_id, d.codigo AS divisao, t.id AS tarefa_id, c.bloco_id,
       coalesce(c.papel, 'fora_de_bloco') AS papel
  FROM rotulo.tarefa t
 CROSS JOIN treino.divisao d
 CROSS JOIN LATERAL treino.fn_conjunto(d.id, t.geom, t.data_referencia, true) c;
COMMENT ON VIEW treino.vw_tarefa_conjunto IS 'Conjunto de cada tarefa (espaço + data). fora_de_bloco = cruza fronteira ou folga';

CREATE VIEW treino.vw_evento_conjunto AS
SELECT row_number() OVER (ORDER BY d.id, e.id) AS id,
       d.id AS divisao_id, e.id AS evento_id, c.bloco_id, coalesce(c.papel, 'fora_de_bloco') AS papel, c.cruza_bloco
  FROM rotulo.evento e
 CROSS JOIN treino.divisao d
 CROSS JOIN LATERAL treino.fn_conjunto(d.id, e.geom, e.mes_inicio, false) c;
COMMENT ON VIEW treino.vw_evento_conjunto IS 'Evento inteiro no conjunto do bloco de maior sobreposição, com data = mês de início';

CREATE VIEW treino.vw_controle_conjunto AS
SELECT row_number() OVER (ORDER BY d.id, ce.id) AS id,
       d.id AS divisao_id, ce.id AS controle_id, c.bloco_id, coalesce(c.papel, 'fora_de_bloco') AS papel, c.cruza_bloco
  FROM rotulo.controle_estavel ce
 CROSS JOIN treino.divisao d
 CROSS JOIN LATERAL treino.fn_conjunto(d.id, ce.geom, NULL, false) c;

CREATE TABLE treino.dataset (
    id            integer GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_dataset PRIMARY KEY,
    codigo        text     NOT NULL,
    versao        smallint NOT NULL CONSTRAINT ck_dataset_versao CHECK (versao > 0),
    campanha_id   integer  NOT NULL REFERENCES rotulo.campanha (id),
    divisao_id    integer  NOT NULL REFERENCES treino.divisao (id),
    grade_id      integer  NOT NULL REFERENCES catalogo.grade (id),
    descricao     text,
    parametros    jsonb    NOT NULL DEFAULT '{}',
    criado_em     timestamptz NOT NULL DEFAULT now(),
    congelado_em  timestamptz,
    CONSTRAINT uq_dataset_codigo_versao UNIQUE (codigo, versao)
);
COMMENT ON TABLE  treino.dataset IS 'Versão imutável de amostras (máscaras, eventos, controles) numa única grade. Depois de congelado, não muda';
COMMENT ON COLUMN treino.dataset.grade_id IS 'Uma grade por dataset: 3 m e 5 m não são intercambiáveis';
COMMENT ON COLUMN treino.dataset.parametros IS 'Filtros: {"produtos": [...], "exigir_todas_classes": true}';

CREATE TABLE treino.dataset_amostra (
    dataset_id        integer NOT NULL REFERENCES treino.dataset (id),
    tarefa_id         integer NOT NULL REFERENCES rotulo.tarefa (id),
    sessao_id         integer NOT NULL REFERENCES rotulo.sessao (id),
    imagem_id         integer NOT NULL REFERENCES catalogo.imagem (id),
    papel_codigo      text    NOT NULL REFERENCES dominio.papel_conjunto (codigo),
    caminho_mascara   text,
    sha256_mascara    char(64) CONSTRAINT ck_amostra_sha256 CHECK (sha256_mascara ~ '^[0-9a-f]{64}$'),
    pixels_por_valor  jsonb,
    gerada_em         timestamptz,
    CONSTRAINT pk_dataset_amostra PRIMARY KEY (dataset_id, tarefa_id)
);
COMMENT ON TABLE treino.dataset_amostra IS 'Máscara de cobertura (tarefa aprovada) no dataset, com conjunto e raster gerado';
CREATE INDEX ix_amostra_sessao ON treino.dataset_amostra (sessao_id);
CREATE INDEX ix_amostra_imagem ON treino.dataset_amostra (imagem_id);

CREATE TABLE treino.dataset_evento (
    dataset_id    integer NOT NULL REFERENCES treino.dataset (id),
    evento_id     integer NOT NULL REFERENCES rotulo.evento (id),
    papel_codigo  text    NOT NULL REFERENCES dominio.papel_conjunto (codigo),
    cruza_bloco   boolean NOT NULL,
    CONSTRAINT pk_dataset_evento PRIMARY KEY (dataset_id, evento_id)
);
COMMENT ON TABLE treino.dataset_evento IS 'Evento confirmado no dataset (referência de mudança)';

CREATE TABLE treino.dataset_controle (
    dataset_id    integer NOT NULL REFERENCES treino.dataset (id),
    controle_id   integer NOT NULL REFERENCES rotulo.controle_estavel (id),
    papel_codigo  text    NOT NULL REFERENCES dominio.papel_conjunto (codigo),
    CONSTRAINT pk_dataset_controle PRIMARY KEY (dataset_id, controle_id)
);
COMMENT ON TABLE treino.dataset_controle IS 'Controle estável confirmado no dataset (falso alarme e deriva de cor)';

CREATE FUNCTION treino.fn_proteger_dataset() RETURNS trigger
LANGUAGE plpgsql AS $$
DECLARE
    v_congelado timestamptz;
BEGIN
    IF TG_TABLE_NAME = 'dataset' THEN
        IF OLD.congelado_em IS NOT NULL AND (TG_OP = 'DELETE' OR
               NEW.congelado_em IS DISTINCT FROM OLD.congelado_em OR NEW.campanha_id <> OLD.campanha_id
            OR NEW.divisao_id <> OLD.divisao_id OR NEW.grade_id <> OLD.grade_id OR NEW.codigo <> OLD.codigo
            OR NEW.versao <> OLD.versao OR NEW.parametros <> OLD.parametros) THEN
            RAISE EXCEPTION 'Dataset %/v% está congelado; crie uma nova versão', OLD.codigo, OLD.versao;
        END IF;
        RETURN CASE WHEN TG_OP = 'DELETE' THEN OLD ELSE NEW END;
    END IF;

    SELECT congelado_em INTO v_congelado FROM treino.dataset
     WHERE id = CASE WHEN TG_OP = 'DELETE' THEN OLD.dataset_id ELSE NEW.dataset_id END;
    IF v_congelado IS NULL THEN
        RETURN CASE WHEN TG_OP = 'DELETE' THEN OLD ELSE NEW END;
    END IF;
    IF TG_TABLE_NAME = 'dataset_amostra' AND TG_OP = 'UPDATE' THEN
        -- registrar a máscara gerada é permitido (IF separado: NEW.tarefa_id só existe nesta tabela)
        IF (NEW.dataset_id, NEW.tarefa_id, NEW.sessao_id, NEW.imagem_id, NEW.papel_codigo)
         = (OLD.dataset_id, OLD.tarefa_id, OLD.sessao_id, OLD.imagem_id, OLD.papel_codigo) THEN
            RETURN NEW;
        END IF;
    END IF;
    RAISE EXCEPTION 'Dataset congelado: amostras, eventos e controles não podem ser incluídos, removidos ou trocados';
END $$;

CREATE TRIGGER tg_dataset_proteger  BEFORE UPDATE OR DELETE ON treino.dataset
    FOR EACH ROW EXECUTE FUNCTION treino.fn_proteger_dataset();
CREATE TRIGGER tg_amostra_proteger  BEFORE INSERT OR UPDATE OR DELETE ON treino.dataset_amostra
    FOR EACH ROW EXECUTE FUNCTION treino.fn_proteger_dataset();
CREATE TRIGGER tg_ds_evento_proteger BEFORE INSERT OR UPDATE OR DELETE ON treino.dataset_evento
    FOR EACH ROW EXECUTE FUNCTION treino.fn_proteger_dataset();
CREATE TRIGGER tg_ds_controle_proteger BEFORE INSERT OR UPDATE OR DELETE ON treino.dataset_controle
    FOR EACH ROW EXECUTE FUNCTION treino.fn_proteger_dataset();

-- Eventos e controles de dataset congelado ficam imutáveis.
CREATE FUNCTION treino.fn_proteger_referencia() RETURNS trigger
LANGUAGE plpgsql AS $$
BEGIN
    IF (TG_TABLE_NAME = 'evento' AND EXISTS (
            SELECT 1 FROM treino.dataset_evento de JOIN treino.dataset d ON d.id = de.dataset_id
             WHERE de.evento_id = OLD.id AND d.congelado_em IS NOT NULL))
    OR (TG_TABLE_NAME = 'controle_estavel' AND EXISTS (
            SELECT 1 FROM treino.dataset_controle dc JOIN treino.dataset d ON d.id = dc.dataset_id
             WHERE dc.controle_id = OLD.id AND d.congelado_em IS NOT NULL)) THEN
        RAISE EXCEPTION '% % pertence a dataset congelado; registre a correção como novo item', TG_TABLE_NAME, OLD.id;
    END IF;
    RETURN CASE WHEN TG_OP = 'DELETE' THEN OLD ELSE NEW END;
END $$;
CREATE TRIGGER tg_evento_congelado BEFORE UPDATE OR DELETE ON rotulo.evento
    FOR EACH ROW EXECUTE FUNCTION treino.fn_proteger_referencia();
CREATE TRIGGER tg_controle_congelado BEFORE UPDATE OR DELETE ON rotulo.controle_estavel
    FOR EACH ROW EXECUTE FUNCTION treino.fn_proteger_referencia();

-- Monta e congela o dataset.
--   Máscaras: tarefas aprovadas da campanha, na grade do dataset, inteiras num bloco útil;
--             fora: planos de avaliação independente e aprendizado ativo em conjunto de teste.
--   Eventos e controles: confirmados, no conjunto do bloco de maior sobreposição.
--   Exige sha256 e QC aceito em toda imagem incluída.
CREATE FUNCTION treino.fn_congelar_dataset(p_dataset_id integer) RETURNS integer
LANGUAGE plpgsql AS $$
DECLARE
    d          treino.dataset;
    n_mask     integer;
    n_ev       integer;
    n_ctl      integer;
    n_ativo    integer;
    v_sem_hash text;
    v_faltam   text;
BEGIN
    SELECT * INTO d FROM treino.dataset WHERE id = p_dataset_id FOR UPDATE;
    IF d.congelado_em IS NOT NULL THEN
        RAISE EXCEPTION 'Dataset %/v% já está congelado', d.codigo, d.versao;
    END IF;

    DELETE FROM treino.dataset_amostra  WHERE dataset_id = d.id;
    DELETE FROM treino.dataset_evento   WHERE dataset_id = d.id;
    DELETE FROM treino.dataset_controle WHERE dataset_id = d.id;

    DROP TABLE IF EXISTS pg_temp.candidata;
    CREATE TEMP TABLE candidata ON COMMIT DROP AS
    SELECT t.id AS tarefa_id, t.sessao_referencia_id, t.imagem_id, tc.papel, t.modo_selecao_codigo
      FROM rotulo.vw_tarefa t
      JOIN treino.vw_tarefa_conjunto tc ON tc.tarefa_id = t.id AND tc.divisao_id = d.divisao_id
      JOIN catalogo.imagem i  ON i.id = t.imagem_id
      JOIN catalogo.produto p ON p.codigo = i.produto_codigo
      LEFT JOIN rotulo.estrato e        ON e.id = t.estrato_id
      LEFT JOIN rotulo.plano_amostral pl ON pl.id = e.plano_id
     WHERE t.campanha_id = d.campanha_id
       AND t.situacao = 'aprovada'
       AND p.grade_id = d.grade_id
       AND tc.papel <> 'fora_de_bloco'
       AND coalesce(pl.uso, 'treino') <> 'avaliacao_independente'
       AND (NOT d.parametros ? 'produtos' OR t.produto_codigo IN (SELECT jsonb_array_elements_text(d.parametros -> 'produtos')));

    SELECT count(*) INTO n_ativo FROM candidata
     WHERE modo_selecao_codigo = 'aprendizado_ativo' AND papel NOT IN ('treino', 'validacao');
    IF n_ativo > 0 THEN
        RAISE NOTICE '% tarefa(s) de aprendizado ativo em conjunto de teste ficaram fora do dataset', n_ativo;
    END IF;

    SELECT string_agg(DISTINCT i.arquivo, ', ') INTO v_sem_hash
      FROM candidata c JOIN catalogo.imagem i ON i.id = c.imagem_id
      JOIN dominio.status_qc q ON q.codigo = i.qc_status_codigo
     WHERE i.sha256 IS NULL OR NOT q.aceita_rotulo;
    IF v_sem_hash IS NOT NULL THEN
        RAISE EXCEPTION 'Imagens sem sha256 ou com QC reprovado: %', v_sem_hash
              USING HINT = 'Rode o inventário (skill inventario-dados) e preencha catalogo.imagem.sha256';
    END IF;

    INSERT INTO treino.dataset_amostra (dataset_id, tarefa_id, sessao_id, imagem_id, papel_codigo)
    SELECT d.id, tarefa_id, sessao_referencia_id, imagem_id, papel FROM candidata
     WHERE NOT (modo_selecao_codigo = 'aprendizado_ativo' AND papel NOT IN ('treino', 'validacao'));
    GET DIAGNOSTICS n_mask = ROW_COUNT;

    INSERT INTO treino.dataset_evento (dataset_id, evento_id, papel_codigo, cruza_bloco)
    SELECT d.id, ec.evento_id, ec.papel, ec.cruza_bloco
      FROM treino.vw_evento_conjunto ec JOIN rotulo.evento e ON e.id = ec.evento_id
     WHERE ec.divisao_id = d.divisao_id AND e.campanha_id = d.campanha_id
       AND e.status_revisao_codigo = 'confirmado' AND ec.papel <> 'fora_de_bloco';
    GET DIAGNOSTICS n_ev = ROW_COUNT;

    INSERT INTO treino.dataset_controle (dataset_id, controle_id, papel_codigo)
    SELECT d.id, cc.controle_id, cc.papel
      FROM treino.vw_controle_conjunto cc JOIN rotulo.controle_estavel ce ON ce.id = cc.controle_id
     WHERE cc.divisao_id = d.divisao_id AND ce.campanha_id = d.campanha_id
       AND ce.status_revisao_codigo = 'confirmado' AND cc.papel <> 'fora_de_bloco';
    GET DIAGNOSTICS n_ctl = ROW_COUNT;

    IF n_mask + n_ev + n_ctl = 0 THEN
        RAISE EXCEPTION 'Nada aprovado/confirmado para o dataset %/v%', d.codigo, d.versao;
    END IF;

    -- Classes de cobertura ausentes em algum dos conjuntos de ajuste e teste espacial.
    SELECT string_agg(k.codigo || ' em ' || pc.codigo, ', ' ORDER BY k.ordem, pc.ordem) INTO v_faltam
      FROM dominio.classe k
      JOIN rotulo.campanha cp ON cp.id = d.campanha_id AND k.taxonomia_id = cp.taxonomia_id
     CROSS JOIN dominio.papel_conjunto pc
     WHERE k.tipo = 'cobertura' AND k.valor_raster IS NOT NULL AND pc.codigo IN ('treino', 'validacao', 'teste')
       AND n_mask > 0
       AND NOT EXISTS (SELECT 1 FROM treino.dataset_amostra da JOIN rotulo.anotacao a ON a.sessao_id = da.sessao_id
                        WHERE da.dataset_id = d.id AND da.papel_codigo = pc.codigo AND a.classe_id = k.id);
    IF v_faltam IS NOT NULL THEN
        IF coalesce((d.parametros ->> 'exigir_todas_classes')::boolean, false) THEN
            RAISE EXCEPTION 'Classes ausentes: %', v_faltam;
        END IF;
        RAISE NOTICE 'Classes ausentes (dataset congelado mesmo assim): %', v_faltam;
    END IF;

    UPDATE treino.dataset SET congelado_em = now() WHERE id = d.id;
    RETURN n_mask + n_ev + n_ctl;
END $$;

-- Entrada da rasterização: o que queimar em cada amostra, na grade da imagem.
CREATE VIEW treino.vw_mascara_poligono AS
SELECT row_number() OVER (ORDER BY da.dataset_id, da.tarefa_id, a.id) AS id,
       da.dataset_id, da.tarefa_id, da.sessao_id, da.imagem_id, da.papel_codigo,
       p.pasta || '/' || i.arquivo AS caminho_imagem, g.id AS grade_id,
       c.valor_raster AS valor, c.ignorar_no_treino, a.certeza_codigo, nc.peso, a.objeto_id, a.geom
  FROM treino.dataset_amostra da
  JOIN rotulo.anotacao a        ON a.sessao_id = da.sessao_id
  JOIN dominio.classe c         ON c.id = a.classe_id
  JOIN dominio.nivel_certeza nc ON nc.codigo = a.certeza_codigo
  JOIN catalogo.imagem i        ON i.id = da.imagem_id
  JOIN catalogo.produto p       ON p.codigo = i.produto_codigo
  JOIN catalogo.grade g         ON g.id = p.grade_id;
COMMENT ON VIEW treino.vw_mascara_poligono IS 'Polígonos a rasterizar por amostra (valor = pixel). Fundo, alfa 0 e fora da AOI: taxonomia.valor_nao_rotulado';

CREATE VIEW treino.vw_mascara_janela AS
SELECT da.dataset_id, da.tarefa_id, da.imagem_id, da.papel_codigo,
       p.pasta || '/' || i.arquivo AS caminho_imagem,
       floor((ST_XMin(t.geom) - g.origem_x) / g.pixel_x)::int  AS col_ini,
       floor((g.origem_y - ST_YMax(t.geom)) / -g.pixel_y)::int AS lin_ini,
       ceil((ST_XMax(t.geom) - g.origem_x) / g.pixel_x)::int   AS col_fim,
       ceil((g.origem_y - ST_YMin(t.geom)) / -g.pixel_y)::int  AS lin_fim,
       g.origem_x, g.origem_y, g.pixel_x, g.pixel_y, tx.valor_nao_rotulado,
       t.geom
  FROM treino.dataset_amostra da
  JOIN treino.dataset d     ON d.id = da.dataset_id
  JOIN rotulo.campanha cp   ON cp.id = d.campanha_id
  JOIN dominio.taxonomia tx ON tx.id = cp.taxonomia_id
  JOIN rotulo.tarefa t      ON t.id = da.tarefa_id
  JOIN catalogo.imagem i    ON i.id = da.imagem_id
  JOIN catalogo.produto p   ON p.codigo = i.produto_codigo
  JOIN catalogo.grade g     ON g.id = p.grade_id;
COMMENT ON VIEW treino.vw_mascara_janela IS 'Janela (col/lin, fim exclusivo) da tarefa na grade da imagem e valor de fundo';

CREATE VIEW treino.vw_evento_referencia AS
SELECT de.dataset_id, de.papel_codigo, de.cruza_bloco, e.id AS evento_id, e.tipo_alteracao_codigo,
       cd.codigo AS classe_de, cp.codigo AS classe_para, e.estagio_codigo,
       to_char(e.mes_inicio, 'YYYY-MM') AS mes_inicio, to_char(e.mes_inicio_min, 'YYYY-MM') AS mes_inicio_min,
       to_char(e.mes_inicio_max, 'YYYY-MM') AS mes_inicio_max, e.certeza_codigo, e.objeto_id, e.area_m2, e.geom
  FROM treino.dataset_evento de
  JOIN rotulo.evento e   ON e.id = de.evento_id
  JOIN dominio.classe cd ON cd.id = e.classe_de_id
  JOIN dominio.classe cp ON cp.id = e.classe_para_id;
COMMENT ON VIEW treino.vw_evento_referencia IS 'Eventos do dataset no formato da avaliação (mês de início, tipo, de→para)';

CREATE VIEW treino.vw_balanco_classe AS
SELECT d.codigo AS dataset, d.versao, m.papel_codigo, c.codigo AS classe, c.tipo,
       count(*) AS n_poligonos,
       round((sum(ST_Area(m.geom)) / 10000)::numeric, 3) AS area_ha,
       round((100 * sum(ST_Area(m.geom)) / sum(sum(ST_Area(m.geom))) OVER (PARTITION BY d.id, m.papel_codigo))::numeric, 2) AS pct_no_conjunto
  FROM treino.vw_mascara_poligono m
  JOIN treino.dataset d ON d.id = m.dataset_id
  JOIN dominio.classe c ON c.taxonomia_id = (SELECT taxonomia_id FROM rotulo.campanha WHERE id = d.campanha_id)
                       AND c.valor_raster = m.valor
 GROUP BY d.id, d.codigo, d.versao, m.papel_codigo, c.codigo, c.tipo, c.ordem
 ORDER BY d.codigo, d.versao, m.papel_codigo, c.ordem;
COMMENT ON VIEW treino.vw_balanco_classe IS 'Área por classe e conjunto: conferir desbalanceamento antes de treinar';


-- =============================================================================
-- AUDITORIA: gatilhos
-- =============================================================================

DO $$
DECLARE
    t text;
BEGIN
    FOREACH t IN ARRAY ARRAY[
        'dominio.taxonomia', 'dominio.classe', 'dominio.transicao_permitida', 'catalogo.imagem',
        'rotulo.campanha', 'rotulo.processamento', 'rotulo.ciclo_aprendizado', 'rotulo.plano_amostral', 'rotulo.estrato',
        'rotulo.serie', 'rotulo.tarefa', 'rotulo.sessao', 'rotulo.anotacao',
        'rotulo.evento', 'rotulo.evento_evidencia', 'rotulo.controle_estavel',
        'treino.divisao', 'treino.dataset', 'treino.dataset_amostra', 'treino.dataset_evento', 'treino.dataset_controle']
    LOOP
        EXECUTE format('CREATE TRIGGER tg_auditoria AFTER INSERT OR UPDATE OR DELETE ON %s
                        FOR EACH ROW EXECUTE FUNCTION auditoria.fn_registrar()', t);
    END LOOP;
END $$;

-- A carga inicial não precisa ficar no histórico.
TRUNCATE auditoria.registro;

COMMIT;
