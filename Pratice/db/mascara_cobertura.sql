-- =============================================================================
-- Banco da máscara de cobertura terrestre (referência para treino e avaliação)
-- SQL plain para PostgreSQL 18 + PostGIS. Rodar com psql num banco vazio:
--
--   createdb -U postgres mudanca_mascara
--   psql -U postgres -d mudanca_mascara -v ON_ERROR_STOP=1 -f db/mascara_cobertura.sql
--
-- O que guarda: polígonos de cobertura (rua, construção, vegetação densa,
-- vegetação rasteira, solo exposto, água...) desenhados sobre UMA imagem, com a
-- DATA do que foi classificado. É só a máscara: o vínculo com a imagem que será
-- vetorizada é feito por imagem.id (e pela data). Os rasters ficam fora do banco
-- (D:\PT2-build\Imagens de Satelite, somente leitura); aqui só o caminho relativo.
--
-- Classes alinhadas com configs/classes.yaml (ids 1-7). Mudou lá, mude aqui.
-- CRS de tudo: EPSG:32723 (configs/pipeline.yaml).
-- Detalhes e uso: docs/banco_mascara.md
-- =============================================================================

SET client_encoding = 'UTF8';
SET client_min_messages = warning;

BEGIN;

CREATE EXTENSION IF NOT EXISTS postgis;

CREATE SCHEMA IF NOT EXISTS mascara;
COMMENT ON SCHEMA mascara IS 'Máscara de cobertura terrestre (rótulos) vinculada às imagens da AOI';

SET search_path = mascara, public;

-- -----------------------------------------------------------------------------
-- Domínios
-- -----------------------------------------------------------------------------

-- Valor gravado no raster da máscara: 1-7 classes, 0 = não rotulado, 255 = ignorar.
CREATE TABLE classe (
    id          smallint PRIMARY KEY CHECK (id BETWEEN 0 AND 255),
    nome        text     NOT NULL UNIQUE,
    rotulo      text     NOT NULL,          -- nome amigável para o QGIS
    descricao   text,
    tipo        text     NOT NULL CHECK (tipo IN ('cobertura', 'exclusao')),
    cor_hex     char(7)  NOT NULL CHECK (cor_hex ~ '^#[0-9A-Fa-f]{6}$'),
    ativo       boolean  NOT NULL DEFAULT true
);
COMMENT ON TABLE  classe IS 'Classes da máscara. id = valor do pixel no raster gerado. tipo exclusao = área a ignorar no treino (não é classe)';
COMMENT ON COLUMN classe.id IS '0 = não rotulado (fora de area_rotulada); 255 = ignorar; 1-7 = cobertura (configs/classes.yaml)';

INSERT INTO classe (id, nome, rotulo, descricao, tipo, cor_hex) VALUES
    (1,   'vegetacao_arborea',  'Vegetação densa',    'árvores, mata, restinga arbórea, mangue',                       'cobertura', '#1B5E20'),
    (2,   'vegetacao_rasteira', 'Vegetação rasteira', 'pasto, campo, gramado, vegetação baixa e brejo vegetado',       'cobertura', '#9CCC65'),
    (3,   'solo_exposto',       'Solo exposto',       'terra sem cobertura, aterro, areia, movimentação de terra',     'cobertura', '#D7A86E'),
    (4,   'edificacao',         'Construção',         'telhados e estruturas fechadas',                                'cobertura', '#C62828'),
    (5,   'via_pavimentada',    'Rua pavimentada',    'asfalto, concreto, calçamento',                                 'cobertura', '#424242'),
    (6,   'via_terra',          'Rua de terra',       'estrada e rua de terra',                                        'cobertura', '#8D6E63'),
    (7,   'agua',               'Massa d''água',      'lagoa, canal, represa',                                         'cobertura', '#1E88E5'),
    (251, 'nuvem',              'Nuvem',              'nuvem ou névoa que impede ver o solo',                          'exclusao',  '#FFFFFF'),
    (252, 'sombra',             'Sombra',             'sombra de nuvem ou de relevo',                                  'exclusao',  '#000000'),
    (253, 'sem_dado',           'Sem dado',           'alfa 0 no raster',                                              'exclusao',  '#FF00FF'),
    (254, 'borda_mosaico',      'Borda de mosaico',   'costura entre cenas com cor ou geometria inconsistente',        'exclusao',  '#FFEB3B'),
    (255, 'ignorar',            'Ignorar / duvidoso', 'o rotulador não sabe dizer; fica fora do treino e da avaliação', 'exclusao',  '#9E9E9E');

