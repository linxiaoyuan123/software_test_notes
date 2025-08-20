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