#!/usr/bin/env python3
# encoding: utf-8

import paramiko
import subprocess
from time import sleep
from os import path

UTMHOST = {
    'hostname': '',
    'port': 22,
    'username': '',
    'password': '',
}

DSTHOST = {
    'hostname': '12.105.32.1',
    'user': 'sixieops',
    'password': 'Sixie971',
}

BUFFSIZE = 8192


class AjzqConnect():
    def __init__(self):
        # 发起到UTMHOST的ssh连接
        self.ssh = paramiko.SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(**UTMHOST)
        self.channel = self.ssh.invoke_shell()
        self.channel.recv(BUFFSIZE)

        # 通过UTM的字符用户界面CUI连接到目标机器, UTM的CUI是嵌在windows系统中的，所以行末以'\r'界定
        for i in range(0, 3):
            self.secure_send('1', '\r')
        self.secure_send(DSTHOST['user'], '\r')
        self.secure_send(DSTHOST['password'], '\r', interval=30)

    def secure_send(self, data, seperator='\n', interval=0.3):
        truedata = data + seperator if seperator else data
        self.channel.send(truedata)
        sleep(interval)
        return self.channel.recv(BUFFSIZE).decode()

    def upload(self, src, dst):
        self.secure_send("cat >> {dst} << EOF".format(dst=dst))
        with open(src, 'r') as f:
            self.secure_send(f.read(), seperator=None)
        self.secure_send("EOF")

    def secure_recv(self, data):
        # send the dd command
        buff = b''
        self.channel.send(data + '\n')
        sleep(0.3)

        # collect the date
        while True:
            resp = self.channel.recv(BUFFSIZE)
            if len(resp) == BUFFSIZE:
                buff += resp
            else:
                buff += resp
                break
            sleep(0.3)
        return buff

    def download(self, src, dst):
        cmd_stmt = "dd if={} 2>/dev/null".format(src)
        idx_start = len(cmd_stmt)
        len_ps1 = len(b'sixieops@debian:~$ ')
        res = self.secure_recv(cmd_stmt)
        # 需要将回传过来中被UTM替换过的CRLF还原成LF，
        # 并且开头的cmd_stmt部分: idx_start + 1, 以及流末的$PS1部分: -len_ps1, 都要剔除
        data = res.replace(b'\r\n', b'\n')[idx_start + 1:-len_ps1]
        with open(dst, 'wb') as f:
            f.write(data)

    def close(self):
        self.channel.close()
        self.ssh.close()


def demo_upload(src, dst):
    conn = AjzqConnect.AjzqConnect()
    conn.download(src, dst)
    conn.close()


def demo_download(src, dst):
    conn = AjzqConnect()
    conn.download(src, dst)
    conn.close()
