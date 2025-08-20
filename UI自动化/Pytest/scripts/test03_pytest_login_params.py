#导包
import time
import config
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
        service = Service(executable_path=config.BASE_PATH + '/chromedriver.exe')
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