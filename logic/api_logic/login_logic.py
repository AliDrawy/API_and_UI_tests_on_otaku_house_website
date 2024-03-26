from infra.api_infra.api_wrapper import OtakuHouseAPI


class OtakuHouseLoginPage(OtakuHouseAPI):
    def __init__(self):  # Constructor method to initialize class attributes
        super().__init__()
        self.json_data = None

    def get_login_page(self):
        return self.api_get_request(f'{self.url}#/login')

    def login_user_to_account(self, mail, password):
        self.json_data = {"username": mail, "password": password}
        self.response = self.request.post(f'{self.url}api/users/login/', json=self.json_data)
        return self.response.status_code

    def register_account(self, username, mail, password):
        self.json_data = {"name": username, "email": mail, "password": password}
        self.response = self.request.post(f'{self.url}api/users/register/', json=self.json_data)
        return self.response.status_code


