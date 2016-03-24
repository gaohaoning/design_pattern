#!/usr/bin/env python
# coding:utf-8

"""
备忘录模式(Memento Pattern)
    在不破坏封装的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态，这样可以在以后将对象恢复到原先保存的状态。

包含三个角色
    [Originator][原发器]
        负责创建一个备忘录，用以记录当前时刻对象的内部状态；
        并可使用备忘录恢复内部状态；
        同时原发器还可以根据需要决定备忘录存储原发器的哪些内部状态；
    [Memento][备忘录]
        用于存储原发器对象的内部状态，并且可以防止原发器以外的对象访问备忘录。
        在备忘录Memento中有两个接口，
            Caretaker只能看到备忘录中的窄接口，它只能将备忘录传递给其他对象。
            Originator可以看到宽接口，允许它访问返回到先前状态的所有数据。
    [Caretaker][负责人]
        负责保存好备忘录。
        不能对备忘录的内容进行操作和访问，只能够将备忘录传递给其他对象。


在备忘录模式中，最重要的就是备忘录Memento了。
我们知道备忘录中存储的就是原发器的部分或者所有的状态信息，而这些状态信息是不能够被其他对象所访问了，
也就是说我们是不可能在备忘录之外的对象来存储这些状态信息，如果暴漏了内部状态信息就违反了封装的原则，
所以，只允许生成该备忘录的那个原发器访问备忘录的内部状态，除了原发器外的其他对象都不可以访问备忘录。

所以，为了实现备忘录模式的封装，我们需要对备忘录的访问做些控制：
    对原发器：可以访问备忘录里的所有信息。
    对负责人：不可以访问备忘录里面的数据，但是他可以保存备忘录并且可以将备忘录传递给其他对象。
    其他对象：不可访问也不可以保存，它只负责接收从负责人那里传递过来的备忘录同时恢复原发器的状态。

优点
    给用户提供了一种可以恢复状态的机制。可以使用户能够比较方便地回到某个历史的状态。
    实现了信息的封装。使得用户不需要关心状态的保存细节。

缺点
    消耗资源。如果类的成员变量过多，势必会占用比较大的资源，而且每一次保存都会消耗一定的内存。

适用情况
    需要保存一个对象在某一个时刻的状态或部分状态。
    如果用一个接口来让其他对象得到这些状态，将会暴露对象的实现细节并破坏对象的封装性，
        一个对象不希望外界直接访问其内部状态，通过负责人可以间接访问其内部状态。
"""

import copy

class Originator(object):
    """
    原发器
    """
    def __init__(self):
        self.state = {}
    def get_state(self):
        return self.state
    def display(self):
        print '%s' % self, ['%s = %s' % (key, self.state[key]) for key in self.state]
    def create_memento(self):
        """
        在原发器中保存状态时必须使用深拷贝，否则备忘录中保存的状态和原发器中的状态是同一个 dict 对象，
        备忘录中的状态会随原发器中状态变化而变化，无法恢复！
        """
        return Memento(copy.deepcopy(self.state))
    def restore_memento(self, memento):
        self.state = memento.state

class Memento(object):
    """
    备忘录
    """
    def __init__(self, state):
        self.state = state
    def get_state(self):
        return self.state

class Caretaker(object):
    """
    负责人
    """
    def __init__(self):
        self.memento = None
    def get_memento(self):
        return self.memento
    def set_memento(self, memento):
        self.memento = memento


print '初始状态'
my_obj = Originator()
my_obj.state = {'hp': 999, 'mp': 999, 'exp': 999}
my_obj.display()
# <__main__.Originator object at 0x10a29c710> ['hp = 999', 'mp = 999', 'exp = 999']

print '保存状态'
caretaker = Caretaker()
memento = my_obj.create_memento()
caretaker.set_memento(memento)

print '状态变化'
my_obj.state.update(hp=11, mp=22, exp=33)
my_obj.display()
# <__main__.Originator object at 0x10a29c710> ['mp = 22', 'exp = 33', 'hp = 11']

print '恢复状态'
memento_restore = caretaker.get_memento()
my_obj.restore_memento(memento_restore)
my_obj.display()
# <__main__.Originator object at 0x10a29c710> ['hp = 999', 'mp = 999', 'exp = 999']
