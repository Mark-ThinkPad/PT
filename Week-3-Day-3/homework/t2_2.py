import json
from lxml import etree

html = etree.parse('51job.html', parser=etree.HTMLParser())
x_path = '//*[@id="resultList"]/div[@class="el"]'
job_list = html.xpath(x_path)
result_list = []

for job in job_list:
    span = job.xpath('.//span')
    dic = {
        # 可以利用 xpath中的内置的函数 normalize-space 去除 节点文本中的换行与前后空白
        'job_title': span[0].xpath('normalize-space(./a)'),
        'job_url': span[0].xpath('./a')[0].get('href'),
        'company_name': span[1].xpath('./a')[0].text,
        'company_url': span[1].xpath('./a')[0].get('href'),
        'job_location': span[2].text,
        'salary': span[3].text,
        'pub_date': span[4].text
    }
    result_list.append(dic)

    #  爬取的数据 保存为JSON格式字符串
    json_str = json.dumps(result_list, ensure_ascii=False)
    with open('job.json', 'w', encoding='utf-8') as f:
        f.write(json_str)
