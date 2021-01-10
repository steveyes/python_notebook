#!/usr/bin/env python3
#


def enuming(ll: list):
    for i, v in enumerate(ll):
        print(f'index: {i}, value: {v}')


if __name__ == '__main__':
    ll = ['A', 'B', 'C']
    enuming(ll)
