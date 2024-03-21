import unittest
from logic.api_logic.login_logic import OtakuHouseLoginPage


class TestOtakuHouseLoginPage(unittest.TestCase):

    def setUp(self):
        self.otaku_house = OtakuHouseLoginPage()
        self.response = None
        self.data = None

    def test_get_login_page(self):
        self.response = self.otaku_house.get_login_page()
        self.assertEqual(self.response.status_code, 200)

    def test_login_user_to_account_with_valid_mail_and_password(self):
        self.response = self.otaku_house.login_user_to_account(self.otaku_house.user_mail,
                                                               self.otaku_house.user_password)
        self.assertEqual(self.response, 200)

    def test_login_user_to_account_with_invalid_mail(self):
        self.response = self.otaku_house.login_user_to_account(self.otaku_house.new_user_mail,
                                                               self.otaku_house.invalid_user_password)
        self.assertNotEqual(self.response, 200)

    def test_login_user_to_account_with_invalid_password(self):
        self.response = self.otaku_house.login_user_to_account(self.otaku_house.user_mail,
                                                               self.otaku_house.invalid_user_password)
        self.assertNotEqual(self.response, 200)

    def test_Register_user_to_account_with_new_account(self):
        self.response = self.otaku_house.register_account(self.otaku_house.user_name, self.otaku_house.new_user_mail,
                                                          self.otaku_house.user_password)
        self.assertEqual(self.response, 200)

    def test_login_user_to_account_with_existing_account(self):
        self.response = self.otaku_house.register_account(self.otaku_house.user_name, self.otaku_house.user_mail,
                                                          self.otaku_house.user_password)
        self.assertNotEqual(self.response, 200)

