import pytest
import requests

from data import Data


@pytest.fixture()
def get_the_courier_data():
    data = {
        "login": Data.get_random_login(),
        "password": Data.get_random_password(),
        "firstname": Data.get_random_firstname()
    }
    return data


@pytest.fixture()
def obtaining_courier_record_data_and_its_further_deletion(get_the_courier_data):
    courier_data = get_the_courier_data
    yield courier_data

    response = requests.post(f'{Data.url}{Data.login_courier}',
                             data={"login": courier_data.get("login"), "password": courier_data.get("password")})
    id_courier = response.json().get("id")
    requests.delete(f'{Data.url}{Data.delete_courier}{id_courier}')


@pytest.fixture()
def get_the_order_data():
    order_data = {
        "firstname": Data.get_random_firstname(),
        "lastname": Data.get_random_lastname(),
        "address": Data.get_random_address(),
        "metro_station": Data.get_random_metro_station(),
        "phone": Data.get_random_phone(),
        "rent_time": Data.get_random_rent_time(),
        "delivery_date": Data.get_random_delivery_date(),
        "comment": Data.get_random_comment()
    }
    return order_data
