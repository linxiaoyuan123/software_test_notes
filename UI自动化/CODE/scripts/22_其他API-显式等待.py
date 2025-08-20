"""
隐式等待和显示等待对比
                    隐式等待                        显式等待
    作用域        只用设置一次，对全局生效             只对指定元素生效
    抛出异常      NoSuchElementException          TimeOutException
    使用方法    driver.implicitly_wait(timeout)   通过WebDriverWait对象
    其它          必须等待整个页面加载完成             只关注指定元素是否加载

显式等待
    定位指定元素时，如果能定位到元素则直接返回该元素，不触发等待;
    如果不能定位到该元素，则间隔一段时间后再去定位元素；
    如果在达到最大时长时还没有找到指定元素，则抛出超时异常TimeoutException

实现方法
导包              from selenium.webdriver.support.wait import WebDriverWait
创建显示等待类对象   WebDriverWait(driver, timeout, poll_frequency=0.5)
调用utils方法      until(method):直到...时
"""
import time

# 导包
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# 打开浏览器
driver = webdriver.Chrome()
# 需求：打开注册页面，完成以下操作
#1）最大化窗口
driver.maximize_window()
driver.get("http://121.43.169.97:8848/pageA.html")
#2)。使用显式等待定位延时加载输入框，输入admin
#lambda: 匿名函数
WebDriverWait(driver,10,1).until(lambda x:x.find_element(By.ID,"username")).send_keys("admin")
# driver.find_element(By.ID,"username").send_keys("admin")
time.sleep(1)

#退出浏览器
driver.quit()


# 项目地址:http://121.43.169.97:8848/pageA.html