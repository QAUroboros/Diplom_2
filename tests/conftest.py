import uuid
import pytest
from API.user_api import UserAPI
from API.order_api import OrderAPI


@pytest.fixture(scope='session')
def user_api():
    return UserAPI()


@pytest.fixture(scope='session')
def order_api():
    return OrderAPI()


@pytest.fixture(scope='function')
def user_data():
    unique_email = f"user_{uuid.uuid4()}@example.com"
    return {
        "email": unique_email,
        "password": "123456",
        "name": "Артём"
    }


@pytest.fixture(scope='function')
def register_user(user_api, user_data):
    response = user_api.register_user(user_data)
    if response.status_code == 200 or (
            response.status_code == 403 and response.json().get('message') == 'User already exists'):
        return user_data
    else:
        assert False, f"Не удалось зарегистрировать пользователя: {response.text}"


@pytest.fixture(scope='function')
def user_token(user_api, register_user):
    credentials = {
        "email": register_user['email'],
        "password": register_user['password']
    }
    response = user_api.login_user(credentials)
    assert response.status_code == 200, f"Не удалось авторизовать пользователя: {response.text}"
    return response.json()['accessToken']


@pytest.fixture(scope='function')
def ingredients(order_api):
    response = order_api.get_ingredients()
    assert response.status_code == 200, f"Не удалось получить ингредиенты: {response.text}"
    return [item['_id'] for item in response.json()['data']]
