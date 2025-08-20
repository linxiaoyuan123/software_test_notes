"""
技术点：定位一组元素
方法：driver.find_elements(定位策略,表达式)
结果：返回所有找到元素的一个列表，通过列表的下标进行取值操件
"""

#导包
import time
from selenium.webdriver.common.by import By
from tools.chromeDriver import get_driver,quit_driver

#获取浏览器并打开页面
driver = get_driver("https://hmshop-test.itheima.net/index.php/Admin/Admin/login")

# 页面操作(ctrl + d 重复当前行的内容到下一行)

driver.find_elements(By.CLASS_NAME,"input-text")[0].send_keys("admin")

driver.find_elements(By.CLASS_NAME,"input-text")[1].send_keys("HM_2025_test")

driver.find_elements(By.CLASS_NAME,"input-text")[2].send_keys("8888")

#.sub
driver.find_element(By.CLASS_NAME,"sub").click()


# 退出浏览器
time.sleep(3)
quit_driver(driver)