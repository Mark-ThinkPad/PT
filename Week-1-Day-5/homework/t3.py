# 题目三
user = {'name': '', 'age': '', 
        'sex': '', 'ID Card': ''}
print('''
----------------------
-----用户管理系统-----
----------------------
-------报名开始-------
''')

user['name'] = input('请输入用户名: ')
user['age'] = input('请输入年龄: ')
user['sex'] = input('请输入性别: ')
user['ID Card'] = input('请输入身份证号码: ')

user_info = [k+': '+v+'\n' for k, v in user.items()]

with open('客户资料.txt', 'w', encoding='UTF-8') as f:
    f.writelines(user_info)

print('用户信息保存成功')
