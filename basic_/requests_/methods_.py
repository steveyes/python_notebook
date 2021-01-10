import requests

response = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(response.headers['Content-Type'])

requests.put('https://httpbin.org/put', data={'key': 'value'})
requests.delete('https://httpbin.org/delete')
json_response = response.json()
print(json_response['args'])

requests.head('https://httpbin.org/get')
requests.patch('https://httpbin.org/patch', data={'key': 'value'})
requests.options('https://httpbin.org/get')
