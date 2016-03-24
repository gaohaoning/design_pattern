#!/usr/bin/env python
# coding:utf-8

"""
代理模式(Proxy Pattern)
    给某一个对象提供一个代理，并由代理对象控制对原对象的引用。

包含三个角色
    [AbstractSubject][抽象主题]
        声明了真实主题和代理主题的共同接口；
    [RealSubject][真实主题]
        定义了代理角色所代表的真实对象，在真实主题角色中实现了真实的业务操作，
        客户端可以通过代理主题角色间接调用真实主题角色中定义的方法。
    [Proxy][代理]
        内部包含对真实主题的引用，从而可以在任何时候操作真实主题对象；

优点
    能够协调调用者和被调用者，在一定程度上降低了系统的耦合度；

缺点
    由于在客户端和真实主题之间增加了代理对象，因此有些类型的代理模式可能会造成请求的处理速度变慢，
    并且实现代理模式需要额外的工作，有些代理模式的实现非常复杂。

远程代理
    远程代理可以将网络的细节隐藏起来，使得客户端不必考虑网络的存在。
    客户完全可以认为被代理的远程业务对象是局域的而不是远程的，而远程代理对象承担了大部分的网络通信工作。

虚拟代理
    当一个对象的加载十分耗费资源的时候，虚拟代理的优势就非常明显地体现出来了。
    虚拟代理模式是一种内存节省技术，那些占用大量内存或处理复杂的对象将推迟到使用它的时候才创建。

保护代理
    可以控制对一个对象的访问，可以给不同的用户提供不同级别的使用权限。

代理模式的英文叫做Proxy或Surrogate，它是一种对象结构型模式。
"""

class Subject(object):
    """
    抽象主题
    """
    def request(self):
        pass

class RealSubject(Subject):
    """
    真实主题
    """
    def request(self):
        print '(%s) this is the real request' % self.__class__.__name__

class Proxy(Subject):
    """
    代理
    """
    def __init__(self):
        self.real_subject = RealSubject()
    def request(self):
        self.real_subject.request()


proxy = Proxy()
proxy.request()
# (RealSubject) this is the real request
