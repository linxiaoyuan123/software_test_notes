# Python基础



>搜索复习用



### 01_hello_world

```python
print("hello world")
```



### 02_注释

```python
"""
注释：对程序解释和说明、是不会被执行的
①单行注释 #要注释的文字
②多行注释 三对单引号或三对双引号包裹要注释的文字
快捷键：ctrL+/
"""

print("输出文字") # print：打印输出指定内容
```



### 03_变量的定义

```python
"""
变量：保存数据
用法：
变量名＝变量值
说明：
1、变量名自定义，需要遵守变量名命名规则
2、变量值可以为不同类型的数据，字符串、整数、小数（浮点数）、元组、字典、列表等
3、= 表示赋值
需求：
定义2个变量记录学生的年龄和姓名
学生年龄：18
学生姓名：石伟
打印输入学生信息
"""

age = 18

# 注意：字符串类型数据需要使用单引号或双引号包起来

name = "石伟"

print(name,age)
```



### 04_查看变量类型

```python
#学生年龄：18
age = 18
print(type(age))
#type（变量)：查看变量的类型
#学生姓名：石伟
#注意：字符串类型数据需要使用单引号或双引号引起来string
name ="石伟"
print(type(name))
# 打印输入学生信息
#说明：同时打印多个字段信息
print(name, age)
```



### 05_标识符命名规则和风格

```python
"""
标识符规则（需求）：
1、由数字、字母、下划线组成
2、不能是数字开头
3、不能使用python内置关键字
4、区分大小写
5、不建议使用中文

有效：由数字、字母、下划线组成；非数字开头；非python内置关键字
有效数据:name、test_04、___

无效：
1、以数字开头，无效数据：123
2、数字、字母、非下划线组合，无效数据：test-04
3、python内置关键字：if
4、变量定义name、变量使用Name
"""


#变量命名风格
# 1、大驼峰
MyName = "JACK"
# 2、小驼峰
myAge = 18
# 3、下划线(python推荐模式）
my_sex="保密"
print(MyName, myAge, my_sex)
```



### 06_常见数据类型及数据类型查看

```python
"""
常见数据类型分类
    数字型
        整型
        浮点型
        布尔型

    非数字型
        字符串'' ""
        列表[]
        元组()
        集合(不常用)
        字典{}
"""


age = 18
type(age) #整型int

price = 1.5
type(price) #浮点float

a = True
type(a) #布尔bool

name ='jack'
type(name) #字符串str

list1 = [1, 12, 'jack']
type(list1) #列表list

tuple1 = (1, 23)
type(tuple1) #元组tuple

dict1 ={"name": "jack","age":18}
type(dict1) #字典dict
```



### 07_input程序输入方式

```python
"""
需求：打印用户输入姓名和年龄
"""
# name = "jack"
# age = 18
# print(name, age)

name=input("请输入姓名:")
# name = input()   # 建议:一般都设置输入的提醒文字

age = input("请输入年龄:")
#注意：使用input接受到的数据是字符串类型数据

print(name, age)
print(type(name), type(age))
```



### 08_if判断

```python
"""
需求：打印输出用户输入的姓名和年龄；
如果姓名为空，提醒用户‘请输入姓名’，否则、打印用户姓名；
如果年龄为空，提醒用户‘请输入年龄‘，否则、打印用户年龄；

判断：
语法 if 条件:
        条件满足要执行的代码
    else:
        条件不满足要执行的代码

为空判断：is None
不为空:is NOT None

说明：
input返回数据类型为字符串，用户不输入比较值为空字符串''
    比较运算 ==
"""

#需求：打印输出用户输入的姓名和年龄；
name=input("请输入姓名:")
#如果姓名为空，提醒用户‘请输入姓名’，否则、打印用户姓名；
if name =="":  # ==：比较运算
    print("请输入姓名")
else:
    print(name, type(name))

#如果年龄为空，提醒用户‘请输入年龄！，否则、打印用户年龄；
age=input("请输入年龄:")
if age =="":  # ==：比较运算
    print("请输入年龄")
else:
    print(age, type(age))
```



