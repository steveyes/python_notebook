from basic_.sqlalchemy_.schemas import User, Database

session = Database.get_session(echo=True)

# create an instance of the mapped class
ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
print(ed_user)

print(ed_user.name)
print(ed_user.nickname)

print(ed_user.id)

# To persist our User object, we Session.add() it to our Session:
session.add(ed_user)

# At this point, we say that the instance is pending;
# no SQL has yet been issued and the object is not yet represented by a row in the database.
# The Session will issue the SQL to persist 'Ed Jones' as soon as is needed, using a process known as a flush.
# If we query the database for 'Ed Jones', all pending information will first be flushed, and the query is issued immediately thereafter.
our_user = session.query(User).filter_by(name='ed').first()
print(our_user)
print(ed_user is our_user)

# add more User objects at once using add_all()
session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy'),
])

# Also, we’ve decided Ed’s nickname isn’t that great, so lets change it:
ed_user.nickname = 'eddie'

# The Session is paying attention. It knows, for example, that Ed Jones has been modified:
print(session.dirty)

# and that three new User objects are pending:
print(session.new)

# The Session emits the UPDATE statement for the nickname change on “ed”, as well as INSERT statements for the three new User objects we’ve added:
session.commit()

# add once
session.add(User(name='robert', fullname='Bob Allan Smith', nickname='bob'))
session.commit()
