# ==一、接口的引入==



# 接口

## 概念

- **接口就是：系统与系统之间，组件与组件之间，数据传递交互的通道。**

  ![image-20210707093347808](./assets/image-20210707093347808.png)

## 接口的类型

- 按协议划分：http、tcp、IP 

- 按语言划分：C++、java、php 。。。

- **按范围划分：**

  - **系统之间：**

    - **多个内部系统之间**
    - **内部系统与外部系统之间**

    ![image-20210707094113199](./assets/image-20210707094113199.png)

  - **程序之间：**

    - **方法与方法之间，函数与函数之间，模块与模块之间**

      ```python
      # 接口
      def eat(something):
          print(f'小鸟在吃{something}')
      
      # 使用接口，传递数据
      def bird():
          eat('苹果')
      
      bird()
      ```

# 接口测试（测服务器端）

## 概念

- **接口测试就是，对系统或组件之间的接口进行测试。校验传递的数据正确性和逻辑依赖关系的正确性！(例如，你想要查看订单，就必须先登录的，这种逻辑依赖关系，总结来说，就是测数据和逻辑依赖是否正确)**

**原理**

- **==接口测试，主要针对的测试目标 —— 服务器==**

- 怎么测？
  - 模拟客户端，向服务器发送请求。
- 用什么测？
  - 工具：fiddler、postman、jmeter
  - 代码：python + UnitTest框架 + Requests框架
- 测什么？
  - 测试 服务器针对客户端请求，回发的响应数据是否与预期结果一致！
    - 人眼对比
    - 断言

**特点**

- 符合质量控制前移的理念
- 可以发现一些页面操作发现不了的问题（**接口测试可以跳过前端界面直接测试功能**）
- 接口测试低成本高效益
- 接口测试是从用户的角度对系统进行检测

**实现方式**

- 工具：JMeter、Postman、fiddler
- 代码：Python + Requests + UnitTest

**什么是自动化接口测试？**

- 借助工具、代码，模拟客户端发送请求给服务器，借助**断言**自动判断 **预期结果和实际结果** 是否一致！




# ==HTTP协议==

**协议**：就是规则。要求通信的双方必须严格遵守！

## HTTP协议简介

- HTTP：（HyperText Transfer Protocol）**超文本传输协议**，是一个基于请求与响应模式的、应用层的协议，也是互联网上应用最为广泛的一种网络协议。

> 应用层：4层
>
> ​	应用层(HTTP所在层)
>
> ​	TCP(在端口上唯一找到应用)
>
> ​	IP(能够唯一标识一台主机)
>
> ​	链路层

- 特征：
  1. 支持客户端/服务器模式
  2. 简单快速
  3. 灵活
  4. 无连接（指客户端不用提前和服务器有连接，只要有端口和IP就可以精准定位到服务器的某个应用上去）
  5. 无状态（TCP协议每次连接状态变化的时候，都有状态产生，而HTTP没有）



## ==URL格式==



- 概念：（Uniform Resource Locator）**统一资源定位符**。
- 作用：在网络环境中，唯一的定义一个数据资源。

![image-20210707105756973](./assets/image-20210707105756973.png)

- **协议：http。 规定数据传输的方式。**
- **域名（IP）：在网络环境中找到主机。—— 用 :// 与协议隔分**
- **端口（port）：（常省略）在网络主机上，标识一个进程（应用程序）—— 用: 与域名**
  - 拓展补充：在linux本地主机上，用PID标识一个进程

- **资源路径：标识网络资源（文件、图片、音视频、变量...）—— 用: / 与端口格分**
- **查询参数：传递给资源路径对应的数据。—— 用 ? 与资源路径隔分。 查询参数内部 用 & 隔分多个kv对（键值对）**

### 练习

请写出以下URL的各个组成部分。这个URL没有写出端口号，它的端口是什么？

![image-20210707110844053](./assets/image-20210707110844053.png)

协议：http

域名：www.itcast.cn

端口号：8080（ 不是默认，只不过网络 网络通信常用！）

资源路径：/news/index.html

查询参数：uid=123&page=1



## ==HTTP请求(客户端)==

**作用：**

- 客户端(app、浏览器)，发送请求给服务器时，使用的协议 —— http请求协议。
- 规定 发送给服务器的数据传输的语法格式。

### 整体格式(HTTP请求包/HTTP请求报文)

- **请求行：**http请求第一行。**请求方法 (空格)  URL  (空格)  协议版本** 
- **请求头：**语法格式：k ：v
  - User-Agent：描述 请求发送端的 浏览器类型。
  - **Content-Type：描述 请求体 的 数据类型！**
- **空行：**代表http请求头结束。
- **请求体：**请求发送时携带的数据。数据类型 Content-Type 的值！ 
  - post 和 put 有请求体
  - get 和 delete 没有请求体


![image-20210215224232033](./assets/image-20210215224232033.png)

![image-20210707113752374](./assets/image-20210707113752374.png)



### fiddler 抓包验证

![image-20210707115816172](./assets/image-20210707115816172.png)

![image-20210707120133271](./assets/image-20210707120133271.png)

### 请求行

- http 请求方法：大小写均可。
  - GET：查询。 —— 没有请求体
  - POST：添加。（登录时常用）
  - put: 修改。
  - delete: 删除。 —— 没有请求体

### 请求头

- 数据格式：k：v
- Content-Type：
  - **application/json： JSON数据格式**
  - **application/x-www-form-urlencoded： form表单数据**

### 请求体

- **GET和DELETE 没有**
- **PUT 和POST有**
- 数据类型受 Content-Type 值影响。

### 练习

- 以下是抓取的某个HTTP协议数据包的请求报文，请问其中，请求行，请求头，请求体分别是什么？

```http
POST http://tpshop-test.itheima.net/index.php HTTP/1.1
Host: tpshop-test.itheima.net
Connection: keep-alive
Content-Length: 53
Accept: application/json, text/javascript, */*; q=0.01
Origin: http://tpshop-test.itheima.net
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90
Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: http://tpshop-test.itheima.net/Home/user/login.html
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: is_mobile=0; province_id=1; city_id=2; district_id=3;
is_distribut=1; PHPSESSID=1b80tii77mhle0fqd2bg52ucg5; cn=0

username=13800138006&password=123456&verify_code=8888
```



## ==HTTP响应(服务器端)==

**作用：**

- 服务器端，针对客户端发送的 http请求，回发响应数据。—— http应答！
- 规定 回发给客户端的数据组织格式。

### 整体格式(HTTP响应包/HTTP响应报文)

- 响应行（状态行）：协议版本 (空格) 状态码 (空格) 状态描述
- 响应头：语法格式：k:v 
  - **Content-Type: 描述 响应体中数据类型。**
