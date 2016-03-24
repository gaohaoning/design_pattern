#!/usr/bin/env python
# coding:utf-8

"""
解释器模式(Interpreter Pattern)
    定义语言(使用规定格式和语法的代码)的文法，并且建立一个解释器来解释该语言中的句子。

包含四个角色
    [AbstractExpression][抽象表达式]
        声明一个抽象的解释操作，
        该接口为抽象语法树中所有的节点共享；
    [TerminalExpression][终结符表达式]
        实现与文法中的终结符相关的解释操作；
        实现抽象表达式中所要求的方法；
        文法中每一个终结符都有一个具体的终结表达式与之相对应；
        比如公式R=R1+R2，在里面R1和R2就是终结符，对应的解析R1和R2的解释器就是终结符表达式；
    [NonterminalExpression][非终结符表达式]
        实现与文法中的非终结符相关的解释操作；
        对文法中的每一条规则，都需要一个具体的非终结符表达式类；
        非终结符表达式一般是文法中的运算符或者其他关键字；
        比如公式R=R1+R2，“+"就是非终结符，解析“+”的解释器就是一个非终结符表达式；
    [Context][环境类]
        包含解释器之外的一些全局信息；
        一般是用来存放文法中各个终结符所对应的具体值；

解释器模式描述了如何构成一个简单的语言解释器，主要应用在使用面向对象语言开发的编译器中。
它描述了如何为简单的语言定义一个文法，如何在该语言中表示一个句子，以及如何解释这些句子。

优点
    可扩展性比较好，灵活。
    增加了新的解释表达式的方式。
    易于实现文法。

缺点
    执行效率比较低，可利用场景比较少。
    对于复杂的文法比较难维护。

适用情况
    需要将一个需要解释执行的语言中的句子表示为一个抽象语法树。
    一些重复出现的问题可以用一种简单的语言来进行表达。
    文法较为简单。
"""

class AbstractExpression(object):
    """
    抽象表达式
    """
    def to_string(self):
        pass
    def interpret(self, context):
        pass

class Constant(AbstractExpression):
    """
    (常量)终结符表达式
    """
    def __init__(self, value):
        self.value = value
    def to_string(self):
        return str(bool(self.value))
    def interpret(self, context):
        return self.value

class Variable(AbstractExpression):
    """
    (变量)终结符表达式
    """
    def __init__(self, name):
        self.name = name
    def to_string(self):
        return str(self.name)
    def interpret(self, context):
        return context.lookup(self)

class And(AbstractExpression):
    """
    (逻辑与)非终结符表达式
    """
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def to_string(self):
        return '(%s AND %s)' % (self.left.to_string(), self.right.to_string())
    def interpret(self, context):
        return self.left.interpret(context) and self.right.interpret(context)

class Or(AbstractExpression):
    """
    (逻辑或)非终结符表达式
    """
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def to_string(self):
        return '(%s OR %s)' % (self.left.to_string(), self.right.to_string())
    def interpret(self, context):
        return self.left.interpret(context) or self.right.interpret(context)

class Not(AbstractExpression):
    """
    (逻辑非)非终结符表达式
    """
    def __init__(self, exp):
        self.exp = exp
    def to_string(self):
        return '(NOT %s)' % (self.exp.to_string(),)
    def interpret(self, context):
        return not self.exp.interpret(context)

class Context(object):
    """
    环境类
    """
    def __init__(self):
        self.map = {}
    def assign(self, key, value):
        self.map[key] = value
    def lookup(self, key):
        return self.map.get(key)




context = Context()

constant_a = Constant(True)
constant_b = Constant(False)
variable_x = Variable('x')
variable_y = Variable('y')
context.assign(variable_x, True)
context.assign(variable_y, False)

expression = And(And(variable_x, constant_a), Not(Or(variable_y, constant_b)))

print 'constant_a =', constant_a.to_string()
print 'constant_b =', constant_b.to_string()
print 'variable_x =', context.lookup(variable_x)
print 'variable_y =', context.lookup(variable_y)
# constant_a = True
# constant_b = False
# variable_x = True
# variable_y = False
print '%s = %s' % (expression.to_string(), expression.interpret(context))
# ((x AND True) AND (NOT (y OR False))) = True
