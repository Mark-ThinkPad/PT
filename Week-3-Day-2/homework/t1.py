import requests

url = 'http://tieba.baidu.com/f'
params = {
    'ie': 'utf-8',
    'kw': '魔兽世界'
}
response = requests.get(url=url, params=params)
print(response.content.decode())
with open('tieba.html', 'w', encoding='UTF-8') as f:
    f.write(response.content.decode())
