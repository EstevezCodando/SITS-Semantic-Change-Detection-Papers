# Conceitos mantidos na base: os do projeto. Conceitos de manual (F1, IoU, CNN, Transformer etc.) e dados que so aparecem como pano de fundo foram removidos.
KEEP_CONCEPTS = {
 # dados
 'PlanetNICFI', 'PlanetProdutos', 'PlanetScope', 'Sentinel1', 'Sentinel2', 'SpaceNet7_MUDS', 'DynamicEarthNet', 'HRSCD', 'SECOND', 'GlobalForestChange', 'PRODES', 'DETER',
 # preparo e rotulos
 'Rotulagem', 'RotulagemTemporal', 'AprendizadoAtivo', 'PreAnotacaoSAM', 'MascaraNuvem', 'MosaicosCompostos', 'Corregistro', 'IndicesEspectrais',
 # tarefas e metodos
 'Deteccao_Mudanca', 'MudancaSemantica', 'SITS', 'Desmatamento', 'DegradacaoFlorestal', 'Edificacoes', 'Vias', 'Mineracao', 'ClassificacaoCobertura',
 'UNet', 'UTAE', 'RedeSiamesa', 'SAM', 'ModeloFundacional', 'SemiAutoSupervisionado', 'SupervisaoFraca', 'PosProcessamentoTemporal',
 # validacao
 'Desbalanceamento', 'DivisaoEspacialBlocos', 'Generalizacao', 'AmostragemEstratificada', 'AmostraIndependente', 'ReferenciaVisual', 'EstimativaArea', 'MetricasMudancaSemantica', 'AcuraciaGlobal',
 # monitoramento
 'Alertas', 'PersistenciaConfirmacao', 'QuaseTempoReal', 'QGIS',
}
