#!/usr/bin/env python
# coding:utf-8

"""
组合模式(Composite Pattern)
    组合模式组合多个对象形成树形结构以表示“整体-部分”的结构层次。
    它定义了如何将容器对象和叶子对象进行递归组合，使得客户在使用的过程中无须进行区分，可以对他们进行一致的处理。

包含三个角色
    [Component][对象声明接口]
        在适当的情况下，实现所有类共有接口的默认行为。
        声明接口用于访问和管理Component子部件。
    [Leaf][叶子对象]
        叶子结点，没有子结点。
    [Composite][容器对象]
        定义有枝节点行为，用来存储子部件，在对象声明接口中实现与子部件有关操作，如增加(add)和删除(remove)等。

在使用组合模式中需要注意一点也是组合模式最关键的地方：叶子对象和容器对象实现相同的接口。
这就是组合模式能够将叶子节点和对象节点进行一致处理的原因。

优点
    可以清楚地定义分层次的复杂对象，表示对象的全部或部分层次，使得增加新构件也更容易。
    客户端调用简单，客户端可以一致的使用组合结构或其中单个对象。
    定义了包含叶子对象和容器对象的类层次结构，叶子对象可以被组合成更复杂的容器对象，而这个容器对象又可以被组合，
        这样不断递归下去，可以形成复杂的树形结构。
    更容易在组合体内加入对象构件，客户端不必因为加入了新的对象构件而更改原有代码。

缺点
    使设计变得更加抽象，对象的业务规则如果很复杂，则实现组合模式具有很大挑战性，而且不是所有的方法都与叶子对象子类都有关联。

适用情况
    需要表示一个对象整体或部分层次，在具有整体和部分的层次结构中，希望通过一种方式忽略整体与部分的差异，可以一致地对待它们。
    让客户能够忽略不同对象层次的变化，客户端可以针对抽象构件编程，无须关心对象层次结构的细节。
"""

class Component(object):
    """
    对象声明接口
    """
    def __init__(self, name):
        self.name = name
    def add(self, component):
        pass
    def remove(self, component):
        pass
    def display(self, depth):
        pass

class Leaf(Component):
    """
    叶子对象
    """
    def add(self, component):
        print '(Leaf can not add)'
    def remove(self, component):
        print '(Leaf can not remove)'
    def display(self, depth):
        print '|-----|' * depth + '[(%s) %s]' % (self.__class__.__name__, self.name)

class Composite(Component):
    """
    容器对象
    """
    def __init__(self, name):
        self.name = name
        self.children = []
    def add(self, component):
        self.children.append(component)
    def remove(self, component):
        if component in self.children:
            self.children.remove(component)
    def display(self, depth):
        print '|-----|' * depth + '[(%s) %s]' % (self.__class__.__name__, self.name)
        for child in self.children:
            child.display(depth+1)


node_0 = Composite('A')
node_1_1 = Leaf('B')
node_1_2 = Composite('C')
node_1_3 = Leaf('D')
node_0.add(node_1_1)
node_0.add(node_1_2)
node_0.add(node_1_3)

node_2_1 = Leaf('E')
node_2_2 = Leaf('F')
node_1_2.add(node_2_1)
node_1_2.add(node_2_2)

node_0.display(0)
# [(Composite) A]
# |-----|[(Leaf) B]
# |-----|[(Composite) C]
# |-----||-----|[(Leaf) E]
# |-----||-----|[(Leaf) F]
# |-----|[(Leaf) D]
