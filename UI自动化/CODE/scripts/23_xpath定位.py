"""
技术点：xpath定位
策略：
①路径定位：绝对路径(/html/xxx   注意：不推荐)  检查==》复制==》复制完整xpath
         相对路径(//* xxx)                检查==》复制==》复制xpath
②文本定位:
        相等 //*[text()='文字']
        包含 //*[contains(text(),'文字')]
场景：当页面元素没有基本信息时。可以继续页面显示文字通过xpath进行定位

"""
import time

#需求：xpath定位实现冷链监控系统自动登录
# 说明：
#项目地址:http://120.26.52.119/
# 账号:admin
#密码:HM_2025test
#
# 导包
from selenium.webdriver.common.by import By

from tools.chromeDriver import get_driver, quit_driver
# 打开页面
driver = get_driver("http://120.26.52.119/")
# 页面操作
# 输入账号
driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[2]/div[1]/div/div[1]/input').send_keys("admin")
# 输入密码
driver.find_element(By.XPATH,'//*[@id="app"]/div/form/div[2]/div[2]/div/div[1]/input').send_keys("HM_2025_test")
#点击登录
driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[2]/button').click()


#实时展示监控页面信息
#点击监控管理
#//*[text()='监控管理'］
driver.find_element(By.XPATH, "//*[text()='监控管理']").click()
time.sleep(1)
#点击实时报警
#//*[contains(text(),'实时报警')]
driver.find_element(By.XPATH, "//*[contains(text(),'实时报警')]").click()
time.sleep(2)

# 退出浏览器
quit_driver(driver)