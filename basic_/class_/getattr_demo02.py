#!/usr/bin/env python3
#


class RestAPI(object):
    def __init__(self, _p_path=''):
        self._p_path = _p_path

    def __getattr__(self, _path):
        return RestAPI(f"{self._p_path}/{_path}")

    def __str__(self):
        return self._p_path


def demo01():
    """
    调用分析
    1 RestAPI()返回一个实例: C1(_p_path='')
    2 RestAPI().status尝试去__getattr__中获取, 并返回一个实例: C2(_p_path='/status')
    3 RestAPI().status.user尝试去__getattr__中获取, 并返回一个实例: C3(_p_path='/status/user')
    4 同上
    5 同上
    :return:
    """
    print(RestAPI())
    print(RestAPI().status)
    print(type(RestAPI().status))
    print(RestAPI().status.user)
    print(type(RestAPI().status.user))
    print(RestAPI().status.user.timeline)
    print(type(RestAPI().status.user.timeline))
    print(RestAPI().status.user.timeline.list)
    print(type(RestAPI().status.user.timeline.list))


def demo02():
    api = RestAPI()
    print(api)
    print(api.status)
    print(api.status.user)
    print(api.status.user.timeline)
    print(api.status.user.timeline.list)


if __name__ == '__main__':
    demo01()
