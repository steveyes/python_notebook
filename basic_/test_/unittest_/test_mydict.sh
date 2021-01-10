#!/usr/bin/bash

# test file patterns are like *_test.py
# test class patterns are like Test*
# test function/case patterns are like test_
# test assert patterns are like assert*


# install pytest
# pip install -U pytest

# run test
# shellcheck disable=SC2034
export PYTHONPATH="/home/$(whoami)/gitrepo/python_example"
python -m unittest test_mydict.TestDict