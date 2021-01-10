import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError

github_adapter = HTTPAdapter(max_retries=3)

session = requests.Session()

session.mount('https://api.github.com', github_adapter)

try:
    response = session.get('https://api.github.com')
    print(response.status_code)
    print(response.json())
except ConnectionError as ce:
    print(ce)


