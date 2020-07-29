import requests
from lxml import etree

url = 'http://www.sina.com.cn'
response = requests.get(url)
html_str = response.content.decode()
html = etree.HTML(html_str)
xpath = '//*[@id="syncad_0"]//a'

for a in html.xpath(xpath):
    response = requests.get(a.get('href'))
    html_str = response.content.decode()
    html = etree.HTML(html_str)
    p_list = html.xpath('//*[@id="article"]/p')
    try:
        print(a.text, a.get('href'), '|'.join([p.text for p in p_list]))
    except:
        pass
