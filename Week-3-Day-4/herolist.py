import requests
import json

url = 'https://pvp.qq.com/web201605/js/herolist.json'
res = requests.get(url)
print(res.text)
print(type(res.text))

hero_list = json.loads(res.text)
print(type(hero_list))
print(hero_list[0]["cname"])

# 跟上面使用json模块操作的效果是一样的
# 爬取json格式的数据时, 可以直接调用响应对象中.json()方法, 将json字符串转化成Python的数据类型
print(res.json())
