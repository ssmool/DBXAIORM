#python
#orm_analitics.py
#19:28 29/08/2025
import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def view_table(db_name,table,_filter,axis_x_name,axis_y_name,_type='bar'):
	cwd = os.getcwd()
	_conn = f'{cwd}/database_xaiorm/db/{db_name}'
	print(_conn)
	conn = sqlite3.connect(_conn)
	cursor = conn.cursor()
	_r_cmd = f"select * from {table} where {_filter}"
	_r = pd.read_sql_query(_r_cmd, conn)
	_r[axis_x_name].value_counts().plot(kind=_type)
	_r[axis_y_name].value_counts().plot(kind=_type)
	_tl = str(f'Database X-AI ORM - {table}')
	plt.title(_tl)
	plt.xlabel(axis_x_name)
	plt.ylabel(axis_y_name)
	plt.show()
	conn.close()

def view_table_with_query(db_name,_cmd,axis_x_name,axis_y_name):
	_r_cmd = f"{_cmd}"
	print(f'={_r_cmd}')
	cwd = os.getcwd()
	_conn = (f'{cwd}/database_xaiorm/db/{db_name}')
	conn = sqlite3.connect(_conn)
	cursor = conn.cursor()
	_r = pd.read_sql_query(_r_cmd, conn)
	print(_r)
	conn.close()
