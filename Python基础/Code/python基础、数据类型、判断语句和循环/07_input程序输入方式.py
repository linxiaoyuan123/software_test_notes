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