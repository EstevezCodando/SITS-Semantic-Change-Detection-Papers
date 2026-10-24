-- Testes das regras do banco mudanca_mascara. Rodam numa transação e desfazem tudo no fim.
--   psql -U postgres -d mudanca_mascara -f db/testes.sql
-- Cada teste imprime "ok: ..." ou interrompe com o motivo.

\set ON_ERROR_STOP on
SET client_min_messages = notice;
\pset tuples_only on
BEGIN;

-- Executa o comando e exige que ele falhe com mensagem contendo o trecho esperado.
CREATE FUNCTION pg_temp.espera_erro(p_sql text, p_trecho text, p_nome text) RETURNS void
LANGUAGE plpgsql AS $$
BEGIN
    BEGIN
        EXECUTE p_sql;
    EXCEPTION WHEN others THEN
        IF position(p_trecho IN SQLERRM) = 0 THEN
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

-- Carga inicial ---------------------------------------------------------------
SELECT pg_temp.confere((SELECT count(*) FROM catalogo.imagem) = 179, 'catálogo com 179 imagens');
SELECT pg_temp.confere((SELECT count(*) FROM catalogo.grade) = 3, '3 grades');
SELECT pg_temp.confere((SELECT count(*) FROM dominio.vw_classe WHERE atribuivel) = 12, '12 classes atribuíveis');
SELECT pg_temp.confere((SELECT count(*) FROM dominio.vw_classe WHERE atribuivel AND tipo = 'cobertura') = 7, '7 classes de cobertura');
SELECT pg_temp.confere((SELECT bool_and(ST_IsValid(geom) AND ST_Area(geom) > 1e6) FROM catalogo.aoi), 'AOI válida e maior que 1 km²');
SELECT pg_temp.confere((SELECT ST_CoveredBy(a.geom, g.geom) FROM catalogo.aoi a, catalogo.grade g WHERE g.codigo = 'planet_4m5_jardim_interlagos'), 'AOI dentro da grade Planet');
SELECT pg_temp.confere((SELECT count(*) FROM treino.bloco) = 30, '30 blocos de 600 m');
SELECT pg_temp.confere((SELECT count(*) FILTER (WHERE papel_codigo = 'treino') = 18 AND count(*) FILTER (WHERE papel_codigo = 'validacao') = 6
                          FROM treino.bloco), 'sorteio 18/6/6');
SELECT pg_temp.confere((SELECT count(*) FROM auditoria.registro) = 0, 'auditoria limpa após carga');

-- Taxonomia -------------------------------------------------------------------
SELECT pg_temp.espera_erro($$INSERT INTO dominio.classe (taxonomia_id, codigo, nome, classe_pai_id, nivel, tipo, valor_raster, cor_hex, ordem)
    SELECT taxonomia_id, 'x', 'x', id, 2, 'cobertura', 1, '#000000', 99 FROM dominio.classe WHERE codigo = 'vegetacao'$$,
    'uq_classe_taxonomia_valor', 'valor de pixel repetido na taxonomia');
SELECT pg_temp.espera_erro($$INSERT INTO dominio.classe (taxonomia_id, codigo, nome, classe_pai_id, nivel, tipo, valor_raster, cor_hex, ordem)
    SELECT taxonomia_id, 'x', 'x', id, 3, 'cobertura', 99, '#000000', 99 FROM dominio.classe WHERE codigo = 'agua'$$,
    'é folha', 'folha não pode ter filhas');

-- Cenário: pessoas, tarefa no bloco (0,0) da imagem 2020-01 -----------------
INSERT INTO rotulo.pessoa (apelido, nome, funcao_codigo) VALUES
    ('ana', 'Ana Teste', 'rotulador'), ('bia', 'Bia Teste', 'rotulador'), ('rev', 'Revisor Teste', 'revisor');

CREATE TEMP TABLE ctx AS
SELECT (SELECT id FROM rotulo.campanha WHERE codigo = 'cobertura_referencia_v1') AS campanha,
       (SELECT id FROM catalogo.imagem WHERE arquivo = 'global_monthly_2020_01_mosaic.tif') AS imagem;

INSERT INTO rotulo.tarefa (campanha_id, imagem_id, data_referencia, geom, motivo)
SELECT campanha, imagem, '1900-01-01', ST_MakeEnvelope(726300, 7462300, 726400, 7462400, 32723), 'teste' FROM ctx;
ALTER TABLE ctx ADD COLUMN tarefa integer;
UPDATE ctx SET tarefa = (SELECT max(id) FROM rotulo.tarefa);

SELECT pg_temp.confere((SELECT data_referencia = '2020-01-01' FROM rotulo.tarefa WHERE id = (SELECT tarefa FROM ctx)),
                       'data da tarefa vem da imagem (ignora a digitada)');
