class A(object):
    def test(self):
        print('test')

    def hello(self):
        print('Hello, I am A')


class B(object):
    def demo(self):
        print('demo')

    def hello(self):
        print('Hello, I am A')


class D(object):
    def hello(self):
        print('Hello, I am D')


class E(D):
    pass


# 多继承
class C(E, A, B):
    pass


if __name__ == "__main__":
    c = C()
    c.test()
    c.demo()
    c.hello()
    print(C.__mro__)
