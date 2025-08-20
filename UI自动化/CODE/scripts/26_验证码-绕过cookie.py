"""
验证码：
    三种处理验证码操作
        去掉验证码、万能验证码
        验证码识别技术(AI)
        记录cookie

cookie概念
    Cookie是由Web服务器生成的，并且保存在用户浏览器上的小文本文件，它可以包含用户相关的信息。
    Cookie数据格式：键值对组成（python中的字典）
    Cookie产生：客户端请求服务器，如果服务器需要记录该用户状态，就向客户端浏览器颁发一个Cookie数据
    Cookie使用：当浏览器再次请求该网站时，浏览器把请求的数据和Cookie数据一同提交给服务器，服务器检查该Cookie，以此来辨认用户状态。

cookie的操作方法
    driver.get_cookie(name)-->获取指定cookie
    driver.get_cookies()-->获取本网站所有本地cookies
    driver.add_cookie(cookie_dict)-->添加cookie
        cookie_dict：一个字典对象，必选的键包括："name"and"value"
"""
import time

#导包
from tools.chromeDriver import get_driver, quit_driver

#打开页面
driver = get_driver("https://hmshop-test.itheima.net/Home/User/index.html")
#1、前置：手动在页面完成登录
#2、前置：获取登录成功之后的c0okie信息（浏览器开发者工具F12==》网络==》找到第一个数据包==》cookies）
test_data = {
    "name": "PHPSESSID",
    "value": "pi1nccopjkq79e8ash304kbak6"
}
# 3、设置cookies数据
driver.add_cookie(test_data)
time.sleep(1)
# 4、刷新页面
driver.refresh()
time.sleep(2)

#退出浏览器
quit_driver(driver)