SELECT pg_temp.espera_erro($$INSERT INTO rotulo.tarefa (campanha_id, imagem_id, data_referencia, geom)
    SELECT campanha, imagem, now(), ST_MakeEnvelope(726350, 7462350, 726450, 7462450, 32723) FROM ctx$$,
    'sobrepõe a tarefa', 'tarefas sobrepostas na mesma imagem');
SELECT pg_temp.espera_erro($$INSERT INTO rotulo.tarefa (campanha_id, imagem_id, data_referencia, geom)
    SELECT campanha, imagem, now(), ST_MakeEnvelope(700000, 7462300, 700100, 7462400, 32723) FROM ctx$$,
    'fora da extensão', 'tarefa fora da imagem');

ALTER TABLE ctx ADD COLUMN s_ana integer, ADD COLUMN s_bia integer;
UPDATE ctx SET s_ana = rotulo.fn_iniciar_sessao(tarefa, 'ana'), s_bia = rotulo.fn_iniciar_sessao(tarefa, 'bia');

-- Anotações -------------------------------------------------------------------
CREATE FUNCTION pg_temp.anotar(p_sessao integer, p_classe text, x0 float, y0 float, x1 float, y1 float) RETURNS void
LANGUAGE sql AS $$
    INSERT INTO rotulo.anotacao (sessao_id, tarefa_id, data_referencia, classe_id, geom)
    SELECT p_sessao, 0, '1900-01-01', c.id, ST_Multi(ST_MakeEnvelope(x0, y0, x1, y1, 32723))
      FROM dominio.classe c WHERE c.codigo = p_classe
$$;

SELECT pg_temp.espera_erro($$SELECT pg_temp.anotar((SELECT s_ana FROM ctx), 'vegetacao', 726300, 7462300, 726350, 7462400)$$,
    'agregadora', 'classe agregadora não é atribuível');

-- Ana: metade esquerda vegetação densa (desenhada passando da borda), direita construção + solo
SELECT pg_temp.anotar((SELECT s_ana FROM ctx), 'vegetacao_arborea', 726250, 7462250, 726350, 7462450);
SELECT pg_temp.confere((SELECT abs(area_m2 - 5000) < 0.01 FROM rotulo.anotacao WHERE sessao_id = (SELECT s_ana FROM ctx)),
                       'anotação recortada ao limite da tarefa (5000 m²)');
SELECT pg_temp.confere((SELECT bool_and(data_referencia = '2020-01-01' AND tarefa_id = (SELECT tarefa FROM ctx))
                          FROM rotulo.anotacao), 'anotação herda data e tarefa');
SELECT pg_temp.espera_erro($$SELECT pg_temp.anotar((SELECT s_ana FROM ctx), 'edificacao', 726340, 7462300, 726400, 7462350)$$,
    'sobrepõe', 'sobreposição na mesma sessão');
SELECT pg_temp.anotar((SELECT s_ana FROM ctx), 'edificacao', 726350, 7462300, 726400, 7462350);

SELECT pg_temp.espera_erro($$SELECT rotulo.fn_enviar_sessao((SELECT s_ana FROM ctx))$$, 'sem classe', 'envio com lacuna');
SELECT pg_temp.confere((SELECT abs(area_m2 - 2500) < 0.01 FROM rotulo.vw_lacuna WHERE id = (SELECT s_ana FROM ctx)), 'lacuna de 2500 m² visível');
SELECT pg_temp.anotar((SELECT s_ana FROM ctx), 'solo_exposto', 726350, 7462350, 726400, 7462400);
SELECT rotulo.fn_enviar_sessao((SELECT s_ana FROM ctx));
SELECT pg_temp.confere((SELECT enviada_em IS NOT NULL FROM rotulo.sessao WHERE id = (SELECT s_ana FROM ctx)), 'sessão enviada');

SELECT pg_temp.espera_erro($$UPDATE rotulo.anotacao SET classe_id = classe_id WHERE sessao_id = (SELECT s_ana FROM ctx)$$,
    'em_andamento', 'anotação travada após envio');

-- Bia: mesma tarefa, discorda no quadrante de solo (marca construção)
SELECT pg_temp.anotar((SELECT s_bia FROM ctx), 'vegetacao_arborea', 726300, 7462300, 726350, 7462400);
SELECT pg_temp.anotar((SELECT s_bia FROM ctx), 'edificacao',        726350, 7462300, 726400, 7462400);
SELECT rotulo.fn_enviar_sessao((SELECT s_bia FROM ctx));
SELECT pg_temp.confere((SELECT acordo_global = 0.75 FROM rotulo.vw_concordancia LIMIT 1), 'acordo global 0,75');
SELECT pg_temp.confere((SELECT iou = 0.5 FROM rotulo.vw_concordancia WHERE classe = 'edificacao'), 'IoU de construção 0,5');
SELECT pg_temp.confere((SELECT iou = 1 FROM rotulo.vw_concordancia WHERE classe = 'vegetacao_arborea'), 'IoU de vegetação densa 1,0');

