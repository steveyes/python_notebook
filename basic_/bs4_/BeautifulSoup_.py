#!/usr/bin/env python3
#

from bs4 import BeautifulSoup, element
import re

__HTML_BLOG = open('./blog.html', encoding='utf-8')
__SOUP = BeautifulSoup(__HTML_BLOG, 'lxml')


# prettify
def print_prettify():
    print(__SOUP.prettify())


# tag
def print_tag():
    print(type(__SOUP.title))
    print(type(__SOUP.head))
    print(type(__SOUP.body))
    print(type(__SOUP.li))
    print(type(__SOUP.a))
    print(type(__SOUP.p))


# name
def print_name():
    print(type(__SOUP.name))
    print(__SOUP.name)
    print(__SOUP.title.name)
    print(__SOUP.a.name)


# attrs
def print_attrs():
    print(__SOUP.attrs)
    print(__SOUP.title.attrs)
    print(__SOUP.a.attrs)


# attr
def print_attr():
    print(__SOUP.a['class'])
    print(__SOUP.a.get('class'))


# string
def print_string():
    print(__SOUP.title.string)


# comment
def print_li_comment():
    print(__SOUP.li)
    print(__SOUP.li.string)
    print(type(__SOUP.li.string))
    if type(__SOUP.li.string) == element.Comment:
        print('<!--%s-->' % __SOUP.li.string)


# contents
def print_contents():
    print(__SOUP.body.contents)
    print(__SOUP.body.contents[1])


# children
def print_child():
    for child in __SOUP.body.children:
        print(child)


# find_all
def print_find_all():
    print(__SOUP.find_all('a'))


# find_all: regex
def print_find_all_re():
    for tag in __SOUP.find_all(re.compile("^b")):
        print(tag.name)


# find_all: list
def print_find_all_list():
    print(__SOUP.find_all(['title', 'b']))


# find_all: True
def print_tag_name():
    for tag in __SOUP.find_all(True):
        print(tag.name)


# find_all: attrs
def print_find_all_attrs():
    print(__SOUP.find_all(attrs={"class": "title"}))


# find_all: text
def print_find_all_attr():
    print(__SOUP.find_all(text=re.compile("Python3.*urllib.error异常")))


# find_all: limit
def print_find_all_limit():
    print(__SOUP.find_all('a', limit=2))


# find_all: kwargs
def print_find_all_class():
    print(__SOUP.find_all(class_="title"))



