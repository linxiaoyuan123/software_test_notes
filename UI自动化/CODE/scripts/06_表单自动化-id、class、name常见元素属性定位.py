#导包
import random
from selenium.webdriver.common.by import By
import time
from tools.chromeDriver import get_driver, quit_driver

#获取驱动、并实现页面元素定位与操作
driver = get_driver("https://hmshop-test.itheima.net/Home/user/reg.html")

# #username
# driver.find_element(By.CSS_SELECTOR, "#username").send_keys("13633331001")
# 引入随机数解决手机号唯一性问题
# driver.find_element(By.CSS_SELECTOR, "#username").send_keys(f"136{random.randint(20000000,88887777)}")
driver.find_element(By.ID, "username").send_keys(f"136{random.randint(20000000,88887777)}")

# .inp.imgcode.J_imgcode
# driver.find_element(By.CSS_SELECTOR, ".inp.imgcode.J_imgcode").send_keys("8888")
driver.find_element(By.CLASS_NAME, "imgcode").send_keys("8888")

# #password
# driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123456")
driver.find_element(By.ID, "password").send_keys("123456")

# #password2
# driver.find_element(By.CSS_SELECTOR, "#password2").send_keys("123456")
driver.find_element(By.ID, "password2").send_keys("123456")

# [name='invite']
# driver.find_element(By.CSS_SELECTOR, "[name='invite']").send_keys("")
driver.find_element(By.NAME, "invite").send_keys("")

# .regbtn.J_btn_agree
time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, ".regbtn.J_btn_agree").click()
driver.find_element(By.CLASS_NAME, "J_btn_agree").click()

# 退出浏览器
quit_driver(driver)