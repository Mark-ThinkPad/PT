import pandas as pd
import numpy as np

arr = np.random.randint(1, 17, (4, 4))
df = pd.DataFrame(arr, index=['A', 'B', 'C', 'D'], columns=['a', 'b', 'c', 'd'])
print(arr)
print(df)


# pandas 的 apply 方法
# 一个参数的函数
def fn(num):
    return num * num

print(df.apply(fn))

# 多个参数的函数
def fn1(num, a, b):
    return num * num - a * b


print(df.apply(fn1, a=10, b=10))