-- Revisão -----------------------------------------------------------------------
SELECT pg_temp.espera_erro($$UPDATE rotulo.sessao SET status_codigo = 'aprovada' WHERE id = (SELECT s_ana FROM ctx)$$,
    'revisor_id', 'aprovação sem revisor');
SELECT pg_temp.espera_erro($$SELECT rotulo.fn_revisar_sessao((SELECT s_ana FROM ctx), 'ana', true)$$,
    'ck_sessao_revisor_diferente', 'autoaprovação');
SELECT rotulo.fn_revisar_sessao((SELECT s_ana FROM ctx), 'rev', true, 'ok');
SELECT pg_temp.espera_erro($$SELECT rotulo.fn_revisar_sessao((SELECT s_bia FROM ctx), 'rev', true)$$,
    'uq_sessao_aprovada_por_tarefa', 'segunda aprovação na mesma tarefa');
SELECT rotulo.fn_revisar_sessao((SELECT s_bia FROM ctx), 'rev', false, 'quadrante SE é solo');
SELECT pg_temp.confere((SELECT situacao = 'aprovada' AND sessao_referencia_id = (SELECT s_ana FROM ctx)
                          FROM rotulo.vw_tarefa WHERE id = (SELECT tarefa FROM ctx)), 'tarefa aprovada com referência da Ana');
SELECT pg_temp.espera_erro($$UPDATE rotulo.sessao SET status_codigo = 'enviada' WHERE id = (SELECT s_bia FROM ctx)$$,
    'Transição', 'transição rejeitada → enviada');
SELECT pg_temp.espera_erro($$UPDATE rotulo.tarefa SET geom = ST_MakeEnvelope(726300, 7462300, 726410, 7462400, 32723) WHERE id = (SELECT tarefa FROM ctx)$$,
    'não mudam', 'recorte travado com sessões');

-- Dataset -----------------------------------------------------------------------
SELECT pg_temp.confere((SELECT papel <> 'fora_de_bloco' FROM treino.vw_tarefa_conjunto WHERE tarefa_id = (SELECT tarefa FROM ctx)),
                       'tarefa dentro de bloco útil');
INSERT INTO treino.dataset (codigo, versao, campanha_id, divisao_id)
SELECT 'teste', 1, campanha, (SELECT id FROM treino.divisao WHERE codigo = 'blocos_600m_s42') FROM ctx;
SELECT pg_temp.confere(treino.fn_congelar_dataset((SELECT id FROM treino.dataset WHERE codigo = 'teste')) = 1, 'dataset congelado com 1 amostra');
SELECT pg_temp.confere((SELECT count(*) = 3 AND sum(ST_Area(geom)) = 10000 FROM treino.vw_mascara_poligono), '3 polígonos cobrindo a tarefa');
SELECT pg_temp.confere((SELECT col_ini = 18 AND lin_ini = 83 AND col_fim = 41 AND lin_fim = 107 FROM treino.vw_mascara_janela),
                       'janela da tarefa na grade (col 18-41, lin 83-107)');
SELECT pg_temp.confere((SELECT sum(pct_no_conjunto) = 100 FROM treino.vw_balanco_classe), 'balanço de classes soma 100%');
SELECT pg_temp.espera_erro($$SELECT rotulo.fn_reabrir_sessao((SELECT s_ana FROM ctx))$$, 'dataset congelado', 'reabrir referência congelada');
SELECT pg_temp.espera_erro($$DELETE FROM treino.dataset_amostra$$, 'congelado', 'remover amostra congelada');
SELECT pg_temp.espera_erro($$UPDATE treino.dataset SET congelado_em = NULL$$, 'congelado', 'descongelar dataset');
UPDATE treino.dataset_amostra SET caminho_mascara = 'runs/x/mask.tif', gerada_em = now();
SELECT pg_temp.confere(true, 'registrar máscara gerada em dataset congelado');

-- Auditoria e operações auxiliares ------------------------------------------------
SELECT pg_temp.confere((SELECT count(*) > 0 FROM auditoria.registro WHERE tabela = 'rotulo.anotacao'), 'auditoria registrou anotações');
SELECT pg_temp.confere(treino.fn_criar_tarefas_por_bloco((SELECT campanha FROM ctx),
                           (SELECT id FROM catalogo.imagem WHERE arquivo = 'global_monthly_2020_02_mosaic.tif'),
                           (SELECT id FROM treino.divisao WHERE codigo = 'blocos_600m_s42'), ARRAY['teste']) > 0,
                       'tarefas criadas a partir dos blocos de teste');

ROLLBACK;
\echo 'TODOS OS TESTES PASSARAM (alterações desfeitas)'
