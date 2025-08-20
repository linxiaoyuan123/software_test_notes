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

