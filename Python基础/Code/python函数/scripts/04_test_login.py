#导包
#from 包.模块 import 函数或类
from python函数.api.login import fun_login

test_data = ["", "13488888888", "13412345678"]
for i in test_data:
    if i == "13488888888":
        assert "Success" == fun_login(i)
    else:
        assert "Error".upper() == fun_login(i)