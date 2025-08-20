"""
PyTest是单元测试框架(Unitest是Python自带的测试框架，Pytest更简洁高效)
    1、可以组织多个用例执行
    2、可以实现参数化
    3、断言
    4、生成测试报告

pytest框架安装
    pip install pytest
    pip show python
"""
class TestLogin:
    #类级别前置代码
    def setup_class(self):
        print("我是类级别前置处理，我只执行一次")
    #类级别后置代码
    def teardown_class(self):
        print("我是类级别后置处理，我只执行一次")
    #方法级别前置代码
    def setup_method(self):
        print("我是方法级别前置处理，用例每执行一次我执行一次")
    #方法级别后置代码
    def teardown_method(self):
        print("我是方法级别后置处理，用例每执行一次我执行一次")
    #case01:登录失败(账号为空)
    def test_login01(self):
        print("case01:登录失败(账号为空)")
    #case02:登录失败(密码为空)
    def test_login02(self):
        print("case02:登录失败(密码为空)")
    #case03:登录成功
    def test_login03(self):
        print("case03:登录成功")