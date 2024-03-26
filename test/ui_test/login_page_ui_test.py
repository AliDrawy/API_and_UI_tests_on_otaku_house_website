import unittest
from infra.ui_infra.browser_wrapper import WebBrowser
from logic.ui_logic.login_page_logic_ui import LoginPage


class LoginPageTests(unittest.TestCase):
    def setUp(self):
        self.navigator = WebBrowser()
        self.browser_driver = self.navigator.launch_browser("chrome")
        self.wait_tool = self.navigator.wait()
        self.LoginPage = LoginPage(self.browser_driver, self.wait_tool)
        self.result = None

    def test_login_with_valid_mail_and_password(self):
        self.assertTrue(self.LoginPage.login_via_valid_mail_and_password(self.navigator.user_mail, self.navigator.user_password))

    def test_login_with_invalid_mail_and_password(self):
        self.assertFalse(self.LoginPage.login_via_valid_mail_and_password(self.navigator.invalid_mail, self.navigator.invalid_user_password))

    def test_login_with_valid_mail_and_invalid_password(self):
        self.assertFalse(self.LoginPage.login_via_valid_mail_and_password(self.navigator.user_mail,self.navigator.invalid_user_password))

    def test_register_with_new_mail(self):
        self.assertTrue(self.LoginPage.register_via_mail_and_password(self.navigator.user_name, self.navigator.register_mail, self.navigator.user_password))

    def test_register_with_old_mail(self):
        self.assertFalse(self.LoginPage.register_via_mail_and_password(self.navigator.user_name, self.navigator.user_mail, self.navigator.user_password))

    def tearDown(self):
        self.navigator.terminate_browser()
