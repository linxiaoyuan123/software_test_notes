"""
集合的定义

    说明:集合中的数据是没有重复的，主要应用列表中的数据去重

    定义方式：
        Set1 = {1,2,3}

        set2 = set()

"""


# 前置随机数使用
# 导包
import random

test_list = []

#产生指定范围的随机数
i=0
# 使用随机数生成10 个1-20之间的随机数
while i<10:
    # print(random.randint(1, 20))
    test_list.append(random.randint(1, 20))
    i+=1
print(test_list)
#对列表中的数据进行去重
print(set(test_list))
# 利用集合数据唯一性特点来实现对列表数据去重