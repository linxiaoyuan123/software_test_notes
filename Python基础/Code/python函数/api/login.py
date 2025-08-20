# 03_函数返回值、导包、断言用
import random


def login(phone):
    if phone == "13488888888":
        # print（"账号正确"）#问题：输出结果是直接打印在控制台，后续业务代码是没有办法继续处理该数据
        return "账号正确" # 解决：通过return返回程序处理结果，供后续业务继续处理
    else:
        # print("账号错误")
        return "账号错误"

# 04_test_login
# 登陆需求01
def fun_login(phone):
    if phone == "13488888888":
        return "Success"
    else:
        return "ERROR"

# 登陆需求02
def fun_login2(phone,pwd):
    if phone == "13488888888" and pwd == "123456":
        return "登录成功"
    else:
        return "手机号或密码错误"


#06_案例_参数指定个数及指定范围内的随机数
"""
需求：定义函数func，
可以按照如下要求生成随机数：
1.该函数可以接收三个参数；
    -参数1，为生成随机数的个数；
    -参数2和参数3为生成的随机数的范围；
    -参数2和参数3，如果不传递，默认生成1-1000之间的随机数
2.要求生成的随机数不能重复。
3.将生成的随机数列表进行返回。
"""
def func(count, start=1, end=1000):
    test_data=[]
    while True: #不确定循环次数
            num = random.randint(start,end)
            if num not in test_data:
                test_data.append(num)
                if len(test_data) == count:
                    return test_data

if __name__ == '__main__':
    print(func(10, 1, 20))