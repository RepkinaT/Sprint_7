import allure
import pytest

from data import Data
from helpers import CourierCreationHelper, AssertHelper


class TestCourierCreation:
    @allure.title('Тест создания курьера')
    @allure.description('Создаем запись курьера передавая логин, пароль и имя. Должны получить код: 201 и'
                        ' текст: "ok":true')
    def test_successful_courier_creation(self, obtaining_courier_record_data_and_its_further_deletion):
        data = obtaining_courier_record_data_and_its_further_deletion
        response = CourierCreationHelper.requests_func(data)
        AssertHelper.assert_func(response, 201, Data.status_code.get(201)[0])

    @allure.title('Тест создания двух записей курьеров с идентичными логинами')
    @allure.description('Пытаемся создать две записи с одинаковыми логинами. Должны получить код: 409 и '
                        'текст:  "Этот логин уже используется"')
    def test_of_impossibility_of_creating_two_identical_couriers(self,
                                                                 obtaining_courier_record_data_and_its_further_deletion):
        data = obtaining_courier_record_data_and_its_further_deletion
        CourierCreationHelper.requests_func(data)
        response = CourierCreationHelper.requests_func(data)
        AssertHelper.assert_func(response, 409, Data.status_code.get(409)[0])

    @allure.title('Тест невозможности создания записи курьера без указания логина и пароля')
    @allure.description('Пытаемся создать две запись без логина или пароля. Должны получить код: 400 и '
                        'текст: "Недостаточно данных"')
    @pytest.mark.parametrize('missing_data', ('login', 'password'))
    def test_courier_creation_without_login_or_password(self, get_the_courier_data, missing_data):
        data = get_the_courier_data
        del data[missing_data]
        response = CourierCreationHelper.requests_func(data)
        AssertHelper.assert_func(response, 400, Data.status_code.get(400)[0])

    @allure.title('Тест создания записи курьера без указания имени')
    @allure.description('Пытаемся создать запись без указания имени. Должны получить код: 201 и '
                        'текст: {"ok":true}')
    def test_for_creating_a_courier_without_name_data(self, obtaining_courier_record_data_and_its_further_deletion):
        data = obtaining_courier_record_data_and_its_further_deletion
        del data["firstname"]
        response = CourierCreationHelper.requests_func(data)
        AssertHelper.assert_func(response, 201, Data.status_code.get(201)[0])
