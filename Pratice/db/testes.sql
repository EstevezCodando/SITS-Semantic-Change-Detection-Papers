-- Testes das regras do banco mudanca_mascara v2. Rodam numa transação e desfazem tudo no fim.
--   psql -U postgres -d mudanca_mascara -f db/testes.sql
-- Cada teste imprime "ok: ..." ou interrompe com o motivo. Seções marcadas com a falha que cobrem (F1–F9).
-- O trecho esperado de cada erro é a mensagem das nossas funções ou o nome da restrição; erros do próprio
-- PostgreSQL, cujo texto muda com o idioma do servidor, são conferidos pelo SQLSTATE.

\set ON_ERROR_STOP on
SET client_encoding = 'UTF8';
SET client_min_messages = notice;
\pset tuples_only on
BEGIN;

CREATE FUNCTION pg_temp.espera_erro(p_sql text, p_trecho text, p_nome text) RETURNS void
LANGUAGE plpgsql AS $$
BEGIN
    BEGIN
        EXECUTE p_sql;
    EXCEPTION WHEN others THEN
        IF position(p_trecho IN SQLERRM) = 0 AND p_trecho <> SQLSTATE THEN
            RAISE EXCEPTION 'FALHOU %: erro inesperado: %', p_nome, SQLERRM;
        END IF;
        RAISE NOTICE 'ok: % (recusado: %)', p_nome, SQLERRM;
        RETURN;
    END;
    RAISE EXCEPTION 'FALHOU %: deveria ter sido recusado', p_nome;
END $$;

CREATE FUNCTION pg_temp.confere(p_cond boolean, p_nome text) RETURNS void
LANGUAGE plpgsql AS $$
BEGIN
    IF p_cond IS NOT TRUE THEN
        RAISE EXCEPTION 'FALHOU %', p_nome;
    END IF;
    RAISE NOTICE 'ok: %', p_nome;
END $$;

CREATE FUNCTION pg_temp.img(p_arquivo text) RETURNS integer
LANGUAGE sql AS $$ SELECT id FROM catalogo.imagem WHERE arquivo = p_arquivo $$;

CREATE FUNCTION pg_temp.classe(p_codigo text) RETURNS integer
LANGUAGE sql AS $$ SELECT id FROM dominio.classe WHERE codigo = p_codigo $$;

CREATE FUNCTION pg_temp.caixa(x0 float, y0 float, x1 float, y1 float) RETURNS geometry
LANGUAGE sql AS $$ SELECT ST_Multi(ST_MakeEnvelope(x0, y0, x1, y1, 32723)) $$;

CREATE FUNCTION pg_temp.anotar(p_sessao integer, p_classe text, x0 float, y0 float, x1 float, y1 float,
                               p_objeto bigint DEFAULT NULL) RETURNS integer
LANGUAGE sql AS $$
    INSERT INTO rotulo.anotacao (sessao_id, tarefa_id, data_referencia, classe_id, geom, objeto_id)
    VALUES (p_sessao, 0, '1900-01-01', pg_temp.classe(p_classe), pg_temp.caixa(x0, y0, x1, y1), p_objeto)
    RETURNING id
$$;

-- Rotula a tarefa inteira com uma classe, envia e aprova (revisor "rev").
CREATE FUNCTION pg_temp.rotular_e_aprovar(p_tarefa integer, p_apelido text, p_classe text) RETURNS integer
LANGUAGE plpgsql AS $$
DECLARE
    s integer := rotulo.fn_iniciar_sessao(p_tarefa, p_apelido);
BEGIN
    INSERT INTO rotulo.anotacao (sessao_id, tarefa_id, data_referencia, classe_id, geom)
    SELECT s, 0, '1900-01-01', pg_temp.classe(p_classe), ST_Multi(geom) FROM rotulo.tarefa WHERE id = p_tarefa;
    PERFORM rotulo.fn_enviar_sessao(s);
    PERFORM rotulo.fn_revisar_sessao(s, 'rev', true);
    RETURN s;
END $$;

CREATE TEMP TABLE ctx (chave text PRIMARY KEY, valor bigint);
CREATE FUNCTION pg_temp.v(p text) RETURNS bigint LANGUAGE sql AS $$ SELECT valor FROM ctx WHERE chave = p $$;
CREATE FUNCTION pg_temp.guarda(p text, x bigint) RETURNS void LANGUAGE sql AS $$
    INSERT INTO ctx VALUES (p, x) ON CONFLICT (chave) DO UPDATE SET valor = excluded.valor $$;

-- =============================================================================
-- Carga inicial
-- =============================================================================
SELECT pg_temp.confere((SELECT count(*) FROM catalogo.imagem) = 179, 'catálogo com 179 imagens');
SELECT pg_temp.confere((SELECT count(*) FROM catalogo.grade) = 3, '3 grades');
SELECT pg_temp.confere((SELECT count(*) FROM dominio.vw_classe WHERE atribuivel) = 12, '12 classes atribuíveis');
SELECT pg_temp.confere((SELECT count(*) FROM dominio.vw_classe WHERE atribuivel AND tipo = 'cobertura') = 7, '7 classes de cobertura');
SELECT pg_temp.confere((SELECT count(DISTINCT tipo_alteracao_codigo) FROM dominio.transicao_permitida) = 8, '8 tipos de alteração com transições');
SELECT pg_temp.confere((SELECT bool_and(ST_IsValid(geom) AND ST_Area(geom) > 1e6) FROM catalogo.aoi), 'AOI válida e maior que 1 km²');
SELECT pg_temp.confere((SELECT ST_CoveredBy(a.geom, g.geom) FROM catalogo.aoi a, catalogo.grade g WHERE g.codigo = 'planet_4m5_jardim_interlagos'), 'AOI dentro da grade Planet');
SELECT pg_temp.confere((SELECT count(*) FROM treino.bloco) = 30, '30 blocos de 600 m');
SELECT pg_temp.confere((SELECT count(*) FILTER (WHERE papel_codigo = 'treino') = 18 AND count(*) FILTER (WHERE papel_codigo = 'validacao') = 6
                          FROM treino.bloco), 'sorteio 18/6/6');
