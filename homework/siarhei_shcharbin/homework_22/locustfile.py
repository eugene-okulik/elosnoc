from locust import task, HttpUser
import random


class RecordsUser(HttpUser):

    @task(0)
    def get_all_records(self):
        self.client.get(url='')

    @task(2)
    def get_record_by_id(self):
        self.client.get(url=f'/{random.randrange(1, 20)}')
