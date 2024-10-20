import requests
from utils.config import BASE_URL


class BaseAPI:
    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()

    def post(self, endpoint, headers=None, json=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, headers=headers, json=json)

    def get(self, endpoint, headers=None, params=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url, headers=headers, params=params)

    def patch(self, endpoint, headers=None, json=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.patch(url, headers=headers, json=json)