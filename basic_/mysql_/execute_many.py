#!/usr/bin/env python3
#

import yaml
import pymysql
from os.path import join as opjoin, dirname, realpath

BASEDIR = dirname(dirname(realpath(__file__)))
CONF = opjoin(BASEDIR, 'conf/conf.yml')
DBCONF = yaml.load(open(CONF).read()).get('database')


def create_args_globbing(num):
    ll = []
    for n in range(num):
        ll.append('?')
    return ', '.join(ll)


def main():
    conn = pymysql.connect(**DBCONF)
    cur = conn.cursor()
    sql = '''insert into user(uid, user, role) values (%s)''' % create_args_globbing(3)
    args = [(1, 'Alice', 'user'),
            (2, 'Bob', 'user'),
            (3, 'Eve', 'adversary'),
            (4, 'Mallory', 'adversary'),
            (5, 'Carol', 'user'),
            (6, 'Dave', 'user'),
            (7, 'Isaac', 'ISP'),
            (8, 'Justin', 'Justice'),
            (9, 'Oscar', 'adversary'),
            (10, 'Pat', 'Prover'),
            (11, 'Victor', 'Verifier'),
            (12, 'Trent', 'Arbitrator'),
            (13, 'Walter', 'Warden')]
    try:
        effect_rows = cur.executemany(sql.replace('?', '%s'), args)
    except BaseException as be:
        raise be
    else:
        print(effect_rows)


if __name__ == '__main__':
    main()
