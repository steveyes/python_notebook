import requests
from basic_.requests_.common import get_credential

with requests.Session() as session:
    session.auth = get_credential()

    response = session.get('https://api.github.com/user')

print(response.headers)
print(response.status_code)
print(response.json())


