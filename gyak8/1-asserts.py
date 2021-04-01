import requests

def jatszunk_meg():
    i = input(f"Játszunk még? ")
    return i.lower() in ["i", "y", "yes", "igen", "nana"]


def square(x):
    return x * x

def test_answer():
    valasz = jatszunk_meg()
    assert valasz

    valasz = square(3)
    assert valasz == 9

    web = requests.get("https://google.com")
    assert web.status_code == 200

    print("Minden lefutott!")

test_answer()