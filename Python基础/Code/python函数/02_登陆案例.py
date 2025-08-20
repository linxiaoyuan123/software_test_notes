"""
需求：
当手机号为”13488888888”，输出"账号正确"；否则"账号错误"。
"""

def login(phone):
    if phone == "13488888888":
        print("账号正确")
    else:
        print("账号错误")

if __name__ =='__main__':
    # login("")
    # login("aaaaaabbbbb")
    # login("1341234567")
    # login("13612345678")
    # login("13488888888")

    # 列表
    test_list = ["", "aaaaaabbbbb","1341234567", "13612345678", "13488888888"]
    for i in test_list:
        login(i)

    # 字典
    print("-" * 80)
    # 提醒：单个参数时，直接使用[“值1”,"值2”, ...]
    # 多个参数时，推荐使用字典[{"参数1": 值1,"参数2": 值1}, {"参数1"：值2, "参数2"：值2}...]
    test_dict = [
        {"phone": ""},
        {"phone": "aaaaaabbbbb"},
        {"phone": "1341234567"},
        {"phone": "13612345678"},
        {"phone": "13488888888"}
    ]
    for i in test_dict:
        login(i.get("phone"))

    #元组
    print("-" * 80)
    test_tuple = ("", "aaaaaabbbbb", "1341234567", "13612345678", "13488888888")
    for i in test_tuple:
        login(i)