from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from basic_.sqlalchemy_.schemas import horizontal_rule, Database, User, Address

session = Database.get_session(echo=True)

# delete
def delete_jack():
    jack = session.query(User).filter(User.fullname == 'Jack Bean').one_or_none()
    print(jack)

    session.delete(jack)
    print(session.query(User).filter_by(name='jack').count())

    print(session.query(Address).filter(Address.email_address.in_(['jack@google.com', 'j25@yahoo.com'])).count())

    # rollback
    session.close()

## Next we’ll declare the User class, adding in the addresses relationship including the cascade configuration (we’ll leave the constructor out too):
# add cascade in User.addresses and recreate tables
# addresses = relationship('Address', back_populates='user', cascade="all, delete, delete-orphan")

def delete_jack_cascade():
    jack:User = session.query(User).filter(User.fullname == 'Jack Bean').one_or_none()
    print(jack)
    del jack.addresses[1]
    print(session.query(Address).filter(
        Address.email_address.in_('jack@google.com j25@yahoo.com'.split())
    ).count())

    session.delete(jack)
    print(session.query(User).filter_by(name='jack').count())
    print(session.query(Address).filter(Address.user == jack).count())
    

if __name__ == '__main__':
    # delete_jack()
    delete_jack_cascade()

