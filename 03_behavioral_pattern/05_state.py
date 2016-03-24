#!/usr/bin/env python
# coding:utf-8

"""
状态模式(State Pattern)
    允许一个对象在其内部状态改变时改变它的行为，对象看起来似乎修改了它的类。

包含三个角色
    [Context][环境类]
        又称为上下文类，它是拥有状态的对象，
        在环境类中维护一个抽象状态类State的实例，这个实例定义当前状态，
        在具体实现时，它是一个State子类的对象，可以定义初始状态；
    [AbstractState][抽象状态类]
        定义一个接口以封装与环境类的一个特定状态相关的行为；
    [ConcreteState][具体状态类]
        是抽象状态类的子类，
        每一个子类实现一个与环境类的一个状态相关的行为，
        每一个具体状态类对应环境的一个具体状态，不同的具体状态类其行为有所不同；

状态模式描述了对象状态的变化以及对象如何在每一种状态下表现出不同的行为。

优点
    封装了转换规则，并枚举可能的状态，它将所有与某个状态有关的行为放到一个类中，并且可以方便地增加新的状态，
    只需要改变对象状态即可改变对象的行为，还可以让多个环境对象共享一个状态对象，从而减少系统中对象的个数；

缺点
    使用状态模式会增加系统类和对象的个数，且状态模式的结构与实现都较为复杂，
    如果使用不当将导致程序结构和代码的混乱，对于可以切换状态的状态模式不满足“开闭原则”的要求。

适用情况
    对象的行为依赖于它的状态（属性）并且可以根据它的状态改变而改变它的相关行为；
    代码中包含大量与对象状态有关的条件语句，这些条件语句的出现，会导致代码的可维护性和灵活性变差，
        不能方便地增加和删除状态，使客户类与类库之间的耦合增强。

其别名为状态对象(Objects for States)，状态模式是一种对象行为型模式。
"""

class Context(object):
    """
    环境类
    """
    def __init__(self):
        self.state = None
        self.state_a = State_concrete_A()
        self.state_b = State_concrete_B()
        self.state_c = State_concrete_C()
    def change_state(self, state):
        self.state = state
    def request(self):
        if self.data <= 10:
            self.change_state(self.state_a)
        elif self.data <= 20:
            self.change_state(self.state_b)
        else:
            self.change_state(self.state_c)
        print 'requesting state: %s %s' % (self.state, id(self.state))
        self.state.handle(self)

class State_abstract(object):
    """
    抽象状态类
    """
    def handle(self, context):
        pass

class State_concrete_A(State_abstract):
    """
    具体状态类
    """
    def handle(self, context):
        print 'handle state A'

class State_concrete_B(State_abstract):
    """
    具体状态类
    """
    def handle(self, context):
        print 'handle state B'

class State_concrete_C(State_abstract):
    """
    具体状态类
    """
    def handle(self, context):
        print 'handle state C'


context = Context()

context.data = 1
context.request()
# requesting state: <__main__.State_concrete_A object at 0x103601110> 4351594768
# handle state A

context.data = 5
context.request()
# requesting state: <__main__.State_concrete_A object at 0x103601110> 4351594768
# handle state A

context.data = 15
context.request()
# requesting state: <__main__.State_concrete_B object at 0x103601150> 4351594832
# handle state B

context.data = 25
context.request()
# requesting state: <__main__.State_concrete_C object at 0x103601190> 4351594896
# handle state C
