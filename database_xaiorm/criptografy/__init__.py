#python
#orm_criptografy.py
#19:29 29/08/2025

from cryptography.fernet import Fernet

def GenerateCriptoKey():
    key = Fernet.generate_key() #this is your "password"
    return key

def CriptographyContent(content, key):
    cipher_suite = Fernet(key)
    __content = content.encode('ISO-8859-1')
    _r = cipher_suite.encrypt(__content)
    return _r

def Uncripto(content, key):
    cipher_suite = Fernet(key)
    _r = cipher_suite.decrypt(content)
    return _r
