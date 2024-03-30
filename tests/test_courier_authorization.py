import allure
import pytest

from data import Data
from helpers import CourierAuthorizationHelper, AssertHelper


class TestCourierAuthorization:
    @allure.title('Тест авторизации')
    @allure.description('Создаем запись курьера и входим с корректными данными. Должны получить код: 200 и текст '
                        'включающий id курьера')
    def test_courier_authorization_successful(self, obtaining_courier_record_data_and_its_further_deletion):
        data = obtaining_courier_record_data_and_its_further_deletion
        response = CourierAuthorizationHelper.requests_func(data)
        AssertHelper.assert_func(response, 200, Data.status_code.get(200)[0])
    
    @allure.title('Тест невозможности авторизации без логина/пароля')
    @allure.description('Создаем запись курьера и пробуем зайти в нее без логина, затем все тоже, '
                        'но без пароля. Должны получить код: 400 и текст: "Недостаточно данных для входа"')
    @pytest.mark.parametrize('missing_data', ('login', 'password'))
    def test_for_the_presence_of_necessary_data_for_authorization(
            self,
            obtaining_courier_record_data_and_its_further_deletion,
            missing_data):
        data = obtaining_courier_record_data_and_its_further_deletion
        response = CourierAuthorizationHelper.requests_func(data, missing_data=missing_data)
        AssertHelper.assert_func(response, 400, Data.status_code.get(400)[0])
    
    @allure.title('Тест невозможности авторизации c некорректным логином/паролем')
    @allure.description('Создаем запись курьера и пробуем зайти в нее с заведомо неправильным логином или паролем. '
                        'Должны получить код: 404 и текст: "Учетная запись не найдена"')
    @pytest.mark.parametrize('incorrect_data', ('login', 'password'))
    def test_for_the_correctness_of_authorization_data(self,
                                                       obtaining_courier_record_data_and_its_further_deletion,
                                                       incorrect_data):
        data = obtaining_courier_record_data_and_its_further_deletion
        response = CourierAuthorizationHelper.requests_func(data, incorrect_data=incorrect_data)
        AssertHelper.assert_func(response, 404, Data.status_code.get(404)[0])
