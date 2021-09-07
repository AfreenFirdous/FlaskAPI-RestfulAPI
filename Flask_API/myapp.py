import json
import requests

def get_req():
    res = requests.get(url="http://127.0.0.1:5000/get")
    data = res.json()
    print(data)

def get_req_by_id():
    res = requests.get(url="http://127.0.0.1:5000/get/4")
    data = res.json()
    print(data)


def post_req():
    data = {
        "title": "Title_test",
        "description": "Description_test"
    }
    # automatically sets content type to json when json param is used
    res = requests.post(url="http://127.0.0.1:5000/post", json=data)

    # or use data parameter and manually set content-type
    # headers = {"Content-Type": "application/json"}
    # res = requests.post(url="http://127.0.0.1:5000/post", data=json.dumps(data), headers=headers)

    data = res.json()
    print(data)

def put_req():
    data = {
        'title': 'Title5_',
        'description': 'Description5'
    }
    res = requests.put(url="http://127.0.0.1:5000/update/5", json=data)
    data = res.json()
    print(data)

def del_req():
    res = requests.delete(url="http://127.0.0.1:5000/delete/3")
    data = res.json()
    print(data)


# get_req()
# get_req_by_id()
# post_req()
put_req()
# del_req()