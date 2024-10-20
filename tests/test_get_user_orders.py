import pytest
import allure


class TestGetUserOrders:

    @pytest.fixture(autouse=True)
    def setup(self, order_api, ingredients, user_token):
        response = order_api.create_order(ingredients[:2], user_token)
        assert response.status_code == 200

    @allure.title('Получение заказов авторизованным пользователем')
    def test_get_orders_authorized(self, order_api, user_token):
        response = order_api.get_orders(user_token)
        assert response.status_code == 200
        assert response.json()['success'] == True
        assert 'orders' in response.json()

    @allure.title('Получение заказов неавторизованным пользователем')
    def test_get_orders_unauthorized(self, order_api):
        response = order_api.get_orders(None)
        assert response.status_code == 401
        assert response.json()['message'] == 'You should be authorised'

