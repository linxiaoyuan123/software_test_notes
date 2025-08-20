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