CREATE TABLE fonte (
    nome        text PRIMARY KEY,
    descricao   text,
    pasta       text NOT NULL,              -- relativa à raiz de dados (configs/pipeline.yaml)
    resolucao_m real NOT NULL CHECK (resolucao_m > 0)
);
COMMENT ON TABLE fonte IS 'Famílias de imagem (configs/pipeline.yaml: dados.fontes)';

INSERT INTO fonte (nome, descricao, pasta, resolucao_m) VALUES
    ('global_monthly',    'Planet basemap visual mensal (série principal candidata)', 'data/planet_basemaps/global_monthly',            4.5),
    ('medres_normalized', 'Planet basemap normalizado',                               'data/planet_basemaps/medres_normalized',         4.5),
    ('psscene',           'Mosaico de cenas PSScene (imagem nova de teste)',          'data/planet_psscene/mosaico_2026-10-23/mosaico', 3.0),
    ('cbers_wpm',         'CBERS-4A WPM fundida 2 m (apoio de rotulagem, não Planet)','CBERS/wpm_fused_2m',                             2.0);

-- -----------------------------------------------------------------------------
-- Imagem: a quem a máscara se vincula
-- -----------------------------------------------------------------------------

CREATE TABLE imagem (
    id              serial PRIMARY KEY,
    fonte           text   NOT NULL REFERENCES fonte (nome),
    arquivo         text   NOT NULL,        -- nome do .tif dentro de fonte.pasta
    data_ini        date   NOT NULL,        -- início do período que a imagem representa
    data_fim        date   NOT NULL,        -- fim (= data_ini para cena de uma data)
    data_referencia date   NOT NULL,        -- data usada para a máscara (padrão: data_ini)
    mes_ref         text   GENERATED ALWAYS AS (   -- to_char não é imutável; montar à mão
                        extract(year FROM data_referencia)::int::text || '-' ||
                        lpad(extract(month FROM data_referencia)::int::text, 2, '0')) STORED,
    resolucao_m     real,
    largura_px      integer CHECK (largura_px > 0),
    altura_px       integer CHECK (altura_px > 0),
    extensao        geometry(Polygon, 32723), -- preenchida pelo inventário (pipeline)
    observacao      text,
    criado_em       timestamptz NOT NULL DEFAULT now(),
    UNIQUE (fonte, arquivo),
    CHECK (data_fim >= data_ini),
    CHECK (data_referencia BETWEEN data_ini AND data_fim)
);
COMMENT ON TABLE  imagem IS 'Uma linha por raster. A máscara aponta para cá; o raster continua fora do banco';
COMMENT ON COLUMN imagem.mes_ref IS 'AAAA-MM, igual a mes_ini/mes_fim do esquema dos vetores';
CREATE INDEX imagem_data_idx     ON imagem (data_referencia);
CREATE INDEX imagem_extensao_gix ON imagem USING gist (extensao);

-- -----------------------------------------------------------------------------
-- Área rotulada: onde a classificação está completa
-- Dentro dela todo pixel tem classe (ou exclusão); fora, o raster recebe 0 e
-- não entra no treino. Sem isso não dá para distinguir "não é edificação" de
-- "ninguém olhou".
-- -----------------------------------------------------------------------------

CREATE TABLE area_rotulada (
    id              serial PRIMARY KEY,
    id_imagem       integer NOT NULL REFERENCES imagem (id) ON DELETE CASCADE,
    data_referencia date    NOT NULL,
    geom            geometry(MultiPolygon, 32723) NOT NULL,
    completa        boolean NOT NULL DEFAULT false, -- true quando o rotulador terminou o recorte
    autor           text,
    observacao      text,
    criado_em       timestamptz NOT NULL DEFAULT now(),
    atualizado_em   timestamptz NOT NULL DEFAULT now()
);
COMMENT ON TABLE area_rotulada IS 'Recortes cuja classificação está (ou estará) completa. Só os completa = true geram máscara';
CREATE INDEX area_rotulada_geom_gix ON area_rotulada USING gist (geom);
CREATE INDEX area_rotulada_img_idx  ON area_rotulada (id_imagem);

-- -----------------------------------------------------------------------------
-- Cobertura: os polígonos da máscara
-- -----------------------------------------------------------------------------

