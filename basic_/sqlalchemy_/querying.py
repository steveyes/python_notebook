import app01.forms
from basic_.sqlalchemy_.schemas import User, Database, horizontal_rule
from sqlalchemy.orm import aliased

session = Database.get_session(echo=True)

for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.fullname)

horizontal_rule()

for name, fullname in session.query(User.name, User.fullname):
    print(name, fullname)

horizontal_rule()

# tuples
for row in session.query(User, User.name).all():
    print(app01.forms.User, row.name)

horizontal_rule()

# label
for row in session.query(User.name.label('name_label')).all():
    print(row.name_label)

horizontal_rule()

# aliased
user_alias = aliased(User, name='user_alias')
for row in session.query(user_alias, user_alias.name).all():
    print(row.user_alias, row.user_alias.name)

horizontal_rule()

# limit and offset
for u in session.query(User).order_by(User.id)[1:3]:
    print(u)

horizontal_rule()

# filter_by() uses keyword arguments
for name, in session.query(User.name).filter_by(fullname='Ed Jones'):
    print(name)

horizontal_rule()

# filter() uses more flexible SQL expression language constructs.
# These allow you to use regular Python operators with the class-level attributes on your mapped class:
for name, in session.query(User.name).filter(User.fullname == 'Ed Jones'):
    print(name)

horizontal_rule()

# two filter as and
for user in session.query(User).filter(User.name == 'ed').filter(User.fullname == 'Ed Jones'):
    print(user)

horizontal_rule()

## Common Filter Operators

# Common Filter Operator __eq__()
print(session.query(User).filter(User.name == 'ed'))

horizontal_rule()

# Common Filter Operator __ne__()
print(session.query(User).filter(User.name != 'ed'))

horizontal_rule()

# Common Filter Operator like()
print(session.query(User).filter(User.name.like('%ed%')))

horizontal_rule()

# Common Filter Operator ilike() (case-insensitive)
print(session.query(User).filter(User.name.ilike('%ed%')))

horizontal_rule()

# Common Filter Operator in_()
print(session.query(User).filter(User.name.in_(['ed', 'wendy', 'jack'])))

horizontal_rule()

# works with query objects toow
print(session.query(User).filter(User.name.in_(
    session.query(User.name).filter(User.name.like('%ed%'))
)))

horizontal_rule()

# use tuple_() for composite (multi-column) queries
from sqlalchemy import tuple_

stmt = session.query(User).filter(
    tuple_(User.name, User.nickname). \
        in_([('ed', 'eddie'), ('wendy', 'windy')])
)
print(stmt)
for user in stmt:
    print(user)

horizontal_rule()

# Common Filter Operator notin_()
print(session.query(~User.name.in_(['ed', 'wendy', 'jack'])))

horizontal_rule()

# Common Filter Operator is_()
print(session.query(User).filter(User.name == None))

# alternatively, if pep8/linters are a concern
print(session.query(User).filter(User.name.is_(None)))

horizontal_rule()

# Common Filter Operator isnot()
print(session.query(User).filter(User.name != None))

# alternatively, if pep8/linters are a concern
print(session.query(User).filter(User.name.isnot(None)))

horizontal_rule()

# Common Filter Operator and_()
from sqlalchemy import and_

print(session.query(User).filter(and_(User.name == 'ed', User.fullname == 'Ed Jones')))

# or send multiple expressions to .filter()
print(session.query(User).filter(User.name == 'ed', User.fullname == 'Ed Jones'))

# or chain multiple filter()/filter_by calls
print(session.query(User).filter(User.name == 'ed').filter(User.fullname == 'Ed Jones'))

horizontal_rule()

# Common Filter Operator or_()
from sqlalchemy import or_

print(session.query(User).filter(or_(User.name == 'ed', User.name == 'wendy')))

horizontal_rule()

# Common Filter Operator match()
print(session.query(User).filter(User.name.match('wendy')))

horizontal_rule()

## Returning Lists and Scalars

# Query.all()
query = session.query(User).filter(User.name.like('%ed')).order_by(User.id)
for user in query.all():
    print(user)

horizontal_rule()

# Query.first()
print(query.first())

horizontal_rule()

## Query.one() fully fetches all rows, and if not exactly one object identity or composite row is present in the result, raises an error.

# With multiple rows found:
try:
    print(query.one())
except Exception as e:
    print(e)

# With no rows found:
try:
    user = query.filter(User.id == 99).one()
    print(user)
except Exception as e:
    print(e)

horizontal_rule()

# Query.one_or_none() is like Query.one(), except that if no results are found, it doesn’t raise an error; it just returns None.
# Like Query.one(), however, it does raise an error if multiple results are found.
user = query.filter(User.id == 99).one_or_none()
print(user)

horizontal_rule()

# Query.scalar() invokes the Query.one() method, and upon success returns the first column of the row:
query = session.query(User.id).filter(User.name == 'ed').order_by(User.id)
print(query.scalar())

horizontal_rule()

## Using Textual SQL
from sqlalchemy import text

for user in session.query(User).filter(text('id<100')).order_by(text('id')).all():
    print(user.name)

horizontal_rule()

# colon and Query.params()
for user in session.query(User).from_statement(
        text('select * from users where name=:name')
).params(name='ed').all():
    print(user)

horizontal_rule()

# TextClause.columns()
stmt = text('select name, id, fullname, nickname from users where name=:name')
# stmt = stmt.columns(User.name, User.id, User.fullname, User.nickname)
for user in session.query(User).from_statement(stmt).params(name='ed').all():
    print(user)

horizontal_rule()

#
stmt = text('select name, id from users where name=:name')
# stmt = stmt.columns(User.name, User.id)
for id, name in session.query(User.id, User.name).from_statement(stmt).params(name='ed').all():
    print(id, name)

horizontal_rule()

## Counting
print(session.query(User).filter(User.name.like('%ed')).count())

# group_by()
from sqlalchemy import func

print(session.query(func.count(User.name), User.name).group_by(User.name).all())

# To achieve our simple SELECT count(*) FROM table, we can apply it as:
print(session.query(func.count('*')).select_from(User).scalar())

# The usage of Query.select_from() can be removed if we express the count in terms of the User primary key directly:
print(session.query(func.count(User.id)).scalar())
