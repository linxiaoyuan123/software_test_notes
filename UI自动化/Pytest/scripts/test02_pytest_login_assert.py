"""
断言:让程序代替人为判断测试程序执行结果是否符合预期结果的过程

学习断言作用：
    提高测试效率
    实现自动化测试(让脚本在无人值守状态下运行)
"""

#导包
import time
import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


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
    def test_login01(self):
        # 页面定位+操作
        self.driver.find_element(By.ID, "username").send_keys("")
        self.driver.find_element(By.ID, "password").send_keys("123456")
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")
        self.driver.find_element(By.NAME, "sbtbutton").click()
        # 页面等待3秒
        time.sleep(3)
        # 获取账号信息，断言比较，若断言成功则为勾，断言失败则为叉，并给出对比
        # print(self.driver.find_element(By.CLASS_NAME, 'layui-layer-padding').text)
        # assert "用户名不能为空" in self.driver.find_element(By.CLASS_NAME, 'layui-layer-padding').text
        # xpath定位
        print(self.driver.find_element(By.XPATH, '//*[@id="layui-layer1"]/div[2]').text)
        assert "用户名不能为空" in self.driver.find_element(By.XPATH, '//*[@id="layui-layer1"]/div[2]').text

    #case02:登录失败(密码为空)
    def test_login02(self):
        # 页面定位+操作
        self.driver.find_element(By.ID, "username").send_keys("13488888888")
        self.driver.find_element(By.ID, "password").send_keys("")
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")
        self.driver.find_element(By.NAME, "sbtbutton").click()
        # 页面等待3秒
        time.sleep(3)
        # 获取账号信息，断言比较，若断言成功则为勾，断言失败则为叉，并给出对比
        # print(self.driver.find_element(By.CLASS_NAME, 'layui-layer-padding').text)
        # assert "密码不能为空" in self.driver.find_element(By.CLASS_NAME, 'layui-layer-padding').text
        # xpath定位
        print(self.driver.find_element(By.XPATH, '//*[@id="layui-layer1"]/div[2]').text)
        assert "密码不能为空" in self.driver.find_element(By.XPATH, '//*[@id="layui-layer1"]/div[2]').text

    #case03:登录成功
    def test_login03(self):
        # 页面定位+操作
        self.driver.find_element(By.ID, "username").send_keys("13488888888")
        self.driver.find_element(By.ID, "password").send_keys("123456")
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")
        self.driver.find_element(By.NAME, "sbtbutton").click()
        # 页面等待3秒
        time.sleep(3)
        # 获取账号信息，断言比较，若断言成功则为勾，断言失败则为叉，并给出对比
        # print(self.driver.find_element(By.CLASS_NAME, 'userinfo').text)
        # assert "13488888888" == self.driver.find_element(By.CLASS_NAME, 'userinfo').text
        # xpath定位
        print(self.driver.find_element(By.XPATH, '//*[@class="red userinfo"]').text)
        assert "13488888888" == self.driver.find_element(By.XPATH, '//*[@class="red userinfo"]').text
