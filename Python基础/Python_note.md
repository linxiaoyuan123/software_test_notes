# Python学习代码



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

