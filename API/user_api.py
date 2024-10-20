from API.base_api import BaseAPI


class UserAPI(BaseAPI):
    def register_user(self, user_data):
        return self.post('/auth/register', json=user_data)

    def login_user(self, credentials):
        return self.post('/auth/login', json=credentials)

    def get_user(self, token):
        headers = {'Authorization': token}
        return self.get('/auth/user', headers=headers)

    def update_user(self, token, new_data):
        headers = {'Authorization': token}
        return self.patch('/auth/user', headers=headers, json=new_data)