#!/usr/bin/env python
# coding:utf-8

"""
简单工厂模式(Simple Factory Pattern)
    在简单工厂模式中，可以根据参数的不同返回不同类的实例。
    简单工厂模式专门定义一个类来负责创建其他类的实例，被创建的实例通常都具有共同的父类。

包含三个角色
    [AbstractProduct][抽象产品]
        是所创建的所有对象的父类，负责描述所有实例所共有的公共接口；
    [ConcreteProduct][具体产品]
        是创建目标，所有创建的对象都充当这个角色的某个具体类的实例；
    [Factory][工厂]
        负责实现创建所有实例的内部逻辑；

优点
    实现对象的创建和对象的使用分离，将对象的创建交给专门的工厂类负责；

缺点
    工厂类不够灵活，增加新的具体产品需要修改工厂类的判断逻辑代码，而且产品较多时，工厂方法代码将会非常复杂；

适用情况
    工厂类负责创建的对象比较少；
    客户端只知道传入工厂类的参数，对于如何创建对象不关心。

简单工厂模式又称为静态工厂方法(Static Factory Method)模式，它属于类创建型模式。
"""

class Product_abstract(object):
    """
    抽象产品
    """
    def use(self):
        pass

class Product_concrete_1(Product_abstract):
    """
    具体产品 1
    """
    def use(self):
        print 'using:', self.__class__.__name__

class Product_concrete_2(Product_abstract):
    """
    具体产品 2
    """
    def use(self):
        print 'using:', self.__class__.__name__

class Factory(object):
    """
    工厂
    """
    def create_product(self, type):
        if type == 1:
            return Product_concrete_1()
        elif type == 2:
            return Product_concrete_2()
        else:
            return None


factory = Factory()

operation = factory.create_product(1)
operation.use()
# using: Product_concrete_1

operation = factory.create_product(2)
operation.use()
# using: Product_concrete_2