### 09_格式化输出format和f

```python
#format

#需求：接受用户输入的姓名和年龄，并格式化输出
name=input("请输入姓名:")
age = input("请输入年龄： ")
# print("小明今年18岁")

# 说明：
#1、将要替换的数据使用{}占位
#2、引用字符串的format方法进行数据的替换
#3、存在多个要替换的数据时，注意参数数据的匹配
print("{}今年{}岁".format(name, age)) #不推荐

print(f"{name}今年{age}岁") #格式化输出，推荐写法
```



### 10_输入输出案例及类型转换函数

```python
#提示用户输入两个数字num1，num2
num1= int(input("请输入数字:"))#ctrl+ d快速复制上一行代码
print(type(num1))
num2=int(input("请输入数字:"))#注意：input返回数据为str类型数据
                            #解决：使用类型转换函数进行数据类型转换
                            #   int(x) 将х转换为整型数据
                            #   float(x) 将x转换为浮点数
                            #   str(x) 将数据类型转换为字符串
# 打印 num1+ num2结果，格式为xx + xx = xx
#
print("{} + {}= {}".format(num1, num2, num1+num2))  # +：字符串的拼接
print(f"{num1} + {num2} = {num1+num2}")
```



### 11_算术、比较运算符及案例

```python
#提示用户输入用户姓名，并保存到变量中
name= input("请输入姓名:")

#提示用户输入用户年龄，保存到变量中，并转换成整数
age= int(input("请输入年龄:"))

#提示用户输入用户身高，保存到变量中，并转换成浮点数
high =float(input("请输入身高： "))

#在控制台输出用户姓名、年龄、身高对应变量的数据类型
print(type(name), type(age), type(high))

#按照以下格式输出用户信息："姓名:xXX年龄:xXX身高:xxx"
print("姓名:{}年龄:{} 身高:{}".format(name,age,high))
print(f"姓名:{name}年龄:{age}身高:{high}")

#在控制台输出该用户5年之后的年龄，格式：“xXX5年之后的年龄是xx"
print(f"{name}5年之后的年龄是{age+5}")

#在控制台输出该用户现在是否成年，格式："xxx是否成年：xxx"
if age >= 18:
    print(f"{name}是否成年:是")
else:
    print(f"{name}是否成年:否")

"""
算术运算符
    +   加
    -   減
    *   乘
    /   除
    //  求商
    %   取余
    
比较运算符
    ==  相等
    !=  不相等
    >   大于
    >=  大于等于
    <   小于
    <=  小于等于
"""
```



### 12_逻辑运算符

```python
# 闰年判断程序（闰年是能被4整除，但不能被100整除的；或者能被400整除的年份)
#输入一个有效的年份，判断是不是闰年year
year = int(input("请输入年份:"))
#如果是闰年，则打印"xxxx年是闰年”；否则打印"xxxx年不是闰年”
#闰年是能被4整除，但不能被100整除的；或者能被400整除的年份
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year}年是闰年")
else:
    print(f"{year}年不是闰年")
#如输入"2018"，将打印"2018年不是闰年”

"""
逻辑运算符
    and 与
    or 或
    not 非
    
运算符优先级
    灵活利用小括号()
"""
```



### 13_if_else基本用法

```python
"""
python中对缩进要求十分严格
Tab相当四个空格，选其一
shift + Tab 回退缩进

判定：
语法：
if 条件:
    条件满足之后要执行的代码块
else:
    条件不满足之后要执行的代码块
测试：
①测试数据满足条件，得到对应预期结果
②测试数据不满足条件，得到对应预期结果



定义一个整数变量记录年龄
判断是否满18岁(>=）
如果满18岁，允许进网吧嗨皮
如果未满18岁，提示回家写作业
"""
age =int(input("请输入年龄:"))
if age >= 18:
    print("允许进网吧嗨皮")
else:
    print("回家写作业")
```



