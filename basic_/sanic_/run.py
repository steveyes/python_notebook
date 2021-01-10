#!/usr/bin/env python3
#

'''
:reference: https://sanic.readthedocs.io
'''

from example_.sanic_example.readthedocs import app

'''
启动脚本
'''


def main():
    app.run('0.0.0.0', port=8090, access_log=False)


if __name__ == '__main__':
    main()
