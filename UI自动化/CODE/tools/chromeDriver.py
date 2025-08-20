# 导包
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


#定义函数：接受不同url，返回driver对象
def get_driver(url):
    # 创建浏览器
    # driver = webdriver.Chrome()

    service = Service(executable_path="../scripts/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    # 访问页面
    driver.get(url)

    # 返回driver对象
    return driver

#定义函数：接受driver并实现退出浏览器
def quit_driver(driver):
    # 退出浏览器
    time.sleep(3)
    driver.quit()