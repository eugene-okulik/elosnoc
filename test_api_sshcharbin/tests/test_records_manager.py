import allure
import pytest


TEST_DATA = {"name": "test_object", "data": {"color": "orange", "size": "medium"}}


@allure.suite('Smoke suite')
@allure.feature('Records')
@allure.story('Getting records')
@allure.title('Check all available records can be received')
def test_get_all_records(get_record_endpoint, start_complete, before_after):
    get_record_endpoint.get_all_records()
    get_record_endpoint.check_status_code_is_200()


@allure.feature('Records')
@allure.story('Getting records')
@allure.title('Check that created record can be received by ID')
def test_get_record(new_record_id, get_record_endpoint):
    record_id = new_record_id
    print(record_id)
    get_record_endpoint.get_record_by_id(record_id=record_id)
    get_record_endpoint.check_id_is_correct(record_id=record_id)


@allure.severity('S0')
@allure.suite('Smoke suite')
@allure.feature('Records')
@allure.story('Records creation')
@allure.title('Check that record can be created')
@pytest.mark.parametrize('object_name', ['test_object', 'second_object', 'last_object'])
def test_create_record(object_name, create_record_endpoint, delete_record_endpoint):
    body = {
        "name": object_name,
        "data": {
            "color": "orange",
            "size": "medium"
        }
    }
    create_record_endpoint.new_record(body=body)
    create_record_endpoint.check_status_code_is_200()
    create_record_endpoint.check_color_is_correct(body['data']['color'])
    create_record_endpoint.check_name_is_correct(body['name'])
    create_record_endpoint.check_size_is_correct(body['data']['size'])
    record_id = create_record_endpoint.retrieve_record_id()
    print(record_id)
    delete_record_endpoint.delete_record_by_id(record_id)
    delete_record_endpoint.check_status_code_is_200()


@allure.suite('Regression suite')
@allure.feature('Records')
@allure.story('Records update')
@allure.title('Check that record can be updated using PUT method')
@pytest.mark.critical
def test_update_put_record(new_record_id, update_record_endpoint):
    body = {
        "name": "updated_put_object",
        "data": {
            "color": "black",
            "size": "medium"
        }
    }
    record_id = new_record_id
    update_record_endpoint.make_changes_by_put(record_id, body)
    update_record_endpoint.check_status_code_is_200()
    update_record_endpoint.check_name_is_correct(body['name'])
    update_record_endpoint.check_color_is_correct(body['data']['color'])
    update_record_endpoint.check_size_is_correct(body['data']['size'])


@allure.suite('Regression suite')
@allure.feature('Records')
@allure.story('Records update')
@allure.title('Check that record can be updated using PATCH method')
def test_update_patch_record(new_record_id, update_record_endpoint):
    body = {
        "data": {
            "color": "grey",
            "size": "big"
        }
    }
    record_id = new_record_id
    update_record_endpoint.make_changes_by_patch(record_id, body)
    update_record_endpoint.check_status_code_is_200()
    update_record_endpoint.check_size_is_correct(body['data']['size'])
    update_record_endpoint.check_color_is_correct(body['data']['color'])
    update_record_endpoint.check_name_is_correct(TEST_DATA['name'])


@allure.severity('S1')
@allure.suite('Smoke suite')
@allure.feature('Records')
@allure.story('Records deletion')
@allure.title('Check that record can be deleted')
@pytest.mark.medium
def test_delete_record(new_record_id, delete_record_endpoint, get_record_endpoint):
    record_id = new_record_id
    print(record_id)
    delete_record_endpoint.delete_record_by_id(record_id)
    delete_record_endpoint.check_status_code_is_200()
    get_record_endpoint.get_record_by_id(record_id)
    get_record_endpoint.check_status_code_is_404()
