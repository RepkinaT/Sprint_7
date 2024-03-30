import allure
import pytest

from data import Data
from helpers import OrderCreationHelper, AssertHelper


class TestOrderCreation:
    @allure.title('Тестирование заказа с выбором любого варианта цветов самоката')
    @allure.description('Формируем заказ передавая разные варианты цветов. '
                        'Должны получить код: 201, и текст в котором есть есть track')
    @pytest.mark.parametrize("scooter_color", Data.get_random_scooter_color())
    def test_creating_an_order_with_a_choice_of_any_color(self, get_the_order_data, scooter_color):
        data = get_the_order_data["color"] = scooter_color
        response = OrderCreationHelper.requests_func(data)
        AssertHelper.assert_func(response, 201, Data.status_code.get(201)[1])
