import requests
from getpass import getpass

auth_endpoint = 'http://localhost:8000/api-token-auth/'
password = getpass()

auth_response = requests.post(auth_endpoint, json={'username': 'shiz', 'password': password})

print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']

    headers = {
        'Authorization': f'Token {token}'
    }

    endpoint = 'http://localhost:8000/todo/'

    get_response = requests.get(endpoint, headers=headers)

    print(get_response.json())