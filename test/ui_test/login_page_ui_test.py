import unittest
from infra.ui_infra.browser_wrapper import WebBrowser
from logic.ui_logic.login_page_logic import LoginPage


class HomePage(unittest.TestCase):
    def setUp(self):
        self.navigator = WebBrowser()
        self.browser_driver = self.navigator.launch_browser("chrome")
        self.wait_tool = self.navigator.wait()
        self.LoginPage = LoginPage(self.browser_driver, self.wait_tool)

    # def test_theme_change_to_dark(self):
    #     self.LoginPage.modify_theme("Dark")
    #     is_theme_applied = self.LoginPage.confirm_theme("Dark")
    #     self.assertTrue(is_theme_applied)
    #
    # def test_theme_change_to_light(self):
    #     self.LoginPage.modify_theme("Light")
    #     is_theme_applied = self.LoginPage.confirm_theme("Light")
    #     self.assertTrue(is_theme_applied)

    def test_login_with_valid_mail_and_password(self):
        self.browser_driver.maximize_window()
        result = self.LoginPage.login_by_valid_mail_and_password("drawyali100@gmail.com", "merr@c53My")
        self.assertTrue(result)
        

    def tearDown(self):
        self.navigator.terminate_browser()