### 14_if语句与and结合

```python
"""
需求：
1，获取用户输入的用户名和密码
2、判断用户名是αdmin并且密码是123456时，在控制台输出：登录成功！
3，否则在控制台输出：登录信息错误
"""

username=input("请输入用户名：")
password= input("请输入密码: ")
if username == "admin" and password == "123456":
    print("登录成功")
else:
    print("登录信息错误")

#设计测试用例
"""
caseθ1：登录成功（用户名和密码正确）
case02：登录失败、提示：登录信息错误（用启名为空)
case03：登录失败、提示：登录信息错误（用户名未注册）
case04：登录失败、提示：登录信息错误（密码为空）
case05：登录失败、提示：登录信息错误（密码与账号不匹配）
"""
```



### 15_if语句与or结合

```python
"""
1．定义两个整数变量python_score、c_score，使用input获取成绩编写代码判断成绩
2、要求只要有一门成绩>=60分就输出合格
"""


python_score= int(input("请输入python分数: "))
c_score= int(input("请输入c分数: "))

if python_score >= 60 or c_score >= 60:
    print("合格")
else:
    print("不合格")


#条件依赖，用判定表
```



### 16_if语句与not结合

```python
"""
1，定义一个浮点数变量high，使用input获取身高信息
2，要求身高低于1，2米，提示免票；否则，提示请购买儿童票。
"""

high=float(input("请输入身高信息:"))
#方式一：
# if high <= 1.2:
#     print("免票")
# else:
#     print("请买票")


#方式二:
if not high > 1.2:
    print("免票")
else:
    print("买票")
```



### 17_elif

```python
"""
技术：多重条件eLif
语法：
if 条件:

elif 条件:
...
else：

需求：
定义score变量记录考试分数
如果分数是大于等于90分显示优
如果分数是大于等于80分并且小于90分显示良
如果分数是大于等于70分并且小于80分显示中
如果分数是大于等于60分并且小于70分显示差
其它分数显示不及格
"""

score = int(input("请输入考试分数："))

# if score >= 90:
#     print("优秀")
# #可以用and写条件
# elif 80 <= score < 90:
#     print("良")
# elif 70 <= score < 80:
#     print("中")
# elif 60 <= score < 70:
#     print("差")
# else:
#     print("不及格")


#可以进行优化，因为if语句是自上而下判断的
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良")
elif score >= 70:
    print("中")
elif score >= 60:
    print("差")
else:
    print("不及格")
```



### 18_if的嵌套

```python
"""
需求：
定义布尔型变量has_ticket表示是否有车票
定义整型变量knife_length表示刀的长度，单位：厘米
首先检查是否有车票，如果有，才允许进行安检
安检时，需要检查刀的长度，判断是否超过20厘米
如果超过20厘米，提示刀的长度，不允许上车
如果不超过20厘米，安检通过
如果没有车票，不允许进门
"""

# has_ticket = True
# knife_length=int(input("请输入刀的长度:"))
# if has_ticket is True:
#     print("请进站进行安检")
#     if knife_length <= 20:
#         print("安检通过")
#     else:
#         print("安检不通过")
# else:
#     print("不允许进门")



#优化上面车票代码，bool类型转换
has_ticket=bool(input("请输入是否有票:"))
#bool(x)：将x转换为布尔型数据
#         注意：有数据就为真，转换之后结果为True；没数据（不输入）时，转换之后结果为Fasle
if has_ticket:
    print("请进站进行安检")
    knife_length = int(input("请输入刀的长度:"))
    if knife_length <= 20:
        print("安检通过")
    else:
        print("安检不通过")
else:
    print("不允许进门")
```



### 19_while循环和赋值运算符