SELECT pg_temp.confere((SELECT count(*) FROM auditoria.registro) = 0, 'auditoria limpa após carga');

-- =============================================================================
-- F9: folga só entre conjuntos diferentes, com distância garantida
-- =============================================================================
SELECT pg_temp.confere((SELECT min(ST_Distance(a.geom_util, b.geom_util)) >= 100 - 1e-6
                          FROM treino.bloco a JOIN treino.bloco b ON b.id > a.id AND b.papel_codigo <> a.papel_codigo
                         WHERE a.geom_util IS NOT NULL AND b.geom_util IS NOT NULL),
                       'áreas úteis de conjuntos diferentes a ≥ 100 m');
SELECT pg_temp.confere((SELECT bool_and(ST_Equals(geom_util, ST_Multi(geom))) FROM treino.bloco WHERE papel_codigo = 'teste'),
                       'blocos de teste não perdem área');
SELECT pg_temp.confere((SELECT 100 * sum(ST_Area(geom_util)) / sum(ST_Area(geom)) > 69.4 FROM treino.bloco),
                       'área útil maior que a da folga uniforme da v1 (69,4%)');
SELECT pg_temp.confere((SELECT limitacao LIKE '%1,6 km%' FROM treino.divisao), 'limitação do tamanho de bloco registrada');

-- =============================================================================
-- Taxonomia
-- =============================================================================
SELECT pg_temp.espera_erro($$INSERT INTO dominio.classe (taxonomia_id, codigo, nome, classe_pai_id, nivel, tipo, valor_raster, cor_hex, ordem)
    SELECT taxonomia_id, 'x', 'x', id, 2, 'cobertura', 1, '#000000', 99 FROM dominio.classe WHERE codigo = 'vegetacao'$$,
    'uq_classe_taxonomia_valor', 'valor de pixel repetido na taxonomia');
SELECT pg_temp.espera_erro($$INSERT INTO dominio.classe (taxonomia_id, codigo, nome, classe_pai_id, nivel, tipo, valor_raster, cor_hex, ordem)
    SELECT taxonomia_id, 'x', 'x', id, 3, 'cobertura', 99, '#000000', 99 FROM dominio.classe WHERE codigo = 'agua'$$,
    'é folha', 'folha não pode ter filhas');

-- =============================================================================
-- Cobertura por data (v1, ainda válida)
-- =============================================================================
INSERT INTO rotulo.pessoa (apelido, nome, funcao_codigo) VALUES
    ('ana', 'Ana Teste', 'rotulador'), ('bia', 'Bia Teste', 'rotulador'), ('rev', 'Revisor Teste', 'revisor');
SELECT pg_temp.guarda('campanha', (SELECT id FROM rotulo.campanha WHERE codigo = 'cobertura_referencia_v1'));
SELECT pg_temp.guarda('img_2020_01', pg_temp.img('global_monthly_2020_01_mosaic.tif'));

INSERT INTO rotulo.tarefa (campanha_id, imagem_id, data_referencia, geom, motivo)
VALUES (pg_temp.v('campanha'), pg_temp.v('img_2020_01'), '1900-01-01', ST_MakeEnvelope(726300, 7462300, 726400, 7462400, 32723), 'teste');
SELECT pg_temp.guarda('tarefa', (SELECT max(id) FROM rotulo.tarefa));

SELECT pg_temp.confere((SELECT data_referencia = '2020-01-01' FROM rotulo.tarefa WHERE id = pg_temp.v('tarefa')),
                       'data da tarefa vem da imagem (ignora a digitada)');
SELECT pg_temp.espera_erro($$INSERT INTO rotulo.tarefa (campanha_id, imagem_id, data_referencia, geom)
    VALUES (pg_temp.v('campanha'), pg_temp.v('img_2020_01'), now(), ST_MakeEnvelope(726350, 7462350, 726450, 7462450, 32723))$$,
    'sobrepõe a tarefa', 'tarefas sobrepostas na mesma imagem');
SELECT pg_temp.espera_erro($$INSERT INTO rotulo.tarefa (campanha_id, imagem_id, data_referencia, geom)
    VALUES (pg_temp.v('campanha'), pg_temp.v('img_2020_01'), now(), ST_MakeEnvelope(700000, 7462300, 700100, 7462400, 32723))$$,
    'fora da extensão', 'tarefa fora da imagem');

SELECT pg_temp.guarda('s_ana', rotulo.fn_iniciar_sessao(pg_temp.v('tarefa')::int, 'ana'));
SELECT pg_temp.guarda('s_bia', rotulo.fn_iniciar_sessao(pg_temp.v('tarefa')::int, 'bia'));

SELECT pg_temp.espera_erro($$SELECT pg_temp.anotar(pg_temp.v('s_ana')::int, 'vegetacao', 726300, 7462300, 726350, 7462400)$$,
    'agregadora', 'classe agregadora não é atribuível');
