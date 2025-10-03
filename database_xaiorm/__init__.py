from database_xaiorm.orm import *
from database_xaiorm.orm_ai import *
from database_xaiorm.orm_migrate import *
from database_xaiorm.html_log import *
from database_xaiorm.criptografy import *
from database_xaiorm.blob import *
from database_xaiorm.analitics import *
import os

def _startdb(database):
	dbcreate(database)
	dict_src = os.getcwd()
	dict_src += '\dict'
	stream_list = []
	print(dict_src)
	for tempx in os.listdir(dict_src):
		print(tempx)
		_cwd = os.path.isfile(os.path.join(dict_src, tempx))
		_dict = _cwd
		print(_dict)
		if(tempx != ''):
			print(tempx)
			dbopen(database)
			#for stream in stream_list:
			table = tempx.lower()
			createtable(table, tempx)
	dbclose()

def dbop(_dbname):
    print('1')
    ORM.dbcreate(_dbname)                     # Create new database
    ORM.dbopen(_dbname)                       # Open database
    ORM.table("users", "users", action="create")  # Create table with model
    ORM.insert;("users", "name='sa', email='sa@sa.com'")                 # Insert with filter
    r = ORM.select("users", "email=sa@sa.com")                 # Select with filter
    for _r in r:
        print('=' + r)
    ORM.update("users", "name='sa12'", "email=sa@sa.com")     # Update values with filter
    ORM.delete("users", "email=sa123@sa.com")                     # Delete with filter
    ORM.write_log("User added", "INSERT", "users")  # Log an action
    ORM.dbclose()                                  # Close database

#_startdb('db_0x01.sqlite3')
print('0')
dbop('db_0x01.sqlite3')
print('2')

