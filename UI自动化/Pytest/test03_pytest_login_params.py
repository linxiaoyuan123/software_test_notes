"""
技术点：参数化（数据驱动）
    作用：将测试数据和测试脚本分离，后期代码维护焦点放在数据
    使用：装饰器@（不改变方法内部的代码逻辑 新增功能）
        @pytest.mark.parametrize ==》循环遍历测试数据调用测试脚本
    步骤：
    ①准备测试数据，格式:[(),(),(),...]
    ②在被测试方法前面引入装饰器
    @pytest.mark.parametrize("保存数据的变量，注意变量个数=(测试数据中数据的个数)"，测试数据)
    def test_login(self,直接复制装饰器中保存数据的一组变量名即可):
        pass
    ③修改测试方法代码引用变量中的数据完成测试

pytest的两种启动方式：
    1、在pycharm中直接右键运行
    2、在终端中，文件对应的路径上，pytest -s test03_pytest_login_params.py
        在终端中返回的测试用例的结果，成功为点·，错误为e

    3、批量启动方式（配置文件，重点）
        创建一个pytest.ini
            内容：
                [pytest]
                #添加命令行参数
                addopts=-s
                #文件搜索路径
                testpaths=./scripts
                #文件名称
                python_files=test*.py
                #类名称
                python_classes=Test*
                #方法名称
                python_functions=test*

        创建一个scripts放测试用例，根据配置文件命名

引入项目配置文件config.py
os可以有效解决驱动报错问题，驱动路径
    config.py
        import os
        BASE_PATH = os.path.dirname(os.path.abspath(__file__)) #获取当前代码文件所在目录信息
"""

#导包
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

test_data = [
    ("","123456","8888"),
    ("13488888888","","8888"),
    ("13488888888","123456","8888")
]

class TestLogin:
    #类级别前置代码
    def setup_class(self):
        # 打开浏览器
        service = Service(executable_path='chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        # driver = webdriver.Chrome()
        self.driver.maximize_window()
    #类级别后置代码
    def teardown_class(self):
        self.driver.quit()
    #方法级别前置代码
    def setup_method(self):
        # 打开网页
        self.driver.get("https://hmshop-test.itheima.net/Home/user/login.html")
        pass
    #方法级别后置代码
    def teardown_method(self):
        # 等待3秒
        time.sleep(3)
    #case01:登录失败(账号为空)
    @pytest.mark.parametrize("username,password,code", test_data)
    def test_login01(self,username,password,code):
        # 页面定位+操作
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "verify_code").send_keys(code)
        self.driver.find_element(By.NAME, "sbtbutton").click()