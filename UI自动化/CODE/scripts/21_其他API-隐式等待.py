"""
隐式等待(对于整一个页面都起作用)
    定位元素时，如果能定位到元素则直接返回该元素，不触发等待；
    如果不能定位到该元素，则间隔一段时间后再去定位元素；
    如果在达到最大时长时还没有找到指定元素，则抛出元素不存在的异常NoSuchElementException。
    driver.implicitly_wait(timeout)
"""
import time

# 导包
from selenium import webdriver
from selenium.webdriver.common.by import By

# 打开浏览器
driver = webdriver.Chrome()
# 需求：打开注册页面，完成以下操作
#1）最大化窗口
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(10)
#找到元素，不触发等待
#找不到，过一段时间继续去找元素，到达设置最大等待10时间后任然找不到元素，抛出异常NoSuchElementException
driver.get("http://121.43.169.97:8848/pageA.html")
#2)。使用隐式等待定位延时加载输入框，输入admin
driver.find_element(By.ID,"username").send_keys("admin")
time.sleep(1)

#退出浏览器
driver.quit()


# 项目地址:http://121.43.169.97:8848/pageA.html