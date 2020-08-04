import numpy as np

arr = np.arange(1, 13).reshape(3, 4)
arr2 = np.arange(1, 13).reshape(4, 3)

print(arr)
print(arr2)

# 矩阵乘法
print(arr.dot(arr2))
print(arr @ arr2)
