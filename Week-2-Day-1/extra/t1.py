# 最直接的方法
for i in range(20):
    for j in range(30):
        print('*', end='')
    print()

# 字符串乘法
print(('*' * 30 + '\n') * 20)

# 老"炫技"了
print('\n'.join(['*' * 20] * 30))
