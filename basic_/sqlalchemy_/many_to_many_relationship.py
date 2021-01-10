from sqlalchemy import Column, Integer, ForeignKey, String, Table, Text
from sqlalchemy.orm import relationship

from basic_.sqlalchemy_.schemas import User, Database

session = Database.get_session(echo=True)

# association table
# We can see declaring a Table directly is a little different than declaring a mapped class. Table is a constructor function,
# so each individual Column argument is separated by a comma.
# The Column object is also given its name explicitly, rather than it being taken from an assigned attribute name.
post_keywords = Table('post_keywords', Database.Base.metadata,
                      Column('post_id', ForeignKey('posts.id'), primary_key=True),
                      Column('keyword_id', ForeignKey('keywords.id'), primary_key=True)
                      )


class BlogPost(Database.Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    headline = Column(String(255), nullable=False)
    body = Column(Text)

    # many to many BlogPost<->Keyword
    keywords = relationship('Keyword', secondary=post_keywords, back_populates=__tablename__)

    # note: declarations illustrate explicit __init__() methods. Remember, when using Declarative, it’s optional!
    def __init__(self, headline, body, author):
        self.author = author
        self.headline = headline
        self.body = body

    def __repr__(self) -> str:
        return f"BLogPost({self.headline}, {self.body}, {self.author}"


class Keyword(Database.Base):
    __tablename__ = "keywords"
    id = Column(Integer, primary_key=True)
    keyword = Column(String(50), nullable=False, unique=True)
    posts = relationship('BlogPost', secondary=post_keywords, back_populates=__tablename__)

    def __init__(self, keyword):
        self.keyword = keyword


# We would also like our BlogPost class to have an author field.
# We will add this as another bidirectional relationship, except one issue we’ll have is that a single user might have lots of blog posts.
# When we access User.posts, we’d like to be able to filter results further so as not to load the entire collection.
# For this we use a setting accepted by relationship() called lazy='dynamic', which configures an alternate loader strategy on the attribute:
BlogPost.author = relationship(User, back_populates=BlogPost.__tablename__)
User.posts = relationship(BlogPost, back_populates="author", lazy="dynamic")

Database.create_tables()

wendy = session.query(User).filter_by(name='wendy').one()
post = BlogPost("Wendy's Blog Post", "This is a test", wendy)
session.add(post)

post.keywords.append(Keyword('wendy'))
post.keywords.append(Keyword('firstpost'))

print(session.query(BlogPost).
      filter(BlogPost.keywords.any(keyword='firstpost')).
      all())

print(session.query(BlogPost).filter(BlogPost.author == wendy). \
      filter(BlogPost.keywords.any(keyword='firstpost')). \
      all())

print(wendy.posts.filter(BlogPost.keywords.any(keyword='firstpost')).all())
