import pandas as pd

# 通过 list 构建 Series 对象
s = pd.Series([1, 2, 3, 4])
print(s, type(s))

# 通过 dict 构建 Series 对象
dic = {
    'python': 90,
    'C++': 80,
    'Java': 70
}
d = pd.Series(dic)
print(d, type(d))
