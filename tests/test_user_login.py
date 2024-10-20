import pytest
import allure


class TestUserLogin:

    @allure.title('Логин под существующим пользователем')
    def test_login_existing_user(self, user_api, register_user):
        credentials = {
            "email": register_user['email'],
            "password": register_user['password']
        }
        response = user_api.login_user(credentials)
        assert response.status_code == 200
        assert response.json()['success'] == True

    @allure.title('Логин с неверным логином и паролем')
    def test_login_invalid_credentials(self, user_api):
        credentials = {
            "email": "wrong_user@example.com",
            "password": "wrongpassword"
        }
        response = user_api.login_user(credentials)
        assert response.status_code == 401
        assert response.json()['message'] == 'email or password are incorrect'