```python
#打印100遍“媳妇儿，我错了"
#while循环：处理重复执行的代码
"""
语法：
计数器/变量 ＝ 初始值
while 条件:
    1、要重复执行的代码
    2、修改计数器值(注意：忘记修改、会形成死循环)
"""

i = 1

while i <= 10:
    print("媳妇儿,我错了")
    #i=i+1
    i+=1

"""
赋值运算符
    =   赋值
    +=  a+=b a=a+b 加后赋值
    -=  a-=b a=a-b 减后赋值
    *=  a*=b a=a*b 乘后赋值
    /=  a/=b a=a/b 除后赋值
    %=  a%=b a=a%b 取余赋值
"""
```



### 20_while循环与if语句结合

```
i = 0

while i <=5:
    score = int(input("请输入考试分数:"))
    if score >= 90:
        print("优秀")
    elif score >= 80:
        print("良")
    elif score >= 70:
        print("中")
    elif score >= 60:
        print("差")
    else:
        print("不及格")
    i+=1
```



### 21_for循环

```python
i=0

while i<10:
    print("我要好好学习")
    i+=1
    #注意：修改计数器的值

print("-" * 80)

for i in range(10): #range(10)产生0~10之间的数字、注意10是取不到的
    print(f"这是第{i}次,我要好好学习")
```



### 22_for循环实现判断闰年和debug

```python
# 代码格式化:ctrl + alt + L   (清除规范波浪线)

"""
需求：
闰年判断程序（闰年是能被4整除，但不能被100整除的；或者能被400整除的年份)
"""


# i=0
# while i< 3:
#     year = int(input("请输入年份: "))
# if (year % 400 == 0) or (year % 4 == and year % 100 != 0):
#     print("闰年")
# else:
#     print("不是闰年")
#     i+=1

for i in range(3): #遍历
    year = int(input("请输入年份: "))
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("闰年")
    else:
        print("不是闰年")


"""
debug
    debug 调试的作用是用来排查代码中的错误的。
    
    1、打断点
        在pycharm中打断点只需要在代码和行号之间点击，出现的红色圆点，就是断点
        再次点击红色圆点可以取消断点
        在pycharm中，如果第一行是注释，需要两个断点
        断点的作用，是代码执行停留的地方
        
    2、右键Debug运行代码
    
    3、点旋转箭头走下一步

"""
```



### 23_字符串定义及下标使用说明

```python
"""
在Python中支持负数索引(从右到左)

字符串：
1、定义：使用单双引号进行定义
2、操作：依据索引/下标进行操作（第一个元素的下标值为0,最后一个元素的下标为-1）
3、计算字符长度：len(字符串)
4、使用for和while进行数据的遍历

需求：
1. str1 = 'abcdefg'
2，打印字符串中第一个位置的字符
3，打印字符串中最后一个位置的字符
4．打印字符串长度
5，分别使用for循环和while循环对字符串进行遍历

"""

str1 = "abcdefg"
print(str1[0]) # a
print(str1[-1]) #g
print(len(str1)) # 7
print(str1[len(str1)-1]) #g  末尾元素的下标 = 字符串长度 - 1

#分别使用for循环对字符串进行遍历
print("*" * 80)

for i in str1:
    print(i)

#分别使用while循环对字符串进行遍历
print("*" * 80)

i=0
while i< len(str1):
    print(str1[i])
    i+=1

```



### 24_字符串切片操作

