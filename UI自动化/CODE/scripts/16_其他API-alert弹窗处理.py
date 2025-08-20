"""
技术点：alert弹窗处理（属于JS弹框，无法通过元素定位进行处理）
[包括alert(警告框)，confirm(确认框)，prompt(提示框)]
注意：alert弹窗右键之后看不到任何功能快捷操作
操作：
1、切换到alert弹窗
alert = driver.switch_to.alert  #三种弹出框，获取方法一样
2、点击弹窗按钮
alert.accept()
alert.dismiss()     #警告框没有取消按钮，取消一样生效
3、获取弹出框文本
alert.text()



需求：打开注册页面，完成以下操作：
1).点击 alert 按钮
2).关闭警告框
3).输入用户名：admin
项目：http://121.43.169.97:8848/pageA.html
"""
#导包
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://121.43.169.97:8848/pageA.html")

# 1).点击 alert 按钮
# driver.find_element(By.ID,"alerta").click()
# driver.find_element(By.ID,"confirma").click()
driver.find_element(By.ID,"prompta").click()
time.sleep(1)
# 2).关闭警告框
alert = driver.switch_to.alert
# alert.accept()
alert.dismiss()
time.sleep(1)

# 3).输入用户名：admin
driver.find_element(By.ID,"userA").send_keys("13488888888")

time.sleep(3)
driver.quit()




