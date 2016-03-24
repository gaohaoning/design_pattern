#!/usr/bin/env python
# coding:utf-8

"""
外观模式(Facade Pattern)
    外部与一个子系统的通信必须通过一个统一的外观对象进行，为子系统中的一组接口提供一个一致的界面，
    外观模式定义了一个高层接口，这个接口使得这一子系统更加容易使用。

包含两个角色
    [Facade][外观角色]
        是在客户端直接调用的角色，在外观角色中可以知道相关的(一个或者多个)子系统的功能和责任，
        它将所有从客户端发来的请求委派到相应的子系统去，传递给相应的子系统对象处理；
    [SubSystem][子系统角色]
        在软件系统中可以同时有一个或者多个子系统角色，每一个子系统可以不是一个单独的类，而是一个类的集合，它实现子系统的功能。

外观模式要求一个子系统的外部与其内部的通信通过一个统一的外观对象进行，外观类将客户端与子系统的内部复杂性分隔开，
使得客户端只需要与外观对象打交道，而不需要与子系统内部的很多对象打交道。

优点
    对客户屏蔽子系统组件，减少了客户处理的对象数目并使得子系统使用起来更加容易，
    它实现了子系统与客户之间的松耦合关系，并降低了大型软件系统中的编译依赖性，简化了系统在不同平台之间的移植过程；

缺点
    不能很好地限制客户使用子系统类，而且在不引入抽象外观类的情况下，增加新的子系统可能需要修改外观类或客户端的源代码，违背了“开闭原则”。

适用情况
    要为一个复杂子系统提供一个简单接口；
    客户程序与多个子系统之间存在很大的依赖性；
    在层次化结构中，需要定义系统中每一层的入口，使得层与层之间不直接产生联系。

外观模式又称为门面模式，它是一种对象结构型模式。
"""

class Tall(object):
    """
    子系统角色
    """
    def behave(self):
        print self.__class__.__name__

class Rich(object):
    """
    子系统角色
    """
    def behave(self):
        print self.__class__.__name__

class Handsome(object):
    """
    子系统角色
    """
    def behave(self):
        print self.__class__.__name__

class Facade(object):
    """
    外观角色
    """
    def __init__(self):
        self.tall = Tall()
        self.rich = Rich()
        self.handsome = Handsome()

    def show_body(self):
        self.tall.behave()
        self.handsome.behave()

    def show_financial(self):
        self.rich.behave()


facade = Facade()
facade.show_body()
# Tall
# Handsome
facade.show_financial()
# Rich