SELECT pg_temp.anotar(pg_temp.v('s_ana')::int, 'vegetacao_arborea', 726250, 7462250, 726350, 7462450);
SELECT pg_temp.confere((SELECT abs(area_m2 - 5000) < 0.01 FROM rotulo.anotacao WHERE sessao_id = pg_temp.v('s_ana')),
                       'anotação recortada ao limite da tarefa (5000 m²)');
SELECT pg_temp.confere((SELECT bool_and(data_referencia = '2020-01-01' AND tarefa_id = pg_temp.v('tarefa')) FROM rotulo.anotacao),
                       'anotação herda data e tarefa');
SELECT pg_temp.espera_erro($$SELECT pg_temp.anotar(pg_temp.v('s_ana')::int, 'edificacao', 726340, 7462300, 726400, 7462350)$$,
    'sobrepõe', 'sobreposição na mesma sessão');
SELECT pg_temp.anotar(pg_temp.v('s_ana')::int, 'edificacao', 726350, 7462300, 726400, 7462350);
SELECT pg_temp.espera_erro($$SELECT rotulo.fn_enviar_sessao(pg_temp.v('s_ana')::int)$$, 'sem classe', 'envio com lacuna');
SELECT pg_temp.confere((SELECT abs(area_m2 - 2500) < 0.01 FROM rotulo.vw_lacuna WHERE id = pg_temp.v('s_ana')), 'lacuna de 2500 m² visível');
SELECT pg_temp.anotar(pg_temp.v('s_ana')::int, 'solo_exposto', 726350, 7462350, 726400, 7462400);
SELECT rotulo.fn_enviar_sessao(pg_temp.v('s_ana')::int, 900);
SELECT pg_temp.confere((SELECT enviada_em IS NOT NULL AND tempo_ativo_s = 900 FROM rotulo.sessao WHERE id = pg_temp.v('s_ana')),
                       'sessão enviada com tempo ativo');
SELECT pg_temp.espera_erro($$UPDATE rotulo.anotacao SET classe_id = classe_id WHERE sessao_id = pg_temp.v('s_ana')$$,
    'em_andamento', 'anotação travada após envio');

SELECT pg_temp.anotar(pg_temp.v('s_bia')::int, 'vegetacao_arborea', 726300, 7462300, 726350, 7462400);
SELECT pg_temp.anotar(pg_temp.v('s_bia')::int, 'edificacao',        726350, 7462300, 726400, 7462400);
SELECT rotulo.fn_enviar_sessao(pg_temp.v('s_bia')::int);
SELECT pg_temp.confere((SELECT acordo_global = 0.75 FROM rotulo.vw_concordancia LIMIT 1), 'acordo global 0,75');
SELECT pg_temp.confere((SELECT iou = 0.5 FROM rotulo.vw_concordancia WHERE classe = 'edificacao'), 'IoU de construção 0,5');

SELECT pg_temp.espera_erro($$UPDATE rotulo.sessao SET status_codigo = 'aprovada' WHERE id = pg_temp.v('s_ana')$$,
    'revisor_id', 'aprovação sem revisor');
SELECT pg_temp.espera_erro($$SELECT rotulo.fn_revisar_sessao(pg_temp.v('s_ana')::int, 'ana', true)$$,
    'ck_sessao_revisor_diferente', 'autoaprovação');
SELECT rotulo.fn_revisar_sessao(pg_temp.v('s_ana')::int, 'rev', true, 'ok');
SELECT pg_temp.espera_erro($$SELECT rotulo.fn_revisar_sessao(pg_temp.v('s_bia')::int, 'rev', true)$$,
    'uq_sessao_aprovada_por_tarefa', 'segunda aprovação na mesma tarefa');
SELECT rotulo.fn_revisar_sessao(pg_temp.v('s_bia')::int, 'rev', false, 'quadrante SE é solo');
SELECT pg_temp.confere((SELECT situacao = 'aprovada' AND sessao_referencia_id = pg_temp.v('s_ana')
                          FROM rotulo.vw_tarefa WHERE id = pg_temp.v('tarefa')), 'tarefa aprovada com referência da Ana');
SELECT pg_temp.espera_erro($$UPDATE rotulo.sessao SET status_codigo = 'enviada' WHERE id = pg_temp.v('s_bia')$$,
    'Transição', 'transição rejeitada → enviada');
SELECT pg_temp.espera_erro($$UPDATE rotulo.tarefa SET geom = ST_MakeEnvelope(726300, 7462300, 726410, 7462400, 32723) WHERE id = pg_temp.v('tarefa')$$,
    'não mudam', 'recorte travado com sessões');

-- =============================================================================
-- F8: QC da imagem
-- =============================================================================
UPDATE catalogo.imagem SET qc_status_codigo = 'reprovada', qc_observacao = 'teste'
 WHERE arquivo = 'global_monthly_2020_04_mosaic.tif';
SELECT pg_temp.espera_erro($$INSERT INTO rotulo.tarefa (campanha_id, imagem_id, data_referencia, geom)
    VALUES (pg_temp.v('campanha'), pg_temp.img('global_monthly_2020_04_mosaic.tif'), now(), ST_MakeEnvelope(726300, 7462300, 726400, 7462400, 32723))$$,
    'QC reprovada', 'imagem reprovada no QC não recebe tarefa');
SELECT pg_temp.espera_erro($$UPDATE catalogo.imagem SET pct_valido = 120 WHERE id = 1$$, 'ck_imagem_pct_valido', 'QC: porcentagem fora de 0–100');

