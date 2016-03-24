#!/usr/bin/env python
# coding:utf-8

"""
策略模式(Strategy Pattern)
    定义一系列算法，将每一个算法封装起来，并让它们可以相互替换。
    策略模式让算法独立于使用它的客户而变化。

包含三个角色
    [Context][环境类]
        维护一个策略类对象的引用，用一个具体策略类来配置；
        定义了调用策略类算法的方法；
    [AbstractStrategy][抽象策略类]
        是所有策略类的父类，为具体策略类所支持的算法声明了接口；
        环境类使用这个接口来调用某个具体策略类中定义的算法；
    [ConcreteStrategy][具体策略类]
        实现了在抽象策略类中定义的算法；

策略模式是对算法的封装，它把算法的责任和算法本身分割开，委派给不同的对象管理。
策略模式通常把一个系列的算法封装到一系列的策略类里面，作为一个抽象策略类的子类。

优点
    对“开闭原则”的完美支持，在不修改原有系统的基础上可以更换算法或者增加新的算法，
    它很好地管理算法族，提高了代码的复用性，是一种替换继承，避免多重条件转移语句的实现方式；

缺点
    客户端必须知道所有的策略类，并理解其区别，
    同时在一定程度上增加了系统中类的个数，可能会存在很多策略类。

适用情况
    在一个系统里面有许多类，它们之间的区别仅在于它们的行为，使用策略模式可以动态地让一个对象在许多行为中选择一种行为；
    一个系统需要动态地在几种算法中选择一种；
    避免使用难以维护的多重条件选择语句；
    希望在具体策略类中封装算法和与相关的数据结构。

也称为政策模式(Policy)，是一种对象行为型模式。
"""

class Context(object):
    """
    环境类
    """
    def __init__(self):
        self.strategy = None
    def set_strategy(self, strategy):
        self.strategy = strategy
    def apply_strategy(self):
        self.strategy.algorithm()

class Strategy_abstract(object):
    """
    抽象策略类
    """
    def algorithm(self):
        pass

class Strategy_concrete_A(Strategy_abstract):
    """
    具体策略类
    """
    def algorithm(self):
        print 'algorithm A'

class Strategy_concrete_B(Strategy_abstract):
    """
    具体策略类
    """
    def algorithm(self):
        print 'algorithm B'


context = Context()
strategy_a = Strategy_concrete_A()
strategy_b = Strategy_concrete_B()

context.set_strategy(strategy_a)
context.apply_strategy()
# algorithm A

context.set_strategy(strategy_b)
context.apply_strategy()
# algorithm B