```python
"""
技术点：字符串切片
作用：从字符串中提取一部分数据
用法：字符串[开始下标值：结束下标值：步长]
说明：
1、开始下标值计数时从θ开始，为0时可以省略不写，如α[：5:1]
2、结束下标值末尾是用-1表示，为-1时可以省略不写，如a[1::1]
3、步长是取值的间隔，默认为1、可以省略不写

注意：
    结束下标位置对应的字符不会被截取到
"""

# 需求:
#1.定义字符串str1='abcdefg'
str1 = "abcdefg"

#2．使用切片打印输出‘cde″
print(str1[2:5:1])
#说明：步长默认为1（可以省略不写）
print(str1[2:5])

#3。使用切片打印输出‘abcde'
print(str1[0:5])
#下标值从0开始计数（字符串起始位置）
print(str1[:5])
#起始位置为取值0时，开始下标可以不写

#4，使用切片打印输出'abcdefg'
print(str1[:])
#5.使用切片打印输出‘aceg'
print(str1[::2])#需要设置步长为2

#6.使用切片打印输出'abcdef'
print(str1[:-1])
```



### 25_字符串去除两端空格

```python
"""
需求：
1．现有字符串数据：'     15000000000   '
2、请设计程序，去除字符串两端的空白字符



字符串的strip方法，只能去除两边的空格，中间空格无法去除
"""


str1=input("请输入测试字符串内容:")
print("去除空格前:",str1)
print("去除空格后：",str1.strip())
```



### 26_字符串大小写转换及拆分

```python
"""
需求：
1。数据常见操作:增（insert）删（delete）改（update）查（select）
    测试数据：
        insert into student values(001, "jack", 18);
        delete from student where id=001,
        update student set name='rose'where id=0θ1;
        select * from student where id=001;
2，请设计程序实现：用户输入字符串为查询操作时，打印”显示查询结果”；
                否则，提醒“当前进行的是非查询操作，需要进行事务提交与回滚"

拆分：
    str.split()  将字符串拆分成数组里的元素

字符串大小写转换：(用于条件识别，防止因大小写问题导致识别不到)
    str.upper() 大写
    str.lower() 小写

"""

#，接受一个字符串
# 测试数据:InSert into student values(oo1,"jack",18)
str1=input("请输入sql语句: ")
#取出空格之前的完整的单词（select/Select/SELECT）、Sql语句是不区分大小写
str2 = str1.split()
# print(str2)
# print(str2[0])

# # 将输入的内容进行大小写转换
# str3 = str2[0].lower()
# str4 = str2[0].upper()

#判定输入的内容为select，打印"显示查询结果"
# if str2[0] == "select":
# if str3 == "select":
# if str4 == "SELECT":

if str1.split()[0].upper() == "SELECT":
    print("显示查询结果")
#否则，提醒"当前进行的是非查询操作，需要进行事务提交与回滚”
else:
    print("当前进行的是非查询操作，需要进行事务提交与回滚")
```



### 27_字符串的其他常见方法

```python
"""

1、替换：
    字符串.replace(原字符串，新子字符串)

2、连接：(一般用于将列表按指定子字符合并为字符串)
    字符串.join(一般为列表)

3、判断是否为纯数字：(返回值为布尔值)
    字符串.isdigit()

"""

str1 = "hello Python and itcast and itheima"

#替换
print(str1.replace("and", "or"))

#连接
print("+".join(str1.split()))

#判断是否为纯数字
a = '1'
b = 'a1'
print(a.isdigit())
print(b.isdigit())
```



### 28_列表定义与增删改查操作

```python
"""

目前的登录只能支持一个账号的判断，如果有多个账号
需要进行判断怎么处理?


技术点：列表操作
定义:
①列表名=[]
②列表名=[字符串，整型，浮点数，布尔型，列表[]，字典{}，元组()]

也可以通过类实例化方式定义：列表名 = list()      了解即可

操作：
①新增数据：列表名.append(数据)
②删除数据：列表名.pop(下标)
③修改数据：列表名[下标]＝新数据
④ 查询数据：列表名
            列表名[下标]
"""
list1 = []
list2 = [18, 176.6, True, "jack"]
print(list1, type(list1))
print(list2, type(list2))

# 追加数据
list2.append("rose")
print(list2)

# 删除数据
#删除末尾数据
list2.pop(-1)
print(list2)

# 删除第一个数据
list2.pop(0)
print(list2)

#删除指定下标的数据
list2.pop(1)
print(list2)

##下标越界错误
# print("-" * 80)
# list2.pop(100)
# print(list2)  # pop index out of range

# 修改数据
list2[-1]= "rose"
print(list2)

```



