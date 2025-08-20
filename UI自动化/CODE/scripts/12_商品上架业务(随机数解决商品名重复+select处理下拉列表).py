"""
select下拉框
    1、导包（写第二步，然后让pycharm智能导包）
        from selenium.webdriver.support.select import Select
    2、创建select对象
        select = Select(element)
    3、选择选项
        select.select_by_value(value)   根据选项的value属性
        select.select_by_index(index)   根据下标、
        select.select_by_visble_text(text)  根据选项文本

注意：
    select类实现选项选择，只适用HTML原生态的<select>+<option>的下拉框
"""

#导包
import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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

#2.3 点击【添加商品】按钮
# 元素定位失败场景1，页面存在frame嵌套，需要：
# 1、先切换到指定的frame页
# 2、完成页面元素定位与操作
# 3、返回默认页面
time.sleep(1)
#2.3.1 切换frame窗口
driver.switch_to.frame(driver.find_element(By.ID,"workspace"))
#2.3.2 frame上元素定位与操作
driver.find_elements(By.CLASS_NAME,"add")[0].click()
#2.3.3 返回默认页面供后续业务操作
driver.switch_to.default_content()

#3、添加商品
#①切换页面
driver.switch_to.frame(driver.find_element(By.ID, "workspace"))
# ②页面操作
#3.1商品名称
time.sleep(1)
driver.find_element(By.NAME, "goods_name").send_keys(f"Jack-Test-1214-{random.randint(101,666)}")
# 3.2 商品分类

#基于select-option 下拉框使用selenium自带的select工具类进行操作
select = Select(driver.find_element(By.ID, "cat_id"))
# select.select_by_value("30")  #根据value属性进行定位
# select.select_by_index(2) #根据option下标取值进行定位(从1开始算)
select.select_by_visible_text("家居")


# 3.3 本店售价
driver.find_element(By.NAME,"shop_price").send_keys("15")
# 3.4 市场价
driver.find_element(By.NAME,"market_price").send_keys("15")
# 3.5 是否包邮
driver.find_element(By.ID,"is_free_shipping_label_1").click()
# 3.6 确认提交
driver.find_element(By.ID,"submit").click()

# 退出浏览器
time.sleep(3)
quit_driver(driver)