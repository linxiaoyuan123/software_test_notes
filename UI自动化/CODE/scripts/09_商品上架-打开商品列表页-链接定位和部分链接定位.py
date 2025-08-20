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

#2、打开商品上架页面
#2.1 点击导航栏的【商城】
time.sleep(1)
# driver.find_element(By.LINK_TEXT,"商城").click()
# 注意包含定位的时候，如果页面中不是唯一的，默认返回第一个
driver.find_element(By.PARTIAL_LINK_TEXT,"商城").click()
#2.2 点击商城里面的商品列表
driver.find_element(By.LINK_TEXT,"商品列表").click()


# 退出浏览器
time.sleep(3)
quit_driver(driver)