#!/usr/bin/env python3
#


class Model(object):
    # cls 是行参， 实参是一个类
    def __new__(cls, *args, **kwargs):
        print('Model.__new__() is running. id of cls is %s' % id(cls))
        r = super(Model, cls).__new__(cls)
        print('id of r is %s' % id(r))
        return r


# 创建类的时候，调用父类的 __new__， 实参为： AliceModel， 行参为： cls
class AliceModel(Model):
    def __init__(self, name):
        print('AliceMode.__init__() is running, id of self is %s' % id(self))
        self.name = name
        print('Alice.name is %s' % self.name)


print('id of Model: ', id(Model))

# 所以这里的AliceModel就是Model中__new__的cls, 实参对应行参
print('id of AliceModel: ', id(AliceModel))

# 这里的am01就相当与AliceModel中__init__的self
am01 = AliceModel('')
print('id of am01: ', id(am01))
