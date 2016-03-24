#!/usr/bin/env python
# coding:utf-8

"""
桥接模式(Bridge Pattern)
    将抽象部分与它的实现部分分离，使它们都可以独立地变化。

包含四个角色
    [Abstraction][抽象类]
        定义了一个实现类接口类型的对象并可以维护该对象；
    [RefinedAbstraction][扩充抽象类]
        扩充由抽象类定义的接口，它实现了在抽象类中定义的抽象业务方法，在扩充抽象类中可以调用在实现类接口中定义的业务方法；
    [AbstractImplementor][实现类接口]
        定义了实现类的接口，实现类接口仅提供基本操作，而抽象类定义的接口可能会做更多更复杂的操作；
    [ConcreteImplementor][具体实现类]
        实现实现类接口，在不同的具体实现类中提供基本操作的不同实现，
        在程序运行时，具体实现类对象将替换其父类对象，提供给客户端具体的业务操作方法。

在桥接模式中，抽象化(Abstraction)与实现化(Implementation)脱耦，它们可以沿着各自的维度独立变化。

优点
    分离抽象接口及其实现部分，是比多继承方案更好的解决方法，
    还提高了系统的可扩充性，在两个变化维度中任意扩展一个维度，都不需要修改原有系统，
    实现细节对客户透明，可以对用户隐藏实现细节；

缺点
    增加系统的理解与设计难度，且识别出系统中两个独立变化的维度并不是一件容易的事情。

适用情况
    需要在构件的抽象化角色和具体化角色之间增加更多的灵活性，避免在两个层次之间建立静态的继承联系；
    抽象化角色和实现化角色可以以继承的方式独立扩展而互不影响；
    一个类存在两个独立变化的维度，且这两个维度都需要进行扩展；
    设计要求需要独立管理抽象化角色和具体化角色；
    不希望使用继承或因为多层次继承导致系统类的个数急剧增加的系统。

桥接模式是一种对象结构型模式，又称为柄体(Handle and Body)模式或接口(Interface)模式。
"""

class PhoneBrand(object):
    """
    抽象类
    """
    def __init__(self):
        self.func = None
    def set_func(self, func):
        self.func = func
    def work(self):
        pass

class PhoneBrand_ios(PhoneBrand):
    """
    扩充抽象类
    """
    def work(self):
        if self.func is not None:
            self.func.run()

class PhoneFunc(object):
    """
    实现类接口
    """
    def run(self):
        pass

class PhoneFunc_Call(PhoneFunc):
    """
    具体实现类
    """
    def run(self):
        print self.__class__.__name__, 'run CALL'

class PhoneFunc_Sms(PhoneFunc):
    """
    具体实现类
    """
    def run(self):
        print self.__class__.__name__, 'run SMS'


phone_ios = PhoneBrand_ios()

func_a = PhoneFunc_Call()
phone_ios.set_func(func_a)
phone_ios.work()
# PhoneFunc_Call run CALL

func_b = PhoneFunc_Sms()
phone_ios.set_func(func_b)
phone_ios.work()
# PhoneFunc_Sms run SMS
