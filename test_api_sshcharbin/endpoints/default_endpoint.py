import allure


class BaseEndpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Verifying correct color in record')
    def check_color_is_correct(self, color):
        assert self.json['data']['color'] == color, 'Incorrect object color'

    @allure.step('Verifying correct name in record')
    def check_name_is_correct(self, name):
        assert self.json['name'] == name, 'Incorrect object name'

    @allure.step('Verifying correct size in record')
    def check_size_is_correct(self, size):
        assert self.json['data']['size'] == size, 'Incorrect object size'

    @allure.step('Verifying that status code is 200')
    def check_status_code_is_200(self):
        assert self.response.status_code == 200, 'Something went wrong: Incorrect status code'

    @allure.step('Verifying 404 Not Found')
    def check_status_code_is_404(self):
        assert self.response.status_code == 404, 'Something went wrong: Incorrect status code'

    @allure.step('Verifying Bad Request 400')
    def check_status_code_is_400(self):
        assert self.response.status_code == 400, 'Something went wrong: Incorrect status code'

    @allure.step('Verifying Security Violation 403')
    def check_status_code_is_403(self):
        assert self.response.status_code == 403, 'Something went wrong: Incorrect status code'
