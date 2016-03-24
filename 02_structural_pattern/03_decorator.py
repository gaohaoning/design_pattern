#!/usr/bin/env python
# coding:utf-8

"""
装饰模式(Decorator Pattern)
    动态地给一个对象增加一些额外的职责(Responsibility)，就增加对象功能来说，装饰模式比生成子类实现更为灵活。

包含四个角色
    [AbstractComponent][抽象构件]
        定义了对象的接口，可以给这些对象动态增加职责（方法）；
    [ConcreteComponent][具体构件]
        定义了具体的构件对象，实现了在抽象构件中声明的方法，装饰器可以给它增加额外的职责（方法）；
    [AbstractDecorator][抽象装饰类]
        是抽象构件类的子类，用于给具体构件增加职责，但是具体职责在其子类中实现；
    [ConcreteDecorator][具体装饰类]
        是抽象装饰类的子类，负责向构件添加新的职责。

使用装饰模式来实现扩展比继承更加灵活，它以对客户透明的方式动态地给一个对象附加更多的责任。
装饰模式可以在不需要创造更多子类的情况下，将对象的功能加以扩展。

优点
    可以提供比继承更多的灵活性，可以通过一种动态的方式来扩展一个对象的功能，
    并通过使用不同的具体装饰类以及这些装饰类的排列组合，可以创造出很多不同行为的组合，
    而且具体构件类与具体装饰类可以独立变化，用户可以根据需要增加新的具体构件类和具体装饰类；

缺点
    使用装饰模式进行系统设计时将产生很多小对象，而且装饰模式比继承更加易于出错，排错也很困难，
    对于多次装饰的对象，调试时寻找错误可能需要逐级排查，较为烦琐。

适用情况
    在不影响其他对象的情况下，以动态、透明的方式给单个对象添加职责；
    需要动态地给一个对象增加功能，这些功能也可以动态地被撤销；
    当不能采用继承的方式对系统进行扩充或者采用继承不利于系统扩展和维护时。

装饰模式可分为透明装饰模式和半透明装饰模式:
    在透明装饰模式中，要求客户端完全针对抽象编程，装饰模式的透明性要求客户端程序不应该声明具体构件类型和具体装饰类型，而应该全部声明为抽象构件类型；
    半透明装饰模式允许用户在客户端声明具体装饰者类型的对象，调用在具体装饰者中新增的方法。

其别名也可以称为包装器(Wrapper)，与适配器模式的别名相同，但它们适用于不同的场合。
根据翻译的不同，装饰模式也有人称之为“油漆工模式”，它是一种对象结构型模式。
"""

class Person(object):
    """
    抽象构件
    """
    def display(self):
        pass

class Man(Person):
    """
    具体构件
    """
    def __init__(self, name=None):
        self.name = name
    def display(self):
        return self.name

class Superhero(Person):
    """
    抽象装饰类
    """
    def __init__(self):
        self.component = None
    def decorate(self, component):
        self.component = component
    def behave(self):
        pass

class Batman(Superhero):
    """
    具体装饰类
    """
    def behave(self):
        return '^^^(B) [%s] (B)^^^' % self.component.display()

class Superman(Superhero):
    """
    具体装饰类
    """
    def behave(self):
        return '<<<(S) [%s] (S)>>>' % self.component.display()


bruce = Man('Bruce')
batman = Batman()
batman.decorate(bruce)
print batman.behave()
# ^^^(B) [Bruce] (B)^^^

clark = Man('Clark')
superman = Superman()
superman.decorate(clark)
print superman.behave()
# <<<(S) [Clark] (S)>>>
