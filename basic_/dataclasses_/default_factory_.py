from random import choice
from dataclasses import dataclass, field
from typing import List

"""
If a field() specifies a default_factory, it is called with zero arguments when a default value for the field is needed. 
For example, to create a new instance of a list, use:

    mylist: list = field(default_factory=list)
    
If a field is excluded from __init__() (using init=False) and the field also specifies default_factory, 
then the default factory function will always be called from the generated __init__() function. 
This happens because there is no other way to give the field an initial value.
"""


@dataclass
class C:
    # mylist: List[int] = field(default_factory=list)
    mylist: List[int] = field(default_factory=list)


c = C()
c.mylist += [1, 2, 3]

print(c)


def get_default_language():
    languages = ['python3', 'java', 'go']
    return choice(languages)


@dataclass
class Article:
    title: str
    author: str
    language: str = field(default_factory=get_default_language)
    upvotes: int = 0


article = Article("DataClass", "alice")
print(article)


@dataclass
class Pizza:
    # ingredients: List = field(default_factory=lambda: ['dow', 'tomatoes'])  # <- wrong! not a 0-argument callable but a list
    ingredients: List = field(default_factory=lambda: ['dow', 'tomatoes'])
