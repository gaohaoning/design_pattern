#!/usr/bin/env python
# coding:utf-8

"""
建造者模式(Builder Pattern)
    将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。
    建造者模式是一步一步创建一个复杂的对象，它允许用户只通过指定复杂对象的类型和内容就可以构建它们，用户不需要知道内部的具体构建细节。

包含四个角色
    [Product][产品]
        是被构建的复杂对象，包含多个组成部件；
    [AbstractBuilder][抽象建造者]
        为创建一个产品对象的各个部件指定抽象接口；
    [ConcreteBuilder][具体建造者]
        实现了抽象建造者接口，实现各个部件的构造和装配方法，定义并明确它所创建的复杂对象，也可以提供一个方法返回创建好的复杂产品对象；
    [Director][指挥者]
        负责安排复杂对象的建造次序，指挥者与抽象建造者之间存在关联关系，可以在其建造方法中调用建造者对象的部件构造与装配方法，完成复杂对象的建造；

在建造者模式的结构中引入了一个指挥者类，该类的作用主要有两个：
    一方面它隔离了客户与生产过程；
    另一方面它负责控制产品的生成过程。
指挥者针对抽象建造者编程，客户端只需要知道具体建造者的类型，即可通过指挥者类调用建造者的相关方法，返回一个完整的产品对象。

优点
    客户端不必知道产品内部组成的细节，将产品本身与产品的创建过程解耦，
    使得相同的创建过程可以创建不同的产品对象，每一个具体建造者都相对独立，而与其他的具体建造者无关，
    因此可以很方便地替换具体建造者或增加新的具体建造者，符合“开闭原则”，还可以更加精细地控制产品的创建过程；

缺点
    由于建造者模式所创建的产品一般具有较多的共同点，其组成部分相似，因此其使用范围受到一定的限制，
    如果产品的内部变化复杂，可能会导致需要定义很多具体建造者类来实现这种变化，导致系统变得很庞大。

适用情况
    需要生成的产品对象有复杂的内部结构，这些产品对象通常包含多个成员属性；
    需要生成的产品对象的属性相互依赖，需要指定其生成顺序；
    对象的创建过程独立于创建该对象的类；
    隔离复杂对象的创建和使用，并使得相同的创建过程可以创建不同类型的产品。

建造者模式属于对象创建型模式。根据中文翻译的不同，建造者模式又可以称为生成器模式。
"""

class Product(object):
    """
    产品
    """
    def __init__(self):
        self.part_a = None
        self.part_b = None
    def __str__(self):
        return '[product:%s]=[part_a:%s]+[part_b:%s]' % (self.__class__.__name__, self.part_a, self.part_b)

class Builder_abstract(object):
    """
    抽象建造者
    """
    def __init__(self):
        self.product = None
    def new_product(self):
        self.product = Product()
    def build_partA(self):
        pass
    def build_partB(self):
        pass

class Builder_concrete_1(Builder_abstract):
    """
    具体建造者 1
    """
    def build_partA(self):
        self.product.part_a = 'big Part_A'
    def build_partB(self):
        self.product.part_b = 'big Part_B'

class Builder_concrete_2(Builder_abstract):
    """
    具体建造者 2
    """
    def build_partA(self):
        self.product.part_a = 'small Part_A'
    def build_partB(self):
        self.product.part_b = 'small Part_B'

class Director(object):
    """
    指挥者
    """
    def __init__(self, builder):
        self.builder = builder
    def build_parts(self):
        self.builder.new_product()
        self.builder.build_partA()
        self.builder.build_partB()
    def get_product(self):
        return self.builder.product


builder_1 = Builder_concrete_1()
director_1 = Director(builder_1)
director_1.build_parts()
product_1 = director_1.get_product()
print product_1
# [product:Product]=[part_a:big Part_A]+[part_b:big Part_B]

builder_2 = Builder_concrete_2()
director_2 = Director(builder_2)
director_2.build_parts()
product_2 = director_2.get_product()
print product_2
# [product:Product]=[part_a:small Part_A]+[part_b:small Part_B]
