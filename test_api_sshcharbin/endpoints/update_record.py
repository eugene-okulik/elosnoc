import requests
import allure
from endpoints.default_endpoint import BaseEndpoint


class UpdateRecord(BaseEndpoint):
    record_id = None

    @allure.step(f'Updating a record with id {record_id}')
    def make_changes_by_put(self, record_id, body, headers=None):
        headers = headers if headers else self.headers
        record_id = record_id if record_id else self.record_id
        self.response = requests.put(
            f'{self.url}/{record_id}',
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        return self.response

    @allure.step(f'Updating a record with id {record_id}')
    def make_changes_by_patch(self, record_id, body, headers=None):
        headers = headers if headers else self.headers
        record_id = record_id if record_id else self.record_id
        self.response = requests.patch(
            f'{self.url}/{record_id}',
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
