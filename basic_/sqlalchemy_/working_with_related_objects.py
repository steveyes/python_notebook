from basic_.sqlalchemy_.schemas import Database, horizontal_rule, User, Address

session = Database.get_session(echo=True)

jack = User(name='jack', fullname='Jack Bean', nickname='gjffdd')
print(jack.addresses)

horizontal_rule()

jack.addresses = [
    Address(email_address='jack@google'),
    Address(email_address='j25@yahoo.com'),
]

horizontal_rule()

print(jack.addresses[0])
print(jack.addresses[1].user)

horizontal_rule()

session.add(jack)
session.commit()

jack = session.query(User).filter_by(name='jack').one()
print(jack)
print(jack.addresses)
print(jack.addresses[0].user)

bob: User = session.query(User).filter(User.fullname == 'Bob Allan Smith').one_or_none()
bob.addresses = [
    Address(email_address='robert@google.com'),
]
session.add(bob)
session.commit()
