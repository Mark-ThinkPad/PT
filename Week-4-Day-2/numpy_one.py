import numpy as np

# np.array 方法支持将列表转换为 ndarray 对象
li = [1, 2, 3, 4, 5, 6]
arr = np.array(li)

print(arr, type(arr))
print(arr.ndim)
print(arr.size)
print(arr.shape)

li2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr2 = np.array(li2)

print(arr2, type(arr2))
print(arr2.ndim)
print(arr2.size)
print(arr2.shape)

arr3 = np.random.rand(3, 4)
print(arr3)

arr4 = np.random.randint(1, 10, (3, 4))
print(arr4)

arr5 = np.arange(1, 10)
print(arr5)
print(arr5.reshape(3, 3))
# 支持链式调用
print(np.arange(20).reshape(4, 5))
