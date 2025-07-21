"""
1．定义两个整数变量python_score、c_score，使用input获取成绩编写代码判断成绩
2、要求只要有一门成绩>=60分就输出合格
"""


python_score= int(input("请输入python分数: "))
c_score= int(input("请输入c分数: "))

if python_score >= 60 or c_score >= 60:
    print("合格")
else:
    print("不合格")


#条件依赖，用判定表