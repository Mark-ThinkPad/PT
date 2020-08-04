import pandas as pd
import numpy as np

# 构建 DataFrame
arr = np.random.randint(1, 17, (4, 4))
df = pd.DataFrame(arr, index=['A', 'B', 'C', 'D'], columns=['a', 'b', 'c', 'd'])
print(df)
print(type(df))

# 提取一列
print(df['b'])
print(type(df['b']))

# 添加列
df['e'] = df['b'] + 2
print(df)

# 通过 loc 属性, 根据行索引获取一行数据
print(df.loc['B'])
