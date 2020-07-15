# 实际上只有一个键值对
d = {1:2, 1:3, 1:5}
print(d)
# 遍历字典
for key in d.keys():
    print(key, d[key])
for k, v in d.items():
    print(k, v)

a = {'name': '姓名'}
a['age'] = '年龄'
a['sex'] = '性别, 性感'
print('-----欢迎进入简易英语翻译器-----')
word = input('请输入您要查询的单词: ')

