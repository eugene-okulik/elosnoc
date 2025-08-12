import allure
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


@allure.suite('Smoke suite')
@allure.feature('Records')
@allure.story('Getting records')
@allure.title('Check all available records can be received')
def test_get_all_records(start_complete, before_after):
    with allure.step('Receiving a record information'):
        response = requests.get('http://objapi.course.qa-practice.com/object')
    with allure.step('Verifying that response status code is 200'):
        assert response.status_code == 200, 'Something went wrong: Incorrect status code'


@pytest.mark.skip('Skipped with no reason')
@allure.feature('Records')
@allure.story('Getting records')
@allure.title('Check that created record can be received by ID')
def test_get_record(new_record_id):
    with allure.step('Creating a record and receiving an ID'):
        record_id = new_record_id
    with allure.step('Receiving a record information by ID'):
        response = requests.get(f'http://objapi.course.qa-practice.com/object/{record_id}').json()
    with allure.step(f'Verifying that record id is {record_id}'):
        assert response['id'] == record_id, 'Id of the record does not match'


@allure.severity('S0')
@allure.suite('Smoke suite')
@allure.feature('Records')
@allure.story('Records creation')
@allure.title('Check that record can be created')
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
    with allure.step('Receiving a record information'):
        response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)
    with allure.step('Getting a record ID'):
        record_id = response.json()['id']
    with allure.step('Verifying that status code is 200'):
        assert response.status_code == 200, 'Something went wrong: Incorrect status code'
    with allure.step('Verifying that color is "orange"'):
        assert response.json()['data']['color'] == 'orange', 'Incorrect object color'
    with allure.step(f'Verifying that name is {object_name}'):
        assert response.json()['name'] == object_name, 'Incorrect object name'
    with allure.step('Verifying that size is "medium"'):
        assert response.json()['data']['size'] == 'medium', 'Incorrect object size'
    with allure.step(f'Deleting a record with id {record_id}'):
        delete_response = requests.delete(f'http://objapi.course.qa-practice.com/object/{record_id}')
    print('Deleting a record')
    with allure.step('Verifying that status code is 200'):
        assert delete_response.status_code == 200, \
            f'Something went wrong while deleting a record, status code: {delete_response.status_code}'


@allure.suite('Regression suite')
@allure.feature('Records')
@allure.story('Records update')
@allure.title('Check that record can be updated using PUT method')
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
    with allure.step('Creating a record and receiving an ID'):
        record_id = new_record_id
    with allure.step(f'Updating a record with id {record_id}'):
        response = requests.put(
            f'http://objapi.course.qa-practice.com/object/{record_id}', json=body, headers=headers
        )
    with allure.step('Verifying that name is "updated_put_object"'):
        assert response.json()['name'] == 'updated_put_object', 'Incorrect object data'
    with allure.step('Verifying that color is "black"'):
        assert response.json()['data']['color'] == 'black', 'Incorrect object data'
    with allure.step('Verifying that size is "medium"'):
        assert response.json()['data']['size'] == 'medium', 'Incorrect object data'
    with allure.step('Verifying that status code is 200'):
        assert response.status_code == 200, 'Something went wrong: Incorrect status code'


@allure.suite('Regression suite')
@allure.feature('Records')
@allure.story('Records update')
@allure.title('Check that record can be updated using PATCH method')
def test_update_patch_record(new_record_id):
    body = {
        "data": {
            "color": "grey",
            "size": "big"
        }
    }
    headers = {'Content-Type': 'application/json'}
    with allure.step('Creating a record and receiving an ID'):
        record_id = new_record_id
    with allure.step(f'Updating a record with id {record_id}'):
        response = requests.patch(
            f'http://objapi.course.qa-practice.com/object/{record_id}', json=body, headers=headers
        )
    with allure.step('Verifying that size is "big"'):
        assert response.json()['data']['size'] == 'big', 'Incorrect object data'
    with allure.step('Verifying that color is "grey"'):
        assert response.json()['data']['color'] == 'grey', 'Incorrect object data'
    with allure.step('Verifying that name is "test_object"'):
        assert response.json()['name'] == 'test_object', 'Incorrect object data'


@allure.severity('S1')
@allure.suite('Smoke suite')
@allure.feature('Records')
@allure.story('Records deletion')
@allure.title('Check that record can be deleted')
@pytest.mark.medium
def test_delete_record(new_record_id):
    with allure.step('Creating a record and receiving an ID'):
        record_id = new_record_id

    with allure.step(f'Deleting a record with id {record_id}'):
        response = requests.delete(f'http://objapi.course.qa-practice.com/object/{record_id}')
    with allure.step('Verifying that status code is 200'):
        assert response.status_code == 200, 'Something went wrong: Incorrect status code'
    with allure.step(f'Getting a record with id {record_id}'):
        response = requests.get(f'http://objapi.course.qa-practice.com/object/{record_id}')
    with allure.step('Verifying that a record can not be found: status code is 404'):
        assert response.status_code == 404, 'Record was not deleted'
