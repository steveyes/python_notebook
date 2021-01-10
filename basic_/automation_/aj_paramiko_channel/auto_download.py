#!/usr/bin/env python3
# encoding: utf-8

import paramiko
import sys
from . import AjzqConnect

# 记录日志
paramiko.util.log_to_file('/tmp/auto_download.log')

if __name__ == '__main__':
    src = sys.argv[1]
    dst = sys.argv[2]
    conn = AjzqConnect.AjzqConnect()
    conn.download(src, dst)
    conn.close()
