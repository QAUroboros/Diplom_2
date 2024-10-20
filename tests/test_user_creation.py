import pytest
import allure


class TestUserCreation:

    @allure.title('Создание уникального пользователя')
    def test_create_unique_user(self, user_api, user_data):
        response = user_api.register_user(user_data)
        assert response.status_code == 200, f"Статус код: {response.status_code}, тело ответа: {response.text}"
        assert response.json()['success'] == True

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_existing_user(self, user_api, register_user):
        response = user_api.register_user(register_user)
        assert response.status_code == 403
        assert response.json()['message'] == 'User already exists'

    @allure.title('Создание пользователя без обязательного поля')
    @pytest.mark.parametrize('missing_field', ['email', 'password', 'name'])
    def test_create_user_missing_field(self, user_api, user_data, missing_field):
        user_data = user_data.copy()
        user_data.pop(missing_field)
        response = user_api.register_user(user_data)
        assert response.status_code == 403
        assert response.json()['message'] == 'Email, password and name are required fields'