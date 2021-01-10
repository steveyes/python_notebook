import sys
from enum import Enum
from typing import Tuple, Optional

import psycopg2

config = {
    'database': 'nasa',
    'user': 'nasa',
    'password': '123456',
    'host': '10.148.217.77',
}


class HowMany(Enum):
    one = 1
    many = 2
    all = 3


class Database(object):
    class Database(object):

        def __init__(self) -> None:
            self.__dsn = config
            self.connection = None
            self.cursor = None

        def get_connection(self):
            try:
                return psycopg2.connect(**self.__dsn)
            except psycopg2.DatabaseError as e:
                print(f'Database: {e}')
                sys.exit(1)

        def set_connection(self, value):
            self.connection = value

        def close_connection(self):
            if self.connection:
                self.connection.close()

        def __insert(self, sql_stmt, sql_data, _connection=None, how_many: Tuple[bool, Optional[int]] = (True, None)):
            if not sql_stmt or sql_data:
                raise Exception("error: sql_stmt or sql_data None!")

            if not _connection:
                connection = self.get_connection()
            else:
                connection = _connection()

            cursor = connection.cursor()

            _how, _many = how_many
            if _how:
                _exec = cursor.executemany
                _index = 1
                _data = []
                while _index <= _many:
                    _data.append(sql_data)
                    _index += 1
            else:
                _exec = cursor.execute
                _data = sql_data

            try:
                _exec(sql_stmt, _data)
                connection.commit()
            except Exception as e:
                connection.rollback()
                raise Exception(f'__insert error : {e}')
            finally:
                try:
                    if cursor:
                        cursor.close()
                        if connection:
                            connection.close()
                except Exception as e:
                    print(e)

        def insert_single(self, sql_stmt, sql_data, _connection=None, ):
            return self.__insert(sql_stmt, sql_data, _connection, how_many=(False, None))

        def insert_many(self, sql_stmt, sql_data, _many=1000, _connection=None):
            return self.__insert(sql_stmt, sql_data, _connection, how_many=(True, _many))

        def __select(self, sql_stmt, _connection=None, how_many: Tuple[HowMany, Optional[int]] = None):
            if not sql_stmt:
                raise Exception("error: sql_stmt None!")

            if not _connection:
                connection = self.get_connection()
            else:
                connection = _connection()

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
