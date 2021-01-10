import requests
from requests.auth import HTTPBasicAuth, AuthBase

from basic_.requests_.common import get_credential


def basic_():
    username, password = get_credential()
    response = requests.get('https://api.github.com/user', auth=(username, password))
    print(response.status_code)
    print(response.json())


def http_basic_auth():
    response = requests.get(
        'https://api.github.com/user',
        auth=HTTPBasicAuth(*get_credential())
    )
    print(response.status_code)
    print(response.json())


class TokenAuth(AuthBase):
    def __init__(self, token=None) -> None:
        self.token = token

    def __call__(self, r):
        r.headers['X-TokenAuth'] = f'{self.token}'
        return r


def http_token_auth():
    response = requests.get(
        'https://httpbin.org/get',
        auth=TokenAuth('12345abcde-token')
    )
    print(response.status_code)
    print(response.json())



