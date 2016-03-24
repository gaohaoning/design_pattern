#!/usr/bin/env python
# coding:utf-8


"""
抽象工厂模式(Abstract Factory Pattern)
    提供一个创建一系列相关或相互依赖对象的接口，而无须指定它们具体的类。

包含四个角色
    [AbstractProduct][抽象产品]
        为每种产品声明接口，在抽象产品中定义了产品的抽象业务方法；
    [ConcreteProduct][具体产品]
        定义具体工厂生产的具体产品对象，实现抽象产品接口中定义的业务方法；
    [AbstractFactory][抽象工厂]
        用于声明生成抽象产品的方法；
    [ConcreteFactory][具体工厂]
        实现了抽象工厂声明的生成抽象产品的方法，生成一组具体产品，这些产品构成了一个产品族，每一个产品都位于某个产品等级结构中；

抽象工厂模式是所有形式的工厂模式中最为抽象和最具一般性的一种形态。
抽象工厂模式与工厂方法模式最大的区别在于，
    工厂方法模式针对的是一个产品等级结构，
    抽象工厂模式则需要面对多个产品等级结构。

优点
    隔离了具体类的生成，使得客户并不需要知道什么被创建，而且每次可以通过具体工厂类创建一个产品族中的多个对象，
    增加或者替换产品族比较方便，增加新的具体工厂和产品族很方便；

缺点
    增加新的产品等级结构很复杂，需要修改抽象工厂和所有的具体工厂类，对“开闭原则”的支持呈现倾斜性；

适用情况
    一个系统不应当依赖于产品类实例如何被创建、组合和表达的细节；
    系统中有多于一个的产品族，而每次只使用其中某一产品族；
    属于同一个产品族的产品将在一起使用；
    系统提供一个产品类的库，所有的产品以同样的接口出现，从而使客户端不依赖于具体实现。

抽象工厂模式又称为Kit模式，属于对象创建型模式。
"""

class Product_abstract_A(object):
    """
    抽象产品 A
    """
    def use(self):
        pass

class Product_concrete_A_1(Product_abstract_A):
    """
    具体产品 A 1
    """
    def use(self):
        print 'using:', self.__class__.__name__

class Product_concrete_A_2(Product_abstract_A):
    """
    具体产品 A 2
    """
    def use(self):
        print 'using:', self.__class__.__name__


class Product_abstract_B(object):
    """
    抽象产品 B
    """
    def use(self):
        pass

class Product_concrete_B_1(Product_abstract_B):
    """
    具体产品 B 1
    """
    def use(self):
        print 'using:', self.__class__.__name__

class Product_concrete_B_2(Product_abstract_B):
    """
    具体产品 B 2
    """
    def use(self):
        print 'using:', self.__class__.__name__


class Factory_abstract(object):
    """
    抽象工厂
    """
    def create_product_A(self):
        return Product_abstract_A()
    def create_product_B(self):
        return Product_abstract_B()

class Factory_concrete_1(Factory_abstract):
    """
    具体工厂 1
    """
    def create_product_A(self):
        return Product_concrete_A_1()
    def create_product_B(self):
        return Product_concrete_B_1()

class Factory_concrete_2(Factory_abstract):
    """
    具体工厂 2
    """
    def create_product_A(self):
        return Product_concrete_A_2()
    def create_product_B(self):
        return Product_concrete_B_2()


factory_1 = Factory_concrete_1()
product_A_int = factory_1.create_product_A()
product_A_int.use()
# using: Product_concrete_A_1
product_B_int = factory_1.create_product_B()
product_B_int.use()
# using: Product_concrete_B_1

factory_2 = Factory_concrete_2()
product_A_str = factory_2.create_product_A()
product_A_str.use()
# using: Product_concrete_A_2
product_B_str = factory_2.create_product_B()
product_B_str.use()
# using: Product_concrete_B_2