- 空行：代表响应头结束
- 响应体：绝大多数不为空。（请求成功：回发数据，失败：回发错误信息）
  - 数据类型受 Content-Type值影响。

![image-20210707122117120](./assets/image-20210707122117120.png)

![image-20210215224253933](./assets/image-20210215224253933.png)

### 状态行(响应行)

- 状态码：
  - 1xx：代表指示信息。表请求已经被接收，等待继续处理。
  - **2xx：代表请求成功被处理、接收。 常见：200、201**
  - 3xx：重定向，待访问的资源，需求重新指定路径访问。
  - **4xx：代表客户端错误。常见：404、 403**
  - 5xx：访问器端错误。

- 状态码描述：一般与状态码 唯一对应。  200 —— ok； 404 —— file not found

### 响应头

- **语法格式：k：v**
- **Content-Type：值为 响应体  的数据类型。**
- Content-Length: 响应体的大小。可以不写，浏览器会自动求取。一旦写，必须准确！

### 响应体

- 回发给客户端的 消息内容。常见的有 html网页、xml、json


### 练习

- 以下是HTTP协议的响应报文内容，请问，状态行、响应头、响应体分别是哪几个部分？

```http
HTTP/1.1 200 OK
Server: nginx
Date: Mon, 29 Jun 2020 03:36:28 GMT
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
Vary: Accept-Encoding
X-Powered-By: PHP/5.6.40
Set-Cookie: is_mobile=0; expires=Mon, 29-Jun-2020 04:36:28 GMT;
Max-Age=3600; path=/
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate, post-
check=0, pre-check=0
Pragma: no-cache
Set-Cookie: user_id=3338; path=/
Set-Cookie: is_distribut=1; path=/
Set-Cookie: uname=13800138006; path=/
Set-Cookie: cn=0; expires=Mon, 29-Jun-2020 02:36:28 GMT; Max-
Age=-3600; path=/
Content-Length: 805

{"status":1,"msg":"\u767b\u9646\u6210\u529f","result":
{"user_id":3338,"email":"","password":"519475228fe35ad067744465
c42a19b2","paypwd":null,"sex":0,"birthday":0,"user_money":"0.00
","frozen_money":"0.00","distribut_money":"0.00","underling_num
ber":0,"pay_points":100,"address_id":0,"reg_time":1590980161,"l
ast_login":1590980161,"last_ip":"","qq":"","mobile":"1380013800
6","mobile_validated":1,"oauth":"","openid":null,"unionid":null
,"head_pic":null,"province":0,"city":0,"district":0,"email_vali
dated":0,"nickname":"13800138006","level":1,"discount":"1.00","
total_amount":"0.00","is_lock":0,"is_distribut":1,"first_leader
":0,"second_leader":0,"third_leader":0,"token":"a26e177bd6506ff
f68c01fd13e742073","message_mask":63,"push_id":"0","distribut_l
evel":0,"level_name":"\u6ce8\u518c\u4f1a\u5458"},"url":""}
```

## 传统风格接口

特点：

- 请求方法，只使用 get 和 post 即可。
- **URL 不唯一**。同一个操作可以对应不同的 URL
- 状态码的使用较单一。200 最常见。

![image-20210707153849856](./assets/image-20210707153849856.png)

## RESTful风格(表现层状态转化)接口

特点：

1. 每一个URL代表一种资源；
2. 客户端和服务器之间，传递这种资源的某种**表现层**（**用图片去描述，或者用文字去描述等等，不同的表现方法**）；
   - **表现层：数据的不同表现形式（如：图片、文字表现同一个数据对象）**
3. 客户端通过四个HTTP动词（GET、post、delete、put），对服务器端资源进行操作，实现"表现层状态转化"；
4. 接口之间传递的数据最常用格式为JSON。

![image-20210707154607898](./assets/image-20210707154607898.png)

# 接口测试流程

![image-20210707160900090](./assets/image-20210707160900090.png)

1.  **分析需求，产生需求文档（产品）。**
2.  **（开发产生接口文档）解析接口文档。**
3.  **产生 接口测试用例（送审）。**
4.  **执行 测试用例**
    - **工具：postman、jmeter、fidller**
    - **代码：python + Requests +UnitTest**
5.  **提交、跟踪缺陷。**
6.  **生成 测试报告。**
7.  **（可选）接口自动化持续集成！**



# 接口文档

## 什么是接口文档

- **由开发人员编写，描述接口信息的文档。**开发团队按接口文档进行开发工作，并要一直维护遵守。

## 作用

1. 能够让前端开发与后台开发人员更好的配合，提高工作效率。（有一个统一参考的文件）
2. 项目迭代或者项目人员更迭时，方便后期人员查看和维护
3. 方便测试人员进行接口测试

## 展现形式

- word 文档形式
- Excel 表格式形式
- pdf 文档形式。

## ==结构==

- **基本信息：**
  - 资源路径 （协议和域名在 “系统信息”中）
  - 请求方法
  - 接口描述
- **请求参数：**
  - 请求头：
    - Content-Type。描述请求体的数据类型！
  - 请求体：
    - 实现该接口使用的 数据及对应类型。
- **返回数据：**
  - 状态码 200
  - 错误码（**自定义状态码**）
    - 码值
    - 描述信息。

# ==接口文档解析==

- 接口文档的解析本质：从接口文档中，找出  http 请求所需要的 数据信息。
  - 主要包含：请求方法、URL 、请求头、请求体、响应状态码、描述。
- **以 “登录” 为例：**
  - 请求方法：POST
  - URL：http://ihrm-test.itheima.net/api/sys/login
  - 请求头：Content-Type ：application/json 
  - 请求体：{"mobile":"13800000002", "password":"123456"}
  - 响应状态码：200
    - 错误码：
      - 10000：操作成功！
      - 20001：用户名或密码错误
      - 99999：抱歉，系统繁忙，请稍后重试！



## 利用fiddler发送http请求

![image-20210707173007275](./assets/image-20210707173007275.png)

![image-20210707173337510](./assets/image-20210707173337510.png)





# ==二、设计编写测试用例，Postman安装==



# 接口用例设计

**为什么写**

1. 防止测试点漏测。条理清晰
2. 方便分配工作，评估工作量和时间
3. 面试时使用！

## 接口测试的测试点

测试点称之为测试维度。

![image-20210708095129193](./assets/image-20210708095129193.png)

### 功能测试

- 单接口功能：
  - 手工测试中的单个业务模块，一般对应一个接口。	
    - 登录业务 ——> 登录接口
    - 加入购物车业务 ——> 加入购物车接口
    - 订单业务 ——> 订单接口
    - 支付业务 ——> 支付接口
  - 借助工具、代码。绕开前端界面，组织接口所需要的数据，展开接口测试。
