#!/usr/bin/env python


import sys
from os import listdir, linesep
from os.path import dirname, basename, isdir, isfile, abspath, join as pathjoin

'''
This script is intended to implement the Step 4 of : https://wiki.vip.corp.ebay.com/pages/editpage.action?pageId=665548545
'''


def replace_lib(file_path, lib_path):
    src = "sys.path.append('/ebay/cassinfra/lib')"
    lib_path = "sys.path.append('%s')" % lib_path + '\n' + "sys.path.append('/ebay/search/lib')"
    if file_path.endswith(".py"):
        f = open(file_path)
        r = f.read()
        s = r.replace(src, lib_path)
        f.close()
        f = open(file_path, 'w')
        f.write(s)
        f.close()


def recusive_lib(root_path, depth):
    files = listdir(root_path)
    for f in files:
        filepath = pathjoin(root_path, f)

        if isdir(filepath):
            depth += 1
            recusive_lib(filepath, depth)
            depth -= 1

        elif isfile(filepath):
            replace_lib(filepath, depth * '../' + 'lib/')


if __name__ == '__main__':
    recusive_lib('bin/', 1)
