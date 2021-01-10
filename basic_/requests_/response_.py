import requests

response = requests.get('https://api.github.com')
print(response.status_code)

# raw bytes
print(response.content)

# unicode
print(response.text)

# loaded raw bytes, usually load to dict
print(response.json())

print(response.headers)

# case-insensitive
print(response.headers['Content-Type'])
print(response.headers['content-type'])
