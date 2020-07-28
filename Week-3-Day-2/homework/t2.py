import requests

url = 'http://tieba.baidu.com/f'
params = {
    'kw': '魔兽世界',
    'ie': 'utf-8'
}

for i in range(10):
    params['pn'] = str(i * 50)
    response = requests.get(url=url, params=params)
    with open('tieba'+str(i+1)+'.html', 'w', encoding='UTF-8') as f:
        f.write(response.content.decode())
