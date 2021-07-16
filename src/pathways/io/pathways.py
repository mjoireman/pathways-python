from .static_layer import StaticLayerItem
from .cache_manager import CacheManager
from .pathways_frame import PathwaysDatasetInfo, PathwaysDatasetTypes, PathwaysFrame
import geopandas as gpd
from geopandas.geodataframe import GeoDataFrame
from ..auth import get_default_credentials
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import re


def read_dataset(id: str) -> PathwaysFrame:
    # get info of dataset
    info = dataset_info(id)
    file_name = process_layer_name(info.name)
    # get exports
    url = export_links(id)

    file_path = CacheManager.cache_file(url)
    layer_df = gpd.read_parquet(file_path)
    layer_df.sindex

    p_info = PathwaysDatasetInfo()
    p_info.dataset_type = PathwaysDatasetTypes.static
    p_info.dataset_info = info
    
    pf = PathwaysFrame(layer_df)
    pf.set_pathways_info(p_info)
    return pf

def dataset_info(id: str) -> StaticLayerItem:
    credentials = get_default_credentials()
    token = credentials.get_token()
    url = f'{credentials.base_url}/api/staticlayer/{id}'
    headers = {"Authorization": f"Bearer {token}"}
    info_dict = requests.get(url, headers=headers).json()['result'][0]
    info = StaticLayerItem.from_json(info_dict)
    return info


def process_layer_name(name):
    name = name.replace(',', '')
    name = name.replace(' ', '_')
    name = re.sub(r'\W+', '', name)
    return name

def export_links(id: str)  -> str:
    credentials = get_default_credentials()
    token = credentials.get_token()
    url = f'{credentials.base_url}/api/staticlayer/{id}/export/parquet'
    headers = {"Authorization": f"Bearer {token}"}
    url = requests.get(url, headers=headers).json()['result']
    return url