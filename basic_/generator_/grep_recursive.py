#!/usr/bin/env python3
#

'''模拟： grep -rl 'iptables' /home/ranging/etc/
'''

import os


# 用来开启协程
def deco(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        next(res)
        return res

    return wrapper


@deco
def find(generator):
    while True:
        # 被deco修饰，所以一旦被再次调用，则运行到yield位置，等待send传值过来，并赋给path
        path = yield
        # 遍历path
        g = os.walk(path)
        for basepath, dirs, files in g:
            for file in files:
                # 取类型是文件的，将其绝对路径通传给迭代器cat
                filepath = os.path.join(basepath, file)
                generator.send(filepath)


@deco
def cat(generator):
    while True:
        # 等待委派生成器find传文件绝对路径过来，并赋值给filepath
        filepath = yield
        with open(filepath, encoding='utf-8') as f:
            # generator.send((filepath, f))
            for line in f:
                # 将filepath和line传给迭代器grep, 并将返回结果赋值给tag
                # 如果tag不为空，表示找到了，跳出当前循环，继续下一个文件的cat
                tag = generator.send((filepath, line))
                if tag:
                    break


@deco
def grep(pattern):
    tag = False
    while True:
        # 等待委派生成器传值过来，赋给filepath和line，并将tag返回
        filepath, line = yield tag
        tag = False
        if pattern in line:
            print(filepath)
            tag = True


def main():
    path = '/home/ranging/etc'
    word = 'iptables'
    find(cat(grep(word))).send(path)


if __name__ == '__main__':
    main()
