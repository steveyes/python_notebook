#!/usr/bin/env bash

export PYTHONPATH="/home/$(whoami)/gitrepo/python_example"

# test file patterns are like test_*.py
# test class patterns are like Test* and mustn't have __init__() method
# test function/case patterns are like test_
# test assert patterns are like assert


# test all case in test_class.py
#pytest test_class.py

# test designated class
#pytest test_class.py::TestClassOne

# test designated case in designated class
#pytest test_class.py::TestClassTwo::test_one

# test in multi-processes
# install pytest-xdist
#pip install -U pytest-xdist
pytest test_class.py -n 4