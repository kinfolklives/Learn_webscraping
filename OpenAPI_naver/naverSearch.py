import requests
import sqlite3
import time 
import json

url = "https://openapi.naver.com/v1/search/news.json?query=스마트"

header = {'X-Naver-client-Id':'8bAmjZT_ZjiskYby8myh','X-Naver-Client-Secret':'TDSvtj0If2'}
res = requests.get(url, headers=header)
if res.status_code == 200:
    rt_dict=json.loads(res.content)
    rt_dict.keys()
import pandas as pd 
print(pd.DataFrame(rt_dict['items']))

