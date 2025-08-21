import requests
import allure
from endpoints.default_endpoint import BaseEndpoint


class CreateRecord(BaseEndpoint):

    @allure.step('Creating a record')
    def new_record(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        return self.json

    @allure.step('Retrieving id of the record')
    def retrieve_record_id(self):
        record_id = self.json['id']
        return record_id
