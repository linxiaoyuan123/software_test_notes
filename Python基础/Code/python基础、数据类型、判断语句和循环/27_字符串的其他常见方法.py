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