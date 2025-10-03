#python
#orm_gui_manager.py
#19:29 29/08/2025
import os
import sqlite3
import pandas as pd
import webview
import uuid

def view_log_html(_database_name, _table='false', _html_path='false', filter='false'):
	_r = 'false'
	_uuid = str(uuid.uuid4()).replace('-','_')
	_cwd = os.getcwd()
	_db = f'{_cwd}/database_xaiorm/db/{_database_name}'
	__log = f'{_cwd}/database_xaiorm/html_log/log/{_uuid}'
	_conn = sqlite3.connect(_db)
	if(filter == 'false' and _r == 'false'):
		df = pd.read_sql_query(f"SELECT * FROM {_table}", _conn)
	else:
		df = pd.read_sql_query(f"SELECT * FROM {_table} WHERE {filter}", _conn)
	if(_html_path == 'false'):
		df.style.background_gradient(cmap='Blues')
	else:
		r(_html_path)
	with open(__log,'w') as _x:
		df.to_html(buf=_x)
	_wx = f'XAIORM DB: {_table}:{__log}'
	webview.create_window(_wx,__log)
	webview.start()

def view_def_log_html(_database_name, _data, _html_path='false'):
	_r = 'false'
	_uuid = str(uuid4()).replace('-','_')
	_cwd = os.getcwd()
	_db = f'{_cwd}/database_xaiorm/db/{_database_name}'
	__log = f'{_cwd}/database_xaiorm/html_log/log/{_uuid}'
	_conn = sqlite3.connect(_db)
	df = _data
	if(_html_path == 'false'):
		df.style.background_gradient(cmap='Blues')
	else:
		df = pd.read_html(_html_path)
	with open(__log,'w') as _x:
		df.to_html(buf=_x)
	_wx = f'XAIORM DB:{__log}'
	webview.create_window(_wx,__log)
	webview.start()
