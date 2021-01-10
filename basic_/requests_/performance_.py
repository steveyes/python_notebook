import requests
from requests.exceptions import Timeout


def get_():
    response1 = requests.get('https://api.github.com', timeout=1)


def get_timeout():
    try:
        # timeout=(f'{connect_timeout}, f'{read_timeout}')
        response2 = requests.get('https://api.github.com', timeout=(2, 4))
    except Timeout:
        print('The request timed out')
    else:
        print('The request did not time out')
        print(response2.status_code)
        print(response2.json())