CREATE TABLE cobertura (
    id              bigserial PRIMARY KEY,
    id_imagem       integer  NOT NULL REFERENCES imagem (id) ON DELETE CASCADE,
    data_referencia date     NOT NULL,  -- data do que está sendo classificado
    id_classe       smallint NOT NULL REFERENCES classe (id),
    geom            geometry(MultiPolygon, 32723) NOT NULL,
    area_m2         double precision GENERATED ALWAYS AS (ST_Area(geom)) STORED,
    origem          text NOT NULL DEFAULT 'manual'
                    CHECK (origem IN ('manual', 'modelo', 'importado')),
    confianca       real CHECK (confianca BETWEEN 0 AND 1), -- do rotulador ou do modelo
    imagem_apoio    integer REFERENCES imagem (id),          -- ex.: CBERS 2 m usada para decidir
    status_revisao  text NOT NULL DEFAULT 'nao_revisado'
                    CHECK (status_revisao IN ('nao_revisado', 'confirmado', 'rejeitado')),
    autor           text,
    revisor         text,
    data_revisao    date,
    observacao      text,
    criado_em       timestamptz NOT NULL DEFAULT now(),
    atualizado_em   timestamptz NOT NULL DEFAULT now()
);
COMMENT ON TABLE  cobertura IS 'Polígonos de cobertura da máscara; sem sobreposição dentro da mesma imagem';
COMMENT ON COLUMN cobertura.data_referencia IS 'Data do que foi classificado; padrão = imagem.data_referencia';
COMMENT ON COLUMN cobertura.imagem_apoio IS 'Imagem auxiliar consultada (não é a imagem rotulada)';
CREATE INDEX cobertura_geom_gix   ON cobertura USING gist (geom);
CREATE INDEX cobertura_img_idx    ON cobertura (id_imagem);
CREATE INDEX cobertura_data_idx   ON cobertura (data_referencia);
CREATE INDEX cobertura_classe_idx ON cobertura (id_classe);

-- -----------------------------------------------------------------------------
-- Gatilhos
-- -----------------------------------------------------------------------------

-- Data padrão vinda da imagem, geometria corrigida (QGIS às vezes grava
-- polígono inválido) e carimbo de atualização.
CREATE FUNCTION preparar_poligono() RETURNS trigger
LANGUAGE plpgsql AS $$
BEGIN
    IF NEW.data_referencia IS NULL THEN
        SELECT i.data_referencia INTO NEW.data_referencia
          FROM mascara.imagem i WHERE i.id = NEW.id_imagem;
    END IF;

    IF NOT ST_IsValid(NEW.geom) THEN
        NEW.geom := ST_Multi(ST_CollectionExtract(ST_MakeValid(NEW.geom), 3));
    END IF;
    IF ST_IsEmpty(NEW.geom) OR ST_Area(NEW.geom) = 0 THEN
        RAISE EXCEPTION 'Polígono vazio ou sem área (tabela %, imagem %)', TG_TABLE_NAME, NEW.id_imagem;
    END IF;

    NEW.atualizado_em := now();
    RETURN NEW;
END $$;

-- A máscara é uma partição: dois polígonos da mesma imagem não podem dividir
-- área (tocar na borda pode). Recorte o vizinho antes de desenhar por cima.
CREATE FUNCTION impedir_sobreposicao() RETURNS trigger
LANGUAGE plpgsql AS $$
DECLARE
    conflito bigint;
BEGIN
    SELECT c.id INTO conflito
      FROM mascara.cobertura c
     WHERE c.id_imagem = NEW.id_imagem
       AND c.id <> NEW.id
       AND c.geom && NEW.geom
       AND ST_Relate(c.geom, NEW.geom, '2********')
     LIMIT 1;
    IF conflito IS NOT NULL THEN
        RAISE EXCEPTION 'Cobertura sobrepõe o polígono % da mesma imagem (%)', conflito, NEW.id_imagem
              USING HINT = 'Use mascara.recortar_vizinhos(geom, id_imagem) ou ajuste no QGIS com aderência';
    END IF;
    RETURN NEW;
END $$;

CREATE TRIGGER cobertura_preparar BEFORE INSERT OR UPDATE ON cobertura
    FOR EACH ROW EXECUTE FUNCTION preparar_poligono();
CREATE TRIGGER cobertura_sem_sobreposicao BEFORE INSERT OR UPDATE OF geom, id_imagem ON cobertura
    FOR EACH ROW EXECUTE FUNCTION impedir_sobreposicao();
CREATE TRIGGER area_rotulada_preparar BEFORE INSERT OR UPDATE ON area_rotulada
    FOR EACH ROW EXECUTE FUNCTION preparar_poligono();

