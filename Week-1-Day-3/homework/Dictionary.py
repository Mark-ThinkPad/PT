a = {'name': '姓名'}
a['age'] = '年龄'
a['sex'] = '性别, 性感'
print('-----欢迎进入简易英语翻译器-----')
word = input('请输入您要查询的单词: ')
if word in a:
    print(word+':', a[word])
else:
    print('词典尚未收录该单词')
