import requests

URL = "http://127.0.0.1:5000/"


def get_product():
    res = requests.get(url=URL+str(6))
    data = res.json()
    print(data)


def post_product():
    data = {
        "id": 7,
        "name": "Play Station",
        "price": 38000.0
    }
    res = requests.post(url=URL+str(7), json=data)
    data = res.json()
    print(data)


def put_product():
    data = {
        "id": 7,
        "name": "Sony TV",
        "price": 150000.0
    }
    res = requests.put(url=URL+str(7), json=data)
    data = res.json()
    print(data)

def del_product():
    res = requests.delete(url=URL+str(7))
    data = res.json()
    print(data)

get_product()
# post_product()
# put_product()
# del_product()