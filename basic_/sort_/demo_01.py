#!/usr/bin/env python3
#

index_dcode = ['54', '51', '63', '62', '53']


def main():
    dd = [
        {'dcode': '51', 'parent_dcode': '0 ', 'level': 'province', 'name': '四川省     '},
        {'dcode': '54', 'parent_dcode': '0 ', 'level': 'province', 'name': '西藏自治区   '},
        {'dcode': '53', 'parent_dcode': '0 ', 'level': 'province', 'name': '云南省     '},
        {'dcode': '63', 'parent_dcode': '0 ', 'level': 'province', 'name': '青海省     '},
        {'dcode': '62', 'parent_dcode': '0 ', 'level': 'province', 'name': '甘肃省     '}
    ]

    dd.sort(key=lambda e: index_dcode.index(e['dcode']))
    [print(d) for d in dd]


if __name__ == '__main__':
    main()
