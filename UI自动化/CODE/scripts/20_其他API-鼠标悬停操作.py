"""
导包          from selenium.webdriver import ActionChains
实例化鼠标对象 action = ActionChains(driver)
调用鼠标方法  action.move_to_element(driver.find_element(By.LINK_TEXT,"服饰"))
执行鼠标操作  action.perform()    #注意：需要执行该语句，鼠标的操作才会真正起作用
"""
#导包
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from tools.chromeDriver import get_driver,quit_driver

#需求：打开商城首页，完成以下操作
driver = get_driver("https://hmshop-test.itheima.net/Home/Index/index.html")

#1）.暂停2s，鼠标悬停【服饰】分类
time.sleep(2)
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.LINK_TEXT,"服饰"))
action.perform()    #注意：需要执行该语句，鼠标的操作才会真正起作用
#2)。暂停2s，查看【服饰】分类下商品信息
time.sleep(2)
driver.find_element(By.LINK_TEXT, "旗袍").click()
time.sleep(2)

#退出浏览器
quit_driver(driver)