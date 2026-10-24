-- Conferência rápida do banco da máscara (rodar depois de mascara_cobertura.sql).
SELECT fonte, count(*) AS imagens, min(mes_ref) AS de, max(mes_ref) AS ate
  FROM mascara.imagem GROUP BY fonte ORDER BY 1;
SELECT tipo, count(*) AS classes FROM mascara.classe GROUP BY tipo ORDER BY 1;
SELECT table_name, table_type FROM information_schema.tables
 WHERE table_schema = 'mascara' ORDER BY table_type, table_name;
SELECT postgis_lib_version() AS postgis;
