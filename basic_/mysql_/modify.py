#!/usr/bin/env python3
#

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from mysql.create import User

engine = create_engine('mysql+pymysql://chekawa_admin:chekawa_admin@192.168.250.239/chekawa', encoding='utf8',
                       echo=True)

# 会话基类
Session_class = sessionmaker(bind=engine)
# 会话实例
Session = Session_class()

# 修改功能
res = Session.query(User).filter(User.user == 'alice').update({'user': 'bob'})
Session.commit()
print(res)
