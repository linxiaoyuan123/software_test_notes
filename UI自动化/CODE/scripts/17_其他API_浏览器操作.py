"""
    窗口最大化   dirver.maxmize_window()
    获取标题    dirver.title
    获取网页地址  dirver.current_url
    刷新页面操作  dirver.refresh()
    关闭当前窗口  dirver.close()
    关闭浏览器   dirver.quit()
"""

#导包
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建浏览器
driver = webdriver.Chrome()
driver.maximize_window()
# 浏览器窗口最大化
#打开页面
driver.get("https://hmshop-test.itheima.net/Home/Index/index.html")
#获取当前页面标题及URL信息
print(driver.title)
print(driver.current_url)
print("-" * 80)

#首页跳转至登录页并登录
driver.find_element(By.LINK_TEXT, "登录").click()
time.sleep(1)
driver.find_element(By.ID, "username").send_keys("13488888888")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "verify_code").send_keys("8888")
driver.find_element(By.NAME, "sbtbutton").click()

#获取登录成功后页面标题及URL信息
time.sleep(1)
print(driver.title)
print(driver.current_url)
print("-" * 80)

#个人中心跳转至我的浏览页面
driver.find_element(By.LINK_TEXT, "我的浏览").click()
time.sleep(1)

#多窗口处理
handles = driver.window_handles
driver.switch_to.window(handles[1]) #切换到新打开的第二个浏览器页面

#获取当前页面标题及URL信息
time.sleep(1)
print(driver.title)
print(driver.current_url)
print("-" * 80)

#关闭我的浏览页面
time.sleep(2)
driver.close()
time.sleep(3)


#退出浏览器
driver.quit()