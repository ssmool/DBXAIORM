#python
#orm_gui_manager.py
#19:30 29/08/2025

import csv, sqlite3
import pandas as pd
import uuid
import pyodbc
import mysql.connector
import psycopg2

_odbc = 'false'
_conn_connect = 'false'
_rdms = 'false'

def view_table_csv_uri(uri):
	_r = 'true'
	df = pd.read_csv(uri)
	print(df.head())
	return _r

def view_table_csv_path(_path):
	_r = 'true'
	df = pd.read_csv(_path)
	print(df.head())
	return _r

def save_table_csv_path(_path,table):
	_path_uuid = str(uuid.uuid4()).replace('-','_')
	_path_uuid_log_x = f"{_path}_{table}_{_path_uuid}.csv"	
	df = pd.read_csv(_path)
	print(df.head())
	df.to_csv(_path_uuid_log_x)
	return _path_uuid_log_x

def save_table_csv_uri(uri,table_csv_name):
	_path_uuid = uuid.uuid4()
	_path_uuid_log_x = f"{_path}_{table}_{_path_uuid}.csv"
	df = pd.read_csv(uri)
	df.to_csv(_path_uuid_log_x)
	return _path_uuid_log_x

def save_table_csv_to_database(database_name,_path,table_name,command='false',type='path'):
	_r = 'true'
	df = ''
	_command_x = command.split(',')
	_command_fl = ''
	_path_uuid = str(uuid.uuid4()).replace('-','_')
	_path_uuid_log_x = f"{_path}_{table_name}_{_path_uuid}.csv"	
	if(type=='path'):
		df = pd.read_csv(_path)
		df.to_csv(_path_uuid_log_x)
	if(command != 'false' and command.equals(',') and command.equals("'")):
		with open(_path_csv_log_temp_x,'r', encoding='utf-8') as fin: # `with` statement available in 2.5+
			dr_aux = csv.DictReader(fin) # comma is default delimiter
			for _command_dx_x in _command_x:
				to_db_aux.append(_command_dx_x)
		con = sqlite3.connect(database_name)
		cur = con.cursor()
		for index in to_db_aux:
			for cmd_x in _command_x:
				_command_x_fl = _command_x_x + ','
				_command_x_fl_rx = '?,'
			cmd = "INSERT INTO {table_name} ({str(_command_x_fl)}) VALUES ({str(_command_x_fl_rx)})"
			print(cmd)
			_cmd_index = ''
			for _index in index:
				_cmd_index += _index + ','
			con.execute(cmd,_cmd_index)
			con.commit()
			print('------------- UPDATED -------------')
		con.close()
		_r = 'true'
	else:
		df = pd.read_csv(_path)
		__conn = sqlite3.connect(database_name)
		df.to_sql(table_name, __conn, if_exists='replace', index=False)
		_r = 'true'
	return 	_r
	
#python
#orm_gui_manager.py
#19:30 29/08/2025
#pip install pyodbc

def orm_import_odbc(database,_conn_odbc):
	_odbc =  pyodbc.connect(_conn_obdc)
	_conn_connect = _conn_sqlite.cursor()
	_conn_connect.execute(_odbc_command)
	_conn_stream_x = _conn_connect.fetchall()
	_conn_connect_sqlite = ''
	_conn_cmd = []
	_conn_info_er_field = []
	for __conn_er_model_field_x in _conn_stream_x.tables():
		_conn_er_model_info_x = _conn_err_model.table_name
		_conn_stream_x = _conn_er_model_info_x(table=_conn_er_model_info_x)
		print(str(_conn_stream_x))
		for _conn_err_model_info_field_x_0x in _conn_stream_x:
			_conn_info_er_field.append(_conn_err_model_info_field_x_0x.column_name)
			_conn_info_er_field.append('?,')
		for _conn_err_model_info_field_upx0 in _conn_info_er_field:
			__conn_attr_x0_x01 = len(_conn_info_er_field)
			_conn_attr_x0 = _conn_info_er_field[__conn_attr_x0_x01 - 1]
			_conn_attr_x0x1 = _conn_info_er_field[__conn_attr_x0_x01]
			_conn_cmd_x = f"CREATE TABLE {_conn_attr_x0} ({_conn_attr_x0x1})"
			_conn_cmd.append(_conn_cmd_x)
			_conn_connect_sqlite.sqlite.execute(_conn_cmd)
			_conn_connect_sqlite.commit()
			for _conn_er_model in _conn_stream_x:
				_cmd_x = f"INSERT INTO {str(_conn_er_model_info_x)} VALUES ({str(_conn_attr_x0x1)})"
				_conn_cmd_temp = (_cmd_x, _conn_er_model)
				_conn_connect_sqlite.commit()
	_conn_connect.close()
	_odbc.close()
	_conn_connect_sqlite.close()
	return true

def orm_viewer_odbc(_conn_odbc):
	_odbc =  pyodbc.connect(_conn_obdc)
	_conn_connect = _conn_sqlite.cursor()
	_conn_connect.execute(_odbc_command)
	_conn_stream_x = _conn_connect.fetchall()
	_conn_connect_sqlite = ''
	_conn_info_er_field = []
	_conn_cmd = {"ER_MODEL:","FALSE","ER_FIELD:",_conn_info_er_field}
	_conn_cmd_x = []
	for __conn_er_model_field_x in _conn_stream_x.tables():
		_conn_er_cpx = _conn_cmd.copy()
		_conn_er_model_info_x = __conn_er_model_field_x.table_name
		_conn_er_cpx["ER_MODEL"] = _conn_er_model_info_x
		_conn_stream_x_0x = _conn_stream_x(table=_conn_er_model_info_x)
		for _conn_err_model_info_field_x in _conn_stream_x_0x:
			_conn_info_er_field.append(_conn_er_model_info_field_x.column_name)
		_conn_er_cpx["ER_FIELD"] = _conn_er_model_info_field
		_conn_cmd_x.append(_conn_er_cpx)
	return _conn_cmd_x

