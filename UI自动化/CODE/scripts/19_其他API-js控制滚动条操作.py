"""
js控制滚动条操作
    js = "window.scrollTo(0, 10000)"    #定义JS字符串(x坐标，y坐标)
    driver.execute_script(js)           #执行JS字符串
"""
# 导包
import time
from tools.chromeDriver import get_driver, quit_driver
#需求：打开商城首页，完成以下操作
driver = get_driver("https://hmshop-test.itheima.net/")

#
#1).暂停2s，控制滚动条滑动到页面最底部
time.sleep(2)
js = "window.scrollTo(0, 10000)"    #定义JS字符串(x坐标，y坐标)
driver.execute_script(js)           #执行JS字符串
#2)。暂停2s，控制滚动条回到顶部
time.sleep(2)
js = "window.scrollTo(0, 0)"
driver.execute_script(js)
time.sleep(2)

#退出浏览器
quit_driver(driver)