- 业务场景功能：
  - 按照用户实际 使用场景，梳理 接口业务 场景。
  - 组织业务场景时，一般只需做 正向 测试即可（与手工一致）。
  - 一般建议用最少的 用例 覆盖最多的业务场景。
    - 登录 —— 搜索商品 —— 加购物车 —— 下单 —— 支付 —— 评价

### 性能测试

- 响应时长
- 吞吐量
- 并发数量
- 服务器资源利用率



### 安全测试

- 攻击安全。 —— 与测试工程师无关。

- 业务安全。 —— 测试的方向。

  - 敏感数据是否加密

    ![image-20210708103259396](./assets/image-20210708103259396.png)

  - SQL注入：在用户能输入数据的位置，写入SQL语句。

    - SQL注入安全，用户恶意写入的SQL语句，不会执行，查询数据库！





> 补充内容：浏览器中的F12打开开发者工具，也能查看http请求

![QQ_1757840188183](./assets/QQ_1757840188183.png)



## ==设计方法与思路==

### 与手工设计相同之处

- 手工测试 对应的 功能测试点，与接口测试对应的功能 完全一致。


> tpshop商城 登录 页面，手工功能测试用例设计要点：
>
> 1.  页面布局是否符合需求
> 2.  测试 用户名 输入框，输入的数据是否正确。
> 3.  测试 密码 输入框，输入的数据是否正确。
> 4.  测试 验证码 输入框， 输入的数据是否正确。

tpshop商城 登录 页面，接口测试用例设计要点：

1.  测试 用户名 输入框对应的 username 的值 是否正确。
2.  测试 密码 输入框对应的 password 的值，是否正确。
3.  测试 验证码 输入框对应的 verify_code 的值，是否正确。

![image-20210708105012588](./assets/image-20210708105012588.png)

### 与手工设计不同之处

1.  手工测试，测写入到输入框中的数据是否正确。接口测试测 参数 对应的 参数值 是否正确。
2.  接口测试，不单单针对 参数值进行，还可以针对 **参数本身** 进行测试。
    - 正向参数：
      - 必选参数：所有的 必选（必填）都包含。
      - 组合参数：所有的 必选 + 任意一个或多个可选参数。
      - 全部参数：所有的 必选 + 所有的 可选参数
    - 反向参数：
      - 多参：多出一个或多个必选参数 （自己造一个或多个必选参数，可以任意指定）
      - 少参：缺少一个或多个必选参数。
      - 无参：没有必选参数。
      - 错误参数：参数名输入错误。

## ==单接口测试用例==

> 手工 测试用例文档  8 大要素：
>
> 编号、用例名称（标题）、模块、优先级、预置条件、测试数据、操作步骤、预期结果

接口 测用例文档 10 要素：

- 编号、用例名称（标题）、模块、优先级、预置条件、请求方法、URL、请求头、请求体(请求数据)、预期结果

![image-20210708112958875](./assets/image-20210708112958875.png)

分析接口文档，以 **“登录接口”** 为例：

