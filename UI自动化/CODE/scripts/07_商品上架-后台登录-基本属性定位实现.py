#导包
import time
from selenium.webdriver.common.by import By
from tools.chromeDriver import get_driver,quit_driver

#获取浏览器并打开页面
driver = get_driver("https://hmshop-test.itheima.net/index.php/Admin/Admin/login")

# 页面操作
#[name='username']
driver.find_element(By.NAME, "username").send_keys("admin")

#[name='password']
driver.find_element(By.NAME, "password").send_keys("HM_2025_test")

# #vertify
driver.find_element(By.ID,"vertify").send_keys("8888")

# .sub
driver.find_element(By.CLASS_NAME,"sub").click()


# 退出浏览器
time.sleep(3)
quit_driver(driver)