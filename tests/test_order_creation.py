import pytest
import allure


class TestOrderCreation:

    @allure.title('Создание заказа с авторизацией и ингредиентами')
    def test_create_order_authorized_with_ingredients(self, order_api, ingredients, user_token):
        response = order_api.create_order(ingredients[:2], user_token)
        assert response.status_code == 200
        assert response.json()['success'] == True

    @allure.title('Создание заказа без авторизации')
    def test_create_order_unauthorized(self, order_api, ingredients):
        response = order_api.create_order(ingredients[:2])
        assert response.status_code == 200
        assert response.json()['success'] == True

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_no_ingredients(self, order_api, user_token):
        response = order_api.create_order([], user_token)
        assert response.status_code == 400
        assert response.json()['message'] == 'Ingredient ids must be provided'

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_invalid_ingredients(self, order_api, user_token):
        response = order_api.create_order(['invalid_id'], user_token)
        assert response.status_code == 500
