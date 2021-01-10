from dataclasses import dataclass, field
from random import choice


@dataclass
class Article1:
    title: str
    author: str
    language: str = field(default='Python3')
    upvotes: int = 0


a1 = Article1('dataclass', 'asdjfasjdif')
print(a1)


def get_default_language():
    languages = ['python3', 'java', 'go']
    return choice(languages)


@dataclass
class Article2:
    title: str
    author: str
    # default_factory : If provided, it must be a zero-argument callable that will be called when a default value is needed for this field.
    language: str = field(default_factory=get_default_language)
    upvotes: int = 0


a2 = Article2('dataclass', 'oaisjdfoijasiodfjioajsf')
print(a2)


@dataclass
class Article3:
    title: str = field(compare=False)
    author: str = field(repr=False)
    language: str = field(default='java')
    upvotes: int = field(init=False, default=0)


a3_1 = Article3('Article3', 'alice')
a3_2 = Article3('article3', 'bob')
print(a3_1, a3_2)
# diff in title but has no impact on comparison, because of `field(compare=False)`
# diff in author has impact on
print(a3_1 == a3_2)


@dataclass
class Article4:
    title: str = field(compare=True)
    author: str = field(repr=False)
    language: str = field(default='java')
    upvotes: int = field(init=False, default=0)


a4_1 = Article4('Article4', 'alice')
a4_2 = Article4('article4', 'alice')
print(a3_1, a3_2)
# diff in title do has impact on comparison, because of `field(compare=True)`
print(a4_1 == a4_2)


@dataclass
class Article5:
    title: str = field(compare=False)
    author: str = field(metadata={'data': 'Profile Handle'})
    language: str = field(default='python3')
    upvotes: int = field(init=False, default=0)


a5 = Article5('Article5', 'carol')
print(a5)
print(a5.__dataclass_fields__['author'].metadata)
