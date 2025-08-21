import requests
import allure
from endpoints.default_endpoint import BaseEndpoint


class DeleteRecord(BaseEndpoint):
    record_id = None

    @allure.step(f'Deleting a record with id {record_id}')
    def delete_record_by_id(self, record_id, headers=None):
        headers = headers if headers else self.headers
        record_id = record_id if record_id else self.record_id
        self.response = requests.delete(
            f'{self.url}/{record_id}',
            headers=headers
        )
        return self.response