### 29_案例列表实现登陆测试数据管理

```python
# 需求:
#定义列表存储测试账号
#遍历列表数据进行测试账号校验
#当手机号为"13488888888"，输出"账号成功"；否则"账号错误"。


#定义列表
list1 = ["13488888888","aaaaaabbbbb","1341234567","", "13566666666"]

#遍历列表数据
for i in list1:
    print(i)
    if i == "13488888888":
        print("账号正确")
    else:
        print("账号错误")
```



### 30_字典定义与增删改查操作

```python
"""
该如何存储更多的测试数据？比如：手机号、密码、验
证码等

还可以通过类实例化方式定义:
    字典名 = dict()

"""

# 定义字典
dict1 = {}
# 字典key是字符串类型数据，具有唯一性
dict2 = {
    "name": "jack",
    "age": 18
}
print(dict1, type(dict1))
print(dict2, type(dict2))

#新增(修改)数据，有键则修改，无键则添加
#语法：字典名称["key键"]=数据
dict2["high"] = 176.5
print(dict2)

# 刪除数据
#删除存在key对应数据
dict2.pop("high")
print(dict2)

# #、删除数据时key不存在
# print("-" * 80)
# dict2.pop("sex")  # KeyError
# print(dict2)

#査询数据
#使用key(若查询不到，会KeyError报错)
print(dict2["high"])
# 使用get方法(若查询不到，则返回None)
print(dict2.get("high"))
```



### 31_字典数据遍历及查看

```python
# 定义字典
dict1={
    "name": "jack",
    "age":18,
    "data":[
        "rose","jack","tom"
    ],
    "data2":{
        "sex": 1
    }
}

# 遍历字典key
for key in dict1.keys():
    print(key)

#遍历字典vaLue*****
print("-" * 80)
for value in dict1.values():
    print(value)

# 遍历字典key和vaLue
print("-" * 80)
for key,value in dict1.items():
    print(f"key={key} value={value}")

#需求1：打印输出sex字段值
print("-" * 80)
print(dict1.get("data2").get("sex"))
print("-" * 80)
print(dict1["data2"]["sex"])

#需求2：打印tom(data列表数据的最后一项)
print("-" * 80)
print(dict1.get("data")[-1])
print("-" * 80)
print(dict1["data"][-1])
```



### 32_案例字典优化登陆案例

```python
"""

需求：
1、定义字典存储测试数据，包含账号和密码
        提示:[{"username":"13488888888”","password":"123456”},
            {"username": ", "password":"123456"}]
2、遍历数据进行测试账号和密码校验
3、当手机号为"13488888888”且密码为"123456"时，输出"登录成功"；否则"错误或密码错误"。

"""

test_data = [
    {
    "username":"13488888888",
    "password":"123456"
    },
    {
    "username":"",
    "password":"123456"
    },
    {
    "username":"13488888888",
    "password":""
    },
]

for i in test_data:
    if i.get("username") == "13488888888" and i.get("password") == "123456":
        print("登录成功")
    else:
        print("账号或密码错误")

```



### 33_元组定义及查询

```python
"""
元组定义还可以通过类实例化方式定义
    元组名 = tuple()

元组和列表一样，都可用于存储多个数据，不同之处在于元组的元素不能修改

"""

# 定义元组
tuple1 = ("jack", 18, 176.5, {"age": 20}, [1, 2, 3])

#打印元组及元组类型
print(tuple1, type(tuple1))

#打印元组指定数据：通过下标获取
print(tuple1[2])

#使用元组交换两个变量的值
num1 = 100
num2 = 200
num2, num1 = num1, num2
print(num1)
print(num2)

#定义元组存储测试账号
print("-" * 80)
tuple2 = ("13488888888","","aaaaaabbbbb","1341234567","13612345678")
#遍历元组数据进行测试账号校验
for i in tuple2:
    #当手机号为“13488888888"，输出“账号成功"；否则"账号错误"
    if i== "13488888888":
        print("账号正确")
    else:
        print("账号错误")
```



