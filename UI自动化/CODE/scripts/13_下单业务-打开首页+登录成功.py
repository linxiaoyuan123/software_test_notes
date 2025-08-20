#导包
import time

from selenium.webdriver.common.by import By

from tools.chromeDriver import get_driver, quit_driver

#获取浏览器驱动
driver = get_driver("https://hmshop-test.itheima.net/index.php/Home/Index/index.html")

# 下单业务
# 1、点击首页【登录】打开登录页面
driver.find_element(By.LINK_TEXT, "登录").click()
# 2、输入手机号/邮箱
driver.find_element(By.ID, "username").send_keys("13488888888")
# 3、输入账号密码
driver.find_element(By.ID, "password").send_keys("123456")
# 4、输入验证码
driver.find_element(By.ID, "verify_code").send_keys("8888")
# 5、点击登录
driver.find_element(By.LINK_TEXT, "登    录").click()
time.sleep(3)

#退出浏览器
quit_driver(driver)