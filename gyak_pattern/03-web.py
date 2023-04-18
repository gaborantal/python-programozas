import json

import requests


def print_anything2(obj):
    match obj:
        case requests.models.Response(status_code=200) as resp:
            print('Minden rendben volt, a válasz HTML-hez kommenteld ki a sort')
            print(resp)
        case requests.models.Response(status_code=400 | 404):
            print('Valami baj volt, 400-as hibakód jött')
        case requests.models.Response(status_code=500 | 501 | 502):
            print('Valami baj volt, 500-as hibakód jött')
        case dict() if obj.get('masked'):
            print('*' * len(json.dumps(obj)))
        case dict():
            print(json.dumps(obj))
        case list() if len(obj) > 0:
            print(', '.join(obj))


def print_anything(obj):
    if isinstance(obj, requests.models.Response) and obj.status_code == 200:
        print("Minden rendben volt, a válasz HTML-hez kommenteld ki a sort")
        # print(obj.text)
    elif isinstance(obj, requests.models.Response) and (obj.status_code == 400 or obj.status_code == 404):
        print("Valami baj volt, 400-as hibakód jött")
    elif isinstance(obj, requests.models.Response) and (obj.status_code == 500 or obj.status_code == 501 or obj.status_code == 502):
        print("Valami baj volt, 500-as hibakód jött")
    elif isinstance(obj, dict):
        if obj.get('masked'):
            print("*" * len(json.dumps(obj)))
        else:
            print(json.dumps(obj))
    elif isinstance(obj, list) and len(obj) > 0:
        print(", ".join(obj))


def main():
    x = requests.get('https://rickastley.co.uk/')
    y = requests.get('https://httpbin.org/status/200%2C400%2C404%2C500%2C501%2C502')

    # print_anything(x)
    # print_anything(y)
    # print_anything({'text': 'Hello bello', 'masked': True})
    # print_anything({'text': 'Hello bello', 'masked': False})
    # print_anything(["alma", "korte"])
    # print_anything([])

    print_anything2(x)
    print_anything2(y)
    print_anything2({'text': 'Hello bello', 'masked': True})
    print_anything2({'text': 'Hello bello', 'masked': False})
    print_anything2(["alma", "korte"])
    print_anything2([])


if __name__ == '__main__':
    main()
