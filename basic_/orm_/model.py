#!/usr/bin/env python3
#

import time
import uuid
import sys
import yaml
import asyncio
from ast import literal_eval
from web.orm import Model, IntegerField, StringField, create_pool, destroy_pool
from os.path import dirname, realpath, join

BASEDIR = dirname(dirname(realpath(__file__)))
CONF = join(BASEDIR, 'conf/conf.yml')
DBCONF = yaml.load(open(CONF).read()).get('database_pool')


def next_id():
    return '%15d%s000' % (int(time.time()), uuid.uuid1().hex)


class User(Model):

    @classmethod
    def enum_map(cls, key):
        usermap = {
            'User': 1,
            'Adversary': 2,
            'ISP': 3,
            'Justice': 4,
            'Prover': 5,
            'Verifier': 6,
            'Arbitrator': 7,
            'Warden': 8,
        }
        return usermap[key]

    __table__ = 'crypto_user'
    uid = IntegerField('uid', primary_key=True)
    user = StringField('user')
    role = IntegerField('role')


class DictTemple(Model):
    __table__ = 'dict_temple'
    uid = IntegerField('uid', primary_key=True)
    zj = StringField('zj', column_type='varchar(30)')
    pb = StringField('pb', column_type='varchar(30)')
    temple_name_cn = StringField('temple_name_cn', column_type='varchar(90)')
    location = StringField('location', column_type='varchar(300)')
    principal = StringField('principal', column_type='varchar(45)')
    rec_create_date = StringField('rec_create_date')
    rec_update_date = StringField('rec_update_date')


class TabTemple(Model):
    @classmethod
    def enum_check_status(cls, key):
        usermap = {
            'passwd': 1,
            'failed': 2,
            'checking': 3,
        }
        return usermap[key]

    __table__ = 'tab_temple'
    uid = IntegerField('uid', primary_key=True)
    login_password = StringField('login_password', column_type='varchar(120)')
    mobile_num = StringField('mobile_num', column_type='varchar(15)')
    phone_num = StringField('phone_num', column_type='varchar(20)')
    temple_name_tibetan = StringField('temple_name_tibetan', column_type='varchar(150)')
    location_reg_cert = StringField('location_reg_cert', column_type='varchar(200)')
    bank_account_license = StringField('bank_account_license', column_type='varchar(200)')
    manager_idcard = StringField('manager_idcard', column_type='varchar(200)')
    other_cert = StringField('other_cert', column_type='varchar(200)')
    check_status = IntegerField('check_status')


async def user_findall():
    loop = asyncio.get_event_loop()
    await create_pool(loop=loop, **DBCONF)
    res = await User.find_all()
    await destroy_pool()
    return res


async def user_findnumber(selectedFields, where):
    loop = asyncio.get_event_loop()
    await create_pool(loop=loop, **DBCONF)
    res = await User.find_number(selectedFields, where)
    await destroy_pool()
    print(res)


async def user_find(pk):
    loop = asyncio.get_event_loop()
    await create_pool(loop=loop, **DBCONF)
    res = await User.find(pk)
    await destroy_pool()
    print(res)


async def user_save(user):
    loop = asyncio.get_event_loop()
    await create_pool(loop=loop, **DBCONF)
    await user.save()
    await destroy_pool()


async def user_update(user):
    loop = asyncio.get_event_loop()
    await create_pool(loop=loop, **DBCONF)
    await user.update()
    await destroy_pool()


async def user_remove(user):
    loop = asyncio.get_event_loop()
    await create_pool(loop=loop, **DBCONF)
    await user.remove()
    await destroy_pool()


async def temple_findall():
    loop = asyncio.get_event_loop()
    await create_pool(loop=loop, **DBCONF)
    res = await TabTemple.find_all()
    await destroy_pool()
    return res


def main():
    u01 = User(uid=10001, user='Alice', role=User.enum_map('User'))
    u02 = User(uid=10002, user='Bob', role=User.enum_map('User'))
    u03 = User(uid=10003, user='Eve', role=User.enum_map('Adversary'))
    u04 = User(uid=10004, user='Mallory', role=User.enum_map('Adversary'))
    u05 = User(uid=10005, user='Carol', role=User.enum_map('User'))
    u06 = User(uid=10006, user='Dave', role=User.enum_map('User'))
    u07 = User(uid=10007, user='Isaac', role=User.enum_map('ISP'))
    u08 = User(uid=10008, user='Justin', role=User.enum_map('Justice'))
    u09 = User(uid=10009, user='Oscar', role=User.enum_map('Adversary'))
    u10 = User(uid=10010, user='Pat', role=User.enum_map('Prover'))
    u11 = User(uid=10011, user='Victor', role=User.enum_map('Verifier'))
    u12 = User(uid=10012, user='Trent', role=User.enum_map('Arbitrator'))
    u13 = User(uid=10013, user='Walter', role=User.enum_map('Warden'))

    # findall
    tasks = [temple_findall()]

    # findnumber
    # tasks = [user_findnumber('id,name,email,password', ''' id=10001 ''')]

    # find
    # tasks = [user_find('10001')]

    # save
    # users = [u01, u02, u03, u04, u05, u06, u07, u08, u09, u10, u11, u12, u13]
    # users = [u01, u02, u03]

    # tasks = []
    # for u in users:
    #     tasks.append(user_save(u))

    # update
    # tasks = [user_update(u2)]

    # remove
    # tasks = [user_remove(u2)]

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()
    except SystemExit:
        print("caught SystemExit")
        raise
    finally:
        loop.close()
    if loop.is_closed():
        sys.exit(0)


if __name__ == '__main__':
    main()
