import requests
from requests.exceptions import HTTPError

HP_API = "http://hp-api.herokuapp.com/api/characters"

response = requests.get(HP_API)
print("Válasz", response.status_code)
if response:
    # A válasz, szövegként
    print(response.text)
    # byte folyamként
    print(response.content)
    # A válasz JSON formátumra alakítva
    print(response.json())
    # A válasz header-ök
    print(response.headers)
    print(response.headers['Content-Type'])
    print(response.headers['content-type'])

try:
    response = requests.get('https://api.github.com/invalid')
    # Kivétel dobása nem megfelelő válasz esetén
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    print('Success!')

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)
print(response.json())

response = requests.post('https://httpbin.org/post', data=[('key', 'value')])
print(response.json())
response = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(response.json())
response = requests.post('https://httpbin.org/post', json={'key':'value'})
print(response.json())

requests.put('https://httpbin.org/put', data={'key': 'value'})
requests.delete('https://httpbin.org/delete')
requests.head('https://httpbin.org/get')
requests.patch('https://httpbin.org/patch', data={'key': 'value'})
requests.options('https://httpbin.org/get')

response = requests.delete('https://httpbin.org/delete')
print(response.json())

# Ha ellenőrizni szeretnénk, hogy konkrétan mit küldtünk, arra a response objektumban található request szolgál.
# Ez tárolja az eredeti kérést
print("eredeti kérés DELETE", response.request)
response = requests.post('https://httpbin.org/post', data=[('key', 'value')])
print("eredeti kérés POST", response.request)
print("eredeti kérés HEADERS", response.request.headers)
print("eredeti kérés URL", response.request.url)
