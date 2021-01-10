import requests

# disable SSL Certificate verification
response = requests.get('https://api.github.com', verify=False)
print(response.status_code)
print(response.json())
