"""
技术点：CSS定位
4种选择器：
1、id选择器：#id属性值   具有唯一性
2、class选择器：.class属性值
              .class属性值1.class属性值2  class值一般都是多个
3、属性选择器：[属性名="属性值"]
            [属性名*="属性值"]
4、层级选择器：
        父子 element1>element2
        后代 element1 element2
提醒：在写代码之前，在开发者工具中确认选择器定位的元素时唯一的
"""

# 导包
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建浏览器
driver = webdriver.Chrome()
driver.maximize_window()

# 访问页面
driver.get("https://hmshop-test.itheima.net/Home/user/login.html")

#页面操作
#用户名：#username
driver.find_element(By.CSS_SELECTOR, "#username").send_keys("13488888888")
#密码:#password
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123456")
#验证码:#verify_code
driver.find_element(By.CSS_SELECTOR, "#verify_code").send_keys("8888")
# 登录:.J-login-submit
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".J-login-submit").click()

# 退出浏览器
time.sleep(3)
driver.quit()