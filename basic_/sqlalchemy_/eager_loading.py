from basic_.sqlalchemy_.schemas import horizontal_rule, Database, User, Address
from sqlalchemy.orm import selectinload, joinedload, contains_eager

session = Database.get_session(echo=True)



# selectinload() option with which emits a second SELECT statement that fully loads the collections associated with the results just loaded
query = session.query(User).options(selectinload(User.addresses)).filter_by(name='jack')
jack = query.one()
print(jack)
print(jack.addresses)

horizontal_rule()

# joinedload() emits a JOIN, by default a LEFT OUTER JOIN, so that the lead object as well as the related object or collection is loaded in one step.
query = session.query(User).options(joinedload(User.addresses)).filter_by(name='jack')
jack = query.one()
print(jack)
print(jack.addresses)

horizontal_rule()

# Explicit Join + Eagerload¶ which is useful for pre-loading the many-to-one object on a query that needs to filter on that same object.
query = session.query(Address).join(Address.user).filter(User.name == 'jack').options(contains_eager(Address.user))
jack_addresses = query.all()
print(jack_addresses)