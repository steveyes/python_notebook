#!/usr/bin/env python3
#

from collections import namedtuple

from multiprocessing import Process
import os

color_pattern = namedtuple('_color', ('red', 'green', 'yellow', 'blue', 'purple', 'azure', 'white'))
color_pattern.red = "\033[31;1m{}\033[0m"
color_pattern.green = "\033[32;1m{}\033[0m"
color_pattern.yellow = "\033[33;1m{}\033[0m"
color_pattern.blue = "\033[34;1m{}\033[0m"
color_pattern.purple = "\033[35;1m{}\033[0m"
color_pattern.azure = "\033[36;1m{}\033[0m"
color_pattern.white = "\033[37;1m{}\033[0m"


def info(title):
    print(title)
    print('module name: ', __name__)
    print('parent process: ', os.getppid())
    print('process id: ', os.getpid())
    print("\n\n")


def f(name):
    info(color_pattern.red.format("called from child process function"))
    print('hello', name)


if __name__ == '__main__':
    info(color_pattern.green.format("main process line"))
    p = Process(target=f, args=('bob',))
    p.start()
