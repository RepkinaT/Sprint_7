import allure
import requests

from data import Data
from helpers import AssertHelper
from urls import Address


class TestOrderListRetrieval:
    @allure.title('Тестирование получения списка заказов')
    @allure.description('Запрашиваем список всех заказов c первой страницы. Должны получить код: 200, '
                        'а в тексте ожидаем слово orders')
    def test_getting_a_list_of_orders(self):
        response = requests.get(f"{Address.url}{Address.get_orders}")
        AssertHelper.assert_func(response, 200, Data.status_code.get(200)[0])
