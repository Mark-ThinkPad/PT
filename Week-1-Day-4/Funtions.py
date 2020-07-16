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


print(Max(1, 2, 3, 4, 5))
print(Min(1, 2, 3, 4, 5))
print(Pow(2, 3))

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


if __name__ == '__main__':
    func()
    func1()
    func2()
    print(__name__)
