# 第七天笔记

## 上午

- 多继承
    - 通过多继承, 子类可以调用多个父类中的方法
    - 多继承的查找顺序: 先从子类内部查找, 然后从左向右对父类进行查找
    - `mro`: 方法搜索顺序, 使用方法 `类名.__mro__`
    - 小口诀: 立足自身, 从左往右, 一撸到底, 招到即止(实在不会, `__mro__`伺候)
- Mixin模式: Mix-in混入
    - Mixin结尾的类, 被称为混入类
    - 混入类不是标准意义上的类, 就是一个方法的容器
    - 所以混入类不要实例化, 而是通过多继承的方式, 让内部的方法被别的类来使用
- 多态(子类对父类方法的重写或拓展)
- **在Python中, 类本身就是一个特殊的对象**
- 对象又称为 **实例**
- 类属性和类方法
    - `类属性` 直接在类名下声明即可
    - 直接通过 `类名.类属性` 即可访问类属性
    - python中是可以通过类的实例来访问类属性的
    - 属性的获取机制
        1. 先在对象内部查看对象属性
        2. 没有找到就会向上寻找类属性
    - 类方法使用装饰器 `@classmethod` 声明
    - 类方法默认参数 `cls` 指向的就是调用该方法的类
- 静态方法
    - 使用装饰器 `@staticmethod` 声明
    - 可以使用 `类名.方法名` 来调用
- 示例项目
    
## 下午

- 写作业
