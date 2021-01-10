from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, event, Table
from sqlalchemy.orm import sessionmaker, relationship
from basic_.sqlalchemy_.schemas import Database

# Naming Columns Distinctly from Attribute Names
''''
class User(Database.Base):
    __tablename__ = 'user'
    # User.id resolves to a column named user_id
    id = Column('user_id', Integer, primary_key=True)
    # User.name resolves to a column named user_name.
    name = Column('user_name', String(50))
'''

class MyClass(Database.Base):
    __table__ = Table("some_table", Database.Base.metadata, autoload=True, autoload_with=Database.get_engine())

@event.listens_for(Table, "column_reflect")
def column_reflect(inspector, table, column_info):
    # set column.key = "attr_<lower_case_name>"
    if table.metadata is Database.Base.metadata:
        column_info['key'] = f"attr_{column_info['name'].lower()}"

