# 代码格式化:ctrl + alt + L   (清除规范波浪线)

"""
需求：
闰年判断程序（闰年是能被4整除，但不能被100整除的；或者能被400整除的年份)
"""


# i=0
# while i< 3:
#     year = int(input("请输入年份: "))
# if (year % 400 == 0) or (year % 4 == and year % 100 != 0):
#     print("闰年")
# else:
#     print("不是闰年")
#     i+=1

for i in range(3): #遍历
    year = int(input("请输入年份: "))
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("闰年")
    else:
        print("不是闰年")


"""
debug
    debug 调试的作用是用来排查代码中的错误的。
    
    1、打断点
        在pycharm中打断点只需要在代码和行号之间点击，出现的红色圆点，就是断点
        再次点击红色圆点可以取消断点
        在pycharm中，如果第一行是注释，需要两个断点
        断点的作用，是代码执行停留的地方
        
    2、右键Debug运行代码
    
    3、点旋转箭头走下一步

"""