#!/usr/bin/env python3
#


class REST_API(object):
    def __init__(self, _p_path=''):
        self._p_path = _p_path

    def __getattr__(self, _path):
        return REST_API(f"{self._p_path}/{_path}")

    def __str__(self):
        return self._p_path


if __name__ == '__main__':
    print(REST_API().api.image.village)