-- Abre espaço para um polígono novo: subtrai a geometria dos vizinhos da mesma
-- imagem (o novo "vence"). Devolve quantos vizinhos foram alterados/removidos.
CREATE FUNCTION recortar_vizinhos(p_geom geometry, p_id_imagem integer)
RETURNS integer LANGUAGE plpgsql AS $$
DECLARE
    n integer;
BEGIN
    DELETE FROM mascara.cobertura c
     WHERE c.id_imagem = p_id_imagem
       AND ST_CoveredBy(c.geom, p_geom);

    UPDATE mascara.cobertura c
       SET geom = ST_Multi(ST_CollectionExtract(ST_Difference(c.geom, p_geom), 3))
     WHERE c.id_imagem = p_id_imagem
       AND c.geom && p_geom
       AND ST_Relate(c.geom, p_geom, '2********');
    GET DIAGNOSTICS n = ROW_COUNT;
    RETURN n;
END $$;

-- -----------------------------------------------------------------------------
-- Visões
-- -----------------------------------------------------------------------------

-- Camada para o QGIS: classe por nome e cor, data e imagem à vista.
CREATE VIEW v_cobertura AS
SELECT c.id, c.id_imagem, i.fonte, i.arquivo, c.data_referencia,
       to_char(c.data_referencia, 'YYYY-MM') AS mes_ref,
       c.id_classe, k.nome AS classe, k.rotulo, k.tipo, k.cor_hex,
       c.area_m2, c.origem, c.confianca, c.status_revisao, c.autor, c.geom
  FROM cobertura c
  JOIN classe k ON k.id = c.id_classe
  JOIN imagem i ON i.id = c.id_imagem;

-- Entrada para rasterizar (gdal_rasterize -a valor ou rasterio.features.rasterize),
-- na ordem de queima: área rotulada completa = 0 de fundo... depois as classes.
-- Polígonos rejeitados na revisão ficam de fora.
CREATE VIEW v_mascara_entrada AS
SELECT c.id_imagem, c.data_referencia, c.id_classe AS valor, 2 AS ordem, c.geom
  FROM cobertura c
 WHERE c.status_revisao <> 'rejeitado'
UNION ALL
SELECT a.id_imagem, a.data_referencia, 0 AS valor, 1 AS ordem, a.geom
  FROM area_rotulada a
 WHERE a.completa;
COMMENT ON VIEW v_mascara_entrada IS 'valor = pixel do raster. Fora de area_rotulada completa use nodata/0 e ignore no treino';

-- Lacunas: parte da área rotulada completa que ainda não tem classe.
CREATE VIEW v_lacunas AS
SELECT a.id AS id_area_rotulada, a.id_imagem, a.data_referencia,
       ST_Multi(ST_CollectionExtract(
           ST_Difference(a.geom, COALESCE(
               (SELECT ST_Union(c.geom) FROM cobertura c
                 WHERE c.id_imagem = a.id_imagem AND c.geom && a.geom),
               'MULTIPOLYGON EMPTY'::geometry(MultiPolygon, 32723))), 3))::geometry(MultiPolygon, 32723) AS geom
  FROM area_rotulada a
 WHERE a.completa;

-- Área por imagem e classe (para conferir balanço de classes antes do treino).
CREATE VIEW v_resumo AS
SELECT i.id AS id_imagem, i.fonte, i.mes_ref, k.nome AS classe,
       count(*) AS n_poligonos, round(sum(c.area_m2)::numeric, 1) AS area_m2,
       round((sum(c.area_m2) / 10000)::numeric, 3) AS area_ha
  FROM cobertura c
  JOIN classe k ON k.id = c.id_classe
  JOIN imagem i ON i.id = c.id_imagem
 WHERE c.status_revisao <> 'rejeitado'
 GROUP BY i.id, i.fonte, i.mes_ref, k.id, k.nome
 ORDER BY i.id, k.id;

-- -----------------------------------------------------------------------------
-- Imagens existentes em D:\PT2-build\Imagens de Satelite (conferido 2026-10-24).
-- Extensão e tamanho ficam nulos: o inventário do pipeline preenche.
-- -----------------------------------------------------------------------------

-- global_monthly: 81 meses, 2020-01 a 2026-09
INSERT INTO imagem (fonte, arquivo, data_ini, data_fim, data_referencia, resolucao_m)
SELECT 'global_monthly',
       format('global_monthly_%s_mosaic.tif', to_char(m, 'YYYY_MM')),
       m::date, (m + interval '1 month - 1 day')::date, m::date, 4.5
  FROM generate_series('2020-01-01'::date, '2026-09-01'::date, interval '1 month') AS m;

