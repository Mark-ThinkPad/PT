# 判断回文数
a = '12321'
flag = True
for i in range(len(a)//2):
    if a[i] != a[-i-1]:
        flag = False
        break
if flag:
    print(a + '是回文数')
else:
    print(a + '不是回文数')

# 设计一个函数, 统计任意的字符在字符串中出现的次数
statistics = lambda a, b: a.count(b)
print(statistics('12321', '2'))

# 字符串倒序
reverse = lambda x: x[::-1]
print(reverse('Hello, World!'))

# 数字转汉字大写
def trans(a: int) -> str:
    a = str(a)
    convert = {'1': '壹', '2': '贰', '3': '叁', '4': '肆', 
               '5': '伍', '6': '陆', '7': '柒', '8': '捌', 
               '9': '玖', '0': '零'}
    res = ''
    for i in a:
        res += convert[i]
    return res

print(trans(12345))

# 数字转汉字货币
def yuan(a: int) -> str:
    a = str(a)
    unit = ['元', '拾', '佰', '仟', '万', 
            '拾万', '佰万', '仟万', '亿']
    word = ['零', '壹', '贰', '叁', '肆', 
            '伍', '陆', '柒', '捌', '玖']
    res = ''
    # l = len(a)
    # for i in a:
    #     l -= 1
    #     i = int(i)
    #     res += word[i] + unit[i]
    return res

print(yuan(12345))
