import unittest
from logic.api_logic.login_logic import OtakuHouseLoginPage


class TestOtakuHouseLoginPage(unittest.TestCase):

    def setUp(self):
        self.otaku_house = OtakuHouseLoginPage()

    def test_get_login_page(self):
        self.assertEqual(self.otaku_house.get_login_page().status_code, 200)

    def test_login_user_to_account_with_valid_mail_and_password(self):
        self.assertEqual(self.otaku_house.login_user_to_account(self.otaku_house.user_mail, self.otaku_house.user_password), 200)

    def test_login_user_to_account_with_invalid_mail(self):
        self.assertNotEqual(self.otaku_house.login_user_to_account(self.otaku_house.new_user_mail,self.otaku_house.invalid_user_password), 200)

    def test_login_user_to_account_with_invalid_password(self):
        self.assertNotEqual(self.otaku_house.login_user_to_account(self.otaku_house.user_mail, self.otaku_house.invalid_user_password), 200)

    def test_Register_user_to_account_with_new_account(self):
        self.assertEqual(self.otaku_house.register_account(self.otaku_house.user_name, self.otaku_house.new_user_mail, self.otaku_house.user_password), 200)

    def test_login_user_to_account_with_existing_account(self):
        self.assertNotEqual(self.otaku_house.register_account(self.otaku_house.user_name, self.otaku_house.user_mail, self.otaku_house.user_password), 200)
