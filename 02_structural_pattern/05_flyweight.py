#!/usr/bin/env python
# coding:utf-8

"""
享元模式(Flyweight Pattern)
    运用共享技术有效地支持大量细粒度对象的复用。
    系统只使用少量的对象，而这些对象都很相似，状态变化很小，可以实现对象的多次复用。
    由于享元模式要求能够共享的对象必须是细粒度对象，因此它又称为轻量级模式，它是一种对象结构型模式。

包含四个角色
    [AbstractFlyweight][抽象享元类]
        声明一个接口，通过它可以接受并作用于外部状态；
    [ConcreteFlyweight][具体享元类]
        实现了抽象享元接口，其实例称为享元对象；
    [UnsharedConcreteFlyweight][非共享具体享元类]
        是不能被共享的抽象享元类的子类；
    [FlyweightFactory][享元工厂类]
        用于创建并管理享元对象，它针对抽象享元类编程，将各种类型的具体享元对象存储在一个享元池中。

享元模式以共享的方式高效地支持大量的细粒度对象，享元对象能做到共享的关键是区分内部状态和外部状态。
其中内部状态是存储在享元对象内部并且不会随环境改变而改变的状态，因此内部状态可以共享；
外部状态是随环境改变而改变的、不可以共享的状态。

优点
    它可以极大减少内存中对象的数量，使得相同对象或相似对象在内存中只保存一份；

缺点
    使得系统更加复杂，并且需要将享元对象的状态外部化，而读取外部状态使得运行时间变长。

适用情况
    一个系统有大量相同或者相似的对象，由于这类对象的大量使用，造成内存的大量耗费；
    对象的大部分状态都可以外部化，可以将这些外部状态传入对象中；
    多次重复使用享元对象。
"""

class Flyweight_abstract(object):
    """
    抽象享元类
    """
    def work(self):
        pass

class Flyweight_concrete_shared(Flyweight_abstract):
    """
    具体享元类(共享的)
    """
    def __init__(self, role):
        self.role = role
    def work(self, name):
        print '(%s) [%s] [%s]' % (self.__class__.__name__, self.role, name)

# class Flyweight_concrete_unshared(Flyweight_abstract):
#     """
#     具体享元类(非共享的)
#     """
#     def __init__(self, role):
#         self.role = role
#         self.name = None
#
#     def work(self, name):
#         self.name = name
#         print '(%s) [%s] [%s]' % (self.__class__.__name__, self.role, name)

class Flyweight_Factory_shared(object):
    """
    享元工厂类
    """
    def __init__(self):
        self.pool = {}
        self.count = {}
    def get_flyweight(self, role):
        if role not in self.pool:
            flyweight = Flyweight_concrete_shared(role)
            print '(%s): %s created' % (self.__class__.__name__, flyweight)
            self.pool[role] = flyweight
            self.count[role] = 1
        else:
            flyweight = self.pool[role]
            print '(%s): %s shared' % (self.__class__.__name__, flyweight)
            self.count[role] += 1
        return flyweight
    def get_count(self):
        print [(role, self.count[role]) for role in self.pool]

# class Flyweight_Factory_unshared(object):
#     """
#     享元工厂类
#     """
#     def __init__(self):
#         self.pool = []
#         self.count = 0
#     def get_flyweight(self, role):
#         flyweight = Flyweight_concrete_unshared(role)
#         print '(%s): %s created' % (self.__class__.__name__, flyweight)
#         self.pool.append(flyweight)
#         self.count += 1
#         return flyweight
#     def get_count(self):
#         print self.count


print '------------------------------------------------------------------------------------------'
factory = Flyweight_Factory_shared()

flyweight = factory.get_flyweight('soldier')
# (Flyweight_Factory_shared): <__main__.Flyweight_concrete_shared object at 0x1092f1dd0> created
flyweight.work('Captain Price')
# (Flyweight_concrete_shared) [soldier] [Captain Price]

flyweight = factory.get_flyweight('soldier')
# (Flyweight_Factory_shared): <__main__.Flyweight_concrete_shared object at 0x1092f1dd0> shared
flyweight.work('Soup Mactavish')
# (Flyweight_concrete_shared) [soldier] [Soup Mactavish]

flyweight = factory.get_flyweight('samurai')
# (Flyweight_Factory_shared): <__main__.Flyweight_concrete_shared object at 0x1092f1e10> created
flyweight.work('Himura Kenshin')
# (Flyweight_concrete_shared) [samurai] [Himura Kenshin]

print factory.pool
# {'soldier': <__main__.Flyweight_concrete_shared object at 0x1092f1dd0>,
#  'samurai': <__main__.Flyweight_concrete_shared object at 0x1092f1e10>}
factory.get_count()
# [('soldier', 2), ('samurai', 1)]
print '------------------------------------------------------------------------------------------'
# factory = Flyweight_Factory_unshared()
#
# flyweight = factory.get_flyweight('soldier')
# # (Flyweight_Factory_unshared): <__main__.Flyweight_concrete_unshared object at 0x101cc2090> created
# flyweight.work('Captain Price')
# # (Flyweight_concrete_unshared) [soldier] [Captain Price]
#
# flyweight = factory.get_flyweight('soldier')
# # (Flyweight_Factory_unshared): <__main__.Flyweight_concrete_unshared object at 0x101cc2150> created
# flyweight.work('Soup Mactavish')
# # (Flyweight_concrete_unshared) [soldier] [Soup Mactavish]
#
# flyweight = factory.get_flyweight('samurai')
# # (Flyweight_Factory_unshared): <__main__.Flyweight_concrete_unshared object at 0x101cc2110> created
# flyweight.work('Himura Kenshin')
# # (Flyweight_concrete_unshared) [samurai] [Himura Kenshin]
#
# print factory.pool
# # [<__main__.Flyweight_concrete_unshared object at 0x101cc2090>,
# #  <__main__.Flyweight_concrete_unshared object at 0x101cc2150>,
# #  <__main__.Flyweight_concrete_unshared object at 0x101cc2110>]
# factory.get_count()
# # 3
print '------------------------------------------------------------------------------------------'
