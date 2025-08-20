# 定义字典
dict1={
    "name": "jack",
    "age":18,
    "data":[
        "rose","jack","tom"
    ],
    "data2":{
        "sex": 1
    }
}

# 遍历字典key
for key in dict1.keys():
    print(key)

#遍历字典vaLue*****
print("-" * 80)
for value in dict1.values():
    print(value)

# 遍历字典key和vaLue
print("-" * 80)
for key,value in dict1.items():
    print(f"key={key} value={value}")

#需求1：打印输出sex字段值
print("-" * 80)
print(dict1.get("data2").get("sex"))
print("-" * 80)
print(dict1["data2"]["sex"])

#需求2：打印tom(data列表数据的最后一项)
print("-" * 80)
print(dict1.get("data")[-1])
print("-" * 80)
print(dict1["data"][-1])