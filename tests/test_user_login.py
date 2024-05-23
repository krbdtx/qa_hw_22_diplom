import allure
from models.app import mid_lvl
from test_data.data import User_login
from faker import Faker
fake = Faker()

user1 = User_login(email='фыв@фыв.com', password='123123')
user2 = User_login(email='11asasdasd1@2asdasasd22.com', password='фывфвфыв123123123asdasdasd')
user3 = User_login(email=fake.email(), password=fake.password())


@allure.step(f"Проверка входа пользователя {user1}")
def test_login():

    mid_lvl.fill_login_page(user1)
    mid_lvl.should_login_good_page()


@allure.step(f"Проверка входа пользователя {user2}")
def test_login():

    mid_lvl.fill_login_page(user2)
    mid_lvl.should_login_negative_page()

@allure.step(f"Проверка входа пользователя {user3}")
def test_login():

    mid_lvl.fill_login_page(user2)
    mid_lvl.should_login_negative_page()