### 34 _集合(了解)

```python
"""
集合的定义

    说明:集合中的数据是没有重复的，主要应用列表中的数据去重

    定义方式：
        Set1 = {1,2,3}

        set2 = set()

"""


# 前置随机数使用
# 导包
import random

test_list = []

#产生指定范围的随机数
i=0
# 使用随机数生成10 个1-20之间的随机数
while i<10:
    # print(random.randint(1, 20))
    test_list.append(random.randint(1, 20))
    i+=1
print(test_list)
#对列表中的数据进行去重
print(set(test_list))
# 利用集合数据唯一性特点来实现对列表数据去重
```



# Python函数



### 01_函数的定义、调用和默认值.py

```python
"""
技术点：
（def是define缩写）
函数：实现了一定功能、需要被重复调用的代码
定义：
def 函数名(参数1, 参数2, ...):  #形参
    pass
说明：函数名符合标识符命名规则(1、字母、数字、下划线 2、不能以数字开头 3、不能为python关键字)
调用：函数名(参数=参数值)          # 实参

程序入口:__name__=='__main__'
(作用：该语句出现后，程序就不会自上而下运行了，它会规定先执行程序入口的内容，再执行其他内容）
快捷写法：直接打一个main然后tab即可

需求：
当手机号为”13488888888”，输出"账号正确"；否则"账号错误"。
"""

def login(phone="13488888888"):
    if phone == "13488888888":
        print("账号正确")
    else:
        print("账号错误")

if __name__ =='__main__':
    login("")
    login("aaaaaabbbbb")
    login("1341234567")
    login("13612345678")
    login("13488888888")
    login() #若设置了函数的默认值，则直接调用函数时，会使用形参的默认值

```



### 02_登陆案例.py

```python
"""
需求：
当手机号为”13488888888”，输出"账号正确"；否则"账号错误"。
"""

def login(phone):
    if phone == "13488888888":
        print("账号正确")
    else:
        print("账号错误")

if __name__ =='__main__':
    # login("")
    # login("aaaaaabbbbb")
    # login("1341234567")
    # login("13612345678")
    # login("13488888888")

    # 列表
    test_list = ["", "aaaaaabbbbb","1341234567", "13612345678", "13488888888"]
    for i in test_list:
        login(i)

    # 字典
    print("-" * 80)
    # 提醒：单个参数时，直接使用[“值1”,"值2”, ...]
    # 多个参数时，推荐使用字典[{"参数1": 值1,"参数2": 值1}, {"参数1"：值2, "参数2"：值2}...]
    test_dict = [
        {"phone": ""},
        {"phone": "aaaaaabbbbb"},
        {"phone": "1341234567"},
        {"phone": "13612345678"},
        {"phone": "13488888888"}
    ]
    for i in test_dict:
        login(i.get("phone"))

    #元组
    print("-" * 80)
    test_tuple = ("", "aaaaaabbbbb", "1341234567", "13612345678", "13488888888")
    for i in test_tuple:
        login(i)
```



### api.login.py(06_案例)

