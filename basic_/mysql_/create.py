#!/usr/bin/env python3
#

import sqlalchemy
import enum
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum

engine = create_engine('mysql+pymysql://chekawa_admin:chekawa_admin@192.168.250.239/chekawa', encoding='utf-8',
                       echo=True)

# ORM基类
Base = declarative_base()


class User(Base):
    class __EnumRole(enum.Enum):
        User = 1
        Adversary = 2
        ISP = 3
        Justice = 4
        Prover = 5
        Verifier = 6
        Arbitrator = 6
        Warden = 7

    __tablename__ = 'test_user'
    uid = Column(Integer, primary_key=True)
    user = Column(String(32))
    role = Column(Enum(__EnumRole))


# 建表功能
User.metadata.create_all(engine)