-- =============================================================================
-- F7: proveniência de pré-rótulo
-- =============================================================================
WITH x AS (
    INSERT INTO rotulo.tarefa (campanha_id, imagem_id, data_referencia, geom)
    VALUES (pg_temp.v('campanha'), pg_temp.v('img_2020_01'), now(), ST_MakeEnvelope(726650, 7462300, 726700, 7462350, 32723))
    RETURNING id)
SELECT pg_temp.guarda('t_pre', id) FROM x;
SELECT pg_temp.guarda('s_pre', rotulo.fn_iniciar_sessao(pg_temp.v('t_pre')::int, 'ana', 'pre_anotacao_sam'));
SELECT pg_temp.espera_erro($$INSERT INTO rotulo.anotacao (sessao_id, tarefa_id, data_referencia, classe_id, geom, origem_codigo)
    VALUES (pg_temp.v('s_pre'), 0, now(), pg_temp.classe('agua'), pg_temp.caixa(726650, 7462300, 726675, 7462350), 'pre_rotulo_modelo')$$,
    'ck_anotacao_pre_rotulo', 'pré-rótulo sem processamento');
INSERT INTO rotulo.processamento (ferramenta_codigo, versao_ferramenta, modelo_ref, parametros)
VALUES ('samgeo', '0.13', 'sam_vit_h', '{"pontos": 25, "resolucao_m": 4.5}');
INSERT INTO rotulo.anotacao (sessao_id, tarefa_id, data_referencia, classe_id, geom, origem_codigo, processamento_id)
VALUES (pg_temp.v('s_pre'), 0, now(), pg_temp.classe('agua'), pg_temp.caixa(726650, 7462300, 726675, 7462350), 'pre_rotulo_modelo',
        (SELECT max(id) FROM rotulo.processamento));
SELECT pg_temp.confere((SELECT NOT editada FROM rotulo.anotacao WHERE sessao_id = pg_temp.v('s_pre')), 'pré-rótulo nasce não editado');
UPDATE rotulo.anotacao SET classe_id = pg_temp.classe('vegetacao_rasteira') WHERE sessao_id = pg_temp.v('s_pre');
SELECT pg_temp.confere((SELECT editada FROM rotulo.anotacao WHERE sessao_id = pg_temp.v('s_pre')), 'pré-rótulo corrigido fica marcado como editado');
SELECT pg_temp.espera_erro($$INSERT INTO rotulo.anotacao (sessao_id, tarefa_id, data_referencia, classe_id, geom, origem_codigo)
    VALUES (pg_temp.v('s_pre'), 0, now(), pg_temp.classe('agua'), pg_temp.caixa(726650, 7462300, 726660, 7462310), 'propagada')$$,
    'anotacao_origem_id', 'propagada sem origem');

-- Trabalho cego: cada pessoa só vê e edita as próprias anotações.
SELECT set_config('app.usuario', 'bia', true);
SELECT pg_temp.confere((SELECT count(*) = 2 AND bool_and(sessao_id = pg_temp.v('s_bia')) FROM rotulo.vw_minha_anotacao),
                       'bia vê só as próprias anotações');
SELECT pg_temp.espera_erro($$INSERT INTO rotulo.vw_minha_anotacao (sessao_id, tarefa_id, data_referencia, classe_id, geom)
    VALUES (pg_temp.v('s_pre'), 0, now(), pg_temp.classe('agua'), pg_temp.caixa(726690, 7462340, 726700, 7462350))$$,
    '44000', 'bia não grava na sessão da ana');
SELECT set_config('app.usuario', 'ana', true);
SELECT pg_temp.confere((SELECT count(*) FROM rotulo.vw_minha_anotacao) = 4, 'ana vê só as próprias anotações');
SELECT set_config('app.usuario', '', true);

-- =============================================================================
-- F2: série, propagação e objeto persistente
-- =============================================================================
SELECT pg_temp.guarda('serie', rotulo.fn_criar_serie(pg_temp.v('campanha')::int, 'global_monthly',
                             ST_MakeEnvelope(726500, 7462300, 726600, 7462400, 32723), '2020-01-01', '2020-03-01'));
SELECT pg_temp.confere((SELECT count(*) = 3 FROM rotulo.tarefa WHERE serie_id = pg_temp.v('serie')), 'série com 3 tarefas mensais');
SELECT pg_temp.guarda('t_s1', (SELECT id FROM rotulo.tarefa WHERE serie_id = pg_temp.v('serie') AND data_referencia = '2020-01-01'));
SELECT pg_temp.guarda('t_s2', (SELECT id FROM rotulo.tarefa WHERE serie_id = pg_temp.v('serie') AND data_referencia = '2020-02-01'));
INSERT INTO rotulo.objeto (campanha_id, observacao) VALUES (pg_temp.v('campanha'), 'lote leste');
SELECT pg_temp.guarda('objeto', (SELECT max(id) FROM rotulo.objeto));

SELECT pg_temp.guarda('s_s1', rotulo.fn_iniciar_sessao(pg_temp.v('t_s1')::int, 'ana'));
SELECT pg_temp.anotar(pg_temp.v('s_s1')::int, 'vegetacao_arborea',  726500, 7462300, 726550, 7462400);
SELECT pg_temp.anotar(pg_temp.v('s_s1')::int, 'vegetacao_rasteira', 726550, 7462300, 726600, 7462400, pg_temp.v('objeto'));
SELECT pg_temp.espera_erro($$SELECT rotulo.fn_propagar_sessao(pg_temp.v('s_s1')::int, pg_temp.v('t_s2')::int, 'ana')$$,
    'enviada ou aprovada', 'não propaga sessão em andamento');
