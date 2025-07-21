


i = 0

while i <=5:
    score = int(input("请输入考试分数:"))
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
    i+=1