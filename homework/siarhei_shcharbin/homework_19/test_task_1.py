import requests
import pytest


@pytest.fixture(scope="session")
def start_complete():
    print('\nStart testing')
    yield
    print('\nTesting completed')


@pytest.fixture(scope="function", autouse=True)
def before_after():
    print('\nbefore test')
    yield
    print('\nafter test')


@pytest.fixture()
def new_record_id():
    body = {
        "name": "test_object",
        "data": {
            "color": "orange",
            "size": "medium"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object', json=body, headers=headers
    )
    record_id = response.json()['id']
    assert response.status_code == 200, 'Something went wrong: Incorrect status code'
    print(f'\nRecord is created with id {record_id}')
    yield record_id
    get_response = requests.get(f'http://objapi.course.qa-practice.com/object/{record_id}')
    if get_response.status_code == 404:
        print(f'\nRecord with id {record_id} already deleted')
    else:
        delete_response = requests.delete(f'http://objapi.course.qa-practice.com/object/{record_id}')
        print(f'\nDELETE response status code: {delete_response.status_code}')
        assert delete_response.status_code == 200, f'Failed to delete record with id {record_id}'
        print(f'\nDeleting record with id {record_id}')


@pytest.fixture()
def record_manager():
    created_records = []

    def create_record(data):
        headers = {'Content-Type': 'application/json'}
        post_response = requests.post(
            'http://objapi.course.qa-practice.com/object', json=data, headers=headers
        )
        assert post_response.status_code == 200, f'Failed to create record: {post_response.text}'
        try:
            created_record_id = post_response.json()['id']
        except KeyError:
            raise AssertionError("Response does not contain 'id'")
        created_records.append(created_record_id)
        print(f'Created record with {created_record_id}')
        return created_record_id

    yield create_record

    for record_id in created_records:
        delete_response = requests.delete(f'http://objapi.course.qa-practice.com/object/{record_id}')
        if delete_response.status_code == 404:
            print(f'\nRecord with id {record_id} already deleted')
        elif delete_response.status_code == 200:
            print(f'Deleted record with id {record_id}')
        else:
            print(f'Failed to delete record with id {record_id}, status code: {delete_response.status_code}')


def test_get_all_records(start_complete, before_after):
    response = requests.get('http://objapi.course.qa-practice.com/object')
    assert response.status_code == 200, 'Something went wrong: Incorrect status code'


def test_get_record(new_record_id):
    record_id = new_record_id
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{record_id}').json()
    assert response['id'] == record_id, 'Id of the record does not match'


@pytest.mark.parametrize('object_name', ['test_object', 'second_object', 'last_object'])
def test_create_record(object_name):
    body = {
        "name": object_name,
        "data": {
            "color": "orange",
            "size": "medium"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)
    record_id = response.json()['id']
    assert response.status_code == 200, 'Something went wrong: Incorrect status code'
    assert response.json()['data']['color'] == 'orange', 'Incorrect object color'
    assert response.json()['name'] == object_name, 'Incorrect object name'
    assert response.json()['data']['size'] == 'medium', 'Incorrect object size'
    delete_response = requests.delete(f'http://objapi.course.qa-practice.com/object/{record_id}')
    print('Deleting a record')
    assert delete_response.status_code == 200, \
        f'Something went wrong while deleting a record, status code: {delete_response.status_code}'


@pytest.mark.critical
def test_update_put_record(new_record_id):
    body = {
        "name": "updated_put_object",
        "data": {
            "color": "black",
            "size": "medium"
        }
    }
    headers = {'Content-Type': 'application/json'}
    record_id = new_record_id
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{record_id}', json=body, headers=headers
    )
    assert response.json()['name'] == 'updated_put_object', 'Incorrect object data'
    assert response.json()['data']['color'] == 'black', 'Incorrect object data'
    assert response.json()['data']['size'] == 'medium', 'Incorrect object data'
    assert response.status_code == 200, 'Something went wrong: Incorrect status code'


def test_update_patch_record(new_record_id):
    body = {
        "data": {
            "color": "grey",
            "size": "big"
        }
    }
    headers = {'Content-Type': 'application/json'}
    record_id = new_record_id
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{record_id}', json=body, headers=headers
    )
    assert response.json()['data']['size'] == 'big', 'Incorrect object data'
    assert response.json()['data']['color'] == 'grey', 'Incorrect object data'
    assert response.json()['name'] == 'test_object', 'Incorrect object data'


@pytest.mark.medium
def test_delete_record(new_record_id):
    record_id = new_record_id
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{record_id}')
    assert response.status_code == 200, 'Something went wrong: Incorrect status code'
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{record_id}')
    assert response.status_code == 404, 'Record was not deleted'
