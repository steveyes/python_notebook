#!/usr/bin/env python3
#


MINI14 = "1.4GHz Mac mini"

'''
这里嵌套了MacMini14类。这是禁止直接实例化一个类的简洁方式。
'''


class AppleFactory:
    class MacMini14:
        def __init__(self):
            self.memory = 4
            self.hdd = 500
            self.gpu = "Intel HD Graphics 5000"

        def __str__(self) -> str:
            info = ('Model: {}'.format(MINI14),
                    'Memory: {}GB'.format(self.memory),
                    'HardDisk: {}GB'.format(self.hdd),
                    'Graphics Card:: {}'.format(self.gpu)
                    )
            return '\n'.join(info)

    def build_computer(self, model):
        if (model == MINI14):
            return self.MacMini14()
        else:
            print("I don't know how to build {}".format(model))


if __name__ == '__main__':
    afac = AppleFactory()
    mac_mini = afac.build_computer(MINI14)
    print(mac_mini)