SELECT rotulo.fn_enviar_sessao(pg_temp.v('s_s1')::int);
SELECT rotulo.fn_revisar_sessao(pg_temp.v('s_s1')::int, 'rev', true);
SELECT pg_temp.espera_erro($$SELECT rotulo.fn_propagar_sessao(pg_temp.v('s_s1')::int, pg_temp.v('tarefa')::int, 'ana')$$,
    'mesma série', 'não propaga para fora da série');

SELECT pg_temp.guarda('s_s2', rotulo.fn_propagar_sessao(pg_temp.v('s_s1')::int, pg_temp.v('t_s2')::int, 'ana'));
SELECT pg_temp.confere((SELECT count(*) = 2 AND bool_and(origem_codigo = 'propagada' AND anotacao_origem_id IS NOT NULL AND NOT editada)
                          FROM rotulo.anotacao WHERE sessao_id = pg_temp.v('s_s2')), 'propagação copia 2 anotações');
SELECT pg_temp.confere((SELECT data_referencia = '2020-02-01' FROM rotulo.anotacao WHERE sessao_id = pg_temp.v('s_s2') LIMIT 1),
                       'anotação propagada recebe a data do destino');
SELECT pg_temp.confere((SELECT count(*) = 1 FROM rotulo.anotacao WHERE sessao_id = pg_temp.v('s_s2') AND objeto_id = pg_temp.v('objeto')),
                       'objeto persistente propagado');
-- Em fevereiro o lote leste virou construção: só ele é editado.
UPDATE rotulo.anotacao SET classe_id = pg_temp.classe('edificacao')
 WHERE sessao_id = pg_temp.v('s_s2') AND objeto_id = pg_temp.v('objeto');
SELECT pg_temp.confere((SELECT count(*) FILTER (WHERE editada) = 1 FROM rotulo.anotacao WHERE sessao_id = pg_temp.v('s_s2')),
                       'só a anotação alterada fica marcada');
SELECT rotulo.fn_enviar_sessao(pg_temp.v('s_s2')::int);
SELECT rotulo.fn_revisar_sessao(pg_temp.v('s_s2')::int, 'rev', true);
SELECT pg_temp.confere((SELECT count(*) = 1 AND min(classe_de) = 'vegetacao_rasteira' AND min(classe_para) = 'edificacao'
                               AND abs(min(area_m2) - 5000) < 0.01 AND min(data_depois) = '2020-02-01'
                               AND 'edificacao_nova' = ANY (min(tipos_candidatos))
                          FROM rotulo.vw_mudanca_derivada WHERE serie_id = pg_temp.v('serie')),
                       'mudança derivada da série: rasteira → construção em 2020-02');
SELECT pg_temp.confere((SELECT count(*) = 0 FROM rotulo.vw_concordancia WHERE tarefa_id = pg_temp.v('t_s2')),
                       'sessão propagada não conta como concordância independente');

-- =============================================================================
-- F1 e F3: eventos de mudança e controles estáveis
-- =============================================================================
CREATE FUNCTION pg_temp.evento(p_apelido text, p_tipo text, p_de text, p_para text, p_inicio date, p_min date, p_max date,
                               x0 float, y0 float, x1 float, y1 float) RETURNS integer
LANGUAGE sql AS $$
    INSERT INTO rotulo.evento (campanha_id, pessoa_id, tipo_alteracao_codigo, classe_de_id, classe_para_id,
                               mes_inicio, mes_inicio_min, mes_inicio_max, geom)
    VALUES (pg_temp.v('campanha'), rotulo.fn_pessoa(p_apelido), p_tipo, pg_temp.classe(p_de), pg_temp.classe(p_para),
            p_inicio, p_min, p_max, pg_temp.caixa(x0, y0, x1, y1))
    RETURNING id
$$;

SELECT pg_temp.guarda('ev_ana', pg_temp.evento('ana', 'edificacao_nova', 'vegetacao_rasteira', 'edificacao',
                                               '2021-05-01', '2021-04-01', '2021-06-01', 727000, 7461000, 727050, 7461050));
SELECT pg_temp.espera_erro($$SELECT pg_temp.evento('ana', 'abertura_via', 'agua', 'edificacao', '2021-05-01', '2021-05-01', '2021-05-01',
                                                   727100, 7461000, 727150, 7461050)$$,
    'não é permitida', 'transição incompatível com o tipo');
SELECT pg_temp.espera_erro($$SELECT pg_temp.evento('ana', 'edificacao_nova', 'solo_exposto', 'edificacao', '2021-05-15', '2021-05-01', '2021-06-01',
                                                   727100, 7461000, 727150, 7461050)$$,
    'ck_evento_meses_dia1', 'mês de início fora do dia 1');
SELECT pg_temp.espera_erro($$SELECT pg_temp.evento('ana', 'edificacao_nova', 'solo_exposto', 'edificacao', '2021-05-01', '2021-06-01', '2021-07-01',
                                                   727100, 7461000, 727150, 7461050)$$,
    'ck_evento_intervalo', 'início fora do intervalo possível');
SELECT pg_temp.espera_erro($$SELECT pg_temp.evento('ana', 'outra', 'agua', 'agua', '2021-05-01', '2021-05-01', '2021-05-01',
                                                   727100, 7461000, 727150, 7461050)$$,
    'em_expansao', 'de = para sem expansão');

