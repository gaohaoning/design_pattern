#!/usr/bin/env python
# coding:utf-8

"""
模板方法模式(Template Method Pattern)
    在一个方法中定义一个算法的骨架，而将一些步骤延迟到子类中。
    模板方法使得子类可以在不改变算法结构的情况下，重新定义算法中的某些步骤。

包含二个角色
    [AbstractClass][抽象类]
        实现了一个模板，定义了算法的基本骨架，
        具体子类将重定义 primitiveOperation() 方法以实现一个算法步骤。
    [ConcreteClass][具体子类]
        实现 primitiveOperation() 方法以完成算法中与特定子类相关的步骤。

模板方法模式就是基于继承的代码复用技术的。
在模板方法模式中，我们可以将相同部分的代码放在父类中，而将不同的代码放入不同的子类中。
也就是说我们需要声明一个抽象的父类，将部分逻辑以具体方法以及具体构造函数的形式实现，
然后声明一些抽象方法让子类来实现剩余的逻辑，不同的子类可以以不同的方式来实现这些逻辑。
所以模板方法的模板其实就是一个普通的方法，只不过这个方法是将算法实现的步骤封装起来的。

优点
    定义了一组算法，将具体的实现交由子类负责。
    是一种代码复用的基本技术。
    导致一种反向的控制结构，通过一个父类调用其子类的操作，通过对子类的扩展增加新的行为，符合“开闭原则”。

缺点
    每一个不同的实现都需要一个子类，导致类的个数增加，使得系统更加庞大。

适用情况
    需要一次性实现一个算法的不变的部分，并将可变的行为留给子类来实现。
    各子类中公共的行为应被提取出来，并集中到一个公共父类中以避免代码重复。
"""

class Beverage(object):
    """
    抽象类
    """
    def prepare(self):
        print 'boil water'
    def brew(self):
        pass
    def serve(self):
        print 'serve %s: %s' % (self.__class__.__name__, self)
    def make(self):
        self.prepare()
        self.brew()
        self.serve()

class Tea(Beverage):
    """
    具体子类
    """
    def brew(self):
        print 'brew [tea]'

class Coffee(Beverage):
    """
    具体子类
    """
    def brew(self):
        print 'brew [coffee]'


tea = Tea()
tea.make()
# boil water
# brew [tea]
# serve Tea: <__main__.Tea object at 0x10873fd50>

coffee = Coffee()
coffee.make()
# boil water
# brew [coffee]
# serve Coffee: <__main__.Coffee object at 0x10873fd90>