-- medres_normalized: 1 trimestre (2020-06 a 2020-08) + 73 meses (2020-09 a 2026-09)
INSERT INTO imagem (fonte, arquivo, data_ini, data_fim, data_referencia, resolucao_m) VALUES
    ('medres_normalized', 'planet_medres_normalized_analytic_2020-06_2020-08_mosaic.tif',
     '2020-06-01', '2020-08-31', '2020-06-01', 4.5);
INSERT INTO imagem (fonte, arquivo, data_ini, data_fim, data_referencia, resolucao_m)
SELECT 'medres_normalized',
       format('planet_medres_normalized_analytic_%s_mosaic.tif', to_char(m, 'YYYY-MM')),
       m::date, (m + interval '1 month - 1 day')::date, m::date, 4.5
  FROM generate_series('2020-09-01'::date, '2026-09-01'::date, interval '1 month') AS m;

-- psscene: mosaico de uma cena, 2026-10-09
INSERT INTO imagem (fonte, arquivo, data_ini, data_fim, data_referencia, resolucao_m, observacao) VALUES
    ('psscene', 'mosaico_mosaico_2026-10-23_rgb.tif', '2026-10-09', '2026-10-09', '2026-10-09', 3.0,
     'datas por pixel em mosaico_mosaico_2026-10-23_datas.tif');

-- cbers_wpm: 21 datas, 2023-04 a 2026-10
INSERT INTO imagem (fonte, arquivo, data_ini, data_fim, data_referencia, resolucao_m)
SELECT 'cbers_wpm', a, d, d, d, 2.0
  FROM (VALUES
    ('2023-04-11_CBERS4A_WPM_PCA_RGB321_20230411_198_142.tif', '2023-04-11'::date),
    ('2023-06-12_CBERS4A_WPM_PCA_RGB321_20230612_198_142.tif', '2023-06-12'),
    ('2023-09-13_CBERS4A_WPM_PCA_RGB321_20230913_198_142.tif', '2023-09-13'),
    ('2023-11-14_CBERS4A_WPM_PCA_RGB321_20231114_198_142.tif', '2023-11-14'),
    ('2023-12-15_CBERS4A_WPM_PCA_RGB321_20231215_198_142.tif', '2023-12-15'),
    ('2024-01-15_CBERS4A_WPM_PCA_RGB321_20240115_198_142.tif', '2024-01-15'),
    ('2024-04-17_CBERS4A_WPM_PCA_RGB321_20240417_198_142.tif', '2024-04-17'),
    ('2024-04-22_CBERS4A_WPM_PCA_RGB321_20240422_197_142.tif', '2024-04-22'),
    ('2024-05-18_CBERS4A_WPM_PCA_RGB321_20240518_198_142.tif', '2024-05-18'),
    ('2024-08-19_CBERS4A_WPM_PCA_RGB321_20240819_198_142.tif', '2024-08-19'),
    ('2025-01-21_CBERS4A_WPM_PCA_RGB321_20250121_198_142.tif', '2025-01-21'),
    ('2025-05-25_CBERS4A_WPM_PCA_RGB321_20250525_198_142.tif', '2025-05-25'),
    ('2025-06-25_CBERS4A_WPM_PCA_RGB321_20250625_198_142.tif', '2025-06-25'),
    ('2025-07-26_CBERS4A_WPM_PCA_RGB321_20250726_198_142.tif', '2025-07-26'),
    ('2025-10-27_CBERS4A_WPM_PCA_RGB321_20251027_198_142.tif', '2025-10-27'),
    ('2026-01-02_CBERS4A_WPM_PCA_RGB321_20260102_197_142.tif', '2026-01-02'),
    ('2026-01-28_CBERS4A_WPM_PCA_RGB321_20260128_198_142.tif', '2026-01-28'),
    ('2026-03-31_CBERS4A_WPM_PCA_RGB321_20260331_198_142.tif', '2026-03-31'),
    ('2026-08-07_CBERS4A_WPM_PCA_RGB321_20260807_197_142.tif', '2026-08-07'),
    ('2026-09-02_CBERS4A_WPM_PCA_RGB321_20260902_198_142.tif', '2026-09-02'),
    ('2026-10-08_CBERS4A_WPM_PCA_RGB321_20261008_197_142.tif', '2026-10-08')
  ) AS t (a, d);

COMMIT;
