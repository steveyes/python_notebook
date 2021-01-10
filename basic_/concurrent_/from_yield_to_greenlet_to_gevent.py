#!/usr/bin/env python3
#


import time
import greenlet
import gevent


class YieldDemo():
    @staticmethod
    def funcA():
        while True:
            print('------func A-----')
            time.sleep(0.5)
            yield

    @staticmethod
    def funcB():
        while True:
            print('-----func B------')
            time.sleep(0.3)
            next(YieldDemo.funcA())

    @staticmethod
    def run():
        YieldDemo.funcB()


class GreentletDemo():
    @staticmethod
    def funcA():
        while True:
            print('------func A-----')
            time.sleep(0.5)
            # g2.switch()
            greenlet.greenlet(GreentletDemo.funcB).switch()

    @staticmethod
    def funcB():
        while True:
            print('-----func B------')
            time.sleep(0.3)
            # g1.switch()
            greenlet.greenlet(GreentletDemo.funcA).switch()

    @staticmethod
    def run():
        # g1 = greenlet.greenlet(GreentletDemo.funcA)
        # g2 = greenlet.greenlet(GreentletDemo.funcB)
        # g1.switch()
        greenlet.greenlet(GreentletDemo.funcA).switch()


class GeventDemo():
    @staticmethod
    def funcA():
        while True:
            print('-----func A------')
            gevent.sleep(0.5)

    @staticmethod
    def funcB():
        while True:
            print('-----func B------')
            gevent.sleep(0.3)

    @staticmethod
    def run():
        g1 = gevent.spawn(GeventDemo.funcA)
        g2 = gevent.spawn(GeventDemo.funcB)
        g1.join()
        g2.join()


if __name__ == '__main__':
    # YieldDemo.run()

    # GreentletDemo.run()

    GeventDemo.run()
