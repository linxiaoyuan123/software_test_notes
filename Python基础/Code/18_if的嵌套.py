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