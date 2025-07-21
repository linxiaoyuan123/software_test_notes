"""
1，定义一个浮点数变量high，使用input获取身高信息
2，要求身高低于1，2米，提示免票；否则，提示请购买儿童票。
"""

high=float(input("请输入身高信息:"))
#方式一：
# if high <= 1.2:
#     print("免票")
# else:
#     print("请买票")


#方式二:
if not high > 1.2:
    print("免票")
else:
    print("买票")