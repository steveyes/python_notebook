#!/usr/bin/env python3
#

def foo():
    while True:
        # x 接受yield通过send发过来的值, 并且返回yield右边的值
        x = yield
        print('value: ', x)


def foo_run():
    # g是一个生成器
    g = foo()

    # 程序运行到yield就停住了,等待下一个next, 或者使用g.send()或者g.send(None)可以达到同样的效果
    next(g)

    # 给yield发送值1,然后这个值被赋值给了x, 并且打印出来, 然后继续下一次循环停在yield处
    g.send(1)
    g.send(2)
    next(g)

    # 程序一旦执行到yield就会停在该处,并且将其返回值进行返回。
    # foo中并没有设置返回值，所有默认程序返回的是None, 通过打印语句来查看一下第一次next的返回值
    print(next(g))

    '''
    send()方法具有两种功能：
        第一，传值，send()方法，将其携带的值传递给yield，注意，是传递给yield，而不是x,然后再将其赋值给x；
        第二，send()方法具有和next()方法一样的功能，也就是说，传值完毕后，会接着上次执行的结果继续执行，知道遇到yield停止。
        这也就为什么在调用g.send()方法后，还会打印出x的数值。
        我们可以总结出send()的两个功能：1.传值；2.next()。
    '''


'''
也就是说，在一个生成器函数未启动之前，是不能传递数值进去。
必须先传递一个None进去或者调用一次next(g)方法，才能进行传值操作。
至于为什么要先传递一个None进去，可以看一下官方说法。

Because generator-iterators begin execution at the top of the
    generator's function body, there is no yield expression to receive
    a value when the generator has just been created.  Therefore,
    calling send() with a non-None argument is prohibited when the
    generator iterator has just started, and a TypeError is raised if
    this occurs (presumably due to a logic error of some kind).  Thus,
    before you can communicate with a coroutine you must first call
    next() or send(None) to advance its execution to the first yield
    expression.
    
问题就来，既然在给yield传值过程中，会调用next()方法，那么是不是在调用一次函数的时候，是不是每次都要给它传递一个空值？
有没有什么简便方法来解决這个问题呢？
答案，装饰器！！
'''

# 装饰器:用来开启协程
def deco(func):
    def wrapper():
        res = func()
        next(res)
        # 返回一个已经执行了next()方法的函数对象, 使其执行到yield的就绪状态
        return res

    return wrapper


@deco
def bar():
    food_list = []
    while True:
        # yield接受send发过来的值赋给food, 并返回food_list给send, send是调用者
        food = yield food_list
        food_list.append(food)
        print('elements in foodlist are: ', food)


g = bar()
print(g.send('苹果'))
print(g.send('香蕉'))
print(g.send('菠萝'))
