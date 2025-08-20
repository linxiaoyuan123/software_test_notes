#导包
import time

from selenium.webdriver.common.by import By

from tools.chromeDriver import get_driver,quit_driver

#页面操作
driver = get_driver("https://hmshop-test.itheima.net/Home/user/login.html")
#用户名：#username
driver.find_element(By.CSS_SELECTOR, "#username").send_keys("13488888888")
#密码:#password
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123456")
#验证码:#verify_code
driver.find_element(By.CSS_SELECTOR, "#verify_code").send_keys("8888")
# 登录:.J-login-submit
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".J-login-submit").click()

#退出浏览器
quit_driver(driver)