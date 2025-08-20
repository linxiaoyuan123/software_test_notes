"""
需求：
1。数据常见操作:增（insert）删（delete）改（update）查（select）
    测试数据：
        insert into student values(001, "jack", 18);
        delete from student where id=001,
        update student set name='rose'where id=0θ1;
        select * from student where id=001;
2，请设计程序实现：用户输入字符串为查询操作时，打印”显示查询结果”；
                否则，提醒“当前进行的是非查询操作，需要进行事务提交与回滚"

拆分：
    str.split()  将字符串拆分成数组里的元素

字符串大小写转换：(用于条件识别，防止因大小写问题导致识别不到)
    str.upper() 大写
    str.lower() 小写

"""

#，接受一个字符串
# 测试数据:InSert into student values(oo1,"jack",18)
str1=input("请输入sql语句: ")
#取出空格之前的完整的单词（select/Select/SELECT）、Sql语句是不区分大小写
str2 = str1.split()
# print(str2)
# print(str2[0])

# # 将输入的内容进行大小写转换
# str3 = str2[0].lower()
# str4 = str2[0].upper()

#判定输入的内容为select，打印"显示查询结果"
# if str2[0] == "select":
# if str3 == "select":
# if str4 == "SELECT":

if str1.split()[0].upper() == "SELECT":
    print("显示查询结果")
#否则，提醒"当前进行的是非查询操作，需要进行事务提交与回滚”
else:
    print("当前进行的是非查询操作，需要进行事务提交与回滚")