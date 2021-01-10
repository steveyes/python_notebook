#!/usr/bin/env python3
#

"""
当前目录是二级目录，使用相对路径导包

1 需要在包所在的__init__.py中输入：
from ... import ...
from ... import ...
__all__ == [...]

2 运行该脚本，则需要cd 到程序的根目录， 然后输入：
    python -m import_.app_
"""

import unittest

from basic_.import_ import TestMyDict


def runTestMyDict():
    unittest.main()


if __name__ == '__main__':
    runTestMyDict()
