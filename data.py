import datetime
import random
from random import randint


class Data:
    url = 'https://qa-scooter.praktikum-services.ru'

    create_courier = "/api/v1/courier"
    login_courier = "/api/v1/courier/login"
    delete_courier = "/api/v1/courier/"
    create_order = "/api/v1/orders"
    get_order = "/api/v1/orders/track?t="
    get_orders = "/api/v1/orders"

    status_code = {200: ["id", "orders"], 201: ['{"ok":true}', "track"], 400: ["Недостаточно данных"],
                   404: ["Учетная запись не найдена"],
                   409: ["Этот логин уже используется"]}

    @staticmethod
    def get_random_login():
        return f"my_login_{random.randint(1, 100000)}"

    @staticmethod
    def get_random_password():
        return random.choice(["Pass.1", "Pass.2", "Pass.3"])

    @staticmethod
    def get_random_firstname():
        return random.choice(["Firstname_1", "Firstname_2", "Firstname_3"])

    @staticmethod
    def get_random_lastname():
        return random.choice(["Lastname_1", "Lastname_2", "Lastname_3"])

    @staticmethod
    def get_random_address():
        return random.choice(["address_1", "address_2", "address_3"])

    @staticmethod
    def get_random_metro_station():
        return random.choice(["station_1", "station_2", "station_3"])

    @staticmethod
    def get_random_phone():
        return random.choice(["89991234567", "89151234567", "89621234567"])

    @staticmethod
    def get_random_delivery_date():
        return datetime.date.today() + datetime.timedelta(days=random.randint(1, 7))

    @staticmethod
    def get_random_rent_time():
        return randint(1, 5)

    @staticmethod
    def get_random_scooter_color():
        return random.choice([['BLACK', 'GREY'], ['BLACK'], ['GREY']])

    @staticmethod
    def get_random_comment():
        return random.choice(["comment_1", "comment_2", "comment_3"])
