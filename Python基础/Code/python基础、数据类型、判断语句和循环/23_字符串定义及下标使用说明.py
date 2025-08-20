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
