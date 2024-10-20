import pytest
from API.user_api import UserAPI
from API.order_api import OrderAPI


@pytest.fixture(scope='session')
def user_api():
    return UserAPI()


@pytest.fixture(scope='session')
def order_api():
    return OrderAPI()