- 请求方法：post
- URL： “系统信息” 中的 协议和域名 + /api/sys/**login**
- 请求头：Content-Type : application/json 
- 请求体：{"mobile":"13800000002","password":"123456"}
- 预期结果： {"success":true,"code":10000,"message":"操作成功！","data":"f5050a1b-7919-444c-9ec4-3c1a7286536d"}
  - **data：值为登录成功生成的 令牌数据。该数据 会定时变化。**

![QQ_1757861389791](./assets/QQ_1757861389791.png)

| 编号      | 用例名称 | 模块 | 优先级 | 预置条件   | 请求方法 | URL                       | 请求头                        | 请求体(请求数据）                            | 预期结果                                                     |
| --------- | -------- | ---- | ------ | ---------- | -------- | ------------------------- | ----------------------------- | -------------------------------------------- | ------------------------------------------------------------ |
| login_001 | 登陆成功 | 登录 | p1     | 账号已注册 | POST     | {协议+域名}/api/sys/login | Content-Type:application/json | {"mobile":"13800000002","password":"123456"} | 状态码：200      {"success":true,"code":10000,"message":"操作成功！","data":"f5050a1b-7919-444c-9ec4-3c1a7286536d"} |

登录模块的接口测试用例测试点：

- 数值
  - 正向：
    - 登录成功
  - 反向：
    - 用户名为空
    - 用户名包含特殊字符、字母
    - 用户名超过11位（12位）
    - 用户名不足11位（10位）
    - 用户名未注册
    - 密码为空
    - 密码包含特殊字符、字母
    - 密码为1位
    - 密码为100位
    - 密码错误
- 参数（接口测试特有）
  - 正向：
    - 必选参数：正确用户名 + 正确密码
    - 组合参数：忽略
    - 全部参数：正确用户名 + 正确密码
  - 反向：
    - 多参：多 abc：“123”
    - 少参（少mobile）：没有用户名，正确密码
    - 无参：没有任何参数
    - 错误参数(手机号参数名错误)：abc:1381234567, password:”123456”

用户名相关 5 条：

| login_002 | 用户名为空               | 登录 | p2   | ——                     | POST | {协议+域名}/api/sys/login | Content-Type:application/json | {"mobile":"","password":"123456"}             | 状态码：200      {"success":false,"code":20001,"message":"用户名或密码错误","data":null} |
| --------- | ------------------------ | ---- | ---- | ---------------------- | ---- | ------------------------- | ----------------------------- | --------------------------------------------- | ------------------------------------------------------------ |
| login_003 | 用户名包含特殊字符、字母 | 登录 | p2   | ——                     | POST | {协议+域名}/api/sys/login | Content-Type:application/json | {"mobile":"13800&#abc","password":"123456"}   | 状态码：200      {"success":false,"code":20001,"message":"用户名或密码错误","data":null} |
| login_004 | 用户名超11位（12位）     | 登录 | p2   | ——                     | POST | {协议+域名}/api/sys/login | Content-Type:application/json | {"mobile":"138000000023","password":"123456"} | 状态码：200      {"success":false,"code":20001,"message":"用户名或密码错误","data":null} |
| login_005 | 用户名不足11位（10位）   | 登录 | p2   | ——                     | POST | {协议+域名}/api/sys/login | Content-Type:application/json | {"mobile":"1380000000","password":"123456"}   | 状态码：200      {"success":false,"code":20001,"message":"用户名或密码错误","data":null} |
| login_006 | 用户名未注册             | 登录 | p2   | 数据库中不存在的手机号 | POST | {协议+域名}/api/sys/login | Content-Type:application/json | {"mobile":"16700542479","password":"123456"}  | 状态码：200      {"success":false,"code":20001,"message":"用户名或密码错误","data":null} |

密码相关 5 条：

| login_007 | 密码为空               | 登录 | p2   | ——   | POST | {协议+域名}/api/sys/login | Content-Type:application/json | {"mobile":"13800000002","password":""}                       | 状态码：200      {"success":false,"code":20001,"message":"用户名或密码错误","data":null} |
| --------- | ---------------------- | ---- | ---- | ---- | ---- | ------------------------- | ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| login_008 | 密码包含特殊字符、字母 | 登录 | p2   | ——   | POST | {协议+域名}/api/sys/login | Content-Type:application/json | {"mobile":"13800000002","password":"123&%rt"}                | 状态码：200      {"success":false,"code":20001,"message":"用户名或密码错误","data":null} |
| login_009 | 密码1位                | 登录 | p2   | ——   | POST | {协议+域名}/api/sys/login | Content-Type:application/json | {"mobile":"13800000002","password":"1"}                      | 状态码：200      {"success":false,"code":20001,"message":"用户名或密码错误","data":null} |
| login_010 | 密码100位              | 登录 | p2   | ——   | POST | {协议+域名}/api/sys/login | Content-Type:application/json | {"mobile":"13800000002","password":"放置100位字符组成的密码"} | 状态码：200      {"success":false,"code":20001,"message":"用户名或密码错误","data":null} |
| login_011 | 错误密码               | 登录 | p2   | ——   | POST | {协议+域名}/api/sys/login | Content-Type:application/json | {"mobile":"13800000002","password":"888888"}                 | 状态码：200      {"success":false,"code":20001,"message":"用户名或密码错误","data":null} |

参数相关：

| login_012 | 必选参数（全部参数）         | 登录 | p2   | ——   | POST | {协议+域名}/api/sys/login | Content-Type:application/json | {"mobile":"13800000002","password":"123456"}             | 状态码：200      {"success":true,"code":10000,"message":"操作成功！","data":"f5050a1b-7919-444c-9ec4-     3c1a7286536d     "} |
| --------- | ---------------------------- | ---- | ---- | ---- | ---- | ------------------------- | ----------------------------- | -------------------------------------------------------- | ------------------------------------------------------------ |
| login_013 | 多参                         | 登录 | p2   | ——   | POST | {协议+域名}/api/sys/login | Content-Type:application/json | {"abc":"123","mobile":"13800000002","password":"123456"} | 状态码：200      {"success":true,"code":10000,"message":"操作成功！","data":"f5050a1b-7919-444c-9ec4-     3c1a7286536d     "} |
| login_014 | 少参（少mobile）             | 登录 | p2   | ——   | POST | {协议+域名}/api/sys/login | Content-Type:application/json | {"password":"123456"}                                    | 状态码：200      {"success":false,"code":20001,"message":"用户名或密码错误","data":null} |
| login_015 | 无参                         | 登录 | p2   | ——   | POST | {协议+域名}/api/sys/login | Content-Type:application/json |                                                          | {"success":false,"code":99999,"message":"抱歉，系统繁忙，请稍后重试！","data":null} |
| login_016 | 错误参数（mobile参数名错误） | 登录 | p2   | ——   | POST | {协议+域名}/api/sys/login | Content-Type:application/json | {"abc":"13800000002","password":"123456"}                | 状态码：200      {"success":false,"code":20001,"message":"用户名或密码错误","data":null} |



> 注意：多参因为开发在写接受参数数据的代码的时候，一般只写需要传参的参数接口，而我们考虑的多参情况，即便把自定义的参数传进去，后台也不会对其进行处理，所以一般预期结果是正确的



## ==业务场景测试用例==

- 用户怎么用，怎样设计业务。
- **用最少的测试用例，尽量覆盖最多的接口。**

### 分析测试点

针对 “**员工管理**” 业务场景：

- 登录 —— 添加员工 —— 查询员工 —— 修改员工 —— 再次查询 —— 删除员工 —— 查询员工列表


### 添加员工

- 请求方法：post

- URL： {协议+域名}/api/sys/user

- 请求头：

  - Content-Type： application/json
  - Authorization： Bearer **f5050a1b-7919-444c-9ec4-3c1a7286536d** （具体数据 来源 **登录成功返回的 响应体中的 data的值**）

- 请求体（请求数据）：{"username":"爱因斯坦","mobile":"17289432100","timeOfEntry":"2021-07-12","formOfEmployment":1,"departmentName":"测试0607","departmentId":"1412421425733664768","workNumber":"234","correctionTime":"2021-07-30T16:00:00.000Z"}

  ![image-20210708155543953](./assets/image-20210708155543953.png)

- 预期结果：

  - 状态码：200
  - {"success":true,"code":10000,"message":"操作成功！", "data":{"id":"113749504"}}

| 用例名称 | 模块     | 优先级 | 预置条件 | 请求方法 | URL                      | 请求头                                                       | 请求体(请求数据）                                            | 预期结果                                                     |
| -------- | -------- | ------ | -------- | -------- | ------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 添加员工 | 员工管理 | p0     | 登录成功 | post     | {协议+域名}/api/sys/user | Content-Type：  application/json，          Authorization： Bearer f5050a1b-7919-444c-9ec4-3c1a7286536d | {"username":"爱因斯坦","mobile":"17289432100","timeOfEntry":"2021-07-12","formOfEmployment":1,"departmentName":"测试0607","departmentId":"1412421425733664768","workNumber":"234","correctionTime":"2021-07-30T16:00:00.000Z"} | 状态码：200      {"success":true,"code":10000,"message":"操作成功！",  "data":{"id":"113749504"}} |

### 查询员工

- 请求方法：GET
- URL： {协议+域名}/api/sys/user/:target
- 请求头：
  - Content-Type： application/json
  - Authorization： Bearer f5050a1b-7919-444c-9ec4-3c1a7286536d （具体数据 来源 登录成功返回的 响应体中的 data的值）
- 请求体:
  - 无
- 返回数据：
  - 状态码：200
  - {"success": true,
    "code": 10000,
    "message": "操作成功！",
    "data": { 所查询的员工的详细信息} }

| emp_manager_002 | 查询员工 | 员工管理 | p1   | 登录成功 | GET  | {协议+域名}/api/sys/user/:target | Content-Type：  application/json，     Authorization： Bearer f5050a1b-7919-444c-9ec4-3c1a7286536d |      | 状态码：200     {"success": true,     "code": 10000,     "message": "操作成功！",     "data": { 所查询的员工的详细信息} } |
| --------------- | -------- | -------- | ---- | -------- | ---- | -------------------------------- | ------------------------------------------------------------ | ---- | ------------------------------------------------------------ |
|                 |          |          |      |          |      |                                  |                                                              |      |                                                              |


### 修改员工

| emp_manager_003 | 修改员工 | 员工管理 | p0   | 登录成功 | PUT  | {协议+域名}/api/sys/user/:target | Content-Type：  application/json，     Authorization： Bearer xxx | {"username":"小猪佩奇"} | 状态码：200      {"success":true,"code":10000,"message":"操作成功！",  "data":{"id":"xxx"}} |
| --------------- | -------- | -------- | ---- | -------- | ---- | -------------------------------- | ------------------------------------------------------------ | ----------------------- | ------------------------------------------------------------ |
|                 |          |          |      |          |      |                                  |                                                              |                         |                                                              |

**返回数据中的 id ，代表 修改的员工id （是一个会变化的数据）。**

### 删除员工

| emp_manager_004 | 删除员工 | 员工管理 | p0   | 登录成功 | delete | {协议+域名} /api/sys/user/:target | Content-Type：  application/json，     Authorization： Bearer xxx |      | 状态码：200      {"success":true,"code":10000,"message":"操作成功！","data":null} |
| --------------- | -------- | -------- | ---- | -------- | ------ | --------------------------------- | ------------------------------------------------------------ | ---- | ------------------------------------------------------------ |
|                 |          |          |      |          |        |                                   |                                                              |      |                                                              |

### 查询员工列表

| emp_manager_005 | 查询员工列表 | 员工管理 | p0   | 登录成功 | GET  | {协议+域名}  /api/sys/user?page=1&size=10 | Content-Type：  application/json，     Authorization： Bearer xxx |      | 状态码：200     {     "success": true,     "code": 10000,     "message": "操作成功！",     "data": {     "total": xxxx,     "rows" [     {},{},… 10个员工的详细信息     ]     }     } |
| --------------- | ------------ | -------- | ---- | -------- | ---- | ----------------------------------------- | ------------------------------------------------------------ | ---- | ------------------------------------------------------------ |
|                 |              |          |      |          |      |                                           |                                                              |      |                                                              |

# ==Postman==

## 简介和安装

- 简介：
  - Postman是一款非常流行的接口调试工具，它使用简单，而且功能也很强大。不仅测试人员会使用，开发人员也会经常使用。
  - 特征：
    1. 简单易用的图形用户界面
    2. 可以保存接口请求的历史记录
    3. 使用测试集Collections可以更有效的管理组织接口
    4. 可以在团队之间同步接口数据
- 安装：
  - 参考 资料补充 里面的 《**Postman环境安装.pdf**》
  - 需要安装postman的**插件newman**，和安装newman的**插件newman-reporter-html**

## ==案例一==

> 使用 postman 发送 http请求，访问 tpshop 商城的 “搜索” 接口
>
> 访问 tpshop 商城的 “搜索” 接口所需要的信息：
>
> —— 结合 F12 浏览器开发者工具（点击network然后操作抓包）分析：
>
> - 请求方法：GET
> - URL：http://tpshop-test.itheima.net/Home/Goods/search.html?q=%E6%89%8B%E6%9C%BA
> - 请求头：无
> - 请求体：无
> - 返回数据：html网页

![image-20210708173517103](./assets/image-20210708173517103.png)

## ==案例二==

> 使用 Postman 向 topshop 商城 登录接口 发送一个密码错误的 登录请求
>
> - 请求方法：post
>
> - URL：http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=do_login&t=0.6693319462870182
>
> - 请求头：Content-Type:application/x-www-form-urlencoded
>
> - 请求体：
>
>   - username:  13812345678
>   - password: 12345699999
>   - verify_code : 8888
>
> - 返回数据：
>
>   {"status":-2,"msg":"密码错误!"}  ---- 实际返回结果 “验证码错误”  与业务有关，后续课程讲解。

![image-20210708175710904](./assets/image-20210708175710904.png)

## ==案例三==

> 从接口文档，获取 登录接口 的 http请求，使用 Postman 发送
>
> ​	如果请求头里面的**Content-Type是application/json，在请求体里面需要选择raw**

![image-20210708180718943](./assets/image-20210708180718943.png)





# <font face="黑体" color=Violet size = 6>三、使用Postman管理、执行测试用例生成测试报告</font>

# Postman 高级用法

## ==管理测试用例Collections==

创建 collections 

![image-20210709093648461](./assets/image-20210709093648461.png)

![image-20210709093733212](./assets/image-20210709093733212.png)

![image-20210709093818921](./assets/image-20210709093818921.png)

![image-20210709094052696](./assets/image-20210709094052696.png)

创建 用例集、子目录和 请求

![image-20210709094409379](./assets/image-20210709094409379.png)

## 用例集导出、导入

**导出**

![image-20210709095322682](./assets/image-20210709095322682.png)

![image-20210709095401113](./assets/image-20210709095401113.png)

![image-20210709095626631](./assets/image-20210709095626631.png)

![image-20210709095723659](./assets/image-20210709095723659.png)

**导入**

![image-20210709100144888](./assets/image-20210709100144888.png)

![image-20210709100214533](./assets/image-20210709100214533.png)

![image-20210709100316070](./assets/image-20210709100316070.png)

![image-20210709100333911](./assets/image-20210709100333911.png)

## ==Postman 断言==

### Postman 断言简介

- postman 断言借助 JavaScript - js 语言编写代码，自动判断预期结果与实际结果是否一致。
- 断言 代码写在 Scripts 的标签中。

### Postman 常用断言

> 点击**Scripts标签，右下角的</>Snippets**中可以直接选择断言类型，**一个用例可以写多个断言**

#### ==1. 断言响应状态码==

**Status code: Code is 200**

1. 在 Scripts 标签中，选中 Status Code：code is 200， 生成对应代码
2. 适当调整 test() 方法参数1，和 匿名函数中的 预期结果。
3. 点击 send 按钮，发送请求，执行断言代码。
4. 查看断言结果。

```js
// 断言响应状态码 是否为 200
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm：代表 postman 的一个实例
test()：是 pm实例的一个方法。有两个参数
	参数1：在断言成功后，给出的文字提示。可以修改。"Status code is 200"
	参数2：匿名函数。
pm.response.to.have.status(200); 
// 意思：postman 的响应结果中应该包含状态码 200
		200 ——> 预期结果！
```

![image-20210709103914593](./assets/image-20210709103914593.png)

#### 2. 断言响应体是否包含某个字符串

**Response body: Contains string**

```js
// 断言响应体包含指定字符串
pm.test("Body matches string", function () {
    pm.expect(pm.response.text()).to.include("string_you_want_to_search");
});

pm：postman的一个实例
test(): postman实例的方法，有两个参数
	参1：断言后显示的文字提示信息，可改。
    参2：匿名函数
pm.expect(pm.response.text()).to.include("string_you_want_to_search"); 
// 意思：pm 期望 响应文本 中，包含 xxxx 字符串。
	"string_you_want_to_search" ——> 预期结果。 可以修改
```

![image-20210709110251175](./assets/image-20210709110251175.png)

#### 3. 断言响应体是否等于某个字符串（对象）

**Response body: Is equal to a string**

- 和整一个响应体作比较

```js
// 断言 响应体 等于某个字符串（对象）
pm.test("Body is correct", function () {
    pm.response.to.have.body("response_body_string");
});

pm.response.to.have.body("response_body_string");


例如：

pm.test("Body is correct", function () {
    pm.response.to.have.body(
        {
    "msg": "操作成功",
    "code": 10000,
    "data": {
        "token": 	"eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjY2OTcyMWRmLTczMzUtNDkxZi1iMDhmLTM3OWIyMDE4YmI2YiJ9.BaqZXTYGzDyRdVZgXnM9pQlryg_T8DlR3NoUldapp0i1xUKcOFdK50HSAvD4M0i-Yb-NIiXC1FWHpKi85yY4Bg"
    }
}

    );
});



// 意思是，pm 的 响应中应该有 响应体 xxx
"response_body_string" ——> 预期结果。 可以修改（内容为整一个响应体的值）

但是因为响应体的值里面的data是一直会变的，所以很难作断言，故不实用
```



#### ==4. 断言JSON数据==

**Response body: JSON value check**

```js
// 断言json的响应结果
pm.test("Your test name", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.value).to.eql(100);
});

var jsonData = pm.response.json();
// var jsonData： 用js语法定义一个变量。jsonData 就是变量名
// pm.response.json();  代表响应的json结果
// 意思就是让定义一个jsonData的变量，这个jsonData等于响应体的json结果

/* 举例：response.json();
{
    "success": true,
    "code": 10000,
    "message": "操作成功！",
    "data": "95c78d75-721c-40fb-b2d5-742fea42cbd5"
}
*/

