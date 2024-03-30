import requests

from data import Data


class CourierAuthorizationHelper:
    @staticmethod
    def requests_func(data, missing_data=None, incorrect_data=None):
        requests.post(f"{Data.url}{Data.create_courier}", data=data)
        if missing_data:
            data[missing_data] = ""
        elif incorrect_data:
            data[incorrect_data] = incorrect_data + "qwerty"
        return requests.post(f"{Data.url}{Data.login_courier}", data=data)


class CourierCreationHelper:
    @staticmethod
    def requests_func(data):
        return requests.post(f"{Data.url}{Data.create_courier}", data=data)


class OrderCreationHelper:
    @staticmethod
    def requests_func(data):
        return requests.post(f"{Data.url}{Data.create_order}", data=data)


class AssertHelper:
    @staticmethod
    def assert_func(response, expected_status_code, expected_text):
        assert response.status_code == expected_status_code and expected_text in response.text
