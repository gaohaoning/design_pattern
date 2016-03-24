#!/usr/bin/env python
# coding:utf-8

"""
迭代器模式(Iterator Pattern)
    提供一种方法顺序访问一个聚合对象中的各个元素，而不暴露其内部的表示。

包含四个角色
    [AbstractIterator][抽象迭代器]
        所有迭代器都需要实现的接口，提供了游走聚合对象元素之间的方法；
    [ConcreteIterator][具体迭代器]
        利用这个具体的迭代器能够对具体的聚合对象进行遍历；
        每一个聚合对象都应该对应一个具体的迭代器；
    [AbstractAggregate][抽象聚合类]
    [ConcreteAggregate][具体聚合类]
        实现 create_iterator() 方法，返回该聚合对象的迭代器；

迭代器模式是将迭代元素的责任交给迭代器，而不是聚合对象，我们甚至在不需要知道该聚合对象的内部结构就可以实现该聚合对象的迭代。
通过迭代器模式，使得聚合对象的结构更加简单，它不需要关注它元素的遍历，只需要专注它应该专注的事情，这样就更加符合单一职责原则了。

优点
    它支持以不同的方式遍历一个聚合对象。
    迭代器简化了聚合类。
    在同一个聚合上可以有多个遍历。
    在迭代器模式中，增加新的聚合类和迭代器类都很方便，无须修改原有代码。

缺点
    由于迭代器模式将存储数据和遍历数据的职责分离，增加新的聚合类需要对应增加新的迭代器类，
    类的个数成对增加，这在一定程度上增加了系统的复杂性。

适用情况
    访问一个聚合对象的内容而无须暴露它的内部表示。
    需要为聚合对象提供多种遍历方式。
    为遍历不同的聚合结构提供一个统一的接口。
"""

class Aggregate_abstract(object):
    """
    抽象迭代器
    """
    def create_iterator(self):
        pass

class Aggregate_concrete(Aggregate_abstract):
    """
    具体迭代器
    """
    def __init__(self):
        self.iterator = None
    def create_iterator(self):
        self.iterator = Iterator_concrete()
        return self.iterator

class Iterator_abstract(object):
    """
    抽象聚合类
    """
    def first_item(self):
        pass
    def next_item(self):
        pass
    def has_next(self):
        pass
    def current_item(self):
        pass

class Iterator_concrete(Iterator_abstract):
    """
    具体聚合类
    """
    def __init__(self):
        self.container = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.position = 0
    def first_item(self):
        return self.container[0]
    def next_item(self):
        self.position += 1
        if self.position < len(self.container):
            return self.container[self.position]
        else:
            self.position = self.position % len(self.container)
            return self.container[self.position]
    def has_next(self):
        return self.position < len(self.container) - 1
    def current_item(self):
        return self.container[self.position]


aggregate = Aggregate_concrete()
iterator = aggregate.create_iterator()

print iterator.first_item()
# Monday

for n in range(10):
    print iterator.next_item()

# Tuesday
# Wednesday
# Thursday
# Friday
# Saturday
# Sunday
# Monday
# Tuesday
# Wednesday
# Thursday
