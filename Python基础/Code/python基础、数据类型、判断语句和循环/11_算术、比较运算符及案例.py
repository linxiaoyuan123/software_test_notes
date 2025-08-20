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