INSERT INTO rotulo.evento_evidencia VALUES (pg_temp.v('ev_ana'), pg_temp.img('global_monthly_2021_03_mosaic.tif'), 'antes', NULL);
INSERT INTO rotulo.evento_evidencia VALUES (pg_temp.v('ev_ana'), pg_temp.img('global_monthly_2021_05_mosaic.tif'), 'inicio', NULL);
INSERT INTO rotulo.evento_evidencia VALUES (pg_temp.v('ev_ana'), pg_temp.img('2023-04-11_CBERS4A_WPM_PCA_RGB321_20230411_198_142.tif'), 'confirmacao', NULL);
SELECT pg_temp.espera_erro($$INSERT INTO rotulo.evento_evidencia VALUES (pg_temp.v('ev_ana'), pg_temp.img('global_monthly_2021_05_mosaic.tif'), 'antes', NULL)$$,
    'anterior ao início', 'evidência "antes" depois do início');

-- Segundo intérprete: mesmo evento, deslocado 10 m e um mês depois.
SELECT pg_temp.guarda('ev_bia', pg_temp.evento('bia', 'edificacao_nova', 'vegetacao_rasteira', 'edificacao',
                                               '2021-06-01', '2021-06-01', '2021-06-01', 727010, 7461000, 727060, 7461050));
SELECT pg_temp.confere((SELECT iou = 0.667 AND mesmo_tipo AND mesma_transicao AND dif_mes_inicio = 1 AND mes_concorda
                          FROM rotulo.vw_concordancia_evento), 'concordância de evento: IoU 0,667, mês ± 1');
SELECT pg_temp.espera_erro($$SELECT rotulo.fn_revisar_evento(pg_temp.v('ev_ana')::int, 'ana', true)$$,
    'ck_evento_revisor_diferente', 'autorrevisão de evento');
SELECT rotulo.fn_revisar_evento(pg_temp.v('ev_ana')::int, 'rev', true);

INSERT INTO rotulo.controle_estavel (campanha_id, pessoa_id, tipo_superficie_codigo, classe_id, periodo_inicio, periodo_fim,
                                     imagem_inicio_id, imagem_fim_id, geom)
VALUES (pg_temp.v('campanha'), rotulo.fn_pessoa('ana'), 'asfalto', pg_temp.classe('via_pavimentada'), '2020-01-01', '2026-09-30',
        pg_temp.img('global_monthly_2020_01_mosaic.tif'), pg_temp.img('global_monthly_2026_09_mosaic.tif'),
        pg_temp.caixa(727400, 7461500, 727450, 7461550));
SELECT pg_temp.guarda('controle', (SELECT max(id) FROM rotulo.controle_estavel));
SELECT pg_temp.espera_erro($$INSERT INTO rotulo.controle_estavel (campanha_id, pessoa_id, tipo_superficie_codigo, classe_id, periodo_inicio, periodo_fim,
                                     imagem_inicio_id, imagem_fim_id, geom)
    VALUES (pg_temp.v('campanha'), rotulo.fn_pessoa('ana'), 'outra', pg_temp.classe('vegetacao_rasteira'), '2020-01-01', '2026-09-30',
            pg_temp.img('global_monthly_2020_01_mosaic.tif'), pg_temp.img('global_monthly_2026_09_mosaic.tif'),
            pg_temp.caixa(727000, 7461000, 727050, 7461050))$$,
    'sobrepõe o evento', 'controle sobre evento');
SELECT pg_temp.espera_erro($$SELECT pg_temp.evento('ana', 'ampliacao_via', 'via_terra', 'via_pavimentada', '2022-01-01', '2022-01-01', '2022-01-01',
                                                   727400, 7461500, 727420, 7461520)$$,
    'controle estável', 'evento sobre controle');
SELECT pg_temp.espera_erro($$INSERT INTO rotulo.controle_estavel (campanha_id, pessoa_id, tipo_superficie_codigo, classe_id, periodo_inicio, periodo_fim,
                                     imagem_inicio_id, imagem_fim_id, geom)
    VALUES (pg_temp.v('campanha'), rotulo.fn_pessoa('ana'), 'asfalto', pg_temp.classe('via_pavimentada'), '2020-01-01', '2026-09-30',
            pg_temp.img('global_monthly_2023_01_mosaic.tif'), pg_temp.img('global_monthly_2026_09_mosaic.tif'),
            pg_temp.caixa(727500, 7461500, 727550, 7461550))$$,
    'pontas do período', 'controle sem conferência no início do período');
SELECT rotulo.fn_revisar_controle(pg_temp.v('controle')::int, 'rev', true);

-- =============================================================================
-- F4: reserva temporal (três regimes de teste)
-- =============================================================================
INSERT INTO rotulo.tarefa (campanha_id, imagem_id, data_referencia, geom, motivo)
SELECT pg_temp.v('campanha'), pg_temp.img('global_monthly_2026_03_mosaic.tif'), now(),
       ST_Expand(ST_Centroid(b.geom_util), 20), 'teste temporal ' || b.papel_codigo
  FROM (SELECT DISTINCT ON (papel_codigo) * FROM treino.bloco
         WHERE papel_codigo IN ('treino', 'teste') AND ST_Area(geom_util) > 250000 ORDER BY papel_codigo, id) b;
SELECT pg_temp.confere((SELECT array_agg(tc.papel ORDER BY tc.papel) = ARRAY['teste_espaco_tempo', 'teste_temporal']
                          FROM rotulo.tarefa t JOIN treino.vw_tarefa_conjunto tc ON tc.tarefa_id = t.id
                         WHERE t.motivo LIKE 'teste temporal%'),
                       'período reservado: treino → teste_temporal, teste → teste_espaco_tempo');
