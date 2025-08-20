# UI自动化



## 一、selenium

#### 01_selenium环境安装

> [selenium安装环境网址](https://googlechromelabs.github.io/chrome-for-testing/)

1）将chromedriver.exe(驱动程序)放入python目录即可

2）selenium的安装

- cmd中输入**pip install selenium**
- 输入**pip show selenium**可以查看selenium版本号

#### 02_UI自动化测试介绍.py

```python
"""
1.UI自动化测试概念
    使用程序、脚本对系统界面体现的功能和数据信息展示等进行的测试技术

2.实施UI自动化测试前置条件(例如：银行之类的页面，或者企业的核心业务，互联网大多不适用)
    项目上线发布频率高，回归测试(旧功能)任务重
    项目需要实现自动化的功能模块，需求变更不频繁
    项目周期要长
3.UI自动化测试执行时机
    一般情况下在手工测试完成之后
    版本或项目功能趋于稳定
4.UI自动化测试的核心作用
    节省人力成本
    提高回归测试效率
    提高测试质量
"""
```

#### 03_selenium入门案例.py

```python
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
```

#### 04_CSS定位(重点).py

```python
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
```

### tools包

#### chromeDriver.py

```python
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
```

### scripts包

#### 05_表单自动化注册实现并使用随机数解决手机号唯一的问题.py

```python
#导包
import random
from selenium.webdriver.common.by import By
import time
from tools.chromeDriver import get_driver, quit_driver

#获取驱动、并实现页面元素定位与操作
driver = get_driver("https://hmshop-test.itheima.net/Home/user/reg.html")

# #username
driver.find_element(By.CSS_SELECTOR, "#username").send_keys("13488888888")
# 引入随机数解决手机号唯一性问题
# driver.find_element(By.CSS_SELECTOR, "#username").send_keys(f"136{random.randint(20000000,88887777)}")

# .inp.imgcode.J_imgcode
driver.find_element(By.CSS_SELECTOR, ".inp.imgcode.J_imgcode").send_keys("8888")

# #password
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123456")

# #password2
driver.find_element(By.CSS_SELECTOR, "#password2").send_keys("123456")

# [name='invite']
driver.find_element(By.CSS_SELECTOR, "[name='invite']").send_keys("")

# .regbtn.J_btn_agree
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".regbtn.J_btn_agree").click()

# 退出浏览器
quit_driver(driver)
```

#### 06_表单自动化-id、class、name常见元素属性定位.py

```python
#导包
import random
from selenium.webdriver.common.by import By
import time
from tools.chromeDriver import get_driver, quit_driver

#获取驱动、并实现页面元素定位与操作
driver = get_driver("https://hmshop-test.itheima.net/Home/user/reg.html")

# #username
# driver.find_element(By.CSS_SELECTOR, "#username").send_keys("13633331001")
# 引入随机数解决手机号唯一性问题
# driver.find_element(By.CSS_SELECTOR, "#username").send_keys(f"136{random.randint(20000000,88887777)}")
driver.find_element(By.ID, "username").send_keys(f"136{random.randint(20000000,88887777)}")

# .inp.imgcode.J_imgcode
# driver.find_element(By.CSS_SELECTOR, ".inp.imgcode.J_imgcode").send_keys("8888")
driver.find_element(By.CLASS_NAME, "imgcode").send_keys("8888")

# #password
# driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123456")
driver.find_element(By.ID, "password").send_keys("123456")

# #password2
# driver.find_element(By.CSS_SELECTOR, "#password2").send_keys("123456")
driver.find_element(By.ID, "password2").send_keys("123456")

# [name='invite']
# driver.find_element(By.CSS_SELECTOR, "[name='invite']").send_keys("")
driver.find_element(By.NAME, "invite").send_keys("")

# .regbtn.J_btn_agree
time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, ".regbtn.J_btn_agree").click()
driver.find_element(By.CLASS_NAME, "J_btn_agree").click()

# 退出浏览器
quit_driver(driver)
```

#### 07_商品上架-后台登录-基本属性定位实现.py

```python
#导包
import time
from selenium.webdriver.common.by import By
from tools.chromeDriver import get_driver,quit_driver

#获取浏览器并打开页面
driver = get_driver("https://hmshop-test.itheima.net/index.php/Admin/Admin/login")

# 页面操作
#[name='username']
driver.find_element(By.NAME, "username").send_keys("admin")

#[name='password']
driver.find_element(By.NAME, "password").send_keys("HM_2025_test")

# #vertify
driver.find_element(By.ID,"vertify").send_keys("8888")

# .sub
driver.find_element(By.CLASS_NAME,"sub").click()


# 退出浏览器
time.sleep(3)
quit_driver(driver)
```

#### 08_商品上架-后台登陆-定位一组元素find_elements.py

```python
"""
技术点：定位一组元素
方法：driver.find_elements(定位策略,表达式)
结果：返回所有找到元素的一个列表，通过列表的下标进行取值操件
"""

#导包
import time
from selenium.webdriver.common.by import By
from tools.chromeDriver import get_driver,quit_driver

#获取浏览器并打开页面
driver = get_driver("https://hmshop-test.itheima.net/index.php/Admin/Admin/login")

# 页面操作(ctrl + d 重复当前行的内容到下一行)

driver.find_elements(By.CLASS_NAME,"input-text")[0].send_keys("admin")

driver.find_elements(By.CLASS_NAME,"input-text")[1].send_keys("HM_2025_test")

driver.find_elements(By.CLASS_NAME,"input-text")[2].send_keys("8888")

#.sub
driver.find_element(By.CLASS_NAME,"sub").click()


# 退出浏览器
time.sleep(3)
quit_driver(driver)
```

#### 09_商品上架-打开商品列表页-链接定位和部分链接定位.py

```python
#导包
import time
from selenium.webdriver.common.by import By
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


# 退出浏览器
time.sleep(3)
quit_driver(driver)
```

#### 10_商品上架-打开商品新增页-页面嵌套iframe技术.py

```python
"""
frame
    HTML页面中的一种框架，主要作用是在当前页面中指定区域显示另一页面元素(类比每个iframe都是一个房间)
        frameset形式
        iframe标签形式

切换指定iframe
    driver.switch_to.frame(frame_reference)
    frame_reference：iframe标签元素对象

恢复默认页面
    driver.switch_to.default_content()
"""

#导包
import time
from selenium.webdriver.common.by import By
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


# 退出浏览器
time.sleep(3)
quit_driver(driver)
```

#### 11_商品上架-添加商品成功.py

```python
#导包
import random
import time
from selenium.webdriver.common.by import By
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
driver.find_element(By.NAME, "goods_name").send_keys("Jack-Test-1213-001")
# 3.2 商品分类
driver.find_element(By.ID, "cat_id").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#cat_id>[value='12']").click()

driver.find_element(By.ID, "cat_id_2").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#cat_id_2>[value='13']").click()

driver.find_element(By.ID, "cat_id_3").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#cat_id_3>[value='14']").click()

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
```

#### 12_商品上架业务(随机数解决商品名重复+select处理下拉列表).py

```python
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
```

#### 13_下单业务-打开首页+登录成功.py

```python
#导包
import time

from selenium.webdriver.common.by import By

from tools.chromeDriver import get_driver, quit_driver

#获取浏览器驱动
driver = get_driver("https://hmshop-test.itheima.net/index.php/Home/Index/index.html")

# 下单业务
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

#退出浏览器
quit_driver(driver)
```

#### 14_下单业务-下单成功-浏览器操作-多窗口切换.py

```python
"""
浏览器操作
    窗口最大化   dirver.maxmize_window()
    获取标题    dirver.title
    获取网页地址  dirver.current_url
    刷新页面操作  dirver.refresh()
    关闭当前窗口  dirver.close()
    关闭浏览器   dirver.quit()

多窗口切换
    多窗口
        在HTML页面中，当点击超链接或按钮时，有的会在新的窗口打开页面
    窗口切换
        selenium需要通过窗口的句柄来实现窗口的切换！

    切换步骤
        handles = driver.window_handles     #获取所有浏览器已打开的窗口信息(句柄) 返回列表
        driver.switch_to.window(handles[1])     #使用下标处理指定的窗口

注意：
    Selenium只能定位当前窗口中的元素，要定位新的窗口元素就必须进行窗口切换
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

#退出浏览器
quit_driver(driver)
```

#### 15_下单业务-截图保存下单结果页.py

```python
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
```

#### 16_其他APl-alert弹窗处理.py

```python
"""
技术点：alert弹窗处理（属于JS弹框，无法通过元素定位进行处理）
[包括alert(警告框)，confirm(确认框)，prompt(提示框)]
注意：alert弹窗右键之后看不到任何功能快捷操作
操作：
1、切换到alert弹窗
alert = driver.switch_to.alert  #三种弹出框，获取方法一样
2、点击弹窗按钮
alert.accept()
alert.dismiss()     #警告框没有取消按钮，取消一样生效
3、获取弹出框文本
alert.text()



需求：打开注册页面，完成以下操作：
1).点击 alert 按钮
2).关闭警告框
3).输入用户名：admin
项目：http://121.43.169.97:8848/pageA.html
"""
#导包
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://121.43.169.97:8848/pageA.html")

# 1).点击 alert 按钮
# driver.find_element(By.ID,"alerta").click()
# driver.find_element(By.ID,"confirma").click()
driver.find_element(By.ID,"prompta").click()
time.sleep(1)
# 2).关闭警告框
alert = driver.switch_to.alert
# alert.accept()
alert.dismiss()
time.sleep(1)

# 3).输入用户名：admin
driver.find_element(By.ID,"userA").send_keys("13488888888")

time.sleep(3)
driver.quit()
```

#### 17_其他API-浏览器操作.py

```python
"""
    窗口最大化   dirver.maxmize_window()
    获取标题    dirver.title
    获取网页地址  dirver.current_url
    刷新页面操作  dirver.refresh()
    关闭当前窗口  dirver.close()
    关闭浏览器   dirver.quit()
"""

#导包
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建浏览器
driver = webdriver.Chrome()
driver.maximize_window()
# 浏览器窗口最大化
#打开页面
driver.get("https://hmshop-test.itheima.net/Home/Index/index.html")
#获取当前页面标题及URL信息
print(driver.title)
print(driver.current_url)
print("-" * 80)

#首页跳转至登录页并登录
driver.find_element(By.LINK_TEXT, "登录").click()
time.sleep(1)
driver.find_element(By.ID, "username").send_keys("13488888888")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "verify_code").send_keys("8888")
driver.find_element(By.NAME, "sbtbutton").click()

#获取登录成功后页面标题及URL信息
time.sleep(1)
print(driver.title)
print(driver.current_url)
print("-" * 80)

#个人中心跳转至我的浏览页面
driver.find_element(By.LINK_TEXT, "我的浏览").click()
time.sleep(1)

#多窗口处理
handles = driver.window_handles
driver.switch_to.window(handles[1]) #切换到新打开的第二个浏览器页面

#获取当前页面标题及URL信息
time.sleep(1)
print(driver.title)
print(driver.current_url)
print("-" * 80)

#关闭我的浏览页面
time.sleep(2)
driver.close()
time.sleep(3)


#退出浏览器
driver.quit()
```

#### 18其他API-获取页面元素信息.py

```python
"""
获取页面元素信息
    获取元素大小
    element.size
    获取元素文本
    element.text
    获取元素属性值
    element.get_attribute('属性名')
    判断元素是否可用
    element.is_enabled()
    判断元素是否勾选
    element.is_selected)
    判断元素是否可见
    element.is_displayed()
"""

#导包
import time

from selenium.webdriver.common.by import By

from tools.chromeDriver import get_driver,quit_driver

driver = get_driver("https://hmshop-test.itheima.net/Home/user/reg.html")

# 需求
#1）。获取手机号码输入框的大小
print(driver.find_element(By.ID, "username").size)  # 获取元素大小：element.size
#2)，获取页面上第一个span标签的文本内容
print(driver.find_elements(By.TAG_NAME, "span")[0].text) # 获取元素文本：element.text
#3)。获取页面上登录超链接的地址
print(driver.find_element(By.PARTIAL_LINK_TEXT, "登录").get_attribute("href"))
# 获取指定属性的值：element.get_attribute("属性名")

#4）.判断页面中【用户服务协议】是否为选中状态
print(driver.find_element(By.ID, "checktxt").is_selected())
#True：选中，False：未选中
#5）.判断页面中的【同意协议并注册】是否可用
print(driver.find_element(By.LINK_TEXT,"同意协议并注册").is_enabled())
#True：可用，False：不可用


#退出浏览器
time.sleep(3)
quit_driver(driver)
```

#### 19_其他API-js控制滚动条操作.py

```python
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
```

#### 20_其他API-鼠标悬停操作.py

```python
"""
导包          from selenium.webdriver import ActionChains
实例化鼠标对象 action = ActionChains(driver)
调用鼠标方法  action.move_to_element(driver.find_element(By.LINK_TEXT,"服饰"))
执行鼠标操作  action.perform()    #注意：需要执行该语句，鼠标的操作才会真正起作用
"""
#导包
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from tools.chromeDriver import get_driver,quit_driver

#需求：打开商城首页，完成以下操作
driver = get_driver("https://hmshop-test.itheima.net/Home/Index/index.html")

#1）.暂停2s，鼠标悬停【服饰】分类
time.sleep(2)
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.LINK_TEXT,"服饰"))
action.perform()    #注意：需要执行该语句，鼠标的操作才会真正起作用
#2)。暂停2s，查看【服饰】分类下商品信息
time.sleep(2)
driver.find_element(By.LINK_TEXT, "旗袍").click()
time.sleep(2)

#退出浏览器
quit_driver(driver)
```

#### 21_其他API-隐式等待.py

```python
"""
隐式等待(对于整一个页面都起作用)
    定位元素时，如果能定位到元素则直接返回该元素，不触发等待；
    如果不能定位到该元素，则间隔一段时间后再去定位元素；
    如果在达到最大时长时还没有找到指定元素，则抛出元素不存在的异常NoSuchElementException。
    driver.implicitly_wait(timeout)
"""
import time

# 导包
from selenium import webdriver
from selenium.webdriver.common.by import By

# 打开浏览器
driver = webdriver.Chrome()
# 需求：打开注册页面，完成以下操作
#1）最大化窗口
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(10)
#找到元素，不触发等待
#找不到，过一段时间继续去找元素，到达设置最大等待10时间后任然找不到元素，抛出异常NoSuchElementException
driver.get("http://121.43.169.97:8848/pageA.html")
#2)。使用隐式等待定位延时加载输入框，输入admin
driver.find_element(By.ID,"username").send_keys("admin")
time.sleep(1)

#退出浏览器
driver.quit()


# 项目地址:http://121.43.169.97:8848/pageA.html
```

#### 22_其他API-显式等待.py

```python
"""
隐式等待和显示等待对比
                    隐式等待                        显式等待
    作用域        只用设置一次，对全局生效             只对指定元素生效
    抛出异常      NoSuchElementException          TimeOutException
    使用方法    driver.implicitly_wait(timeout)   通过WebDriverWait对象
    其它          必须等待整个页面加载完成             只关注指定元素是否加载

显式等待
    定位指定元素时，如果能定位到元素则直接返回该元素，不触发等待;
    如果不能定位到该元素，则间隔一段时间后再去定位元素；
    如果在达到最大时长时还没有找到指定元素，则抛出超时异常TimeoutException

实现方法
导包              from selenium.webdriver.support.wait import WebDriverWait
创建显示等待类对象   WebDriverWait(driver, timeout, poll_frequency=0.5)
调用utils方法      until(method):直到...时
"""
import time

# 导包
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# 打开浏览器
driver = webdriver.Chrome()
# 需求：打开注册页面，完成以下操作
#1）最大化窗口
driver.maximize_window()
driver.get("http://121.43.169.97:8848/pageA.html")
#2)。使用显式等待定位延时加载输入框，输入admin
#lambda: 匿名函数
WebDriverWait(driver,10,1).until(lambda x:x.find_element(By.ID,"username")).send_keys("admin")
# driver.find_element(By.ID,"username").send_keys("admin")
time.sleep(1)

#退出浏览器
driver.quit()


# 项目地址:http://121.43.169.97:8848/pageA.html
```

#### 23_xpath定位.py

```python
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
```

#### 24 _xpath属性定位.py

```python
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
```

#### 25_拓展-解决浏览器启动慢的问题.py

```python
"""
将浏览器的驱动移动到当前目录内

去chromeDriver文件里面指定驱动路径

"""
```

#### 26_验证码-绕过cookie.py

```python
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
```



## 二、pytest框架

#### test00_login.py

```python
#导包
import time
from sys import executable

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#打开浏览器
service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)
# driver = webdriver.Chrome()
driver.maximize_window()

#打开网页
driver.get("https://hmshop-test.itheima.net/Home/user/login.html")

#页面定位+操作
driver.find_element(By.ID, "username").send_keys("13488888888")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "verify_code").send_keys("8888")
driver.find_element(By.NAME, "sbtbutton").click()

#等待3秒
time.sleep(3)

#退出浏览器
driver.quit()
```

#### test01_Pytest入门案例.py

```python
"""
PyTest是单元测试框架(Unitest是Python自带的测试框架，Pytest更简洁高效)
    1、可以组织多个用例执行
    2、可以实现参数化
    3、断言
    4、生成测试报告

pytest框架安装
    pip install pytest
    pip show python
"""
class TestLogin:
    #类级别前置代码
    def setup_class(self):
        print("我是类级别前置处理，我只执行一次")
    #类级别后置代码
    def teardown_class(self):
        print("我是类级别后置处理，我只执行一次")
    #方法级别前置代码
    def setup_method(self):
        print("我是方法级别前置处理，用例每执行一次我执行一次")
    #方法级别后置代码
    def teardown_method(self):
        print("我是方法级别后置处理，用例每执行一次我执行一次")
    #case01:登录失败(账号为空)
    def test_login01(self):
        print("case01:登录失败(账号为空)")
    #case02:登录失败(密码为空)
    def test_login02(self):
        print("case02:登录失败(密码为空)")
    #case03:登录成功
    def test_login03(self):
        print("case03:登录成功")
```

#### test02_pytest login.py

```python
"""
self作为参数
让driver能在各个类的范围中使用
"""

#导包
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestLogin:
    #类级别前置代码
    def setup_class(self):
        # 打开浏览器
        service = Service(executable_path='chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        # driver = webdriver.Chrome()
        self.driver.maximize_window()
    #类级别后置代码
    def teardown_class(self):
        self.driver.quit()
    #方法级别前置代码
    def setup_method(self):
        # 打开网页
        self.driver.get("https://hmshop-test.itheima.net/Home/user/login.html")
        pass
    #方法级别后置代码
    def teardown_method(self):
        # 等待3秒
        time.sleep(3)
    #case01:登录失败(账号为空)
    def test_login01(self):
        # 页面定位+操作
        self.driver.find_element(By.ID, "username").send_keys("")
        self.driver.find_element(By.ID, "password").send_keys("123456")
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")
        self.driver.find_element(By.NAME, "sbtbutton").click()
    #case02:登录失败(密码为空)
    def test_login02(self):
        # 页面定位+操作
        self.driver.find_element(By.ID, "username").send_keys("13488888888")
        self.driver.find_element(By.ID, "password").send_keys("")
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")
        self.driver.find_element(By.NAME, "sbtbutton").click()
    #case03:登录成功
    def test_login03(self):
        # 页面定位+操作
        self.driver.find_element(By.ID, "username").send_keys("13488888888")
        self.driver.find_element(By.ID, "password").send_keys("123456")
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")
        self.driver.find_element(By.NAME, "sbtbutton").click()
```

#### test03_pytest_login_params.py

```python
"""
技术点：参数化（数据驱动）
    作用：将测试数据和测试脚本分离，后期代码维护焦点放在数据
    使用：装饰器@（不改变方法内部的代码逻辑 新增功能）
        @pytest.mark.parametrize ==》循环遍历测试数据调用测试脚本
    步骤：
    ①准备测试数据，格式:[(),(),(),...]
    ②在被测试方法前面引入装饰器
    @pytest.mark.parametrize("保存数据的变量，注意变量个数=(测试数据中数据的个数)"，测试数据)
    def test_login(self,直接复制装饰器中保存数据的一组变量名即可):
        pass
    ③修改测试方法代码引用变量中的数据完成测试

pytest的两种启动方式：
    1、在pycharm中直接右键运行
    2、在终端中，文件对应的路径上，pytest -s test03_pytest_login_params.py
        在终端中返回的测试用例的结果，成功为点·，错误为e

    3、批量启动方式（配置文件，重点）
        创建一个pytest.ini
            内容：
                [pytest]
                #添加命令行参数
                addopts=-s
                #文件搜索路径
                testpaths=./scripts
                #文件名称
                python_files=test*.py
                #类名称
                python_classes=Test*
                #方法名称
                python_functions=test*

        创建一个scripts放测试用例，根据配置文件命名

引入项目配置文件config.py
os可以有效解决驱动报错问题，驱动路径
    config.py
        import os
        BASE_PATH = os.path.dirname(os.path.abspath(__file__)) #获取当前代码文件所在目录信息
"""

#导包
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

test_data = [
    ("","123456","8888"),
    ("13488888888","","8888"),
    ("13488888888","123456","8888")
]

class TestLogin:
    #类级别前置代码
    def setup_class(self):
        # 打开浏览器
        service = Service(executable_path='chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        # driver = webdriver.Chrome()
        self.driver.maximize_window()
    #类级别后置代码
    def teardown_class(self):
        self.driver.quit()
    #方法级别前置代码
    def setup_method(self):
        # 打开网页
        self.driver.get("https://hmshop-test.itheima.net/Home/user/login.html")
        pass
    #方法级别后置代码
    def teardown_method(self):
        # 等待3秒
        time.sleep(3)
    #case01:登录失败(账号为空)
    @pytest.mark.parametrize("username,password,code", test_data)
    def test_login01(self,username,password,code):
        # 页面定位+操作
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "verify_code").send_keys(code)
        self.driver.find_element(By.NAME, "sbtbutton").click()
```

#### config.py

```python
import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__)) #获取当前代码文件所在目录信息
print(BASE_PATH)

#E:\study\软件测试\UI自动化\Pytest + '\chromedriver.exe'
```

#### pytest.ini

```python
[pytest]
#添加命令行参数
addopts=-s --alluredir report
#文件搜索路径
testpaths=./scripts
#文件名称
python_files=test*.py
#类名称
python_classes=Test*
#方法名称
python_functions=test*
```

#### test04_Allure报告.py

```python
"""
Allure报告
    介绍
        能生成美观易读的报告
        支持多种开发语言，如java、python等
        能快速上手
    操作步骤
        生成测试结果文件(json文件)
        使用allure命令生成在线报告

    1、安装环境
        安装插件：pip install allure-pytest
        验证：pip show allure-pytest
        下载allure：https://github.com/allure-framework/allure2/releases(需要解压到纯英文的路径)
        添加环境变量：点开path，新增，将allure的bin路径复制进去
        确认是否成功添加：allure --version
    2、调整配置文件
        report文件夹没有会自动创建
        在pytest.ini文件里的添加--alluredir report
            #添加命令行参数
            addopts=-s --alluredir report
    3、生成测试报告
        运行测试脚本：pytest
        生成测试报告：allure serve report

"""
```



### scripts包-批量启动

#### test01_Pytest入门案例.py

```python
"""
PyTest是单元测试框架(Unitest是Python自带的测试框架，Pytest更简洁高效)
    1、可以组织多个用例执行
    2、可以实现参数化
    3、断言
    4、生成测试报告

pytest框架安装
    pip install pytest
    pip show python
"""
class HmLogin:
    #类级别前置代码
    def setup_class(self):
        print("我是类级别前置处理，我只执行一次")
    #类级别后置代码
    def teardown_class(self):
        print("我是类级别后置处理，我只执行一次")
    #方法级别前置代码
    def setup_method(self):
        print("我是方法级别前置处理，用例每执行一次我执行一次")
    #方法级别后置代码
    def teardown_method(self):
        print("我是方法级别后置处理，用例每执行一次我执行一次")
    #case01:登录失败(账号为空)
    def test_login01(self):
        print("case01:登录失败(账号为空)")
    #case02:登录失败(密码为空)
    def test_login02(self):
        print("case02:登录失败(密码为空)")
    #case03:登录成功
    def test_login03(self):
        print("case03:登录成功")
```

#### test02_pytest login.py

```python
"""
self作为参数
让driver能在各个类的范围中使用
"""

#导包
import time
import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestLogin:
    #类级别前置代码
    def setup_class(self):
        # 打开浏览器
        service = Service(executable_path=config.BASE_PATH + '/chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        # driver = webdriver.Chrome()
        self.driver.maximize_window()
    #类级别后置代码
    def teardown_class(self):
        self.driver.quit()
    #方法级别前置代码
    def setup_method(self):
        # 打开网页
        self.driver.get("https://hmshop-test.itheima.net/Home/user/login.html")
        pass
    #方法级别后置代码
    def teardown_method(self):
        # 等待3秒
        time.sleep(3)
    #case01:登录失败(账号为空)
    def test_login01(self):
        # 页面定位+操作
        self.driver.find_element(By.ID, "username").send_keys("")
        self.driver.find_element(By.ID, "password").send_keys("123456")
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")
        self.driver.find_element(By.NAME, "sbtbutton").click()
    #case02:登录失败(密码为空)
    def hm_login02(self):
        # 页面定位+操作
        self.driver.find_element(By.ID, "username").send_keys("13488888888")
        self.driver.find_element(By.ID, "password").send_keys("")
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")
        self.driver.find_element(By.NAME, "sbtbutton").click()
    #case03:登录成功
    def hm_login03(self):
        # 页面定位+操作
        self.driver.find_element(By.ID, "username").send_keys("13488888888")
        self.driver.find_element(By.ID, "password").send_keys("123456")
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")
        self.driver.find_element(By.NAME, "sbtbutton").click()
```

#### test02_pytest_login_assert.py

```python
"""
断言:让程序代替人为判断测试程序执行结果是否符合预期结果的过程

学习断言作用：
    提高测试效率
    实现自动化测试(让脚本在无人值守状态下运行)
"""

#导包
import time
import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestLogin:
    #类级别前置代码
    def setup_class(self):
        # 打开浏览器
        service = Service(executable_path=config.BASE_PATH + '/chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        # driver = webdriver.Chrome()
        self.driver.maximize_window()
    #类级别后置代码
    def teardown_class(self):
        self.driver.quit()
    #方法级别前置代码
    def setup_method(self):
        # 打开网页
        self.driver.get("https://hmshop-test.itheima.net/Home/user/login.html")
        pass
    #方法级别后置代码
    def teardown_method(self):
        # 等待3秒
        time.sleep(3)
    #case01:登录失败(账号为空)
    def test_login01(self):
        # 页面定位+操作
        self.driver.find_element(By.ID, "username").send_keys("")
        self.driver.find_element(By.ID, "password").send_keys("123456")
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")
        self.driver.find_element(By.NAME, "sbtbutton").click()
        # 页面等待3秒
        time.sleep(3)
        # 获取账号信息，断言比较，若断言成功则为勾，断言失败则为叉，并给出对比
        # print(self.driver.find_element(By.CLASS_NAME, 'layui-layer-padding').text)
        # assert "用户名不能为空" in self.driver.find_element(By.CLASS_NAME, 'layui-layer-padding').text
        # xpath定位
        print(self.driver.find_element(By.XPATH, '//*[@id="layui-layer1"]/div[2]').text)
        assert "用户名不能为空" in self.driver.find_element(By.XPATH, '//*[@id="layui-layer1"]/div[2]').text

    #case02:登录失败(密码为空)
    def test_login02(self):
        # 页面定位+操作
        self.driver.find_element(By.ID, "username").send_keys("13488888888")
        self.driver.find_element(By.ID, "password").send_keys("")
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")
        self.driver.find_element(By.NAME, "sbtbutton").click()
        # 页面等待3秒
        time.sleep(3)
        # 获取账号信息，断言比较，若断言成功则为勾，断言失败则为叉，并给出对比
        # print(self.driver.find_element(By.CLASS_NAME, 'layui-layer-padding').text)
        # assert "密码不能为空" in self.driver.find_element(By.CLASS_NAME, 'layui-layer-padding').text
        # xpath定位
        print(self.driver.find_element(By.XPATH, '//*[@id="layui-layer1"]/div[2]').text)
        assert "密码不能为空" in self.driver.find_element(By.XPATH, '//*[@id="layui-layer1"]/div[2]').text

    #case03:登录成功
    def test_login03(self):
        # 页面定位+操作
        self.driver.find_element(By.ID, "username").send_keys("13488888888")
        self.driver.find_element(By.ID, "password").send_keys("123456")
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")
        self.driver.find_element(By.NAME, "sbtbutton").click()
        # 页面等待3秒
        time.sleep(3)
        # 获取账号信息，断言比较，若断言成功则为勾，断言失败则为叉，并给出对比
        # print(self.driver.find_element(By.CLASS_NAME, 'userinfo').text)
        # assert "13488888888" == self.driver.find_element(By.CLASS_NAME, 'userinfo').text
        # xpath定位
        print(self.driver.find_element(By.XPATH, '//*[@class="red userinfo"]').text)
        assert "13488888888" == self.driver.find_element(By.XPATH, '//*[@class="red userinfo"]').text
```

#### test03_pytest_login_params.py

```python
#导包
import time
import config
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

test_data = [
    ("","123456","8888"),
    ("13488888888","","8888"),
    ("13488888888","123456","8888")
]

class TestLogin:
    #类级别前置代码
    def setup_class(self):
        # 打开浏览器
        service = Service(executable_path=config.BASE_PATH + '/chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        # driver = webdriver.Chrome()
        self.driver.maximize_window()
    #类级别后置代码
    def teardown_class(self):
        self.driver.quit()
    #方法级别前置代码
    def setup_method(self):
        # 打开网页
        self.driver.get("https://hmshop-test.itheima.net/Home/user/login.html")
        pass
    #方法级别后置代码
    def teardown_method(self):
        # 等待3秒
        time.sleep(3)
    #case01:登录失败(账号为空)
    @pytest.mark.parametrize("username,password,code", test_data)
    def test_login01(self,username,password,code):
        # 页面定位+操作
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "verify_code").send_keys(code)
        self.driver.find_element(By.NAME, "sbtbutton").click()
```

