import sys
import psycopg2
from typing import Tuple, Optional
from enum import Enum

from basic_.config_.config import configs
from basic_.config_.logger_init import Logger

import logging

LOG_FORMAT = "%(asctime)s %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger('netmon')


class HowMany(Enum):
    one = 1
    many = 2
    all = 3


class Database(object):

    def __init__(self) -> None:
        self.__dsn = configs.database.__dict__
        self.connection = None
        self.cursor = None

    def get_connection(self):
        try:
            return psycopg2.connect(**self.__dsn)
        except psycopg2.DatabaseError as e:
            Logger.detailed.error(f'Database: {e}')
            sys.exit(1)

    def set_connection(self, value):
        self.connection = value

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def __insert(self, sql_stmt, sql_data, connection=None, many=True, auto_commit=True):
        if not (sql_stmt and sql_data):
            raise Exception("error: sql_stmt or sql_data None!")

        if not connection:
            connection = self.get_connection()
        else:
            connection = connection()

        cursor = connection.cursor()

        if many:
            execute = cursor.executemany
        else:
            execute = cursor.execute

        try:
            Logger.detailed.info(sql_stmt, sql_data)
            execute(sql_stmt, sql_data)
            if auto_commit:
                connection.commit()

        except Exception as e:
            connection.rollback()
            Logger.detailed.error(e)
            raise Exception(f'__insert error : {e}')
        finally:
            try:
                if cursor:
                    cursor.close()
                    if connection:
                        connection.close()
            except Exception as e:
                Logger.detailed.warning(e)

    def insert_one(self, sql_stmt, sql_data, _connection=None, ):
        return self.__insert(sql_stmt, sql_data, _connection, many=False)

    def insert_many(self, sql_stmt, sql_data, _connection=None, ):
        return self.__insert(sql_stmt, sql_data, _connection, many=True)

    def __select(self, sql_stmt, connection=None, how_many: Tuple[HowMany, Optional[int]] = None):
        if not sql_stmt:
            raise Exception("error: sql_stmt None!")

        if not connection:
            connection = self.get_connection()
        else:
            connection = connection()

        cursor = connection.cursor()

        _how, _many = how_many

        try:
            cursor.execute(sql_stmt)
            if _how == HowMany.one:
                records = cursor.fetchone()
            elif _how == HowMany.many:
                records = cursor.fetchmany(_many)
            elif _how == HowMany.all:
                records = cursor.fetchall()
            else:
                # records = []
                raise Exception('error: no such choice!')

            return records

        except Exception as e:
            raise Exception(f'__select error : {e}')

        finally:
            cursor.close()
            connection.close()

    def select_one(self, sql_stmt, _connection=None):
        return self.__select(sql_stmt, _connection, how_many=(HowMany.one, -1))

    def select_many(self, sql_stmt, _connection=None, _many=100):
        return self.__select(sql_stmt, _connection, how_many=(HowMany.many, _many))

    def select_all(self, sql_stmt, _connection=None, ):
        return self.__select(sql_stmt, _connection, how_many=(HowMany.all, -1))


database = Database()
