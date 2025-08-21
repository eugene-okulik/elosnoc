import requests
import allure
from endpoints.default_endpoint import BaseEndpoint


class GetRecord(BaseEndpoint):
    record_id = None

    @allure.step('Retrieving all records data')
    def get_all_records(self):
        self.response = requests.get(
            self.url
        )
        if self.response.status_code == 200:
            self.json = self.response.json()
        return self.response

    @allure.step('Retrieving a record')
    def get_record_by_id(self, record_id):
        record_id = record_id if record_id else self.record_id
        self.response = requests.get(
            f'{self.url}/{record_id}',
        )
        if self.response.status_code == 200:
            self.json = self.response.json()
        return self.response

    @allure.step('Verifying correct id in record')
    def check_id_is_correct(self, record_id):
        assert int(self.json['id']) == record_id, 'Incorrect object id'
