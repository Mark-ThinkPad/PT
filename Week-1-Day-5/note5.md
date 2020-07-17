# 第五天笔记

## 上午

- 可迭代:
    - 判断一个对象是可迭代: `print(isinstance([1, 2, 3], Iterable))`
    - 可迭代并不意味着这个对象是迭代器
    - 可迭代意味着可以用在 for...in 语句中

- 迭代器:
    - 是一个可以记住遍历的位置的对象
    - 如果一个对象可以被 next() 函数调用, 那么该对象就是一个迭代器
    - 迭代器有两个基本的方法：iter() 和 next()
    - 字符串，列表或元组对象都可用于创建迭代器
    - 迭代器对象可以使用 for 语句进行遍历

```python
l = [1, 2, 3, 4, 5]
it = iter(l)
for i in range(5):
    print(next(it), end=' ')
print()
for i in it:
    print(i)
```

- 生成器:
    - 使用了 yield 的函数被称为生成器（generator）
    - 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作

```python
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
```

- 一些内置函数: 一批类型转换函数, `len()`等

- 布置的小练习:
    - 设计一个函数, 统计任意的字符在字符串中出现的次数
    - 字符串倒序
    - 数字转汉字大写
    - 数字转汉字货币

## 下午

- 模块: pip换国内镜像源
- 文件: 读, 写, 追加, 读写图片
