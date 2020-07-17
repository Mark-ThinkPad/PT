from collections.abc import Iterable

# 判断一个对象是可迭代
# 可迭代并不意味着这个对象是迭代器
# 可迭代意味着可以用在 for...in 语句
print(isinstance([1, 2, 3], Iterable))
print(isinstance((1, 2, 3), Iterable))
print(isinstance({1: 4, 2: 5, 3: 6}, Iterable))
print(isinstance(1, Iterable))
print(isinstance('ABCD', Iterable))

# 迭代器: 是一个可以记住遍历的位置的对象
# 如果一个对象可以被 next() 函数调用, 那么该对象就是一个迭代器
# 迭代器有两个基本的方法：iter() 和 next()
# 字符串，列表或元组对象都可用于创建迭代器
l = [1, 2, 3, 4, 5]
it = iter(l)
for i in range(5):
    print(next(it), end=' ')
print()
# 迭代器对象可以使用常规 for 语句进行遍历
for i in it:
    print(i)

# 生成器: 使用了 yield 的函数被称为生成器（generator）
# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作
# 简单的生成器
g = (x * x for x in range(10))
print(g)
# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1

f = fib(10)
print(f)
for i in f:
    print(i, end=' ')
print()
