# 黑马头条



> 注意：
>
> ​	黑马头条APP端软件已经停止维护了，仅有头条自媒体端和后台管理端正常运行。
>
> ​	本次项目用网易新闻APP代替测试。
>
> 黑马头条自媒体端：https://heima-wemedia-java.itheima.net/#/login
>
> ​	账号：demo
>
> ​	密码：842itheima.CN032@.当前日期
>
> 黑马头条后台端口：https://heima-admin-java.itheima.net/#/login
>
> ​	账号：demo
>
> ​	密码：623itheima.CN032@.当前日期
>
> 以下代码,文字,及部分解决办法,皆为视频+本人理解写的笔记记录，用于复习



## 一、项目介绍(了解)



### 1、项目介绍



- **黑马头条**：是由传智播客教育机构研发的一款科技咨询产品，可以发表技术文章和探讨技术交流。

- **项目目标**：

  - 上线运行

  - 从运营产品中孵化课程案例

  - 构建公司数据仓库和算法模型



### 2、项目架构(了解)

```
自媒体：又称个人媒体，是传递信息的新媒体的总称

前端子系统：

​	用户端：app（主要作用：查看文章、问答交流）

​	自媒体运行平台：PC网页（主要作用：发布文章、查看分析粉丝数据）

​	后台管理：PC网页（主要作用：审核文章、运营管理）

后端系统组成部分：

​	推荐系统（负责为用户个性化推荐文章）

​	人工智能（审核文章，保存用户画像）

​	日志系统（保存用户行为数据、系统运行状态数据）

​	爬虫部分（爬取网站数据）
```



### 3、项目技术架构(了解)

![QQ_1758150573995](.\assets\note\QQ_1758150573995.png)

- **负载均衡**：将工作任务分给不同的服务器出来，提高并发处理能力

- **消息列队**：

​		异步处理：业务处理串行变为并行

​		应用解耦：消息生产者不在直接将消息推送到消息使用者

​		流量削锋：避免处理请求消息过大导致系统挂掉

​		日志处理：解决大量日志传输问题



## 二、UI自动化测试



### 1、Selenium Grid介绍

#### 	（1）作用：

​			实现**分布式**测试（解决重复执行测试），解决**兼容性**问题（解决多浏览器兼容性测试）；

#### 	（2）原理：

​			1、Selenium Grid 分布式测试由**一个 hub 主节点**和**若干个 node 代理节点**组成
​			2、Hub 节点用来管理 node 节点注册信息
​			3、脚本 <-> Hub节点 <-> node节点

![QQ_1758152720224](.\assets\note\QQ_1758152720224.png)



> 提示：
>
> ​	Selenium中包含三大组件：Selenium RC、Selenium IDE、Selenium Grid
>
> 重点：
> 	node节点中必须存在脚本代码所需环境（python、selenium、浏览器及驱动）



### 2、Selenium Grid环境部署及节点启动



#### 2.1 下载jar包

> 搭建selenium grid教程网址：https://www.selenium.dev/zh-cn/documentation/grid/getting_started/

- 下载地址：https://github.com/SeleniumHQ/selenium/releases
- 在cmd窗口里输入 pip show selenium，查看selenium版本，根据对应版本下载Selenium Server jar。



#### 2.2 单机部署（Standalone）

