#!/usr/bin/env python3
#

import json
from urllib import request


class EaseMob(object):
    org_name = '1481181212068965'
    app_name = 'kefuchannelapp61658'
    url_scheme = 'http'
    url_host = 'a1-vip5.easemob.com'

    client_id = "YXA6xmbA8P3eEeidX53XVw5Wsw"
    client_secret = "YXA6tsY8B2lg86XuxXjrRqRg65jXeRM"
    password = 'P7X9gexGZc'

    @staticmethod
    def get_token():
        # headers
        headers = {"Content-Type": "application/json", "Accept": "application/json"}

        # body
        data_body = {
            "grant_type": "client_credentials",
            "client_id": EaseMob.client_id,
            "client_secret": EaseMob.client_secret,
        }
        # data = parse.urlencode(data_body).encode('utf-8')
        data = json.dumps(data_body).encode('utf-8')

        # url
        url_path = f'{EaseMob.org_name}/{EaseMob.app_name}/token'
        url_easemob = f'{EaseMob.url_scheme}://{EaseMob.url_host}/{url_path}'

        # request
        req = request.Request(url=url_easemob, data=data, headers=headers)
        resp = request.urlopen(req)
        resp_str = json.loads(resp.read().decode('utf-8'))

        access_token = resp_str.get('access_token', '')
        # expires_in = resp_str.get('expires_in', '')

        return access_token

    @staticmethod
    def create_user(username):
        # headers
        access_token = EaseMob.get_token()
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f'Bearer {access_token}',
        }

        # body
        data_body = [{
            "username": username,
            "password": EaseMob.password,
        }, ]
        data = json.dumps(data_body).encode('utf-8')

        # url
        url_path = f'{EaseMob.org_name}/{EaseMob.app_name}/users'
        url_easemob = f'{EaseMob.url_scheme}://{EaseMob.url_host}/{url_path}'

        # request
        req = request.Request(url=url_easemob, data=data, headers=headers)
        resp = request.urlopen(req)
        resp_code = resp.getcode()

        return resp_code

    @staticmethod
    def delete_use(username):
        # headers
        access_token = EaseMob.get_token()
        headers = {
            "Accept": "application/json",
            "Authorization": f'Bearer {access_token}',
        }

        # url
        url_path = f'{EaseMob.org_name}/{EaseMob.app_name}/users/{username}'
        url_easemob = f'{EaseMob.url_scheme}://{EaseMob.url_host}/{url_path}'

        # request
        req = request.Request(url=url_easemob, headers=headers, method='DELETE')
        resp = request.urlopen(req)
        resp_code = resp.getcode()

        return resp_code


if __name__ == '__main__':
    user1 = 'alice'
    # res = EaseMob.create_user(user1)
    # res = EaseMob.delete_use(user1)
    # print(res)
