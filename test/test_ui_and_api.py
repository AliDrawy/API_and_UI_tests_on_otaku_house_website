import unittest
from infra.ui_infra.browser_wrapper import WebBrowser
from logic.ui_logic.login_page_logic import LoginPage
from logic.api_logic.login_logic import OtakuHouseLoginPage


class HomePage(unittest.TestCase):
    def setUp(self):
        self.navigator = WebBrowser()
        self.browser_driver = self.navigator.launch_browser("chrome")
        self.wait_tool = self.navigator.wait()
        self.LoginPage = LoginPage(self.browser_driver, self.wait_tool)
        self.otaku_house = OtakuHouseLoginPage()
        self.response = None
        self.data = None

    def test_creat_account_via_api_and_login_via_ui(self):
        self.response = self.otaku_house.register_account(self.otaku_house.user_name, self.otaku_house.new_user_mail, self.otaku_house.user_password)
        self.browser_driver.maximize_window()
        result = self.LoginPage.login_by_valid_mail_and_password("drawyali100@gmail.com", "merr@c53My")
        self.assertTrue(result)

    def tearDown(self):
        self.navigator.terminate_browser()