def orm_viewer_odbc_conn_close():
	_conn_connect.close()
	_odbc.close()

def orm_import_odbc_connector(_conn_odbc):
	_odbc =  pyodbc.connect(_conn_obdc)
	_conn_connect = _odbc.cursor()
	return _conn_connect
	
#python
#orm_gui_manager.py
#19:31 29/08/2025

def orm_import_mysql(database,_conn_rdms_host,_conn_rdms_user,_conn_rdms_password,_conn_rdms_database, _conn_rdms_port):
	_rdms =  mysqlconnector.connector.connect(host={_conn_rdms_host},user={_conn_rdms_user},password={_conn_rdms_password},database={_conn_rdms_database})
	_conn_connect = _rdms.cursor()
	_conn_stream_x = _conn_connect.fetchall()
	_conn_connect_info = _con_connect.description
	conn_connect_sqlite = ''
	_conn_cmd = []
	for _in_x,_conn_er_model_field_x in enumerate(conn_connect_info):
		_conn_er_model_info_x_name = _conn_err_model_field_x[4]
		for _conn_err_model_info_field_x in _conn_stream_x(table=_conn_er_model_info_x):
			_conn_info_er_field.append(_conn_er_model_info_field_x[0])
			_conn_info_er_field_val.append('?,')
		_conn_connect_sqlite.sqlite.execute('CREATE TABLE {_conn_er_model_info_x_name} (str({_conn_info_er_model_field_x}))')
		_conn_connect_sqlite.commit()
		_conn_stream_x_0x = _conn_connect_sqlite.execute('SELECT * FROM {_conn_er_model_info_x_name}')
		_conn_stream_x_0x = _conn_connect.fetchall()
		__conn_attr_x0_x01 = len(_conn_info_er_field)
		_conn_attr_x0 = _conn_info_er_field[__conn_attr_x0_x01 - 1]
		_conn_attr_x0x1 = _conn_info_er_field[__conn_attr_x0_x01]
		for _conn_er_model in _conn_stream_x_0x:
			_conn_cmd_temp = f"INSERT INTO {_conn_info_er_model_info_x_name} VALUES ({str(_conn_stream_x_0x1)})"
			_conn_connect_sqlite.execute(_conn_cmd_temp, _conn_er_model)
			_conn_connect_sqlite.commit()
	_conn_connect.close()
	_odbc.close()
	_conn_connect_sqlite.close()
	return true

def orm_import_mysql_connector(_conn_rdms_host,_conn_rdms_user,_conn_rdms_password,_conn_rdms_database):
	_rdms =  mysqlconnector.connector.connect(host={_conn_rdms_host},user={_conn_rdms_user},password={_conn_rdms_password},database={_conn_rdms_database})
	_conn_connect = _rdms.cursor()
	return _conn_connect

def orm_import_postgre(_conn_rdms_host,_conn_rdms_user,_conn_rdms_password,_conn_rdms_database):
	_rdms =  psycopg2(dbname={_conn_rdms_database},user={_conn_rdms_user},password={_conn_rdms_password},host={_conn_rdms_host},port={_conn_rdms_port})
	_conn_connect.autocomiit = True
    #_conn_connect.cursor()
	with _conn_connect() as cursor:
		_command = "SELECT table_name, column_name FROM information_schema.columns WHERE table_schema = 'public' ORDER BY table_name, ordinal_position;"
		cursor.execute(_command)
		_fields = cursor.fetchall()
		if _fields:
			for _in_x,_conn_er_model_field_x in _fields:
				_conn_er_model_info_x_name = _in_x
				_conn_info_er_field.append(_conn_er_model_info_field_x)
				_conn_info_er_field_val.append('?')
		_cmd_x = f'CREATE TABLE {_conn_er_model_info_x_name} (str({_conn_info_er_model_field_x}))'
		_conn_connect_sqlite.sqlite.execute(_cmd_x)
		_conn_connect_sqlite.commit()
		_cmd_x0 = f'SELECT * FROM {_conn_er_model_info_x_name}'
		_conn_stream_x_0x = _conn_connect_sqlite.execute(_cmd_x0)
		for conn_er_model in _conn_stream_x_0x:
			_conn_cmd_temp = f"INSERT INTO {_conn_info_er_model_info_x_name} VALUES ({str(_conn_info_er_field_val)})"
			_conn_connect_sqlite.execute(_conn_cmd_temp, _conn_er_model)
			_conn_connect_sqlite.commit()
	_conn_connect.close()
	return true

def orm_import_postgre_connector(_conn_rdms_host,_conn_rdms_user,_conn_rdms_password,_conn_rdms_database,_conn_rdms_port):
	_rdms =  psycopg2(dbname={_conn_rdms_database},user={_conn_rdms_user},password={_conn_rdms_password},host={_conn_rdms_host},port={_conn_rdms_port})
	_conn_connect.autocomiit = True
	return _conn_connect

#def orm_import_sqlserver(_conn_rdms_host,_conn_rdms_user,_conn_rdms_password,_conn_rdms_database):
#	return 'false'

#def orm_import_postgre_connector(_conn_rdms_host,_conn_rdms_user,_conn_rdms_password,_conn_rdms_database,_conn_rdms_port):
#	return 'false'
