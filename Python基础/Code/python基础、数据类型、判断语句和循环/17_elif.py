"""
技术：多重条件eLif
语法：
if 条件:

elif 条件:
...
else：

需求：
定义score变量记录考试分数
如果分数是大于等于90分显示优
如果分数是大于等于80分并且小于90分显示良
如果分数是大于等于70分并且小于80分显示中
如果分数是大于等于60分并且小于70分显示差
其它分数显示不及格
"""

score = int(input("请输入考试分数："))

# if score >= 90:
#     print("优秀")
# #可以用and写条件
# elif 80 <= score < 90:
#     print("良")
# elif 70 <= score < 80:
#     print("中")
# elif 60 <= score < 70:
#     print("差")
# else:
#     print("不及格")


#可以进行优化，因为if语句是自上而下判断的
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良")
elif score >= 70:
    print("中")
elif score >= 60:
    print("差")
else:
    print("不及格")