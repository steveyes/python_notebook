#!/usr/bin/env python3
#

def reader():
    # 模拟从文件读取数据的生成器
    for i in range(4):
        yield '<< %s' % i


def reader_wrapper1(g):
    # 循环迭代从reader产生的数据
    for v in g:
        yield v


wrap1 = reader_wrapper1(reader())
print('----------wrapper1----------')
for i in wrap1:
    print(i)


def reader_wrapper2(g):
    # 效果等同于 for v in g: yield v
    yield from g


wrap2 = reader_wrapper2(reader())
print('----------wrapper2----------')
for i2 in wrap2:
    print(i2)
