## HOW TO IMPORT LIBRARY MODDULES FROM DBXAIORM
---
import database_xaiorm.orm as ORM
import database_xaiorm.orm_ai as AI
import database_xaiorm.orm_migrate as MIGRATE
import database_xaiorm.html_log as HTMLOG
import database_xaiorm.criptografy as CRIPTO
import database_xaiorm.blob as BLOB
import database_xaiorm.analitics as ANALYTICS
import database_xaiorm.mock as MOCK
import os
---

### BLOB:TO CREATE BLOB DATA INTO BASE64 STRINGS FOR REGISTER FILES INTO DATABASE FIELDS
def blob():
    print('a')
    with open('/home/smoolisky-dotosky/Pictures/44283403-comic-book-speech-bubbles-a-set-of-colourful-and-retro-comic-book-design-elements-with-speech.jpg','rb') as _fx:
        _x_streax = _fx.read()
    #TO CREATE BLOB DATA INTO BASE64 HASLIST BY BUFFER DEFAULT 1024 byts
    _blox = BLOB.set_data_blob(_x_streax,_buff=1024)
    #TO CREATE BASE64 STRING WITH TEXT
    _blox_64x = BLOB.set_string_64('_blox')
    #TO DECODE BASE64 STRING TO DEFAULT TEXT
    _blox_64x0 = BLOB.get_string_64(_blox_64x)
    print(f'_blox={str(_blox)} | _blox_64={_blox_64x} | _blox_64x0={_blox_64x0}')

### MOCK:TO GENERATE DATA FOR CSV FILES WITH POPULATED VALUES
def mock():
    #TO GENERATE DATA FOR CSV FILES WITH POPULATED VALUES (captions,values,range_result) 
    _dx = MOCK.generate_mock_data("val,val_x,val_y,val_z","'v','v',0,0.0",100)
    #TO SAVE MOCK GENERATED TO CSV
    _dx_x = MOCK.save_mock_csv(_dx)
    return _dx

### AI:TO CREATE MODELS ON /dict for commit new tables by model with AI
def ai():
    #define fields by caption separeted by , comma
    prompt = 'uuid_fk, uuid_fr, product, price, units, saled'
    #define your file.db to generated, table name, and use your prompt
    AI.create_prompt('db_0x01.sqlite3','_store',prompt)
    #your model will registered on /dict models with .pyiaorm

### CRIPTO:TO CRIPTOGRAFY DATA with a automatic generated _key
def cripto():
    #automatic generated _key
    _key = CRIPTO.GenerateCriptoKey()
    print(str(_key))
    #criptografy text with generated _key
    _crip = CRIPTO.CriptographyContent('content', _key)
    print(str(_crip))
    #uncriptografy text with generated _key
    _uncrip = CRIPTO.Uncripto(_crip, _key)
    print(str(_uncrip))

### LOG:READ DATABASE TABLES with ORM and VIEW RESULTS ON WEBVIEW WITH TABLES
def log():
    #VIEW TABLE tusers from db_0x01.sqlite3 with filter where by field and WHERE SQL
    HTMLOG.view_log_html("db_0x01.sqlite3", 'tusers', 'false', filter="email LIKE '%sa.com%'")

### ANALITICS:USE PANDAS DATAFRAME AND MATPLOTLIB TO SELECT DATA FROM TABLE AND VIEW WITH GRAPHICS X,Y AND CHOICE _type="bar"
def analitics():
    #orm:open database "db_0x01.sqlite3"
    ORM.dbopen("db_0x01.sqlite3")
    #ORM SELECT into tusers with filter where SQL SINTAX
    _s = ORM.select('tusers',"name LIKE 'sa'")
    #CLOSE DataBase
    ORM.dbclose()
    #VIEW TABLE ROWS RESULTS
    for __s in _s:
        print(f'__s={__s}')
    #OPEM AMALITYCS WITH FILTER FOR TABLE tusers with axis graphs x=email and y=name
    ANALYTICS.view_table("db_0x01.sqlite3", "tusers", "email LIKE '%sa.com%'", "email", "name", _type="bar")
    #OPEM AMALITYCS WITH SQL SELECT COMMAND with axis graphs x=email and y=name
    ANALYTICS.view_table_with_query("db_0x01.sqlite3", "select * from tusers where name LIKE '%sa%'",'email','name')

### MIGRATE:TO MIGRATE DATA AND USE CONNECTORS ODBC, RDBMS and CSV - FOR SQLite, MySQL, Postgree, *Commming soon: Oracle, MS SQLServer
def migrate():
    _mock_csv = mock()
    print(f'_mock_csv={_mock_csv}')
    MIGRATE.view_table_csv_uri(_mock_csv)
    _mock_csv_0x = mock()
    MIGRATE.view_table_csv_path(_mock_csv_0x)
    _mock_csv_0x_x = _mock_csv_0x.replace('.csv','_novel.csv')
    print(f'_mock_csv={_mock_csv}')
    MIGRATE.save_table_csv_path(_mock_csv, "tusers")
    MIGRATE.save_table_csv_to_database("db_0x01.sqlite3", _mock_csv, "tusers")

###INSTALL AND MOUNT NEW DATABASE WITH MODELS WRITED ON /dict with .pyiaorm models 
def _startdb(database):
	dbcreate(database)
	dict_src = os.getcwd()
	dict_src += '/dict'
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

###ORM:BASIC COMMANDS FOR SUBTIME EFFORTS TO USE DATABASE TABLES OPERATIONS
def dbop(_dbname):
    print('1')
    ORM.dbcreate(_dbname)                     # Create new database
    ORM.dbopen(_dbname)                       # Open database
    ORM.createmodel('tusers','name TEXT NOT NULL,email TEXT NOT NULL UNIQUE,created TIMESTAMP DEFAULT CURRENT_TIMESTAMP') #Create Model With Text Command
    ORM.table("tusers", "tusers", action="create")  # Create table with model
    ORM.insert("tusers", "name='sa',email='zxxaxzaxsa@sa.com'")                 # Insert with filter
    r = ORM.select("tusers", "email='sa@sa.com'")                 # Select with filter
    for _r in r:
        print(f'={r}')
    ORM.update("tusers", "name='sa12'", "email='sa@sa.com'")     # Update values with filter
    ORM.delete("tusers", "email='xsa123@sa.com'")                     # Delete with filter
    ORM.writelog("User added", "INSERT", "tusers")  # Log an action
    ORM.dbclose()                                  # Close database

### TEST BOARD
## For TEST MODULES IF ALL RIGHT PASS
print('TEST=_startdb')
_startdb('db_0x01.sqlite3')
print('TEST=dbop')
dbop('db_0x01')
print('TEST=migrate()')
migrate()
print('TEST=analitics()')
analitics()
print('TEST=blob()')
blob()
print('TEST=cripto()')
cripto()
print('TEST=log()')
log()
print('TEST=ai()')
ai()
print('TEST=blob()')
blob()