SELECT pg_temp.confere((SELECT papel = 'teste_temporal' OR papel = 'teste_espaco_tempo' FROM treino.vw_evento_conjunto ec
                          JOIN rotulo.evento e ON e.id = ec.evento_id WHERE e.id = pg_temp.v('ev_ana')) IS NOT TRUE,
                       'evento de 2021 fica fora da reserva temporal');

-- =============================================================================
-- F5: plano amostral independente e aprendizado ativo
-- =============================================================================
INSERT INTO rotulo.plano_amostral (campanha_id, codigo, uso, semente, descricao)
VALUES (pg_temp.v('campanha'), 'aval_2020_01', 'avaliacao_independente', 7, 'teste');
INSERT INTO rotulo.estrato (plano_id, codigo, geom, n_alvo)
VALUES ((SELECT max(id) FROM rotulo.plano_amostral), 'estavel', pg_temp.caixa(726300, 7462500, 726345, 7462545), 5);
SELECT pg_temp.guarda('estrato', (SELECT max(id) FROM rotulo.estrato));
SELECT pg_temp.confere(rotulo.fn_sortear_pontos(pg_temp.v('estrato')::int, pg_temp.v('img_2020_01')::int, 5) = 5, '5 pontos sorteados');
SELECT pg_temp.confere((SELECT bool_and(abs(area_m2 - 20.25) < 1e-6) AND count(DISTINCT prob_inclusao) = 1
                               AND min(prob_inclusao) = 5.0 / 90
                          FROM rotulo.tarefa WHERE estrato_id = pg_temp.v('estrato')),
                       'pontos de 1 pixel com prob_inclusao = 5/90');
SELECT pg_temp.guarda('t_pt', (SELECT min(id) FROM rotulo.tarefa WHERE estrato_id = pg_temp.v('estrato')));
SELECT pg_temp.rotular_e_aprovar(pg_temp.v('t_pt')::int, 'bia', 'solo_exposto');
SELECT pg_temp.confere((SELECT peso = 18 AND classe_referencia = 'solo_exposto' FROM rotulo.vw_amostra_avaliacao
                         WHERE tarefa_id = pg_temp.v('t_pt')), 'amostra de avaliação com peso 18 e classe de referência');
SELECT pg_temp.espera_erro($$INSERT INTO rotulo.tarefa (campanha_id, imagem_id, data_referencia, geom, modo_selecao_codigo)
    VALUES (pg_temp.v('campanha'), pg_temp.v('img_2020_01'), now(), ST_MakeEnvelope(726400, 7461000, 726410, 7461010, 32723), 'aleatoria')$$,
    'ck_tarefa_prob_obrigatoria', 'sorteio sem probabilidade de inclusão');
SELECT pg_temp.espera_erro($$INSERT INTO rotulo.tarefa (campanha_id, imagem_id, data_referencia, geom, modo_selecao_codigo)
    VALUES (pg_temp.v('campanha'), pg_temp.v('img_2020_01'), now(), ST_MakeEnvelope(726300, 7461000, 726310, 7461010, 32723), 'aprendizado_ativo')$$,
    'ck_tarefa_ativo_ciclo', 'aprendizado ativo sem ciclo');

INSERT INTO rotulo.processamento (ferramenta_codigo, modelo_ref, parametros, run_id)
VALUES ('pipeline_mudanca', 'unet_r18_v0', '{"criterio": "entropia"}', 'run_teste');
INSERT INTO rotulo.ciclo_aprendizado (campanha_id, numero, processamento_id, limiar, fracao_aleatoria)
VALUES (pg_temp.v('campanha'), 1, (SELECT max(id) FROM rotulo.processamento), 0.6, 0.2);
INSERT INTO rotulo.tarefa (campanha_id, imagem_id, data_referencia, geom, modo_selecao_codigo, ciclo_id, incerteza, motivo)
SELECT pg_temp.v('campanha'), pg_temp.v('img_2020_01'), now(), ST_Expand(ST_Centroid(b.geom_util), 20),
       'aprendizado_ativo', (SELECT max(id) FROM rotulo.ciclo_aprendizado), 0.8, 'ativo em teste'
  FROM treino.bloco b WHERE b.papel_codigo = 'teste' AND ST_Area(b.geom_util) > 250000 ORDER BY b.id LIMIT 1;
SELECT pg_temp.guarda('t_ativo', (SELECT id FROM rotulo.tarefa WHERE motivo = 'ativo em teste'));
SELECT pg_temp.rotular_e_aprovar(pg_temp.v('t_ativo')::int, 'bia', 'vegetacao_arborea');

-- =============================================================================
-- F6: uma grade por dataset
-- =============================================================================
INSERT INTO rotulo.tarefa (campanha_id, imagem_id, data_referencia, geom, motivo)
VALUES (pg_temp.v('campanha'), pg_temp.img('2023-04-11_CBERS4A_WPM_PCA_RGB321_20230411_198_142.tif'), now(),
        ST_MakeEnvelope(726300, 7462300, 726400, 7462400, 32723), 'cbers');
SELECT pg_temp.guarda('t_cbers', (SELECT id FROM rotulo.tarefa WHERE motivo = 'cbers'));
SELECT pg_temp.rotular_e_aprovar(pg_temp.v('t_cbers')::int, 'bia', 'vegetacao_arborea');

