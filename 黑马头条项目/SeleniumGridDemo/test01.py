"""
目标：Selenium Grid的使用
需求：
    1.使用chrome浏览器
    2.打开百度并搜索python关键字
    3.暂停3秒关闭浏览器
"""
# 导包
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
# 不指定平台和版本，可以让Grid自动匹配
# 设置浏览器名称（通常不需要，因为Options已经特定于Chrome）
# options.browser_name = "chrome"  # 这行通常不需要，因为Options已经是Chrome的
# 设置浏览器版本（如果有需要）
# chrome_options.set_capability('browserVersion', '')  # 你可以填入具体版本，如'90.0'
# 设置平台（如果有需要）
# chrome_options.set_capability('platformName', 'Windows 11')

# 如果需要设置其他选项，例如无头模式等，可以继续设置
# options.add_argument('--headless')

driver = webdriver.Remote(
    command_executor="http://192.168.88.1:4444/wd/hub",
    options=chrome_options
)

# 打开百度
driver.get("http://www.baidu.com")

# 输入关键字
driver.find_element(By.ID, "chat-textarea").send_keys("python")
# 点击搜索按钮
driver.find_element(By.ID, "chat-submit-button").click()

# 暂停三秒
sleep(3)

# 确保无论如何都会关闭浏览器
driver.quit()