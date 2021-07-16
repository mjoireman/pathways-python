from typing import Optional
from pathways_client.auth import get_default_credentials
import pandas as pd
from pandas.core.frame import DataFrame
import requests

def search(q: Optional[str] = '') -> DataFrame:
    credentials = get_default_credentials()
    token = credentials.get_token()
    url = f'{credentials.base_url}/api/staticlayer/?q={q}&pageNo=1&pageSize=10000'
    headers = {"Authorization": f"Bearer {token}"}
    items = requests.get(url, headers=headers).json()['result']['data']
    #print(items[0])
    result = []
    for item in items:
        result.append({'Id': item['id'], 'Name': item['name'], 'DisplayName': item['mapServiceLayers']['displayName'], 'GeometryType': item['mapServiceLayers']['geometryType']})
    return pd.DataFrame(result)