-- =============================================================================
-- Dataset: montagem, exigências e congelamento
-- =============================================================================
INSERT INTO treino.dataset (codigo, versao, campanha_id, divisao_id, grade_id)
SELECT 'teste', 1, pg_temp.v('campanha'), d.id, d.grade_id FROM treino.divisao d WHERE d.codigo = 'blocos_600m_s42';
SELECT pg_temp.guarda('ds', (SELECT id FROM treino.dataset WHERE codigo = 'teste'));
SELECT pg_temp.espera_erro($$SELECT treino.fn_congelar_dataset(pg_temp.v('ds')::int)$$, 'sem sha256', 'dataset exige sha256 das imagens');
UPDATE catalogo.imagem SET sha256 = repeat('a', 64), qc_status_codigo = 'aprovada', qc_em = now()
 WHERE produto_codigo = 'global_monthly' AND qc_status_codigo <> 'reprovada';

INSERT INTO treino.dataset (codigo, versao, campanha_id, divisao_id, grade_id, parametros)
SELECT 'teste_estrito', 1, pg_temp.v('campanha'), d.id, d.grade_id, '{"exigir_todas_classes": true}'
  FROM treino.divisao d WHERE d.codigo = 'blocos_600m_s42';
SELECT pg_temp.espera_erro($$SELECT treino.fn_congelar_dataset((SELECT id FROM treino.dataset WHERE codigo = 'teste_estrito'))$$,
    'Classes ausentes', 'dataset estrito recusa classe ausente num conjunto');

SELECT pg_temp.confere(treino.fn_congelar_dataset(pg_temp.v('ds')::int) = 5, 'dataset congelado: 3 máscaras + 1 evento + 1 controle');
SELECT pg_temp.confere((SELECT array_agg(tarefa_id ORDER BY tarefa_id) = ARRAY[pg_temp.v('tarefa'), pg_temp.v('t_s1'), pg_temp.v('t_s2')]::int[]
                          FROM treino.dataset_amostra WHERE dataset_id = pg_temp.v('ds')),
                       'máscaras: tarefa e série; sem ponto de avaliação, sem ativo no teste, sem CBERS');
SELECT pg_temp.confere((SELECT count(*) = 1 AND min(mes_inicio) = '2021-05' AND min(tipo_alteracao_codigo) = 'edificacao_nova'
                          FROM treino.vw_evento_referencia WHERE dataset_id = pg_temp.v('ds')),
                       'evento confirmado da ana no dataset (o da bia, não revisado, fica fora)');
SELECT pg_temp.confere((SELECT count(*) = 1 FROM treino.dataset_controle WHERE dataset_id = pg_temp.v('ds')), 'controle confirmado no dataset');
SELECT pg_temp.confere((SELECT count(*) = 3 AND abs(sum(ST_Area(geom)) - 10000) < 0.01 FROM treino.vw_mascara_poligono
                         WHERE dataset_id = pg_temp.v('ds') AND tarefa_id = pg_temp.v('tarefa')), '3 polígonos cobrindo a tarefa');
SELECT pg_temp.confere((SELECT col_ini = 18 AND lin_ini = 83 AND col_fim = 41 AND lin_fim = 107 FROM treino.vw_mascara_janela
                         WHERE dataset_id = pg_temp.v('ds') AND tarefa_id = pg_temp.v('tarefa')),
                       'janela da tarefa na grade (col 18-41, lin 83-107)');
SELECT pg_temp.confere((SELECT bool_and(abs(s - 100) < 0.01) FROM (SELECT sum(pct_no_conjunto) AS s FROM treino.vw_balanco_classe
                         WHERE dataset = 'teste' GROUP BY papel_codigo) x), 'balanço de classes soma 100% por conjunto');

SELECT pg_temp.espera_erro($$SELECT rotulo.fn_reabrir_sessao(pg_temp.v('s_ana')::int)$$, 'dataset congelado', 'reabrir referência congelada');
SELECT pg_temp.espera_erro($$DELETE FROM treino.dataset_amostra WHERE dataset_id = pg_temp.v('ds')$$, 'congelado', 'remover amostra congelada');
SELECT pg_temp.espera_erro($$DELETE FROM treino.dataset_evento WHERE dataset_id = pg_temp.v('ds')$$, 'congelado', 'remover evento de dataset congelado');
SELECT pg_temp.espera_erro($$UPDATE treino.dataset SET congelado_em = NULL WHERE id = pg_temp.v('ds')$$, 'congelado', 'descongelar dataset');
SELECT pg_temp.espera_erro($$UPDATE rotulo.evento SET observacao = 'x' WHERE id = pg_temp.v('ev_ana')$$, 'dataset congelado', 'evento congelado imutável');
SELECT pg_temp.espera_erro($$UPDATE rotulo.controle_estavel SET observacao = 'x' WHERE id = pg_temp.v('controle')$$, 'dataset congelado', 'controle congelado imutável');
UPDATE rotulo.evento SET observacao = 'ainda editável' WHERE id = pg_temp.v('ev_bia');
UPDATE treino.dataset_amostra SET caminho_mascara = 'runs/x/mask.tif', gerada_em = now() WHERE dataset_id = pg_temp.v('ds');
SELECT pg_temp.confere(true, 'registrar máscara gerada em dataset congelado');

-- =============================================================================
-- Auditoria e operações auxiliares
-- =============================================================================
SELECT pg_temp.confere((SELECT count(DISTINCT tabela) >= 8 FROM auditoria.registro), 'auditoria registrou as tabelas de rotulagem');
SELECT pg_temp.confere(treino.fn_criar_tarefas_por_bloco(pg_temp.v('campanha')::int, pg_temp.img('global_monthly_2020_05_mosaic.tif'),
                           (SELECT id FROM treino.divisao WHERE codigo = 'blocos_600m_s42'), ARRAY['validacao']) > 0,
                       'tarefas criadas a partir dos blocos de validação');

ROLLBACK;
\echo 'TODOS OS TESTES PASSARAM (alterações desfeitas)'