pm.expect(jsonData.value).to.eql(100);
// 意思：pm 预期 json结果 key对应的值 等于 xxx
// to.eql(100); 中的 100 代表预期结果。可以修改的。

//value 就是 响应体中的 key

/* 举例：
		jsonData.value 的  value：
        取 ：success、code、message、data
*/
```

示例：

```js
// 断言json的响应结果-success的值为true
pm.test("断言响应结果success的值为true", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.success).to.eql(true);
});

pm.test("断言响应结果中code的值为10000", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.code).to.eql(10000);
});

pm.test("断言响应结果中message的值为 操作成功", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.message).to.eql("操作成功！");
});
```

![image-20210709114639784](./assets/image-20210709114639784.png)

#### 5. 断言响应头

**Response headers: Content-Type header check**

```js
// 断言响应头
pm.test("Content-Type is present", function () {
    pm.response.to.have.header("Content-Type");
});

pm.response.to.have.header("Content-Type");
// pm 的响应 头中包含 Content-Type

// 示例：可以在 header 中，添加 响应头中的 key 对应的 value 判定。用 ，隔分。
// 断言响应头
pm.test("Content-Type is present", function () {
    pm.response.to.have.header("Content-Type", "application/json;charset=UTF-8");
});
```

### ==Postman断言工作原理==

![image-20210709122129466](./assets/image-20210709122129466.png)



## ==全局变量和环境变量==

**全局变量**

- 概念：在 Postman 全局生效的变量，全局唯一。

- 设置：

  - **代码设置**：`pm.globals.set(“全局变量名”，全局变量的值)`

    ```js
    // 示例：
    pm.globals.set("glb_age", 100)
    ```

- 获取：

  - **代码获取**: `var 接收值的变量 = pm.globals.get(“全局变量名”)`

    ```js
    // 示例：
    var ret = pm.globals.get("glb_age")  // ret 的值为 100
    ```

  - **请求参数获取**（postman界面获取，例如，url，params headers）: `{{全局变量名}}`

    ```js
    // 示例：
    {{glb_age}}
    ```

**环境变量**

- 概念：在 特定环境（生产环境、开发环境、测试环境）下，生效的变量，在本环境内唯一。

- 设置：

  - 代码设置：`pm.environment.set("环境变量名", 环境变量值)`

    ```js
    // 示例
    pm.environment.set("env_age", 99)
    ```

- 获取：

  - 代码获取：`var 接收值的变量 = pm.environment.get("环境变量名")`

    ```js
    // 示例
    var ret = pm.environment.get("env_age")  // ret 的值为 99
    ```

  - 请求参数获取（postman界面获取）：`{{环境变量名}}`

    ```js
    // 示例
    {{env_age}}
    ```



## Postman 请求前置脚本

- 在 send 按钮点击后，请求前置脚本代码，第一时间被执行。在 postman 内部实际发送 http请求之前。

> 假设，这样一种场景：
>
> ​		调某接口时，要输入 “时间戳”，如果输入的 “时间戳” 的绝对值，超过标准时间10分钟。 则不允许调用。

### 时间戳

- 时间戳：对应绝对时间，从 1970年1月1日00:00:00 到现在 所经历的秒数。


> 一天：24 x 60 x 60 = 86400秒
>
> 1970年距今 55年/9月/15天  =  （ 55 x 365 + 9 x 30 + 15 ）天 x 86400秒 = 20360 x 86400 = 1,759,104,000

### 案例

>  调用百度首页接口，传时间戳给服务器		

实现步骤：

1. 在Scripts标签页中的Pre-request，添加代码。拿到时间戳，写入全局变量

   ```js
   // 拿到时间戳
   var timestamp = new Date().getTime()
   
   // 将时间戳设置到 全局变量
   pm.globals.set("glb_timestamp", timestamp)
   ```

2. 点击 Send 按钮，发送请求。请求发送前执行 上述代码。写入全局变量

3. 查看写入的变量

   ![QQ_1757952524071](.\assets\note\QQ_1757952524071.png)

4. 在 请求参数(界面)中，使用全局变量。{{全局变量名}}

   ![image-20210709161444553](./assets/image-20210709161444553.png)

5. 在 postman的 控制台，查看 发送的 http请求

   ![image-20210709161525707](./assets/image-20210709161525707.png)

   ![image-20210709161642714](./assets/image-20210709161642714.png)

### 工作原理

![image-20210709164313771](./assets/image-20210709164313771.png)

## ==Postman 关联==

**介绍：**应用于 多个 http请求之间，有数据关联、或依赖关系时。

### 实现步骤

A接口 依赖 B接口 的数据

1.  向B接口发送http请求，获取数据
2.  将数据 设置 至 全局变量（环境变量）中
3.  A 接口 获取 全局变量（环境变量）中 数据值，进行使用。

### 案例

> 请求  获取天气接口， 提取响应结果中的 城市， 将城市名，给百度搜索接口使用。
>
> 因为要获取响应结果中的城市，所以不能写在前置脚本中

实现步骤：

1. 创建 用例集，分别创建 查询天气 请求 和 百度搜索的请求

   ![image-20210709170257422](./assets/image-20210709170257422.png)

2. 在查询天气请求 Tests 中，编写代码 获取 城市名，写入全局变量

   ```js
   // 获取 全部响应结果
   var jsonData = pm.response.json()
   // 从响应结果中 获取 城市名
   var city = jsonData.weatherinfo.city
   // 将城市名写入到全局变量
   pm.globals.set("glb_city", city)
   ```

3. 点击 Send 按钮，发送 请求，查看设置的全局变量。

   ![image-20210709170550685](./assets/image-20210709170550685.png)

4. 修改 百度搜索请求，使用全局变量，按 城市名进行搜索。(key必须是wd，wd是关键词的意思)

   ```url
   http://www.baidu.com/s?wd={{glb_city}}
   ```

   ![image-20210709172113952](./assets/image-20210709172113952.png)

## 批量执行测试用例

![image-20210709174508328](./assets/image-20210709174508328.png)

![image-20210709174635008](./assets/image-20210709174635008.png)



# ==Postman 测试报告==

## 安装newman

- 资料补充里的《Postman环境安装.pdf》
- 若在cmd中写newman命令里加 -r 会报错，则说明newman-reporter-html没有安装成功



## ==使用newman生成测试报告(cmd)==

步骤：

1. 批量执行测试用例集。（确认无误）

2. 导出 Export 用例集。（得到 xxxx.json文件）

3. 在 终端 中 执行命令，生成测试报告

   ```shell
   # 现在 终端中，测试一下。
   newman run xxxx.json
   
   # 完整的命令
   newman run xxxx.json -e 环境变量文件 -d 外部数据文件 -r html --reporter-html-export 测试报告名.html
   
   # 示例：
   newman run 批量执行测试用例.postman_collection.json -r html --reporter-html-export 我的第一个测试报告.html
   
   # 如果添加 -r html 就报错！说明: newman-reporter-html 安装失败！
   ```

   





# ==三、使用Postman实现iHRM系统登录模块和员工管理模块接口测试==



# ==Postman参数化（读取外部数据文件）==

当 http请求，使用的 数据有较高相似度，相同的请求时，考虑使用参数化（将数据组织到数据文件中）。

## 数据文件简介

- **CSV：**

  - 优点：
    - 数据组织形式简单，适用于大量数据的场合。
  - 缺点：
    1. 不支持 bool类型数据。（数据被 postman读入后，自动添加 “” 包裹bool值。）
    2. 不支持 多参、少参、无参、错误参数 的接口测试。
    3. 不支持复杂数据类型。（如 嵌套字典、列表等）

  ![image-20210711095615565](./assets/image-20210711095615565.png)

- **JSON：**

  - 优点：
    1. 支持 bool 类型。
    2. 支持 多参、少参、无参、错误参数。
    3. 支持复杂数据类型。
  - 缺点：
    - 对于相同数据量，json数据文件大小远大于 CSV文件。

![image-20210711095830591](./assets/image-20210711095830591.png)



## 导入外部数据文件

### CSV文件

1. 创建 xxx.csv 文件。

2. 将数据写入到 csv文件中。

   - 第一行 写入 的是 数据对应的 “字段名”。
   - 从第二行向后依次是对应的数值，数据间用 英文逗号隔分。

   ![image-20210711101728973](./assets/image-20210711101728973.png)

   ![image-20210711101941523](./assets/image-20210711101941523.png)

3. 在 Postman 中，选中使用数据文件的 用例集，导入数据文件。

   1.  点击用例集名称，使用 Run 按钮，进入 “Runner” 页面。
   2.  使用 “Select File” 按钮选择 xxx.csv 文件。
   3.  点击 预览按钮，校验数据文件是否正确。

![image-20210711102644911](./assets/image-20210711102644911.png)

![image-20210711102431060](./assets/image-20210711102431060.png)

### JSON文件

1. 创建 xxx.json 数据文件

2. 在 数据文件中，按json 语法写入json数据。postman要求，json格式的数据文件，**数据内容的最外层，必须是 [ ]** 。**内部所有的数据用 {} 存储**。（ 建议：使用 json.cn 在线网站编写。）

3. 在 Postman 中，选中使用数据文件的 用例集，导入数据文件。

   1.  点击用例集名称，使用 Run 按钮，进入 “Runner” 页面。
   2.  使用 “Select File” 按钮选择 xxx.json 文件。
   3.  点击 预览按钮，校验数据文件是否正确。

   ![image-20210711105123951](./assets/image-20210711105123951.png)



## 读取数据文件数据

### 理论

**根据使用数据 位置 不同，有两种获取数据文件中数据的方法。**

- 第一种：**请求参数**（请求行、请求头、请求体）中，使用  数据文件中 的数据
  - **使用 {{}}** 包裹 csv 文件 字段名 或 json 文件中的  key 
    - 如： {{username}}  或 {{password}}
- 第二种：**代码**（断言、请求前置脚本）中，使用  数据文件中 的数据
  - 需要借助 postman 提供的 **关键字data** 点 csv 文件的字段名 或 json文件的 key
    - 如： data.username  或  data.password


### 案例

> 需求：批量查询手机号归属地、所属运营商，校验运营商数据正确性
>
> 接口： http://cx.shouji.360.cn/phonearea.php?number=13012345678
>
> 测试数据：
>
> ​			手机号: 13012345678 	运营商: 联通
> ​			手机号: 13800001111 	运营商: 移动
> ​			手机号: 18966778899 	运营商: 电信

1. 测试单个接口，工作中 参数和 响应体 数据对应关系。

   ![image-20210711114155244](./assets/image-20210711114155244.png)

2. 写好数据文件，按 csv 或 json 对应语法的语法格式组织数据。

   ![image-20210711114357631](./assets/image-20210711114357631.png)

3. 替换 上述用例中的 两处：

   1. 归属地：在 代码中。 用 data.字段名 替换
   2. 手机号：在 查询参数中。 用 {{字段名}} 替换。

4. 强调：一旦替换完成，Send 就不再能正常获取 响应数据。（数据必须从数据文件中读取，才能正常发送请求，Send 不具备读取数据文件的功能）

   ![image-20210711114722064](./assets/image-20210711114722064.png)

5. 选择使用数据文件的用例集， 进入 Runner 页面。导入数据文件。运行。

   ![image-20210711114912888](./assets/image-20210711114912888.png)

6. 如果有异常，借助 postman 的控制台，查看。

   ![image-20210711114951207](./assets/image-20210711114951207.png)

   ![image-20210711115031718](./assets/image-20210711115031718.png)

小结：借助 数据文件，实现 **“数据驱动”。**—— 有多少条数据，对应就有多少个 http请求。



### 生成测试报告

步骤：

1. 批量执行测试用例（借助数据文件）

2. 导出 测试用例集 （建议与 数据文件 放在一起）

3. 执行生成测试报告的命令

   ```shell 
   newman run 用例集名称.json -d 数据文件名.csv/.json -r html --reporter-html-export  报告名称.html
   ```

   

# ==iHRM项目实战==

## 简介

- 功能模块

![image-20210711144951189](./assets/image-20210711144951189.png)

- 技术架构

  ![image-20210711145339903](./assets/image-20210711145339903.png)



## 初始化项目环境

### ==新建用例集==

![image-20210711151048576](./assets/image-20210711151048576.png)

### ==创建环境变量==

![image-20210711151430201](./assets/image-20210711151430201.png)

![image-20210711152455941](./assets/image-20210711152455941.png)



## 登录模块

### ==登录成功接口==

#### 请求接口

![image-20210711154411446](./assets/image-20210711154411446.png)

#### ==添加断言==

![image-20210711155006129](./assets/image-20210711155006129.png)

### 其他接口共性分析

1. 由于是同一个接口，因此 他们的 请求方法、URL、请求头 完全一致。
2. 请求体（请求数据），各不相同。
3. 预期结果，大致分为 3 类：
   1. 操作成功！—— 登录成功、多参、全部参数
   2. 抱歉系统繁忙。。。—— 无参
   3. 用户名密码错误！—— 其他情况

### 实现其他接口

![image-20210711161311197](./assets/image-20210711161311197.png)

![image-20210711164021369](./assets/image-20210711164021369.png)

## 员工管理模块

### 总析

1.  **登录成功，返回的 “令牌”，被 添加、查询、修改、删除 员工接口依赖。**
2.  **添加员工成功，返回的 “员工id”，被  查询、修改、删除 员工接口依赖。**

以上的依赖关系，借助 postman关联 和 环境变量 来实现！！

### ==提取令牌（注意空格）==

1. 发送 http 登录请求，在响应体中 得到 data值。

2. 将 data值 拼接 “Bearer” 和 “空格” ，组成一个 合法令牌。

3. 将 拼接后的令牌 环境变量中。（在 Tests 中通过代码写入）

   

   > 令牌是有有效时间的，所以需要用令牌的业务测试，需要将登录令牌放在同一模块里

   ```js
   // 拼接 data的值，添加 Bearer 和 空格。组成合法令牌
   // 获取 响应体, 保存在 jsonData变量中。
   var jsonData = pm.response.json()
   
   // 提取 data的值。保存在 tmp_token 中。
   var tmp_token = jsonData.data
   
   // 拼接 Bearer 和 空格 到 data值的前面。 "Bearer" + " " + tmp_token
   pm.environment.set("env_token", "Bearer"+" "+tmp_token)
   ```

![image-20210711170846822](./assets/image-20210711170846822.png)

### ==添加员工==

![image-20210711172535754](./assets/image-20210711172535754.png)

![image-20210711172504566](./assets/image-20210711172504566.png)

### ==提取添加员工的id==

1. 获取 添加员工成功的 data下面的 id值。

2. 将 员工id，设置 环境变量（代码写入 Tests 中）

   ```js
   // 获取添加员工的 响应体
   var jsonData = pm.response.json()
   // 提取员工id
   var tmp_id = jsonData.data.id
   // 设置到环境变量。
   pm.environment.set("env_emp_id", tmp_id)
   ```

3. 发送 Send 之前，注意先修改 手机号，保证手机号唯一！

4. 点击 “眼睛” 图标 查看。

![image-20210711175034450](./assets/image-20210711175034450.png)

### ==查询员工==

将测试用例中的，请求方法、URL、请求头，写入到 postman对应请求中。

给 **:target** 对应 的 路径参数，填充上 “员工id”的值。（ {{员工id环境变量}} ）

![image-20210711180257649](./assets/image-20210711180257649.png)

### 其他员工操作

修改员工

![image-20210711181523446](./assets/image-20210711181523446.png)

删除员工

![image-20210711182232744](./assets/image-20210711182232744.png)

查询员工列表：

![image-20210711182624138](./assets/image-20210711182624138.png)

## ==批量运行测试用例==

1. 给 每个http请求添加 断言（成功断言）
2. 点击用例集名称，run，进入 Runner 页面。批量执行。
3. 导出 用例集。

## ==生成测试报告==

1. 将环境导出成一个 环境文件。

   ![image-20210711183420655](./assets/image-20210711183420655.png)

2. 将 环境文件，与测试用例集文件，放置到同一个目录下。

3. 执行命令：

   ```shell
   newman run 测试用例集文件.json -e 环境文件.json -r html --reporter-html-export 测试报告名.html
   # 示例：
   newman run iHRM人力资源管理系统测试用例集.postman_collection.json -e 测试环境.postman_environment.json -r html --reporter-html-export iHRM的测试报告.html
   ```

   



> 提醒：在做单接口测试的时候，因为较多雷同的数据，所以可以在postman里复制上一个测试用例文件修改
>
> ​	而在做业务测试的时候，请务必一个一个复制测试用例文档里的内容，防止出错



# 注意！！！！！！

```
本人学习接口测试视频使用的是新版postman，视频中的postman是老版
而图中的value指的是current value即当前值，只在我本地使用，即便我导出环境文件，导出的文件也不会有相应的值，
在老版postman中，INITIAL VALUE(初始值)和当前值是同时显示在表格的，
而在新版，INITIAL VALUE(初始值)不显示在环境或全局变量表格中。

尝试解决：
	仔细研究了我自己的postman，权限上是我创建的，没有问题，界面操作上也没有网上所说的按键
	然后去问了AI，搜CSDN，网络搜索，都没找到相应的解决方法，
	尝试卸载新版本，打开旧版本，旧版本打开无法加载内容，

结果：
	暂时搁置
	
再次尝试：
	postman中将鼠标放入value中，会有一个云朵图案"share",
	在新版本postman，点击"share"，然后再导出环境文件，环境文件中包含有value值
	即-> 点击share就相当将该value值设置为初始值(INITIAL VALUE)
	
结果：
	成功解决


```



## 问题图片及对比：

![1186eb0677a1e61f0dd729e8943f6ea0](.\assets\note\1186eb0677a1e61f0dd729e8943f6ea0.png)

![d7cebacec8d93dac492f9c301b52272a](.\assets\note\d7cebacec8d93dac492f9c301b52272a.png)



## 问题解决：

![QQ_1758042185121](.\assets\note\QQ_1758042185121.png)
![QQ_1758042384049](.\assets\note\QQ_1758042384049.png)

![QQ_1758042411856](.\assets\note\QQ_1758042411856.png)