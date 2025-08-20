"""
页面操作：
    定位元素：
        element = driver.find_element(定位方法,值)       单一元素
        element = driver.find_elements(定位方法,值)      一组元素
    操作元素：
        输入  element.send_keys(value)
        清空  element.clear()
        点击  element.click()


"""

# 1、导包
import time
from selenium import webdriver
# 快捷导包 ctrl + alt + 空格
from selenium.webdriver.common.by import By

# 2、打开浏览器
driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()

# 3、访问页面
driver.get("https://hmshop-test.itheima.net/Home/user/login.html")

# 4、页面操作
#用户名查找及操作
# element = driver.find_element(By.ID, "username")

#CSS选择器定位，可以在浏览器中按F12，选定UI，然后在蓝色那行右键选中复制CSS选择器

element = driver.find_element(By.CSS_SELECTOR, "#username")
element.send_keys("13488888888")

# 密码查找及操作
# element = driver.find_element(By.ID, "password")
element = driver.find_element(By.CSS_SELECTOR, "#password")
element.send_keys("123456")
#验证码査找及操作
# driver.find_element(By.ID,"verify_code").send_keys("8888")
driver.find_element(By.CSS_SELECTOR, "#verify_code").send_keys("8888")
#登录按钮查找及操作
# driver.find_element(By.NAME, "sbtbutton").click()
driver.find_element(By.CSS_SELECTOR, "#loginform > div > div.login_bnt >a").click()

# 5、关闭浏览器
time.sleep(3)
driver.quit()


