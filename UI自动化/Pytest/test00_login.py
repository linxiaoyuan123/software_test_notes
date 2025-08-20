#导包
import time
from sys import executable

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#打开浏览器
service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)
# driver = webdriver.Chrome()
driver.maximize_window()

#打开网页
driver.get("https://hmshop-test.itheima.net/Home/user/login.html")

#页面定位+操作
driver.find_element(By.ID, "username").send_keys("13488888888")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "verify_code").send_keys("8888")
driver.find_element(By.NAME, "sbtbutton").click()

#等待3秒
time.sleep(3)

#退出浏览器
driver.quit()