#!/usr/bin/env python
# coding:utf-8

"""
原型模式(Prototype Pattern)
    用原型实例指定创建对象的种类，并且通过拷贝(复制)这些原型创建新的对象。

包含二个角色
    [AbstractPrototype][抽象原型类]
        声明克隆自身的接口。
    [ConcretePrototype][具体原型类]
        实现克隆的具体操作。

在我们应用程序可能有某些对象的结构比较复杂，但是我们又需要频繁的使用它们，
如果这个时候我们来不断的新建这个对象势必会大大损耗系统内存的，
这个时候我们需要使用原型模式来对这个结构复杂又要频繁使用的对象进行克隆。

优点
    如果创建新的对象比较复杂时，可以利用原型模式简化对象的创建过程，同时也能够提高效率。
    可以使用深克隆保持对象的状态。
    原型模式提供了简化的创建结构。

缺点
    在实现深克隆的时候可能需要比较复杂的代码。
    需要为每一个类配备一个克隆方法，而且这个克隆方法需要对类的功能进行通盘考虑，
        这对全新的类来说不是很难，但对已有的类进行改造时，不一定是件容易的事，必须修改其源代码，违背了“开闭原则”。

适用情况
    如果创建新对象成本较大，我们可以利用已有的对象进行复制来获得。
    如果系统要保存对象的状态，而对象的状态变化很小，或者对象本身占内存不大的时候，也可以使用原型模式配合备忘录模式来应用。
        相反，如果对象的状态变化很大，或者对象占用的内存很大，那么采用状态模式会比原型模式更好。
    需要避免使用分层次的工厂类来创建分层次的对象，并且类的实例对象只有一个或很少的几个组合状态，
        通过复制原型对象得到新实例可能比使用构造函数创建一个新实例更加方便。
"""

import copy

class Prototype_abstract(object):
    """
    抽象原型类
    """
    def clone(self):
        pass

class Prototype_concrete(Prototype_abstract):
    """
    具体原型类
    """
    def clone(self, **kwargs):
        new_object = copy.deepcopy(self)
        new_object.__dict__.update(**kwargs)
        return new_object


# 让一个原型克隆自身,从而获得一个新的对象:
prototype_0 = Prototype_concrete()
prototype_a = prototype_0.clone(a='A')
prototype_b = prototype_a.clone(b='B')
prototype_c = prototype_b.clone(c='C')

print id(prototype_0), prototype_0.__dict__
print id(prototype_a), prototype_a.__dict__
print id(prototype_b), prototype_b.__dict__
print id(prototype_c), prototype_c.__dict__
# 4559790800 {}
# 4559790992 {'a': 'A'}
# 4559791056 {'a': 'A', 'b': 'B'}
# 4559791120 {'a': 'A', 'c': 'C', 'b': 'B'}
