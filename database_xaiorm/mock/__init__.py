import os
import uuid

def generate_mock_data(_fields,_values,_limit):
    _mx = 0
    _mx_r = 0
    _mx_r_v = len(_values)
    ___cmd = ''
    ___vsl_fx0 = ''
    _cmd = _fields.replace(' ','_')
    _vsl = _values.split(',')
    for _vsl_x in _vsl:
        ___vsl_fx0 += f"{_vsl_x};"
    ___vsl_fx0 += f"{_vsl_x}\n"
    while _limit > _mx:
        _vsl_tex = ''
        for __vsl in _vsl:
            _vsl_tex += f"{__vsl};"
        ___cmd += f"{str(_vsl_tex)}\n"
        _mx += 1
    print(f'_cmd={___cmd}')
    _out_mock_local = os.getcwd()
    _out_mock = str(uuid.uuid4()).replace('-','_')
    _out_mock_local_data = f'{_out_mock_local}/database_xaiorm/mock/data/{_out_mock}.mock_xaiorm'
    with open(_out_mock_local_data,'a') as _mock_buff_write:
        ____cmd = f'{str(___vsl_fx0)}\n{str(___cmd)}'
        _mock_buff_write.write(str(____cmd))
    return _out_mock_local_data

def save_mock_csv(_path_mock_aiorm):
    with open(_path_mock_aiorm,'r') as _mock_buff_read:
        _t_x = _mock_buff_read.read()
    _path_mock_csv = _path_mock_aiorm.replace('.mock_xaiorm','.csv')
    with open(_path_mock_csv,'a') as _mock_buff_write:
        _mock_buff_write.write(str(_t_x))
    return _path_mock_csv
