"""

需求：
1、定义字典存储测试数据，包含账号和密码
        提示:[{"username":"13488888888”","password":"123456”},
            {"username": ", "password":"123456"}]
2、遍历数据进行测试账号和密码校验
3、当手机号为"13488888888”且密码为"123456"时，输出"登录成功"；否则"错误或密码错误"。

"""

test_data = [
    {
    "username":"13488888888",
    "password":"123456"
    },
    {
    "username":"",
    "password":"123456"
    },
    {
    "username":"13488888888",
    "password":""
    },
]

for i in test_data:
    if i.get("username") == "13488888888" and i.get("password") == "123456":
        print("登录成功")
    else:
        print("账号或密码错误")
