from infra.api_infra.api_wrapper import OtakuHouseAPI


class OtakuHouseProfilePage(OtakuHouseAPI):
    def __init__(self):  # Constructor method to initialize class attributes
        super().__init__()
        self.json_data = None

    def update_profile(self, id, name, mail, password):
        self.json_data = {"id": id, "name": name, "email": mail, "password": password}
        self.response = self.request.put(f'{self.url[:-2]}api/users/profile/update/', json=self.json_data,
                                         headers=self.headers)
        return self.response

    def get_order_dietels(self, order_id):
        return self.request.get(f'{self.url[:-2]}api/orders/{order_id}/', headers=self.headers)
