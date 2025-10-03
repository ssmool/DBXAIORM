#python
#orm_blob.py
#19:28 29/08/2025

import base64

def set_data_blob(_data,_buff=1024):
	_r = []
	for __data in range(0, len(_data), _buff):
		chunk = _data[__data:__data+_buff]
		encoded = base64.b64encode(chunk).decode('utf-8')
		_r.append(encoded)
	return _r

def set_string_64(_data):
	__data = _data.encode('utf-8')
	_r = base64.b64encode(__data).decode('utf-8')
	return _r
	
def get_string_64(_data):
	__data = base64.b64decode(_data)
	_r = __data.decode('utf-8')
	return _r
