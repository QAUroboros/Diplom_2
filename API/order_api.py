from API.base_api import BaseAPI


class OrderAPI(BaseAPI):

    def get_ingredients(self):
        return self.get('/ingredients')

    def create_order(self, ingredients, token=None):
        headers = {'Authorization': token} if token else {}
        order_data = {"ingredients": ingredients}
        return self.post('/orders', headers=headers, json=order_data)

    def get_orders(self, token):
        headers = {'Authorization': token}
        return self.get('/orders', headers=headers)