**Standalone** 可以将所有 Grid [组件](https://www.selenium.dev/zh-cn/documentation/grid/components/) 无缝地整合成一个单独的实体。在 **Standalone** 模式下运行 Grid，只需一个命令即可获得一个完整的 Grid，并在一个进程中运行。**Standalone** 只能在一台机器上运行。

**Standalone** 模式也是最容易启动 Selenium Grid 的模式。默认情况下，服务器将在 [http://localhost:4444](http://localhost:4444/) 上监听 `RemoteWebDriver` 请求，并且服务器将从系统 [PATH](https://www.selenium.dev/zh-cn/documentation/webdriver/troubleshooting/errors/driver_location/#3-path-环境变量) 中检测可以使用的驱动程序。

```shell
java -jar selenium-server-<version>.jar standalone
```

成功启动 Standalone 模式的 Grid 后，将你的 WebDriver 测试指向 [http://localhost:4444](http://localhost:4444/)。

**Standalone** 的常见用途包括：

- 本地使用 `RemoteWebDriver` 开发或调试测试
- 推送代码之前运行快速测试套件
- 在 CI/CD 工具（GitHub Actions、Jenkins 等）中设置简单的 Grid



#### 2.3 Hub and Node

**Hub和Node**是最常用的角色，因为它允许：

- 将不同的机器组合成一个单一的Grid
  - 例如拥有不同操作系统和/或浏览器版本的机器
- 在不同的环境中运行WebDriver测试有一个单一的入口点
- 在不破坏Grid的情况下增加或减少容量。

##### Hub

一个Hub由以下[组件](https://www.selenium.dev/zh-cn/documentation/grid/components/)组成： 路由器（Router）、分发器（Distributor）、会话映射（Session Map）、新会话队列（New Session Queue）和事件总线（Event Bus）。

```shell
java -jar selenium-server-<version>.jar hub
```

默认情况下，服务器将在 [http://localhost:4444](http://localhost:4444/) 上监听`RemoteWebDriver`请求。

##### Node

在启动时，**Node**将从系统的[`PATH`](https://www.selenium.dev/zh-cn/documentation/webdriver/troubleshooting/errors/driver_location/#3-path-环境变量)中检测可用的驱动程序。

以下命令假设**Node**正在运行的机器与**Hub**在同一台机器上。

```shell
java -jar selenium-server-<version>.jar node
```



- ##### 同一台机器上的多个Node

**Node** 1

```shell
java -jar selenium-server-<version>.jar node --port 5555
```

**Node** 2

```shell
java -jar selenium-server-<version>.jar node --port 6666
```



- ##### 不同机器上的Node和Hub

**Hub**和**Nodes**通过HTTP和[**事件总线**](https://www.selenium.dev/zh-cn/documentation/grid/components/#event-bus)（**事件总线**位于**Hub**内部）进行通信。

**Node**通过事件总线向**Hub**发送消息以开始注册过程。当**Hub**收到消息时，通过HTTP与**Node**联系以确认其存在。

要成功将**Node**注册到**Hub**，重要的是要在**Hub**机器上公开**事件总线**端口（默认为4442和4443）。这也适用于**Node**端口。有了这个，**Hub**和**Node**都能够通信。

如果**Hub**使用默认端口，则可以使用 `--hub` 注册**Node**。

```shell
java -jar selenium-server-<version>.jar node --hub http://<hub-ip>:4444
```

当**Hub**未使用默认端口时，需要使用`--publish-events`和`--subscribe-events`。

例如，如果**Hub**使用端口8886、8887和8888。

```shell
java -jar selenium-server-<version>.jar hub --publish-events tcp://<hub-ip>:8886 --subscribe-events tcp://<hub-ip>:8887 --port 8888
```

**Node**需要使用这些端口才能成功注册。

```shell
java -jar selenium-server-<version>.jar node --publish-events tcp://<hub-ip>:8886 --subscribe-events tcp://<hub-ip>:8887
```



> <hub-ip>指的是hub机注册地址



#### 2.4 案例（python文件test01.py）

> 说明：
>
> ​	1、黑马教程中的Selenium基本是旧版语法，在新版本中，我们通常不再直接写capabilities字典，而是使用Options类。但是，如果你需要设置额外的capabilities（比如设置平台、版本等），可以通过Options对象设置，或者使用`options.set_capability`方法，如下面代码。
>
> ​	2、且在Selenium 4中，版本和平台通常不需要设置，因为Grid会自动选择可用的节点。
>
> 注意：
>
> ​	1、hub和node节点必须正确启动。
>
> ​	2、连接hub中央节点地址可以从hub节点启动窗口复制，ip地址只要是能访间hub节点机器即可(http://192.168.88.1:4444/wd/hub)。

```python
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
```



#### 2.5 多线程(threading)

> 多线程：即便每一个线程中都加了sleep(5)，但是他们依旧同时打印出来，是并发进行的

```python
"""
    目标：
        1、多线程应用
        2、不同浏览器启动参数
"""
from time import sleep


#函数1 说话
def say(name):
    print(f"你好{name}")
    sleep(5)

#函数2 唱歌
def sing(name):
    print(f"{name} 正在唱歌")
    sleep(5)

# 导包
import threading
# 实例化 线程1 线程2
# args=(参数1,参数2...)
t1 = threading.Thread(target=say, args=("张三",))
t2 = threading.Thread(target=say, args=("李四",))
# 启动线程
t1.start()
t2.start()
```



### 3、自动化测试流程

1. 抽取功能用例转化为自动化用例

2. 搭建本机自动化测试环境(python、selenium、pycharm...）

3. 搭建项目目录结构(base、page、scripts、data...)

4. 编写测试脚本

5. 执行测试脚本

6. 生成测试报告

7. 持续集成

   > ◆自动测试开始阶段：在功能测试完成之后
   > ◆自动化测试属于：功能测试
   > ◆自动化测试与功能测试依赖项目环境完全相同



### 4、编写自动化测试用例的原则

1. 自动化测试用例一般只实现**核心业务流程**或者**重复执行率较高**的功能。
2. 自动化测试用例的选择一般以“**正向**”逻辑的验证为主。
3. 不是所有手工用例都可以使用自动化测试来执行。
4. 尽量减少多个用例脚本之间的依赖。
5. 自动化测试用例执行完毕之后，一般需要回归**原点**。



### 5、用例模板

> 视频中的用例模板顺序与下图中有所不同，我根据之前学的内容作了顺序的调整

![QQ_1758184978728](.\assets\note\QQ_1758184978728.png)

#### 1）自媒体登录、发布自动化测试用例编写

![QQ_1760431020717](.\assets\note\QQ_1760431020717.png)

### 6、项目目录搭建（结构）- 登录

```
1、base：所有page页面基类，page页面 公共方法 目录
2、page：页面对象目录
3、scripts：测试脚本
4、image：失败图片存储目录
5、report：测试报告存储目录
6、data：测试数据存储目录
7、log：脚本运行日志存储目录
8、tools：工具类存储目录
```

![QQ_1758464906870](.\assets\note\QQ_1758464906870.png)



#### 1）base结构(装公共方法的目录)

> ==cls==和==self==的区别：
>
> -  cls 代表**类**， self 代表**实例对象**。
>
> pass是占位符。

代码：

```python
import allure
from selenium.webdriver.support.wait import WebDriverWait
from tools.get_log import GetLog

log = GetLog.get_logger()

class Base :

    # 初始化
    def __init__(self, driver):
        log.info(f"正在初始化driver：{driver}！")
        """
        解决driver,将driver变成实例的属性
            因为下面函数还会调用driver，所以必须解决作用域的问题
        """
        self.driver = driver

    # 查找 方法封装
    def base_find(self, loc, timeout=30, poll=0.5):
        # 显示等待
        """
        :param loc: 格式为列表或元组，内容：元素定位信息使用By类
        :param timeout: 查找元素超时时间，默认 30秒
        :param poll: 查找元素频率 默认为0.5
        :return: 元素
        """
        log.info(f"正在查找元素：{loc}！")
        return WebDriverWait(self.driver , timeout ,poll).until(lambda x: x.find_element(*loc))

    # 输入 方法封装
    def base_input(self, loc, value):
        """
        :param loc: 元素的定位信息
        :param value: 要输入的值
        """
        # 1、获取元素
        el = self.base_find(loc)
        # 2、清空操作
        log.info(f"正在对：{loc} 元素执行清空操作！")
        el.clear()
        # 3、输入操作
        log.info(f"正在对：{loc} 元素执行输入：{value} 操作！")
        el.send_keys(value)

    # 点击 方法封装
    def base_click(self, loc):
        """
        :param loc:元素定位信息
        """
        log.info(f"正在对：{loc} 元素执行点击操作！")
        # 获取元素并点击
        self.base_find(loc).click()

    # 获取 元素文本
    def base_get_text(self, loc):
        """
        :param loc: 元素定位信息
        :return: 返回元素的文本值
        """
        log.info(f"正在对：{loc} 元素获取文本操作！获取元素文本：{self.base_find(loc).text}")
        return self.base_find(loc).text

    # 截图
    def base_get_img(self):
        # 一旦出现截图，则说明肯定报错了，所以使用error级别
        log.error("断言出错，正在执行截图操作！")
        # 1、调用截图方法
        self.driver.get_screenshot_as_file("./image/err.png")
        log.error("断言出错，正在将错误图片写入allure报告！")
        # 2、调用图片写入报告方法
        self.__base_write_img()

    # 将图片写入报告方法(私有)
    def __base_write_img(self):
        # 1、获取图片文件流,图片是多媒体文件，以二进制的形式读取
        with open("./image/err.png","rb") as f:
            # 2、调用allure.attach附加方法
            # 三个参数分别为，图片流，文本text，图片类型
            # allure.attach("错误原因:",f.read() , allure.attachment_type.PNG)
            allure.attach(f.read(),"错误原因:",allure.attachment_type.PNG)

    
"""
只要看到 获取 ，就直接在函数体里面写return，
loc，是location的简称，定位的意思
"""

```

![QQ_1758270340548](.\assets\note\QQ_1758270340548.png)

![QQ_1758457876568](.\assets\note\QQ_1758457876568.png)



##### （1）查找元素方法实现(显示等待)：

![QQ_1758275101813](.\assets\note\QQ_1758275101813.png)

> 元素等待：
>
> ​	显示等待（WebDriverWait(self.driver, 10,poll_frequency=0.5).until(lambda x: x.find_element(*loc))）
>
> ​	隐式等待（driver.implicitly_wait(timeout)）
>
> ​	强制等待（time）
>
> 注意：
>
> ​	这里find_element()里面用元组或列表代表，是因为这个公共方法是需要在多个地方用的，让其可以更灵活的变换方法
>
> ​	在代码前后加括号，可以在代码中间处换行而不改变其代码意义 





#### 2）page目录结构(页面对象层)

#####  （1）page_mp_login

```
取名方法：page_子系统简称_模块名
```

- page_mp_login.py

```python
from time import sleep
from base.base import Base
import page
from tools.get_log import GetLog

log = GetLog.get_logger()

class PageMpLogin(Base):
    # 输入用户名
    def page_input_username(self,username):
        # 调用父类中输入方法
        self.base_input(page.mp_username,username)

    # 输入密码
    def page_input_password(self,password):
        # 调用父类中输入方法
        self.base_input(page.mp_password,password)

    # 点击登录按钮
    def page_click_login_btn(self):
        # 解决电脑浏览器加载过快，而服务器的登录按钮还没显示就已经完成脚本任务导致的报错
        sleep(1)
        # 调用父类中点击方法
        self.base_click(page.mp_login_bt)

    # 获取名称封装
    def page_get_nickname(self):
        # 调用父类获取文本方法
        return self.base_get_text(page.mp_nickname)

    # 组合业务方法
    def page_mp_login(self, username, password):
        log.info(f"正在调用自媒体登录业务方法，用户名：{username} 密码：{password}")
        """提示：调用相同页面操作步骤，跨页面暂时不考虑"""
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()
```

![QQ_1758346692005](.\assets\note\QQ_1758346692005.png)

![QQ_1758356541156](.\assets\note\QQ_1758356541156.png)

##### （2）统一入口类编写

**page_in.py**

```python
from page.page_mp_login import PageMpLogin


class PageIn:
    def __init__(self, driver):
        self.driver = driver

    # 获取PageMpLogin对象
    def page_get_PageMpLogin(self):
        return PageMpLogin(self.driver)
```

- **凡是page中有的类对象，都要在统一入口类里面获取其对应的对象。**



##### （3）元素配置信息整理

```python
#文件名：__init__.py
#用这个方法来整理元素配置信息的好处：包名.元素配置信息，可以直接引用

"""
注意：元组
mp_nickname = (By.CSS_SELECTOR, ".user-name")
若元组只有两个参数
无论你写不写括号都是元组例如：
mp_nickname = By.CSS_SELECTOR, ".user-name"
"""
```

```python
from selenium.webdriver.common.by import By

"""以下数据为自媒体、后台管理url"""
#自媒体url
url_mp = "https://heima-wemedia-java.itheima.net/#/login"
#后台管理url
url_mis = "https://heima-admin-java.itheima.net/#/login"

"""以下为自媒体模块配置数据,元组或列表格式"""

# 用户名
mp_username = (By.CSS_SELECTOR, "[type = 'text']")
# 密码
mp_password = (By.CSS_SELECTOR, "[type = 'password']")
# 登录按钮
mp_login_bt = (By.CSS_SELECTOR, ".el-button")
# 名称
mp_nickname = (By.CSS_SELECTOR, ".user-name")
```

![QQ_1758348776135](.\assets\note\QQ_1758348776135.png)



#### 3）scripts(测试脚本业务层)

##### （1）test01_mp_login.py

```python
import pytest
from page.page_in import PageIn
from tools.get_driver import GetDriver
import page
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestMpLogin:
    # 初始化
    def setup_class(self):
        #1、获取driver
        driver = GetDriver.get_web_driver(page.url_mp)
        #2、通过统一入口类获取PageMpLogin对象
        self.mp = PageIn(driver).page_get_PageMpLogin()

    # 结束
    def teardown_class(self):
        # 调用关闭driver
        GetDriver.quit_web_driver()

    # 测试业务方法
    @pytest.mark.parametrize("username,password,expect", read_yaml("mp_login.yaml"))
    def test_mp_login(self, username, password, expect):
        # 调用登录业务方法
        self.mp.page_mp_login(username, password)
        try:
            # 断言
            assert expect == self.mp.page_get_nickname()
        except Exception as e:
            log.error(f"断言出错，错误信息：{e}")
            #输出错误信息
            print("错误原因：", e)
            #截图
            self.mp.base_get_img()
            #抛异常
            raise
```



- **异常回顾**(用于断言失败异常捕获及截图报告)

```python
"""
异常的概念：
    程序在运行时，如果Python解释器遇到到一个错误，则会停止程序的执行，并且提示一些错误信息，这就是异常.
    程序停止执行并且提示错误信息这个动作，通常称之为：抛出（raise）异常

提示：
    程序开发时，很难将所有的特殊情况都处理的面面俱到，通过异常捕获可以针对突发事件做集中的处理，
    从而保证程序的稳定性和健壮性，在自动化测试过程中，也可以借助捕获异常操作，完成类似：
    用例执行报错时截图、打印日志信息等操作

捕获异常有两种：
    捕获特定异常类型
        try:
            #尝试执行的代码
        except 异常类型(举例：ValueError，ZeroDivisionError):
            #出现异常时执行的代码

    捕获未知类型异常(重要)
        try:
            #尝试执行的代码
        except Exception as e:
            #出现异常时执行的代码
            print('异常信息为: {}'.format(e))

    说明：
        如果希望程序无论出现任何错误，都不会因为Python解释器抛出异常而被终止，可以捕获Exception
        exceptException as e:e表示捕获到的异常对象，记录异常的错误信息，e为惯用变量名，可以自定义

需求：
提示用户输入一个整数
使用8除以用户输入的整数并且输出
要求：为了简化代码，统一捕获所有异常类型
"""

#以下为捕获未知类型异常的操作
try:
    num1 = int(input("请输入一个整数："))
    num2 = 8 / num1
    print(num2)
except Exception as e:
    print('异常信息为: {}'.format(e))   #打印异常
    #raise "程序出错了"  #抛出异常
finally:
    print("程序结束")
```



![QQ_1758358342775](.\assets\note\QQ_1758358342775.png)

![QQ_1758447697565](.\assets\note\QQ_1758447697565.png)

![QQ_1758456159497](.\assets\note\QQ_1758456159497.png)

##### （2）__init _.py(文件)

```
文件名：__init__.py
```

```python
import sys
import os
sys.path.append(os.getcwd())
#意思是。在系统path路径里面追加(append)，os系统当前所在的相对路径
```

- 将 sys.path.append(os.getcwd())写在此处，能避免多次编写问题
  - 之后pytest测试的每一个测试脚本，都会自动调用这个文件

```
如果不写这两个包，直接使用pytest，会报错，报错内容为导入其他包错误
```



#### 4）tools(工具类)

##### （1）获取driver和退出driver

- **get_driver.py**

```python
from selenium import webdriver

class GetDriver:
    # 1、声明变量
    # 避免类名.可以调用driver，所以__变私有，受保护，避免调用失误
    __web_driver = None

    # 2、获取driver方法
    # @classmethod 类方法
    @classmethod
    def get_web_driver(cls, url):
        # 判断是否为空
        if cls.__web_driver is None:
            #设置driver操作
            #获取浏览器
            cls.__web_driver = webdriver.Chrome()
            #最大化浏览器
            cls.__web_driver.maximize_window()
            #打开url
            cls.__web_driver.get(url)
        #返回driver
        return cls.__web_driver

    # 3、退出driver方法
    @classmethod
    def quit_web_driver(cls):
        #判断driver不为空
        if cls.__web_driver:
            #退出操作
            cls.__web_driver.quit()
            #置空操作 重点-->上面一步虽然把driver对象清空了
            #   但是driver在内层中的地址还没有清空，所以需要置空操作
            cls.__web_driver = None
```

![QQ_1758438408854](.\assets\note\QQ_1758438408854.png)



##### （2）read_yaml.py

```python
import os
import yaml
from config import BASE_PATH

# 定义函数
def read_yaml(filename):
    file_path = BASE_PATH + os.sep + "data" + os.sep + filename
    # 定义空列表 组装测试数据
    arr = []
    # 获取文件流
    with open(file_path,"r", encoding="utf-8") as f:
        # 遍历 调用yaml.safe_load(f).values()方法
        for datas in yaml.safe_load(f).values():
            #arr.append(datas.values()) 这种格式追加给arr的数据为列表嵌套列表
            #强转元组，成列表嵌套元组
            arr.append(tuple(datas.values()))
    # 返回 结果
    return arr

#验证下结果
"""
回顾：
    程序入口:__name__=='__main__'
    (作用：该语句出现后，程序就不会自上而下运行了，它会规定先执行程序入口的内容，再执行其他内容）
    快捷写法：直接打一个main然后tab即可
"""

if __name__ == "__main__":
    print(read_yaml("mp_login.yaml"))

```



##### （3）get_log.py(获取日志)

```python
# 导包
import logging.handlers
import os
from config import BASE_PATH


# 新建 类
class GetLog:

    # 新建一个日志变量
    __logger = None
    # 新建获取日志器的方法
    @classmethod
    def get_logger(cls):
        # 判断日志器是否为空：
        if cls.__logger is None:
            # 获取日志器
            cls.__logger = logging.getLogger()
            # 修改默认级别
            cls.__logger.setLevel(logging.INFO)
            log_path = BASE_PATH + os.sep + "log" + os.sep + "hmtt.log"
            # 获取处理器
            th = logging.handlers.TimedRotatingFileHandler(filename=log_path,
                                                           when="MIDNIGHT",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding="utf-8")
            # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器中
            th.setFormatter(fm)
            # 将处理器添加到日志器中
            cls.__logger.addHandler(th)
        # 返回日志器
        return cls.__logger

# 测试一下
#if __name__ == '__main__':
#    log = GetLog.get_logger()
#    log.info("测试信息级别日志")
#    log.error("测试错误级别")
#现在测试没有模块，所以会报错
#工作中没必要记忆，用的时候，复制封装的方法即可


#我们在常用的测试里面就用两个级别:
#	一个是info,记录程序运行的步骤
#	一个是error,记录程序运行的错误

```

![QQ_1758462197559](.\assets\note\QQ_1758462197559.png)

![QQ_1758463635722](.\assets\note\QQ_1758463635722.png)



#### 5）pytest.ini(文件，在根目录下)

- **pytest.ini**

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

![QQ_1758440924842](.\assets\note\QQ_1758440924842.png)



#### 6）config.py(文件，在根目录下)

```python
#os可以有效解决驱动报错问题，驱动路径
import os

BASE_PATH = os.path.dirname(__file__) #获取当前代码文件所在目录信息

# print(BASE_PATH)
# E:\study\AutoTest_HMTT

# print(os.sep)
# \
```



- 用于参数化（引用**UI自动化学习的笔记**，复习）：

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



#### 7）data（数据包，参数化数据）

- **mp_login.yaml**

```python
mp_login001:
    username: "demo"
    password: "842itheima.CN032@.20250921"
    expect: "demo"
```



#### 8）image(断言失败图片目录)

- 这里给的截图是断言报告的图片，下面那个错误原因里面的图片是image存放的err图

![QQ_1758457586499](.\assets\note\QQ_1758457586499.png)



#### 9）report(测试报告)

- 该目录里面存放allure server report产生的测试报告文件

![QQ_1758457796134](.\assets\note\QQ_1758457796134-1758457826531-13.png)



#### 10）log(存放日志处)



### 7 、自媒体发布文章用例

![QQ_1760431020717](.\assets\note\QQ_1760431020717-1760431248160-5.png)

```
和黑马20年的视频有所不同的是:
	25年黑马头条的自媒体端网站发布文章没有iframe元素切换的环节,即网站没有写iframe元素
	且流程也有所不同,以以下流程为准

流程:
	1、登录
	2、点击发布文章
	3、输入标题
	4、输入内容
	5、输入标签
	6、选择频道
	7、选择发布时间
	8、选择封面
	9、点击发布
	
说明:
	1、依赖登录方法(在PageMpLogin单独封装中实现)
	2、实现本条用例Base 需新增 选择频道方法
	（网站没有iframe元素，了解下面内容）
	3、输入文章注意:
		a)切换iframe(根据iframe元素切换)
		b)输入内容
		c)回到默认目录(跳出当前iframe)
		
```



#### 1）base查找频道方法封装

- web_base.py

```python
from time import sleep
from selenium.webdriver.common.by import By
from base.base import Base
from tools.get_log import GetLog

log = GetLog.get_logger()

#继承Base
class WebBase(Base):
    """以下为web项目专属方法"""
    #根据显示文本点击指定元素
    def web_base_click_element(self, placeholder_text, click_text):
        # 1、点击父选框
        loc = By.CSS_SELECTOR, "[placeholder= '{}']".format(placeholder_text)
        log.info(f"正在对：{loc} 元素执行点击操作！")
        self.base_click(loc)
        # 2、暂停
        sleep(1)
        # 3、点击包含显示文本的元素
        loc = By.XPATH, "//*[contains(text(),'{}')]".format(click_text)
        log.info(f"正在对：{loc} 元素执行点击操作！")
        self.base_click(loc)
```

##### a）回顾xpath定位

###### 23_xpath定位.py

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

###### 24 _xpath属性定位.py

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

![QQ_1758887711694](.\assets\note\QQ_1758887711694.png)



#### 2）依赖登录方法实现，发布文章页面操作

##### a）依赖登录方法实现，Base改为WebBase

- page/page_mp_login.py

```python
from time import sleep
import page
from base.web_base import WebBase
from tools.get_log import GetLog

log = GetLog.get_logger()

#修改继承类
class PageMpLogin(WebBase):
    # 输入用户名
    def page_input_username(self,username):
        # 调用父类中输入方法
        self.base_input(page.mp_username,username)

    # 输入密码
    def page_input_password(self,password):
        # 调用父类中输入方法
        self.base_input(page.mp_password,password)

    # 点击登录按钮
    def page_click_login_btn(self):
        # 解决电脑浏览器加载过快，而服务器的登录按钮还没显示就已经完成脚本任务导致的报错
        sleep(1)
        # 调用父类中点击方法
        self.base_click(page.mp_login_bt)

    # 获取名称封装
    def page_get_nickname(self):
        # 调用父类获取文本方法
        return self.base_get_text(page.mp_nickname)

    # 组合业务方法 -> 测试脚本层调用
    def page_mp_login(self, username, password):
        log.info(f"正在调用自媒体登录业务方法，用户名：{username} 密码：{password}")
        """提示：调用相同页面操作步骤，跨页面暂时不考虑"""
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()

    # 新加的
    # 组合业务方法 -> 发布文章依赖使用
    def page_mp_login_success(self, username, password):
        log.info(f"正在调用自媒体登录业务方法，用户名：{username} 密码：{password}")
        """提示：调用相同页面操作步骤，跨页面暂时不考虑"""
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()
```

##### b）发布文章页面操作，注意iframe切换

- page/page_mp_article.py

```python
from base.web_base import WebBase


class PageMpArticle(WebBase):
    # 点击 发布文章
    def page_click_publish_article(self):
        pass

    # 输入 标题
    def page_input_title(self):
        pass

    # 输入 内容
    def page_input_content(self):
        """
        如果有iframe结构的话
        1、切换iframe

        3、回到默认目录
        """
        # 2、输入内容


        pass

    # 输入 标签
    def page_input_tag(self):
        pass

    # 选择 频道
    def page_click_channel(self):
        # 调用WebBase封装方法
        pass

    # 选择 定时发布-即刻
    def page_click_publish_timing(self):
        pass

    # 选择封面
    def page_click_cover(self):
        pass

    # 点击 发表按钮
    def page_click_submit(self):
        pass

    # 获取 发表提示信息
    def page_get_info(self):
        pass

    # 组合发布文章业务方法
    def page_mp_article(self):
        pass
```



#### 3）页面元素配置信息整理

- page/init.py

```python
from selenium.webdriver.common.by import By

"""以下数据为自媒体、后台管理url"""
#自媒体url
url_mp = "https://heima-wemedia-java.itheima.net/#/login"
#后台管理url
url_mis = "https://heima-admin-java.itheima.net/#/login"

"""以下为自媒体模块配置数据,元组或列表格式"""

# 用户名
mp_username = (By.CSS_SELECTOR, "[type = 'text']")
# 密码
mp_password = (By.CSS_SELECTOR, "[type = 'password']")
# 登录按钮
mp_login_bt = (By.CSS_SELECTOR, ".el-button")
# 名称
mp_nickname = (By.CSS_SELECTOR, ".user-name")

# 发布文章 XPATH文本包含语法
# 另一种 等于语法 //span[text()='发布文章']
mp_publish_article = By.XPATH, "//*[contains(text(),'发布文章')]"
# 文章标题 能用CSS，就不要用XPATH
mp_title = By.CSS_SELECTOR, "[placeholder='请在这里输入标题']"
"""
若有iframe页面切换的情况下，iframe
mp_iframe = By.CSS_SELECTOR, ".iframe"
"""
# 编辑内容按钮
mp_content_bt = By.CSS_SELECTOR, "[title='编辑内容']"
# 文章内容 正常来说，定位到body，不要定位到段落p标签，这里网站只有个div写内容，所以定位到div
mp_content = By.CSS_SELECTOR, ".el-textarea__inner"
# 文章标签
mp_tag = By.CSS_SELECTOR, "[placeholder='请输入标签']"
# 文章定时发布时间
mp_time = By.CSS_SELECTOR, "[placeholder='请选择日期时间']"
# 定时发布时间-此刻
mp_time_now = By.CSS_SELECTOR, ".el-button--text"
# 封面
mp_cover = By.XPATH, "//*[text()='自动']/.."
# 提交审核
mp_submit = By.XPATH, "//*[contains(text(),'提交审核')]/.."
# 结果
mp_result = By.XPATH, "//*[contains(text(),'新增文章成功')]"

```

> 1、切换iframe框架，使用元素切换（未加载时激活显示等待）
> 2、输入文章元素定位到body



#### 4）页面结构方法实现，统一入口类

##### a）页面结构方法实现

- page_mp_article.py

```python
from time import sleep
from base.web_base import WebBase
import page
from page import mp_content_bt


class PageMpArticle(WebBase):
    # 点击 发布文章
    def page_click_publish_article(self):
        sleep(1)
        self.base_click(page.mp_publish_article)

    # 输入 标题
    def page_input_title(self, title):
        sleep(2)
        self.base_input(page.mp_title, title)


    # 输入 内容
    def page_input_content(self, content):
        """
        如果有iframe结构的话
        1、切换iframe
        iframe = self.base_find(page.mp_iframe)
        self.driver.switch_to.frame(iframe)
        2、输入内容
        self.base_input(page.mp_content, content)
        3、回到默认目录
        self.driver.switch_to.default_content()
        """

        """
        黑马2025年头条的输入内容页面有点特殊，无法直接输入，
            需要先将鼠标悬停在输入框上，然后点了编辑内容按钮，弹出框才能输入
            但视频里面是没这个情况的，在这种项目结构里面我暂时不知道怎么解决
            所以把输入内容注释掉了
        """
        # 1、点击编辑内容按钮
        self.base_click(mp_content_bt)
        # 2、暂停
        sleep(1)
        # 3、输入内容
        self.base_input(page.mp_content, content)

    # 输入 标签
    def page_input_tag(self, tag):
        self.base_input(page.mp_tag, tag)
        sleep(1)

    # 选择 频道
    def page_click_channel(self):
        # 调用WebBase封装方法
        self.web_base_click_element(placeholder_text="请选择频道",click_text="大数据")

    # 选择 定时发布-即刻
    def page_click_publish_timing(self):
        self.web_base_click_element(placeholder_text="请选择日期时间", click_text="此刻")

    # 选择封面
    def page_click_cover(self):
        self.base_click(page.mp_cover)

    # 点击 发表按钮
    def page_click_submit(self):
        self.base_click(page.mp_submit)

    # 获取 发表提示信息
    def page_get_info(self):
        return self.base_get_text(page.mp_result)

    # 组合发布文章业务方法
    def page_mp_article(self,title,tag):
        self.page_click_publish_article()
        self.page_input_title(title)
        #self.page_input_content(content)
        self.page_input_tag(tag)
        self.page_click_channel()
        self.page_click_publish_timing()
        self.page_click_cover()
        self.page_click_submit()
```



##### b）统一入口类

- page_in.py

```python
from page.page_mp_article import PageMpArticle
from page.page_mp_login import PageMpLogin


class PageIn:
    def __init__(self, driver):
        self.driver = driver

    # 获取PageMpLogin对象
    def page_get_PageMpLogin(self):
        return PageMpLogin(self.driver)

    # 获取PageMpArticle对象
    def page_get_PageMpArticle(self):
        return PageMpArticle(self.driver)
```



#### 5）测试脚本实现，初次运行bug调试

- scripts/test02_mp_article.py

```python
import pytest
import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()

class TestMpArticle:
    #1、初始化
    def setup_class(self):
        """
        1、要获取driver，原因：获取统一入口类的时候必须传入driver
        2、统一入口类里面是继承了base的？
        3、要统一入口类，原因：PageMpLogin和PageMpArticle两个对象的获取在统一入口类PageIn中
        """
        # 1、获取driver
        driver = GetDriver.get_web_driver(page.url_mp)
        # 2、获取统一入口类对象
        self.page_in = PageIn(driver)
        # 3、获取PageMpLogin对象并调用成功登录的依赖方法
        self.page_in.page_get_PageMpLogin().page_mp_login_success('demo','842itheima.CN032@.20251013')
        # 4、获取PageMpArticle页面对象
        self.article = self.page_in.page_get_PageMpArticle()


    # 2、结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_web_driver()

    # 3、测试发布文章方法
    @pytest.mark.parametrize("title,tag,expect", read_yaml("mp_article.yaml"))
    def test_mp_article(self,title,tag,expect):
        # 调用发布文章业务方法
        self.article.page_mp_article(title,tag)
        try:
            # 查看断言信息
            assert expect == self.article.page_get_info()
        except Exception as e:
        # 使用所有的基类异常，重命名错误信息为e
            #日志(有三个地方需要标注，base，page，scripts)
            log.eroor(e)
            #截图
            self.article.base_get_img()
            #抛异常
            raise
```





### 8、后台管理登录用例

#### 1）业务分析、登录按钮设置

![QQ_1760431396799](.\assets\note\QQ_1760431396799.png)

![老版登录页面](.\assets\note\QQ_1760432039377.png)

![新版登录页面](.\assets\note\QQ_1760432122279.png)

```
1)后台管理https://heima-admin-java.itheima.net/#/login
2)登录账号：demo
3)登录密码：623itheima.CN032@.20251014

4)js设置disabled属性失效,用cookie也可以解决，
(这个是老版页面有的一个登录问题，需要通过验证码，验证通过后会将登录按钮的disabled属性设为false
这个时候我们才可以点击登录，而为了跳过这个过程，我们可以直接用JS将语句修改为false)
js 代码:document.getElementById("inp1").disabled=false

二、业务：
1)输入账号
2)输入密码
3)点击登录按钮
4)获取昵称

分析思路：
	先分析page页面需要用的base公共方法有没有，如果没有则补充
	然后搭建后台管理登录的page页面结构搭建
```



#### 2）page结构搭建、统一入口类管理page对象

##### a）page结构搭建

- page/page_mis_login.py

```python
from base.web_base import WebBase


class PageMisLogin(WebBase):
    # 1、输入用户名
    def page_input_username(self):
        pass

    # 2、输入密码
    def page_input_password(self):
        pass

    # 3、点击登录按钮
    def page_click_login_btn(self):
        pass

    # 4、获取名称封装
    def page_get_nickname(self):
        pass

    # 5、组合后台管理登录业务方法
    def page_mis_login(self):
        pass
```



##### b）统一入口管理page对象

- page/page_in.py

```python
from page.page_mis_login import PageMisLogin
from page.page_mp_article import PageMpArticle
from page.page_mp_login import PageMpLogin


class PageIn:
    def __init__(self, driver):
        self.driver = driver

    # 获取PageMpLogin对象
    def page_get_PageMpLogin(self):
        return PageMpLogin(self.driver)

    # 获取PageMpArticle对象
    def page_get_PageMpArticle(self):
        return PageMpArticle(self.driver)

    # 获取PageMisLogin对象
    def page_get_PageMisLogin(self):
        return PageMisLogin(self.driver)
```



#### 3）page页面元素配置信息整理、页面方法具体实现

##### a）page页面元素配置信息整理

- page/_init__.py

```python
from selenium.webdriver.common.by import By

"""以下数据为自媒体、后台管理url"""
#自媒体url
url_mp = "https://heima-wemedia-java.itheima.net/#/login"
#后台管理url
url_mis = "https://heima-admin-java.itheima.net/#/login"

"""以下为自媒体模块配置数据,元组或列表格式"""

# 用户名
mp_username = (By.CSS_SELECTOR, "[type = 'text']")
# 密码
mp_password = (By.CSS_SELECTOR, "[type = 'password']")
# 登录按钮
mp_login_bt = (By.CSS_SELECTOR, ".el-button")
# 名称
mp_nickname = (By.CSS_SELECTOR, ".user-name")

# 发布文章 XPATH文本包含语法
# 另一种 等于语法 //span[text()='发布文章']
mp_publish_article = By.XPATH, "//*[contains(text(),'发布文章')]"
# 文章标题 能用CSS，就不要用XPATH
mp_title = By.CSS_SELECTOR, "[placeholder='请在这里输入标题']"
"""
若有iframe页面切换的情况下，iframe
mp_iframe = By.CSS_SELECTOR, ".iframe"
"""
# 编辑内容按钮
mp_content_bt = By.CSS_SELECTOR, "[title='编辑内容']"
# 文章内容 正常来说，定位到body，不要定位到段落p标签，这里网站只有个div写内容，所以定位到div
mp_content = By.CSS_SELECTOR, ".el-textarea__inner"
# 文章标签
mp_tag = By.CSS_SELECTOR, "[placeholder='请输入标签']"
# 文章定时发布时间
mp_time = By.CSS_SELECTOR, "[placeholder='请选择日期时间']"
# 定时发布时间-此刻
mp_time_now = By.CSS_SELECTOR, ".el-button--text"
# 封面
mp_cover = By.XPATH, "//*[text()='自动']/.."
# 提交审核
mp_submit = By.XPATH, "//*[contains(text(),'提交审核')]/.."
# 结果
mp_result = By.XPATH, "//*[contains(text(),'新增文章成功')]"


"""以下配置信息为后台管理系统"""
# 用户名
mis_username = By.CSS_SELECTOR, "[type='text']"
# 密码
mis_pwd = By.CSS_SELECTOR, "[type='password']"
# 登录按钮
mis_login_btn = By.CSS_SELECTOR, ".el-button"
# 昵称
mis_nickname = By.CSS_SELECTOR, ".user-name"
```



##### b）页面方法具体实现

- page/page_mis_login.py

```python
import page
from base.web_base import WebBase


class PageMisLogin(WebBase):
    # 1、输入用户名
    def page_input_username(self,username):
        self.base_input(page.mis_username,username)

    # 2、输入密码
    def page_input_password(self,pwd):
        self.base_input(page.mis_pwd,pwd)

    # 3、点击登录按钮
    def page_click_login_btn(self):
        """
        如果登录按钮是有个disabled属性在控制按钮的可用性的情况下，
            且需验证通过才会将disabled设置为false，然后按钮为可用。
                这种情况可用JS直接修改属性
        #1、处理JS
        js = "document.getElementById('inpl').disabled=false"
        self.driver.execute_script(js)
        """
        #2、调用点击操作
        self.base_click(page.mis_login_btn)

    # 4、获取昵称封装
    def page_get_nickname(self):
        return self.base_get_text(page.mis_nickname)

    # 5、组合后台管理登录业务方法
    def page_mis_login(self,username,pwd):
        self.page_input_username(username)
        self.page_input_password(pwd)
        self.page_click_login_btn()
```



#### 4）scripts结构搭建

- scripts/test03_mis_login.py

```python
import page
from page.page_in import PageIn
from tools.get_driver import GetDriver


class TestMisLogin:
    # 1、初始化
    def setup_class(self):
        # 1、获取driver
        driver = GetDriver.get_web_driver(page.url_mis)
        # 2、通过统一入口类对象获取PageMisLogin对象
        self.mis = PageIn(driver).page_get_PageMisLogin()

    # 2、结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_web_driver()

    # 3、登录测试业务方法
    def test_mis_login(self,username="demo",pwd="623itheima.CN032@.20251017"):
        # 1、调用登录业务方法
        self.mis.page_mis_login(username,pwd)
        # 2、调式断言信息
        print("获取的昵称为：", self.mis.page_get_nickname())
```



#### 5）断言及捕获处理、参数化

##### a）断言及捕获处理

- page/page_mis_login.py

```python
import page
from base.web_base import WebBase
from tools.get_log import GetLog

log = GetLog.get_logger()

class PageMisLogin(WebBase):
    # 1、输入用户名
    def page_input_username(self,username):
        self.base_input(page.mis_username,username)

    # 2、输入密码
    def page_input_password(self,pwd):
        self.base_input(page.mis_pwd,pwd)

    # 3、点击登录按钮
    def page_click_login_btn(self):
        """
        如果登录按钮是有个disabled属性在控制按钮的可用性的情况下，
            且需验证通过才会将disabled设置为false，然后按钮为可用。
                这种情况可用JS直接修改属性
        #1、处理JS
        js = "document.getElementById('inpl').disabled=false"
        self.driver.execute_script(js)
        """
        #2、调用点击操作
        self.base_click(page.mis_login_btn)

    # 4、获取昵称封装
    def page_get_nickname(self):
        return self.base_get_text(page.mis_nickname)

    # 5、组合后台管理登录业务方法
    def page_mis_login(self,username,pwd):
        log.info("正在调用后台管理系统登录业务方法，用户名：{} 密码：{}".format(username, pwd))
        self.page_input_username(username)
        self.page_input_password(pwd)
        self.page_click_login_btn()
```

- scripts/test03_mis_login.py

```python
import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog

log = GetLog.get_logger()

class TestMisLogin:
    # 1、初始化
    def setup_class(self):
        # 1、获取driver
        driver = GetDriver.get_web_driver(page.url_mis)
        # 2、通过统一入口类对象获取PageMisLogin对象
        self.mis = PageIn(driver).page_get_PageMisLogin()

    # 2、结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_web_driver()

    # 3、登录测试业务方法
    def test_mis_login(self,username="demo",pwd="623itheima.CN032@.20251017",expect="demo"):
        # 1、调用登录业务方法
        self.mis.page_mis_login(username,pwd)
        try:
            # 2、调式断言信息
            assert expect in self.mis.page_get_nickname()
        except Exception as e:
        # 使用所有的基类异常，重命名错误信息为e
            #日志(有三个地方需要标注，base，page，scripts，但后台管理无新增base方法，所以无需标注base)
            log.eroor(e)
            #截图
            self.mis.base_get_img()
            #抛异常
            raise
```



##### b）参数化

- data/mis_login.yaml

```
mis_login001:
  username: "demo"
  pwd: "623itheima.CN032@.20251017"
  expect: "demo"
```

- scripts/test03_mis_login.py

```python
import pytest
import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()

class TestMisLogin:
    # 1、初始化
    def setup_class(self):
        # 1、获取driver
        driver = GetDriver.get_web_driver(page.url_mis)
        # 2、通过统一入口类对象获取PageMisLogin对象
        self.mis = PageIn(driver).page_get_PageMisLogin()

    # 2、结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_web_driver()

    # 3、登录测试业务方法
    @pytest.mark.parametrize("username,pwd,expect",read_yaml("mis_login.yaml"))
    def test_mis_login(self,username,pwd,expect):
        # 1、调用登录业务方法
        self.mis.page_mis_login(username,pwd)
        try:
            # 2、调式断言信息
            assert expect in self.mis.page_get_nickname()
        except Exception as e:
        # 使用所有的基类异常，重命名错误信息为e
            #日志(有三个地方需要标注，base，page，scripts，但后台管理无新增base方法，所以无需标注base)
            log.eroor(e)
            #截图
            self.mis.base_get_img()
            #抛异常
            raise

```



### 9、后台管理审核文章用例

![QQ_1760431396799](.\assets\note\QQ_1760431396799.png)

#### 1）page页面结构搭建，统一入口类管理页面对象

#### a）page页面结构搭建



#### b）统一入口类管理页面对象
