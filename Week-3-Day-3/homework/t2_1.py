import requests

url = 'https://search.51job.com/list/180200,000000,0000,00,9,99,%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE,2,' \
      '1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0' \
      '&dibiaoid=0 '

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/84.0.4147.105 Safari/537.36 '
}

res = requests.get(url, headers=headers)
html_str = res.content.decode(encoding='gbk')
with open('51job.html', 'w', encoding='gbk') as f:
    f.write(html_str)
