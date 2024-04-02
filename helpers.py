import allure
import requests

from urls import Address


class CourierAuthorizationHelper:

    @staticmethod
    @allure.step('Авторизация курьера')
    def courier_authorization_requests(data, missing_data=None, incorrect_data=None):
        requests.post(f"{Address.url}{Address.create_courier}", data=data)
        if missing_data:
            data[missing_data] = ""
        elif incorrect_data:
            data[incorrect_data] = incorrect_data + "qwerty"
        return requests.post(f"{Address.url}{Address.login_courier}", data=data)


class CourierCreationHelper:
    @staticmethod
    @allure.step('Создание учетной записи курьера')
    def courier_creation_request(data):
        return requests.post(f"{Address.url}{Address.create_courier}", data=data)


class OrderCreationHelper:
    @staticmethod
    @allure.step('Создание заказа')
    def order_creation_request(data):
        return requests.post(f"{Address.url}{Address.create_order}", data=data)


class CourierDeletionHelper:
    @staticmethod
    @allure.step('Удаление учетной записи курьера')
    def courier_deletion_requests(data):
        response = requests.post(f'{Address.url}{Address.login_courier}',
                                 data={"login": data.get("login"), "password": data.get("password")})
        id_courier = response.json().get("id")
        requests.delete(f'{Address.url}{Address.delete_courier}{id_courier}')


class AssertHelper:
    @staticmethod
    @allure.step('Сопоставление ответов с ожидаемыми данными')
    def assert_func(response, expected_status_code, expected_text):
        assert response.status_code == expected_status_code and expected_text in response.text
