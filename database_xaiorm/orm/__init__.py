#python
#orm_gui_manager.py
#19:30 29/08/2025

import os
import sqlite3
from datetime import datetime

py_orm_conn = None
cwd = 	'false'
py_model = 'false'

def getpath():
	global cwd
	global py_model
	cwd = os.getcwd()
	print(cwd)

def createmodel(_table,_model):
	getpath()
	#stream_model = temp_file.split(';')
	_py_model = f'{cwd}/database_xaiorm/dict/{_table}.pyiaorm'
	with open(_py_model,'w') as temp_file:
		_rx_model = _model
		content = temp_file.write(_rx_model)
	return _py_model

def dbcreate(db_name):
	getpath()
	_cwd = f"{cwd}/database_xaiorm/db/{db_name}.sqlite3"
	print(_cwd)
	conn = sqlite3.connect(_cwd)
	conn.close()

def dbopen(db_name):
	getpath()
	global py_orm_conn
	_cwd = f"{cwd}/database_xaiorm/db/{db_name}"
	py_orm_conn = sqlite3.connect(_cwd)
	print(f'={_cwd}')
	return py_orm_conn

def dbclose():
	py_orm_conn.close()

def select(table,filter='None'):
	py_cmd = 'select '
	if(filter != None):
		py_cmd += f'* from {table} where {filter}'
	else:
		py_cmd += f'* from {table}'
	print(py_cmd)
	print(py_orm_conn)
	py_cursor = py_orm_conn.cursor()
	py_cursor.execute(py_cmd)
	py_fetchall = py_cursor.fetchall()
	return py_fetchall

def insert(table,values):
	py_cmd = 'insert '
	if(values != None):
	    py_val = values.split(',')
	    py_cmd = ''
	    py_cmd_val_0x0 = ''
	    py_cmd_val_0x1 = ''
	    for py in py_val:
	        py_q = py.split('=')
	        py_cmd_val_0x0 += f"{py_q[0]},"
	        py_cmd_val_0x1 += f"{py_q[1]},"
	    py_cmd_r = py_cmd_val_0x0.rindex(',')
	    py_cmd_val_0x0 = py_cmd_val_0x0[0:(py_cmd_r)]
	    py_cmd_r = py_cmd_val_0x1.rindex(',')
	    py_cmd_val_0x1 = py_cmd_val_0x1[0:(py_cmd_r)]
	    py_cmd += f'insert into {table} ({py_cmd_val_0x0}) values ({py_cmd_val_0x1})'
	print(str(py_cmd))
	py_orm_conn.execute(py_cmd)
	py_orm_conn.commit()
	return True

def update(table,values,filter):
	py_cmd = f"update {table} set "
	if(values != None and filter != None):
		py_cmd += f"{str(values)}"
		#fx = (py_cmd.rfind(',')-1)
		#py_cmd = py_cmd[0:fx]
		py_cmd += f' where {str(filter)}'
	print(py_cmd)
	py_orm_conn.execute(py_cmd)
	py_orm_conn.commit()
	return True

def delete(table, filter):
	py_cmd = f'delete from {table} where {filter}'
    #py_cursor = py_orm_conn.cursor()
	#py_cursor.execute(py_cmd)
	py_orm_conn.execute(py_cmd)
	py_orm_conn.commit()
	py_orm_conn.commit()
	return True

def table(table, model, action='None'):
	status = 'None'
	match action.lower():
		case 'create':
			status = createtable(table,model)
		case 'alter':
			status = updatetable(table,model_name)
		case 'drop':
			status = droptable(table,model)

def createtable(_table='false', _model='false'):
	getpath()
	if(_table == 'false'):
	    _table = _model.replace('.pyiaorm','')
	py_cmd = f'create table if not exists {_table} ('
	py_cmd += 'ID INTEGER PRIMARY KEY,'
	_py_model = f'{cwd}/database_xaiorm/dict/{_model}.pyiaorm'
	with open(_py_model,'r') as temp_file:
		content = temp_file.read()
	stream_model = content.split(',')
	for stream in stream_model:
		py_cmd += f'{stream}, '
	_fx = (py_cmd.rindex(','))
	_py_cmd = py_cmd[0:_fx]
	_py_cmd += ');'
	print(_py_cmd)
    #py_cursor = py_orm_conn.cursor()
	#py_cursor.execute(py_cmd)
	print(_py_cmd)
	py_orm_conn.execute(_py_cmd)
	py_orm_conn.commit()
	writelog(f'CREATE TABLE BY MODEL {_model}', 'CREATE TABLE', f'Model:{_py_model};Backup Model:{_py_cmd}')
	return True

def renametable(table, model_name):
	py_cmd = f'alter table {table} RENAME TO {model_name}'
	py_orm_conn.executescript(py_cmd)
	py_orm_conn.commit()

def alterable(table, model):
	py_cmd = f'alter table {table} ADD COLUMN '
	cwd = os.getcwd()
	py_model = f'{cwd}/database_xaiorm/dict/{model}.pyiaorm'
	with open(py_model,'r') as temp_file:
		content = temp_file.read()
	stream_model = temp_file.split(';')
	for stream in stream_model:
		field = stream.split(' ');
		for property in field:
			py_cmd += '{property}'
		py_cmd += ','
	py_cmd = py_cmd[0:fx]
	py_cmd += ');'
	py_orm_conn.executescript(py_cmd)
	py_orm_conn.commit()
	writelog(f'ALTER TABLE BY MODEL {model}', 'ALTER TABLE', f'Model:{py_model}\nBackup Model:{py_model_bkp}')
	return status

def droptable(table):
	py_cmd = f'drop table if exists {table};'
	py_orm_conn.executescript(py_cmd)
	py_orm_conn.commit()
	writelog(f'DROP TABLE: {table}', 'DROP TABLE', '{table} DROPPED')
	return status

def writelog(msg, action, details):
	cwd = os.getcwd()
	dt_log = str(datetime.now())
	py_log = f'{cwd}/database_xaiorm/log/{action}_{dt_log}.log'
	print(py_log)
	with open(py_log,'a') as file:
		file.write(f'UPDATED:{dt_log}\\n\\nACTION:{action}\\n\\nDETAILS:{details}\\n\\nMESSAGE:{msg}')
