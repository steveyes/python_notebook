from basic_.sqlalchemy_.schemas import User, Database

session = Database.get_session(echo=True)

# ed_user = User(name='ed', fullname='Ed Jones', nickname='eddie')
ed_user = User(fullname='Ed Jones')
ed_user.name = 'Edwardo'
session.add(ed_user)

fake_user = User(name='fakeuser', fullname='Invalid', nickname='12345')
session.add(fake_user)

# Querying the session, we can see that they’re flushed into the current transaction:
print(session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all())

session.rollback()

print(session.query(User).filter(User.name.in_(['ed', 'fakeuser'])).all())
