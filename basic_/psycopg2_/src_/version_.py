from __future__ import absolute_import

from Database import database

if __name__ == '__main__':
    version, = database.execute('select VERSION()', fetch_one=True)
    print(version)
