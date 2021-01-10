#!/usr/bin/env python3
#

from typing import Optional, Any

ll = {'bob': 75, 'Adam': 92, 'Bart': 66, 'lisa': 88}


def by_name(t: Optional) -> Any:
    return t[0].lower()


def by_score(t: Optional) -> Any:
    return t[1]


if __name__ == '__main__':
    print(sorted(ll.items(), key=by_name, reverse=False))
    print(sorted(ll.items(), key=by_name, reverse=True))

    print(sorted(ll.items(), key=by_score, reverse=False))
    print(sorted(ll.items(), key=by_score, reverse=True))
