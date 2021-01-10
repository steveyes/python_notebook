import pytest


def add1(x):
    return x + 1


def test_add1():
    assert add1(4) == 5


