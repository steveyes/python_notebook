import requests

"""If, however, you need to send JSON data, you can use the json parameter. When you pass JSON data via json, 
requests will serialize your data and add the correct Content-Type header for you. """
# response = requests.post('https://httpbin.org/post', data={'key': 'value'})
response = requests.post('https://httpbin.org/post', json={'key': 'value'})

json_response = response.json()

print(json_response['data'])
print(json_response['headers']['Content-Type'])
