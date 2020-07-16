# 求最大值
def Max(*args):
    m = 0
    for i in args:
        if m < i:
            m = i
    return m

# 求最小值
def Min(*args):
    m = args[0]
    for i in args:
        if m > i:
            m = i
    return m

# 求幂运算
def Pow(x, y):
    return x ** y

a = 1

def func():
    a = 3
    print(a)

def func1():
    global a
    print(a)

def func2():
    s = 4
    print(s)

def test():
    pass

# 匿名函数
s = lambda x, y: sum(range(x, y+1))

# 推导式
l = [x for x in range(1, 10)]
t = (x for x in range(1, 10))
d = {x: x ** 2 for x in range(11) if x % 2 == 0}

# 迭代器

if __name__ == '__main__':
    print(d)
