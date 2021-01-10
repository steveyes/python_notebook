#!/usr/bin/env python3
#

import pexpect
from time import sleep

log_file = '/tmp/auto_ssh.log'


def exp(child, prompt, inputs, interval):
    explist = [prompt, pexpect.EOF, pexpect.TIMEOUT]
    index = child.expect(explist)
    if index == 0:
        child.sendline(inputs)
    elif index == 1:
        print("warning: EOF")
    elif index == 2:
        print("warning: TIMEOUT")
    sleep(interval)


def main():
    # 创建一个子进程(child)去连接12.1.30.15，记录日志，并设置适当的tty窗口大小
    child = pexpect.spawn('/bin/bash', ['-c', 'ssh user01@127.0.0.1'])
    child.logfile = open(log_file, 'wb')
    child.setwinsize(62, 206)
    exp(child, 'password', '123456', 0.1)

    # 自动与UTM交互，登录到目标机器
    exp(child, 'input_demo', '1\r', 0.1)
    exp(child, 'input_demo', '1\r', 0.1)
    exp(child, 'input_demo', '1\r', 0.1)
    child.sendcontrol('u')
    exp(child, 'account', 'user01', 0.1)
    exp(child, 'passwd', 'passwd01', 0.1)

    # 将子进程(child)从后台切到前台
    child.interact()


if __name__ == '__main__':
    main()
