#!/usr/bin/env python3
#


import json
from pprint import pprint


def demo_01():
    my_mapping = {'a': 23, 'b': 42, 'c': 0x10}
    print(my_mapping)
    pprint(my_mapping)
    print(json.dumps(my_mapping, indent=4, sort_keys=True))
    pprint(json.dumps(my_mapping, indent=4, sort_keys=True))


if __name__ == '__main__':
    demo_01()
