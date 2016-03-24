#!/usr/bin/env python
# coding:utf-8

"""
责任链模式(Chain of Responsibility)
    很多对象由每一个对象对其下家的引用而连接起来形成一条链。请求在这个链上传递，直到链上的某一个对象决定处理此请求。

包含两个角色
    [AbstractHandler][抽象处理者]
        定义了一个处理请求的方法；
        所有的具体处理者都必须实现该抽象类；
    [ConcreteHandler][具体处理者]
        处理它所负责的请求，同时也可以访问它的后继者；
        如果它能够处理该请求则处理，否则将请求传递到它的后继者；

优点
    实现了请求者与处理者代码分离:
        发出这个请求的客户端并不知道链上的哪一个对象最终处理这个请求，
        这使得系统可以在不影响客户端的情况下动态地重新组织和分配责任，提高系统的灵活性和可扩展行。

缺点
    每次都是从链头开始。

责任链模式强调的是每一个对象及其对下家的引用来组成一条链，利用这种方式将发送者和接收者解耦。
"""

class Handler(object):
    """
    抽象处理者
    """
    def __init__(self):
        self.successor = None
    def handle(self, request):
        pass
    def set_successor(self, successor):
        self.successor = successor

class Handler_concrete_1(Handler):
    """
    具体处理者
    """
    def handle(self, request):
        if request <= 10:
            print '(request:%s) %s handled' % (request, self.__class__.__name__)
        else:
            self.successor.handle(request)

class Handler_concrete_2(Handler):
    """
    具体处理者
    """
    def handle(self, request):
        if request > 10 and request <= 20:
            print '(request:%s) %s handled' % (request, self.__class__.__name__)
        else:
            self.successor.handle(request)

class Handler_concrete_3(Handler):
    """
    具体处理者
    """
    def handle(self, request):
        if request > 20:
            print '(request:%s) %s handled' % (request, self.__class__.__name__)
        else:
            self.successor.handle(request)


h1 = Handler_concrete_1()
h2 = Handler_concrete_2()
h3 = Handler_concrete_3()
h1.set_successor(h2)
h2.set_successor(h3)

requests = [5, 15, 25]
for request in requests:
    h1.handle(request)

# (request:5) Handler_concrete_1 handled
# (request:15) Handler_concrete_2 handled
# (request:25) Handler_concrete_3 handled
