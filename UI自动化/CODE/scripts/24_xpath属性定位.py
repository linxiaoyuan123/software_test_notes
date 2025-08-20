"""
属性定位
    概念：利用元素的属性来进行定位。
    示例：
        //input[@type='submit']
        //*[@value='提交']

"""


#打开页面
#需求：打开注册页面。完成以下操作：
#1)。利用元素的属性信息精准定位用户名输入框，并输入：admin
# 项目地址:http://121.43.169.97:8848/pageA.html

# 导包
import time
from selenium.webdriver.common.by import By
from tools.chromeDriver import get_driver, quit_driver
# 打开页面
driver = get_driver("http://121.43.169.97:8848/pageA.html")
# 页面操作
# xpath属性定位
driver.find_element(By.XPATH, "//*[@id='userA']").send_keys("admin")
time.sleep(1)

# xpath属性与逻辑结合
driver.find_element(By.XPATH, "//*[@name='user' and @class='login']").send_keys("admin123")
time.sleep(1)

# xpath属性与层级结合
driver.find_element(By.XPATH, "//*[ @id='p1']/input[@name='user']").clear()
time.sleep(1)
driver.find_element(By.XPATH, "//*[ @id='p1']/input[@name='user']").send_keys("admin666")

# 退出浏览器
quit_driver(driver)