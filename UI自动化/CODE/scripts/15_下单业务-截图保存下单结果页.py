"""
窗口截图
    使用场景：
        UI自动测试统一运行时无人值守
        错误信息记录不是十分明确
        有截图结合错误信息方便快速分析错误

    driver.get_screenshot_as_file("imgpath")
        imgpath:图片保存路径
"""
#导包
import time

from selenium.webdriver.common.by import By

from tools.chromeDriver import get_driver, quit_driver

#获取浏览器驱动
driver = get_driver("https://hmshop-test.itheima.net/index.php/Home/Index/index.html")

# 下单业务

# 登陆业务
# 1、点击首页【登录】打开登录页面
driver.find_element(By.LINK_TEXT, "登录").click()
# 2、输入手机号/邮箱
driver.find_element(By.ID, "username").send_keys("13488888888")
# 3、输入账号密码
driver.find_element(By.ID, "password").send_keys("123456")
# 4、输入验证码
driver.find_element(By.ID, "verify_code").send_keys("8888")
# 5、点击登录
driver.find_element(By.LINK_TEXT, "登    录").click()
time.sleep(3)


# 6、选择搜索框输入
driver.find_element(By.ID,"q").send_keys("Jack-Test-1214")
# 7、点击搜索按钮
driver.find_element(By.LINK_TEXT,"搜索").click()
time.sleep(2)

# 8、点击商品列表中的加入购物车
driver.find_elements(By.LINK_TEXT,"加入购物车")[0].click()
time.sleep(2)
# 9、关闭弹窗
driver.find_element(By.CLASS_NAME,"layui-layer-setwin").click()
time.sleep(2)
# 10、点击购物车(多值类，用CSS选择器)
driver.find_element(By.CSS_SELECTOR,".c-n.fl").click()

# 11、订单页面-去结算
driver.find_element(By.LINK_TEXT,"去结算").click()
time.sleep(2)

# 12、提交订单
driver.find_element(By.ID,"submit_order").click()
# 元素定位失败常见场景：页面元素未加载完全、导致定位失败
"""
解决：
    设置等待时间
    强制等待(time.sleep)
    显示等待
    隐式等待
"""
time.sleep(5)

# 13、支付页面-确认支付方式
driver.find_element(By.LINK_TEXT,"确认支付方式").click()
time.sleep(2)

# 打印当前页面标题信息
print(driver.title)
print(driver.current_url)

# 14、点击我的订单，查看订单信息
driver.find_element(By.LINK_TEXT,"我的订单").click()
time.sleep(2)

# 切换窗口信息
# 定位失败的常见场景：浏览器多窗口切换
handles = driver.window_handles     #获取所有浏览器已打开的窗口信息(句柄) 返回列表
driver.switch_to.window(handles[1])     #使用下标处理指定的窗口

# 打印当前页面标题信息
print(driver.title)
print(driver.current_url)

# 15、使用截图保存下单的结果页面
# driver.get_screenshot_as_file("order.png")        #当前目录保存截图
driver.get_screenshot_as_file("../images/order2.png")   #相对路径保存截图

#退出浏览器
quit_driver(driver)