```python
# 03_函数返回值、导包、断言用
import random


def login(phone):
    if phone == "13488888888":
        # print（"账号正确"）#问题：输出结果是直接打印在控制台，后续业务代码是没有办法继续处理该数据
        return "账号正确" # 解决：通过return返回程序处理结果，供后续业务继续处理
    else:
        # print("账号错误")
        return "账号错误"

# 04_test_login
# 登陆需求01
def fun_login(phone):
    if phone == "13488888888":
        return "Success"
    else:
        return "ERROR"

# 登陆需求02
def fun_login2(phone,pwd):
    if phone == "13488888888" and pwd == "123456":
        return "登录成功"
    else:
        return "手机号或密码错误"


#06_案例_参数指定个数及指定范围内的随机数
"""
需求：定义函数func，
可以按照如下要求生成随机数：
1.该函数可以接收三个参数；
    -参数1，为生成随机数的个数；
    -参数2和参数3为生成的随机数的范围；
    -参数2和参数3，如果不传递，默认生成1-1000之间的随机数
2.要求生成的随机数不能重复。
3.将生成的随机数列表进行返回。
"""
def func(count, start=1, end=1000):
    test_data=[]
    while True: #不确定循环次数
            num = random.randint(start,end)
            if num not in test_data:
                test_data.append(num)
                if len(test_data) == count:
                    return test_data

if __name__ == '__main__':
    print(func(10, 1, 20))
```



### scripts.03_函数返回值、导包、断言

```python
"""
api指接口，scripts指测试脚本

模块的概念：
    每一个以 `.py` 结尾的Python.代码文件都是一个模块
    模块名同样也是一个标识符，需要符合标识符的命名规则
    在模块中定义的 `全局变量、函数、类` 都是提供给外界直接使用的 `工具`
    模块就好比是工具包，要想使用这个工具包中的工具，就需要先导入模块

模块的导入方式：
    1、import 导入
    2、from ... import 导入
    (若模块名字太长，可以使用import 模块名1 as 模块别名，给模块取个简单名字，以便使用)


包的概念：
    包：(Package)是一个包含多个模块的特殊目录
    目录下有一个特殊的文件_init_py
    包名的命名方式和变量名一致
    作用：python文件较多时，方便分目录管理维护(python Package)

导包的常用方式：
    #方式一
    import 包名.模块名
    包名.模块名.工具名
    # 方式二
    from 包名 import 模块名
    模块名.工具名
    # 方式三
    from 包名.模块名 import 工具名
    工具名
"""

#导入登陆函数
# from python函数.api.login import login
# 快捷导包 ctrl + alt + 空格
from python函数.api.login import login

#调用
print(login("13488888888"))

# 断言 assert(正确无反应，但错误会报错)
"""
断言：自动判断实际结果和预期结果
用法：
1、断言相等：assert 预期结果 == 实际结果
2、断言包含：assert 预期结果 in 实际结果  （只要返回值中包含有预期结果中的内容，则PASS）
结果：
通过PASS：不显示
失败FALL：报错并提示"AssertionError'
"""
assert "账号正确" == login("13488888888")

if __name__ == '__main__':
    assert "账号正确" == login("13488888888")
    assert "账号错误" == login("13466666666")
    assert "错误" in login("13466666666")
```



### scripts.04_test login

```python
#导包
#from 包.模块 import 函数或类
from python函数.api.login import fun_login

test_data = ["", "13488888888", "13412345678"]
for i in test_data:
    if i == "13488888888":
        assert "Success" == fun_login(i)
    else:
        assert "Error".upper() == fun_login(i)
```



### scripts.05_test login2

```python
# 导包
from python函数.api.login import fun_login2
#准备测试数据
test_data =[
    {
        "username":"13488888888",
        "password":"123456"
    },
    {
        "username":"",
        "password": "123456"
    },
    {
        "username":"13488888888",
        "password": ""
    }
]

# 遍历数据，调用方法获取实际结果
for i in test_data:
    print(f"测试账号为:{i.get('username')} 测试密码为:{i.get('password')} 测试结果:{fun_login2(i.get('username'),i.get('password'))}")
    if i.get('username')=="13488888888" and i.get('password')=="123456" :
        assert "成功" in fun_login2(pwd=i.get("password"),phone=i.get("username"))
    else:
        assert "错误" in fun_login2(pwd=i.get("password"),phone=i.get("username"))
```



### 07_异常及异常处理try except finally

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

