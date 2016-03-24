#!/usr/bin/env python
# coding:utf-8

"""
观察者模式(Observer Pattern)
    定义对象间的一对多依赖关系，使得每当一个对象状态发生改变时，其相关依赖对象皆得到通知并被自动更新。

包含四个角色
    [Subject][目标]
        又称为主题，它是指被观察的对象；
        他把所有对观察者的引用保存在一个聚集里，每一个主题都可以有多个观察者；
    [ConcreteSubject][具体目标]
        是目标类的子类，
        通常它包含有经常发生改变的数据，当它的状态发生改变时，向它的各个观察者发出通知；
    [Observer][观察者]
        将对观察目标的改变做出反应；
        为所有的具体观察者定义一个接口，在得到目标的通知时能够及时的更新自己；
    [ConcreteObserver][具体观察者]
        维护一个指向具体目标对象的引用，它存储具体观察者的有关状态，这些状态需要和具体目标的状态保持一致；

观察者模式定义了一种一对多的依赖关系，让多个观察者对象同时监听某一个目标对象，
当这个目标对象的状态发生变化时，会通知所有观察者对象，使它们能够自动更新。

优点
    可以实现表示层和数据逻辑层的分离，并在观察目标和观察者之间建立一个抽象的耦合，支持广播通信；

缺点
    如果一个观察目标对象有很多直接和间接的观察者的话，将所有的观察者都通知到会花费很多时间，
    而且如果在观察者和观察目标之间有循环依赖的话，观察目标会触发它们之间进行循环调用，可能导致系统崩溃。

适用情况
    一个抽象模型有两个方面，其中一个方面依赖于另一个方面；
    一个对象的改变将导致其他一个或多个对象也发生改变，而不知道具体有多少对象将发生改变；
    一个对象必须通知其他对象，而并不知道这些对象是谁；
    需要在系统中创建一个触发链。

观察者模式又叫做发布-订阅（Publish/Subscribe）模式、模型-视图（Model/View）模式、源-监听器（Source/Listener）模式或从属者（Dependents）模式。
观察者模式是一种对象行为型模式。
"""

class Subject(object):
    """
    目标
    """
    def __init__(self):
        self.observer_list = []
    def attach(self, observer):
        if observer not in self.observer_list:
            self.observer_list.append(observer)
    def detach(self, observer):
        if observer in self.observer_list:
            self.observer_list.remove(observer)
    def notify(self):
        for observer in self.observer_list:
            print '%s notifying %s' % (self, observer)
            observer.update()

class Subject_concrete(Subject):
    """
    具体目标
    """
    def __init__(self):
        super(Subject_concrete, self).__init__()
        self._data = None
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, value):
        self._data = value
        """
        数据发生改变时，向所有观察者发出通知
        """
        self.notify()
    @data.deleter
    def data(self):
        del self._data

class Observer(object):
    """
    观察者
    """
    def __init__(self, subject):
        self.subject = subject
    def update(self):
        pass

class Observer_concrete(Observer):
    """
    具体观察者
    """
    def update(self):
        print '%s get notified from %s new data = %s' % (self, self.subject, self.subject.data)


subject = Subject_concrete()
observer_1 = Observer_concrete(subject)
observer_2 = Observer_concrete(subject)
subject.attach(observer_1)
subject.attach(observer_2)

subject.data = 1
# <__main__.Subject_concrete object at 0x101c93050> notifying <__main__.Observer_concrete object at 0x101c930d0>
# <__main__.Observer_concrete object at 0x101c930d0> get notified from <__main__.Subject_concrete object at 0x101c93050> new data = 1
# <__main__.Subject_concrete object at 0x101c93050> notifying <__main__.Observer_concrete object at 0x101c93110>
# <__main__.Observer_concrete object at 0x101c93110> get notified from <__main__.Subject_concrete object at 0x101c93050> new data = 1

subject.data = 2
# <__main__.Subject_concrete object at 0x101c93050> notifying <__main__.Observer_concrete object at 0x101c930d0>
# <__main__.Observer_concrete object at 0x101c930d0> get notified from <__main__.Subject_concrete object at 0x101c93050> new data = 2
# <__main__.Subject_concrete object at 0x101c93050> notifying <__main__.Observer_concrete object at 0x101c93110>
# <__main__.Observer_concrete object at 0x101c93110> get notified from <__main__.Subject_concrete object at 0x101c93050> new data = 2
