class Tool:
    # 类属性
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    # 类方法
    # cls指向的就是调用该方法的类
    @classmethod
    def get_count_display(cls):
        print(f'工具类已经生成了{cls.count}个实例')


if __name__ == '__main__':
    hammer = Tool('锤子')
    tq = Tool('铁锹')
    print(Tool.count)
    print(hammer.count)
    print(tq.count)

    # 为hammer实例, 绑定了一个count的实例属性, 值为10
    # 并不会给类属性count赋值
    hammer.count = 10
    print(Tool.count)  # 2
    print(hammer.count)  # 10
    print(tq.count)  # 2

    # 把hammer的实例属性count从内存中销毁了
    del hammer.count
    print(Tool.count)  # 2
    print(hammer.count)  # 2
    print(tq.count)  # 2

    Tool.get_count_display()
