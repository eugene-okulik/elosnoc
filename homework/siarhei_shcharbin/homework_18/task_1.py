import requests


def get_all_records():
    response = requests.get("http://objapi.course.qa-practice.com/object")
    assert response.status_code == 200, 'Something went wrong: Incorrect status code'


def get_record():
    record_id = new_record()
    response = requests.get(f"http://objapi.course.qa-practice.com/object/{record_id}").json()
    assert response['id'] == record_id, 'Id of the record does not match'
    clear(record_id)


def create_record():
    body = {
        "name": "test_object",
        "data": {
            "color": "orange",
            "size": "medium"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post("http://objapi.course.qa-practice.com/object", json=body, headers=headers)
    assert response.status_code == 200, 'Something went wrong: Incorrect status code'
    assert response.json()['data']['color'] == 'orange', 'Incorrect object data'
    assert response.json()['name'] == 'test_object', 'Incorrect object data'
    assert response.json()['data']['size'] == 'medium', 'Incorrect object data'
    record_id = response.json()['id']
    clear(record_id)


def new_record():
    body = {
        "name": "test_object",
        "data": {
            "color": "orange",
            "size": "medium"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post("http://objapi.course.qa-practice.com/object", json=body, headers=headers)
    return response.json()['id']


def update_put_record():
    record_id = new_record()
    body = {
        "name": "updated_put_object",
        "data": {
            "color": "black",
            "size": "medium"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f"http://objapi.course.qa-practice.com/object/{record_id}", json=body, headers=headers)
    print(response)
    assert response.json()['name'] == 'updated_put_object', 'Incorrect object data'
    assert response.json()['data']['color'] == 'black', 'Incorrect object data'
    assert response.json()['data']['size'] == 'medium', 'Incorrect object data'
    assert response.status_code == 200, 'Something went wrong: Incorrect status code'
    clear(record_id)


def update_patch_record():
    record_id = new_record()
    body = {
        "data": {
            "color": "grey",
            "size": "big"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f"http://objapi.course.qa-practice.com/object/{record_id}", json=body, headers=headers)
    print(response)
    assert response.json()['data']['size'] == 'big', 'Incorrect object data'
    assert response.json()['data']['color'] == 'grey', 'Incorrect object data'
    assert response.json()['name'] == 'test_object', 'Incorrect object data'
    clear(record_id)


def delete_record():
    record_id = new_record()
    response = requests.delete(f"http://objapi.course.qa-practice.com/object/{record_id}")
    assert response.status_code == 200, 'Something went wrong: Incorrect status code'


def clear(record_id):
    response = requests.delete(f"http://objapi.course.qa-practice.com/object/{record_id}")
    return response.status_code


get_record()
get_all_records()
create_record()
update_put_record()
update_patch_record()
delete_record()
