# 一个5位数，判断它是不是回文数
a = input('请输入一个五位数: ')
flag = True
for i in range(len(a)//2):
    if a[i] != a[-i - 1]:
        flag = False
        break
if flag:
    print(a + '是回文数')
else:
    print(a + '不是回文数')
