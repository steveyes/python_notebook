#!/usr/bin/env python3
#

from conf import CONFIG
import psycopg2
from bs4 import BeautifulSoup

DBCONF = CONFIG().CONF_DB

DBCONN = {
    'host': DBCONF['host'],
    'database': DBCONF['database_example'],
    'user': DBCONF['user'],
    'password': DBCONF['password']
}
COUNT = 3857


def meta_parser(entry, tag):
    tag_soup = BeautifulSoup(str(entry), 'lxml')
    return [ts.string for ts in tag_soup.find_all(tag)]


def tag_parser(td_list, tag):
    t_list = list()
    for td in td_list[1:]:
        tag_soup = BeautifulSoup(str(td), 'lxml').find_all(tag)
        tag_list = [td.attrs['title'] if 'title' in td.attrs.keys() else td.string for td in tag_soup]
        t_list.append(tuple(['' if ll is None else ll for ll in tag_list]))
    return t_list


def page_parser(html):
    with open(html, mode='r') as f:
        soup = BeautifulSoup(f, 'lxml')

    tr_list = soup.find_all('tr')
    td_list = tag_parser(tr_list, 'td')

    sql = """insert into t_temple (zj, pb, name_cn, location, principal) values """
    args = ','.join([str(ll) for ll in td_list])

    try:
        with psycopg2.connect(**DBCONN) as conn:
            with conn.cursor() as cur:
                cur.execute(sql + args)
    except Exception as err:
        print(err)


def write_t_temple():
    for i in range(1, 215 + 1):
        page_parser('crawler/sara/html/sara.html.%s' % i)


if __name__ == '__main__':
    write_t_temple()
    # print(DBCONF)
