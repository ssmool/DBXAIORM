import database_xaiorm.orm as ORM
import database_xaiorm.orm_ai as AI
import database_xaiorm.orm_migrate as MIGRATE
import database_xaiorm.html_log as HTMLOG
import database_xaiorm.criptografy as CRIPTO
import database_xaiorm.blob as BLOB
import database_xaiorm.analitics as ANALYTICS
import database_xaiorm.mock as MOCK
import os

def blob():
    print('a')
    with open('/home/smoolisky-dotosky/Pictures/44283403-comic-book-speech-bubbles-a-set-of-colourful-and-retro-comic-book-design-elements-with-speech.jpg','rb') as _fx:
        _x_streax = _fx.read()
    _blox = BLOB.set_data_blob(_x_streax,_buff=1024)
    _blox_64x = BLOB.set_string_64('_blox')
    _blox_64x0 = BLOB.get_string_64(_blox_64x)
    print(f'_blox={str(_blox)} | _blox_64={_blox_64x} | _blox_64x0={_blox_64x0}')
def mock():
    _dx = MOCK.generate_mock_data("val,val_x,val_y,val_z","'v','v',0,0.0",100)
    _dx_x = MOCK.save_mock_csv(_dx)
    return _dx

def ai():
    prompt = 'uuid_fk, uuid_fr, product, price, units, saled'
    AI.create_prompt('db_0x01.sqlite3','_store',prompt)

def cripto():
    _key = CRIPTO.GenerateCriptoKey()
    print(str(_key))
    _crip = CRIPTO.CriptographyContent('content', _key)
    print(str(_crip))
    _uncrip = CRIPTO.Uncripto(_crip, _key)
    print(str(_uncrip))

def log():
    HTMLOG.view_log_html("db_0x01.sqlite3", 'tusers', 'false', filter="email LIKE '%sa.com%'")

def analitics():
    ORM.dbopen("db_0x01.sqlite3")
    _s = ORM.select('tusers',"name LIKE 'sa'")
    ORM.dbclose()
    for __s in _s:
        print(f'__s={__s}')
    ANALYTICS.view_table("db_0x01.sqlite3", "tusers", "email LIKE '%sa.com%'", "email", "name", _type="bar")
    ANALYTICS.view_table_with_query("db_0x01.sqlite3", "select * from tusers where name LIKE '%sa%'",'email','name')

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

#_startdb('db_0x01.sqlite3')
print('0')
#dbop('db_0x01')
print('2')
#migrate()
print('3')
#analitics()
print('4')
#blob()
print('5')
#cripto()
print('6')
#log()
print('7')
#ai()
print('8')
blob()
