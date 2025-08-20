# 导包
from python函数.api.login import fun_login2
#准备测试数据
test_data =[
    {
        "username":"13488888888",
        "password":"123456"
    },
    {
        "username":"",
        "password": "123456"
    },
    {
        "username":"13488888888",
        "password": ""
    }
]

# 遍历数据，调用方法获取实际结果
for i in test_data:
    print(f"测试账号为:{i.get('username')} 测试密码为:{i.get('password')} 测试结果:{fun_login2(i.get('username'),i.get('password'))}")
    if i.get('username')=="13488888888" and i.get('password')=="123456" :
        assert "成功" in fun_login2(pwd=i.get("password"),phone=i.get("username"))
    else:
        assert "错误" in fun_login2(pwd=i.get("password"),phone=i.get("username"))