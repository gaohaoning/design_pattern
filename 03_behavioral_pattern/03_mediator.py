#!/usr/bin/env python
# coding:utf-8

"""
中介者模式(Mediator Pattern)
    用一个中介对象来封装一系列的对象交互，中介者使各对象不需要显式地相互引用，从而使其耦合松散，而且可以独立地改变它们之间的交互。

式包含四个角色
    [AbstractMediator][抽象中介者]
        定义一个接口，该接口用于与各同事对象之间的通信；
    [ConcreteMediator][具体中介者]
        是抽象中介者的子类，通过协调各个同事对象来实现协作行为，了解并维护它的各个同事对象的引用；
    [AbstractColleague][抽象同事类]
        定义各同事的公有方法；
    [ConcreteColleague][具体同事类]
        是抽象同事类的子类，在具体同事类中实现了在抽象同事类中定义的方法；
        每一个同事对象都引用一个中介者对象；
        每一个同事对象在需要和其他同事对象通信时，先与中介者通信，通过中介者来间接完成与其他同事类的通信；

通过引入中介者对象，可以将系统的网状结构变成以中介者为中心的星形结构，中介者承担了中转作用和协调作用。
中介者类是中介者模式的核心，它对整个系统进行控制和协调，简化了对象之间的交互，还可以对对象间的交互进行进一步的控制。

优点
    简化了对象之间的交互，将各同事解耦，还可以减少子类生成，对于复杂的对象之间的交互，通过引入中介者，可以简化各同事类的设计和实现；

缺点
    具体中介者类中包含了同事之间的交互细节，可能会导致具体中介者类非常复杂，使得系统难以维护。

适用情况
    系统中对象之间存在复杂的引用关系，产生的相互依赖关系结构混乱且难以理解；
    一个对象由于引用了其他很多对象并且直接和这些对象通信，导致难以复用该对象；
    想通过一个中间类来封装多个类中的行为，而又不想生成太多的子类。

中介者模式又称为调停者模式，它是一种对象行为型模式。
"""

class Colleage_abstract(object):
    """
    抽象同事类
    """
    def __init__(self, mediator):
        self.mediator = mediator
    def send(self, target, msg):
        pass
    def receive(self, source, msg):
        pass

class Colleage_concrete_A(Colleage_abstract):
    """
    具体同事类
    """
    def send(self, target, msg):
        print '%s send to %s: %s' % (self, target, msg)
        self.mediator.forward(self, target, msg)
    def receive(self, source, msg):
        print '%s receive from %s: %s' % (self, source, msg)

class Colleage_concrete_B(Colleage_abstract):
    """
    具体同事类
    """
    def send(self, target, msg):
        print '%s send to %s: %s' % (self, target, msg)
        self.mediator.forward(self, target, msg)
    def receive(self, source, msg):
        print '%s receive from %s: %s' % (self, source, msg)

class Mediator_abstract(object):
    """
    抽象中介者
    """
    def forward(self):
        pass

class Mediator_concrete(Mediator_abstract):
    """
    具体中介者
    """
    def forward(self, source, target, msg):
        target.receive(source, msg)


mediator = Mediator_concrete()
colleage_a = Colleage_concrete_A(mediator)
colleage_b = Colleage_concrete_B(mediator)

colleage_a.send(colleage_b, 'How are you ?')
# <__main__.Colleage_concrete_A object at 0x107dbb090> send to <__main__.Colleage_concrete_B object at 0x107dbb0d0>: How are you ?
# <__main__.Colleage_concrete_B object at 0x107dbb0d0> receive from <__main__.Colleage_concrete_A object at 0x107dbb090>: How are you ?

colleage_b.send(colleage_a, 'Fine, thank you, and you ?')
# <__main__.Colleage_concrete_B object at 0x107dbb0d0> send to <__main__.Colleage_concrete_A object at 0x107dbb090>: Fine, thank you, and you ?
# <__main__.Colleage_concrete_A object at 0x107dbb090> receive from <__main__.Colleage_concrete_B object at 0x107dbb0d0>: Fine, thank you, and you ?
