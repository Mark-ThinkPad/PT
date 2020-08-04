import numpy as np

arr = np.arange(1, 13).reshape(3, 4)

# numpy 中的统计函数
print(np.mean(arr))
print(np.sum(arr))
print(np.max(arr))
print(np.min(arr))
# 标准差
print(np.std(arr))
# 方差
print(np.var(arr))
