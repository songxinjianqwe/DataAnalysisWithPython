import json
from pandas import DataFrame
# 读写json

obj = """
    {"name": "Wes",
     "places_lived": ["United States","Spain","Genmany"],
     "pet":null,
     "siblings": [{"name":"Scott" , "age":25 , "pet":"Zuko"},
                  {"name":"Katie","age":33,"pet":"Cisco"}]
    }
"""
# 字符串转python对象
result = json.loads(obj)
print(result)
# {'name': 'Wes', 'places_lived': ['United States', 'Spain', 'Genmany'], 'pet': None, 'siblings': [{'name': 'Scott', 'age': 25, 'pet': 'Zuko'}, {'name': 'Katie', 'age': 33, 'pet': 'Cisco'}]}

# python对象转为json
asJson = json.dumps(result)
print(asJson)
# 打印结果同上

# 向DataFrame的构造器中传入一组Json对象
siblings = DataFrame(result['siblings'], columns=['name', 'age'])
print(siblings)
#     name  age
# 0  Scott   25
# 1  Katie   33

