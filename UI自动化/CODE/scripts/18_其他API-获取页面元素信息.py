"""
获取页面元素信息
    获取元素大小
    element.size
    获取元素文本
    element.text
    获取元素属性值
    element.get_attribute('属性名')
    判断元素是否可用
    element.is_enabled()
    判断元素是否勾选
    element.is_selected)
    判断元素是否可见
    element.is_displayed()
"""

#导包
import time

from selenium.webdriver.common.by import By

from tools.chromeDriver import get_driver,quit_driver

driver = get_driver("https://hmshop-test.itheima.net/Home/user/reg.html")

# 需求
#1）。获取手机号码输入框的大小
print(driver.find_element(By.ID, "username").size)  # 获取元素大小：element.size
#2)，获取页面上第一个span标签的文本内容
print(driver.find_elements(By.TAG_NAME, "span")[0].text) # 获取元素文本：element.text
#3)。获取页面上登录超链接的地址
print(driver.find_element(By.PARTIAL_LINK_TEXT, "登录").get_attribute("href"))
# 获取指定属性的值：element.get_attribute("属性名")

#4）.判断页面中【用户服务协议】是否为选中状态
print(driver.find_element(By.ID, "checktxt").is_selected())
#True：选中，False：未选中
#5）.判断页面中的【同意协议并注册】是否可用
print(driver.find_element(By.LINK_TEXT,"同意协议并注册").is_enabled())
#True：可用，False：不可用


#退出浏览器
time.sleep(3)
quit_driver(driver)