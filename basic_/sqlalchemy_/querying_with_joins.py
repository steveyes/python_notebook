from sqlalchemy.sql.elements import or_

from basic_.sqlalchemy_.schemas import Database, horizontal_rule, User, Address
from sqlalchemy.orm import aliased
from sqlalchemy.sql import func, exists

session = Database.get_session(echo=True)

# legacy implicit join
query = session.query(User, Address). \
    filter(User.id == Address.user_id). \
    filter(Address.email_address == 'jack@google.com')

for u, a in query.all():
    print(u)
    print(a)

horizontal_rule()

# The actual SQL JOIN syntax, on the other hand, is most easily achieved using Quering.join() method
query = session.query(User, Address.email_address).join(Address). \
    filter(Address.email_address == 'jack@google.com')

for user, email_address in query.all():
    print(user)
    print(email_address)

horizontal_rule()

## Query.join() knows how to join between User and Address because there’s only one foreign key between them.
## If there were no foreign keys, or several, Query.join() works better when one of the following forms are used:

# explicite condition, from User join Address
query = session.query(User.id, Address). \
    join(Address, User.id == Address.user_id). \
    filter(Address.email_address == 'jack@google.com')

for user_id, address in query:
    print(user_id)
    print(address)

horizontal_rule()

# specify relationship from left to right, from Address join User
query = session.query(User, Address). \
    join(Address.user). \
    filter(Address.email_address == 'jack@google.com')

for user, address in query:
    print(user)
    print(address)

horizontal_rule()

# same as above, with explicit target, from User join Address
query = session.query(Address, User). \
    join(Address, User.addresses). \
    filter(Address.email_address == 'jack@google.com')

for address, user in query:
    print(address)
    print(user)

horizontal_rule()

# Query.outerjoin()
query = session.query(User, Address).outerjoin(User.addresses)

for user, address in query:
    print(f"{user}:{address}")

horizontal_rule()

## The Query.join() method will typically join from the leftmost item in the list of entities, when the ON clause is omitted, or if the ON clause is a plain SQL expression.
## To control the first entity in the list of JOINs, use the Query.select_from() method:

# from Address join User
query = session.query(User, Address).select_from(Address).join(User)
horizontal_rule()

## Using Aliases

# Below we join to the Address entity twice, to locate a user who has two distinct email addresses at the same time:
addr1_alias: Address = aliased(Address)
addr2_alias: Address = aliased(Address)
query = session.query(User.name, addr1_alias.email_address, addr2_alias.email_address). \
    join(User.addresses.of_type(addr1_alias)). \
    join(User.addresses.of_type(addr2_alias)). \
    filter(addr1_alias.email_address == 'jack@google.com'). \
    filter(addr2_alias.email_address == 'j25@yahoo.com')

for user_name, email1, email2 in query:
    print(f'<{user_name} {email1} {email2}>')

horizontal_rule()

## Using Subqueries

sub_query = session.query(
    Address.user_id,
    func.count('*').label('address_count')
).group_by(Address.user_id).subquery()
print(sub_query)
print()

# The columns on the statement are accessible through an attribute called c:
query = session.query(User, sub_query.c.address_count). \
    outerjoin(sub_query, User.id == sub_query.c.user_id). \
    order_by(User.id)

for u, count in query:
    print(u, count)

horizontal_rule()

## Selecting Entities from Subqueries

# Above, we just selected a result that included a column from a subquery.
# What if we wanted our subquery to map to an entity ?
# For this we use aliased() to associate an “alias” of a mapped class to a subquery:
sub_query = session.query(Address). \
    filter(Address.email_address != 'j25@yahoo.com'). \
    subquery()
print(sub_query)
print()

address_alias = aliased(Address, sub_query)

query = session.query(User, address_alias).join(address_alias, User.addresses)

for user, address in query:
    print(user)
    print(address)

horizontal_rule()

## Using EXISTS
stmt_exists = exists().where(Address.user_id == User.id)
print(stmt_exists)
print()

query = session.query(User.name).filter(stmt_exists)

for name, in query:
    print(name)

horizontal_rule()

# The Query features several operators which make usage of EXISTS automatically.
# Above, the statement can be expressed along the User.addresses relationship using Comparator.any():
query = session.query(User.name).filter(User.addresses.any())

for name, in query:
    print(name)

horizontal_rule()

# Comparator.any() takes criterion as well, to limit the rows matched:
query = session.query(User.name).filter(User.addresses.any(Address.email_address.ilike('%google%')))

for name, in query:
    print(name)

horizontal_rule()

# Comparator.has() is the same operator as Comparator.any() for many-to-one relationships (note the ~ operator here too, which means “NOT”):
query = session.query(Address).filter(~Address.user.has(User.name == 'jack'))

for address in query.all():
    print(address)

horizontal_rule()

## Common Relationship Operators

# __eq__() many-to-one "equals" comparison
user = session.query(User).filter(User.fullname == 'Bob Allan Smith').one_or_none()
print(user)

address: tuple = session.query(Address).filter(Address.user == user).all()
print(address)

# __ne__() many-to-one "not equals" comparison
address: tuple = session.query(Address).filter(Address.user != user).all()
print(address)

# IS NULL many-to-one comparison
address: tuple = session.query(Address).filter(Address.user == None).all()
print(address)

# contains() one-to-many collections
addresses: tuple = session.query(Address).filter(Address.email_address == 'jack@google.com').one_or_none()
print(addresses)
user: list = session.query(User).filter(User.addresses.contains(addresses)).one_or_none()
print(user)

# any() used for collections
print(session.query(User).filter(User.addresses.any(Address.email_address == 'jack@google.com')).all())

# has() used for scalar references
print(session.query(Address).filter(Address.user.has(User.name == 'jack')).all())

horizontal_rule()

# with_parent() used for any relationship
print(session.query(Address).with_parent(user, 'addresses').all())
