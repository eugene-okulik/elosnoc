import pytest
from endpoints.create_record import CreateRecord
from endpoints.update_record import UpdateRecord
from endpoints.get_record import GetRecord
from endpoints.delete_record import DeleteRecord


@pytest.fixture()
def create_record_endpoint():
    return CreateRecord()


@pytest.fixture()
def update_record_endpoint():
    return UpdateRecord()


@pytest.fixture()
def get_record_endpoint():
    return GetRecord()


@pytest.fixture()
def delete_record_endpoint():
    return DeleteRecord()


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
def new_record_id(create_record_endpoint, get_record_endpoint, delete_record_endpoint):
    body = {
        "name": "test_object",
        "data": {
            "color": "orange",
            "size": "medium"
        }
    }
    create_record_endpoint.new_record(body=body)
    record_id = create_record_endpoint.retrieve_record_id()
    print(record_id)

    yield record_id

    if get_record_endpoint.get_record_by_id(record_id).status_code == 404:
        print(f'\nRecord with id {record_id} already deleted')
    else:
        delete_response = delete_record_endpoint.delete_record_by_id(record_id)
        print(f'\nDELETE response status code: {delete_response.status_code}')
        assert delete_response.status_code == 200, f'Failed to delete record with id {record_id}'
        print(f'\nDeleting record with id {record_id}')
