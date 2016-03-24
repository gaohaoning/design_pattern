#!/usr/bin/env python
# coding:utf-8

"""
命令模式(Command Pattern)
    将一个请求封装为一个对象，从而使我们可用不同的请求对客户进行参数化；
    对请求排队或者记录请求日志，以及支持可撤销的操作。

包含四个角色
    [AbstractCommand][抽象命令类]
        声明执行操作的接口；
    [ConcreteCommand][具体命令类]
        是抽象命令类的子类，实现了在抽象命令类中声明的方法；
        它拥有一个接收者对象，将接收者对象的动作绑定其中；
        通过调用接收者对象的动作，执行相应的操作；
    [Invoker][调用者]
        即请求的发送者，又称为请求者，它通过命令对象来执行请求；
    [Receiver][接收者]
        执行与请求相关的操作，它具体实现对请求的业务处理；

命令模式的本质是对命令进行封装，将发出命令的责任和执行命令的责任分割开。
命令模式使请求本身成为一个对象，这个对象和其他对象一样可以被存储和传递。

优点
    降低系统的耦合度，增加新的命令很方便，而且可以比较容易地设计一个命令队列和宏命令，并方便地实现对请求的撤销和恢复；

缺点
    可能会导致某些系统有过多的具体命令类。

适用情况
    需要将请求调用者和请求接收者解耦，使得调用者和接收者不直接交互；
    需要在不同的时间指定请求、将请求排队和执行请求；
    需要支持命令的撤销操作和恢复操作，需要将一组操作组合在一起，即支持宏命令。

命令模式是一种对象行为型模式，其别名为动作(Action)模式或事务(Transaction)模式。
"""

class Invoker(object):
    """
    调用者
    """
    def __init__(self, command):
        self.command = command
    def call(self):
        print '%s call()' % self.__class__.__name__,
        self.command.execute()

class Command_abstract(object):
    """
    抽象命令类
    """
    def execute(self):
        pass

class Command_concrete(Command_abstract):
    """
    具体命令类
    """
    def __init__(self, receiver):
        self.receiver = receiver
    def execute(self):
        print '%s execute()' % self.__class__.__name__,
        self.receiver.action()

class Receiver(object):
    """
    接收者
    """
    def action(self):
        print '%s action()' % self.__class__.__name__,
        print 'this is receiver action ...'


receiver = Receiver()
command_concrete = Command_concrete(receiver)
invoker = Invoker(command_concrete)
invoker.call()

# Invoker call()
# Command_concrete execute()
# Receiver action()
# this is receiver action ...
