import numpy as np

arr = np.arange(1, 13).reshape(3, 4)
arr1 = np.arange(2, 14).reshape(3, 4)

print(arr)
print(arr + arr)
print(arr * arr)

print(arr + arr1)
print(arr * arr1)

print(arr + 1)
print(arr - 10)
