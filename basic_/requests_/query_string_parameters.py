import requests

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    # save the three params
    # params=[('q', 'requests+language:python')],
    # params=b'q=requests+language:python',

)

json_response = response.json()
repository = json_response['items'][0]
print(f"Repository name: {repository['name']}")
print(f"Repository description: {repository['description']}")
