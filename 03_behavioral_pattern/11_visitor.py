#!/usr/bin/env python
# coding:utf-8

"""
访问者模式(Visitor Pattern)
    表示一个作用于某对象结构中的各元素的操作。
    它使我们可以在不改变各元素的类的前提下定义作用于这些元素的新操作。

包含五个角色
    [AbstractElement][抽象元素]
        定义一个 Accept 操作，以一个 Visitor 为参数。
    [ConcreteElement][具体元素]
        实现 Accept 操作。
    [AbstractVisitor][抽象访问者]
        为 ConcreteElement 的每一个类声明的一个 Visit 操作。
    [ConcreteVisitor][具体访问者]
        实现每一个由 AbstractVisitor 声明的操作。
        每个操作实现算法的一部分。
    [ObjectStructure][对象结构]
        能够枚举元素，可以提供一个高层的接口以允许 Visitor 访问它的元素。

访问者模式的目的是封装一些施加于某种数据结构元素之上的操作，一旦这些操作需要修改的话，接受这个操作的数据结构可以保持不变。
为不同类型的元素提供多种访问操作方式，且可以在不修改原有系统的情况下增加新的操作方式。

优点
    使得增加新的访问操作变得更加简单。
    能够使得用户在不修改现有类层次结构的情况下，定义新的操作。
    将有关元素对象的访问行为集中到一个访问者对象中，而不是分散搞一个个的元素类中。

缺点
    增加新的元素类很困难。
        在访问者模式中，每增加一个新的元素类都意味着要在抽象访问者角色中增加一个新的抽象操作，
        并在每一个具体访问者类中增加相应的具体操作，违背了“开闭原则”的要求。
    破坏封装。
        当采用访问者模式的时候，就会打破组合类的封装。
    比较难理解。
        据说是最难的设计模式。

适用情况
    对象结构中对象对应的类很少改变，但经常需要在此对象结构上定义新的操作。
    需要对一个对象结构中的对象进行很多不同的并且不相关的操作，而需要避免让这些操作“污染”这些对象的类，也不希望在增加新操作时修改这些类。
"""

class Website(object):
    """
    抽象元素
    """
    def accept(self, visitor):
        pass

class Baidu(Website):
    """
    具体元素
    """
    def accept(self, visitor):
        return visitor.visit_baidu()

class Google(Website):
    """
    具体元素
    """
    def accept(self, visitor):
        return visitor.visit_google()

class AbstractVisitor(object):
    """
    抽象访问者
    """
    def visit_baidu(self):
        pass
    def visit_google(self):
        pass

class Visitor_Chinese(object):
    """
    具体访问者
    """
    def visit_baidu(self):
        print '%s visit_baidu, [chinese advertisement]' % self.__class__.__name__
    def visit_google(self):
        print '%s visit_google, [chinese information]' % self.__class__.__name__

class Visitor_American(object):
    """
    具体访问者
    """
    def visit_baidu(self):
        print '%s visit_baidu, [american advertisement]' % self.__class__.__name__
    def visit_google(self):
        print '%s visit_google, [american information]' % self.__class__.__name__

class ObjectStructure(object):
    """
    对象结构
    """
    def __init__(self):
        self.website_list = []
    def add(self, website):
        self.website_list.append(website)
    def display(self, visitor):
        for website in self.website_list:
            website.accept(visitor)


os = ObjectStructure()
baidu = Baidu()
google = Google()
os.add(baidu)
os.add(google)

visitor_chinese = Visitor_Chinese()
os.display(visitor_chinese)
# Visitor_Chinese visit_baidu, [chinese advertisement]
# Visitor_Chinese visit_google, [chinese information]

visitor_american = Visitor_American()
os.display(visitor_american)
# Visitor_American visit_baidu, [american advertisement]
# Visitor_American visit_google, [american information]
