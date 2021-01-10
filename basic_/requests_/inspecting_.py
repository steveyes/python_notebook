import requests

response = requests.post('https://httpbin.org/post', json={'key': 'value'})
print(response.request.headers['Content-Type'])
print(response.request.url)
print(response.request.body)
