#python
#orm_gui_manager.py
#19:30 29/08/2025

import os
import sqlite3
import web_diver as _webdiver
import database_xaiorm.orm as ORM
from datetime import datetime

py_orm_conn = None
ENDPOINT = "https://api.bing.microsoft.com/v7.0/search"

def create_prompt(_db_name, _table, _fields='auto', _APY_KEY_BING='_false'):
    if _fields == 'auto':
        inferred_fields = infer_fields_from_web(f'sql model {_table} table schema', _APY_KEY_BING, ENDPOINT)
    else:
        __fields = _fields.split(',')
        __model = []
        for ___fields in __fields:
            _sx = f'{___fields} TEXT NOT NULL'
            __model.append(_sx)
        inferred_fields = __model if isinstance(__model, list) else [__model]
    _flag_fields = ',\n  '.join(inferred_fields)
    _r = f"CREATE TABLE {_table} (\n  {_flag_fields}\n);"
    ORM.createmodel(_table,_flag_fields)
    return _r

def infer_fields_from_web(query, api_key, endpoint):
    headers = {
        "Ocp-Apim-Subscription-Key": api_key
    }
    params = {
        "q": query,
        "count": 5,
        "textDecorations": True,
        "textFormat": "HTML"
    }
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()
    results = response.json()
    _r = []
    for item in results.get("webPages", {}).get("value", []):
        _r.append({
            "title": item["name"],
            "snippet": item["snippet"],
            "url": item["url"]
        })
    return _r

def py_write_log(msg, action, details):
	cwd = os.getcwd()
	dt_log = str(datetime.now())
	py_log = f'{cwd}/database_xaiorm/log/{action}_{dt_log}.log'
	with file_path.open('a') as file:
		file.write(f'UPDATED:{dt_log}\n\nACTION:{action}\n\nDETAILS:{details}\n\n\MESSAGE:{msg}')
