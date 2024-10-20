import pytest
import allure


class TestUserDataChange:

    @allure.title('Изменение данных пользователя с авторизацией')
    def test_change_user_data_authorized(self, user_api, user_token):
        new_data = {"name": "New Name"}
        response = user_api.update_user(user_token, new_data)
        assert response.status_code == 200
        assert response.json()['user']['name'] == 'New Name'

    @allure.title('Изменение данных пользователя без авторизации')
    def test_change_user_data_unauthorized(self, user_api):
        new_data = {"name": "Another Name"}
        response = user_api.update_user(None, new_data)
        assert response.status_code == 401
        assert response.json()['message'] == 'You should be authorised'