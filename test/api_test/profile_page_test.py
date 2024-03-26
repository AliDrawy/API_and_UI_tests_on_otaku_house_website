import unittest
from logic.api_logic.profile_page import OtakuHouseProfilePage
from logic.api_logic.login_logic import OtakuHouseLoginPage


class TestOtakuHouseProfilePage(unittest.TestCase):

    def setUp(self):
        self.profile_page = OtakuHouseProfilePage()
        self.login_page = OtakuHouseLoginPage()
        self.response = None
        self.data = None

    def test_update_profile_name(self):
        self.response = self.profile_page.update_profile(self.profile_page.user_id, self.profile_page.user_name,
                                                         self.profile_page.user_mail,
                                                         self.profile_page.user_password)
        self.response = self.login_page.login_user_to_account(self.profile_page.user_mail,
                                                              self.profile_page.user_password)
        self.assertEqual(self.response, 200)

    def test_update_profile_mail(self):
        self.response = self.profile_page.update_profile(self.profile_page.user_id, self.profile_page.user_name,
                                                         self.profile_page.new_user_mail,
                                                         self.profile_page.user_password)
        self.response = self.login_page.login_user_to_account(self.profile_page.new_user_mail,
                                                              self.profile_page.user_password)
        self.assertEqual(self.response, 200)

    def test_update_profile_password(self):
        self.response = self.profile_page.update_profile(self.profile_page.user_id, self.profile_page.user_name,
                                                         self.profile_page.user_mail,
                                                         self.profile_page.user_password)
        self.response = self.login_page.login_user_to_account(self.profile_page.user_mail,
                                                              self.profile_page.user_password)
        self.assertEqual(self.response, 200)

    def test_getting_order_dietels(self):
        self.response = self.profile_page.get_order_dietels(self.profile_page.order_id)
        self.assertEqual(self.response.status_code, 200)

