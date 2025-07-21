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