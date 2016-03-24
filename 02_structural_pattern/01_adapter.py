#!/usr/bin/env python
# coding:utf-8

"""
适配器模式(Adapter Pattern)
    将一个接口转换成客户希望的另一个接口，适配器模式使接口不兼容的那些类可以一起工作，其别名为包装器(Wrapper)。
    适配器模式既可以作为类结构型模式，也可以作为对象结构型模式。

包含三个角色
    [Target][目标抽象类]
        定义客户要用的特定领域的接口；
    [Adaptee][适配者类]
        是被适配的角色，它定义了一个已经存在的接口，这个接口需要适配；
    [Adapter][适配器类]
        可以调用另一个接口，作为一个转换器，对适配者和抽象目标类进行适配，它是适配器模式的核心；

在类适配器模式中，适配器类实现了目标抽象类接口并继承了适配者类，并在目标抽象类的实现方法中调用所继承的适配者类的方法；
在对象适配器模式中，适配器类继承了目标抽象类并定义了一个适配者类的对象实例，在所继承的目标抽象类方法中调用适配者类的相应业务方法。

优点
    将目标类和适配者类解耦，增加了类的透明性和复用性，同时系统的灵活性和扩展性都非常好，更换适配器或者增加新的适配器都非常方便，符合“开闭原则”；

缺点
    类适配器模式的缺点是适配器类在很多编程语言中不能同时适配多个适配者类；
    对象适配器模式的缺点是很难置换适配者类的方法；

适用情况
    系统需要使用现有的类，而这些类的接口不符合系统的需要；
    想要建立一个可以重复使用的类，用于与一些彼此之间没有太大关联的一些类一起工作。
"""

class Cat(object):
    """
    适配者类
    """
    def __init__(self):
        self.name = self.__class__.__name__
    def meow(self):
        return 'meow ~'

class Dog(object):
    """
    适配者类
    """
    def __init__(self):
        self.name = self.__class__.__name__
    def bark(self):
        return 'woof !'

class Human(object):
    """
    适配者类
    """
    def __init__(self):
        self.name = self.__class__.__name__
    def speak(self):
        return 'hello ?'

class Target(object):
    """
    目标抽象类
    """
    def make_noise(self):
        return '......'

class Adapter(Target):
    """
    适配器类
    """
    def __init__(self, adaptee):
        self.adaptee = adaptee
    """
    object.__getattr__(self, name)
        Called when an attribute lookup has not found the attribute in the usual places
        (i.e. it is not an instance attribute nor is it found in the class tree for self).
        name is the attribute name.
        This method should return the (computed) attribute value or raise an AttributeError exception.
    """
    def __getattr__(self, attr):
        return getattr(self.adaptee, attr)
    def make_noise(self):
        if isinstance(self.adaptee, Cat):
            return self.adaptee.meow()
        elif isinstance(self.adaptee, Dog):
            return self.adaptee.bark()
        elif isinstance(self.adaptee, Human):
            return self.adaptee.speak()


cat = Cat()
dog = Dog()
human = Human()
animals = [Adapter(cat), Adapter(dog), Adapter(human)]
# 针对目标抽象类进行编程,调用在目标抽象类中定义的方法:
for animal in animals:
    print animal.name, animal.make_noise()

# Cat meow ~
# Dog woof !
# Human hello ?
