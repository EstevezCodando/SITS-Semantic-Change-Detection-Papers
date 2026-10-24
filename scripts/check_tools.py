"""Verifica repositorios GitHub (existencia, licenca, ultimo push, arquivado) e pacotes PyPI/CRAN. Saida: dados/tools.json"""
import json, sys, urllib.request, urllib.error, concurrent.futures as cf
sys.stdout.reconfigure(encoding='utf-8')
UA = {'User-Agent': 'research-collection-script', 'Accept': 'application/vnd.github+json'}
REPOS = {
    'TorchGeo': 'torchgeo/torchgeo', 'Open-CD': 'likyoo/open-cd', 'PyTorch Change Models / AnyChange': 'Z-Zheng/pytorch-change-models',
    'SpaceNet 7 solutions': 'SpaceNetChallenge/SpaceNet7_Multi-Temporal_Solutions', 'TSSCD': 'CUG-BEODL/TSSCD',
    'U-TAE / PaPs': 'VSainteuf/utae-paps', 'ChangeFormer': 'wgcban/ChangeFormer', 'ChangeMamba (MambaCD)': 'ChenHongruixuan/MambaCD',
    'MapFormer': 'mxbh/mapformer', 'CCDC': 'GERSL/CCDC', 'FC-Siam (Daudt)': 'rcdaudt/fully_convolutional_change_detection',
    'STANet': 'justchenhao/STANet', 'PerASCD': 'SathShen/PerASCD', 'Seg2Change': 'yogurts-sy/Seg2Change',
    'SAMPolyBuild': 'wchh-2000/SAMPolyBuild', 'DINO Soars': 'rfaulk/DINO_Soars',
    'GeoAI (geoai-py + plugin QGIS)': 'opengeos/geoai', 'segment-geospatial (samgeo)': 'opengeos/segment-geospatial',
    'geemap': 'gee-community/geemap', 'Deepness (plugin QGIS)': 'PUTvision/qgis-plugin-deepness',
    'IAMAP (plugin QGIS)': 'umr-amap/iamap', 'Geo-SAM (plugin QGIS)': 'coolzhao/Geo-SAM',
    'Semi-Automatic Classification Plugin': 'semiautomaticgit/SemiAutomaticClassificationPlugin',
    'MOLUSCE (plugin QGIS)': 'nextgis/qgis_molusce', 'sits (R)': 'e-sensing/sits', 'gdalcubes': 'appelmar/gdalcubes',
    'openEO Python client': 'Open-EO/openeo-python-client', 'XGBoost': 'dmlc/xgboost', 'LightGBM': 'microsoft/LightGBM',
    'Ultralytics (YOLO)': 'ultralytics/ultralytics', 'Segment Anything (SAM)': 'facebookresearch/segment-anything',
    'SAM 3': 'facebookresearch/sam3', 'Grounded-SAM': 'IDEA-Research/Grounded-Segment-Anything', 'DINOv3': 'facebookresearch/dinov3',
    'Prithvi-EO-2.0': 'NASA-IMPACT/Prithvi-EO-2.0', 'Scale-MAE': 'bair-climate-initiative/scale-mae', 'DOFA': 'zhu-xlab/DOFA',
    'STAC spec': 'radiantearth/stac-spec', 'RoadTracer': 'mitroadmaps/roadtracer',
}
PYPI = ['torchgeo', 'geoai-py', 'segment-geospatial', 'geemap', 'xgboost', 'lightgbm', 'ultralytics', 'openeo', 'pystac', 'rasterio', 'optuna', 'shap', 'open-cd', 'leafmap']


def gh(item):
    name, repo = item
    try:
        with urllib.request.urlopen(urllib.request.Request('https://api.github.com/repos/' + repo, headers=UA), timeout=30) as r:
            d = json.load(r)
        return name, {'repo': repo, 'ok': True, 'stars': d['stargazers_count'], 'license': (d.get('license') or {}).get('spdx_id'),
                      'pushed': d['pushed_at'][:10], 'archived': d['archived'], 'desc': d.get('description')}
    except urllib.error.HTTPError as e:
        return name, {'repo': repo, 'ok': False, 'status': e.code}
    except Exception as e:
        return name, {'repo': repo, 'ok': False, 'status': type(e).__name__}


def pypi(p):
    try:
        with urllib.request.urlopen(urllib.request.Request(f'https://pypi.org/pypi/{p}/json', headers=UA), timeout=30) as r:
            d = json.load(r)
        i = d['info']
        return p, {'ok': True, 'version': i['version'], 'license': i.get('license') or '', 'requires_python': i.get('requires_python')}
    except Exception as e:
        return p, {'ok': False, 'status': str(e)[:40]}


with cf.ThreadPoolExecutor(6) as ex:
    repos = dict(ex.map(gh, REPOS.items()))
    pk = dict(ex.map(pypi, PYPI))
json.dump({'repos': repos, 'pypi': pk, 'data': '2026-10-24'}, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for n, v in repos.items(): print(n, v.get('ok'), v.get('stars'), v.get('pushed'), v.get('archived'), v.get('status', ''))
for n, v in pk.items(): print('pypi', n, v)

