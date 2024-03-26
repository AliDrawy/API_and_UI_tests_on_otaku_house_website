import unittest
from infra.ui_infra.browser_wrapper import WebBrowser
from logic.ui_logic.login_page_logic_ui import LoginPage
from logic.ui_logic.home_page_logic_ui import HomePage


class HomePageTests(unittest.TestCase):
    def setUp(self):
        self.navigator = WebBrowser()
        self.browser_driver = self.navigator.launch_browser("chrome")
        self.wait_tool = self.navigator.wait()
        self.LoginPage = LoginPage(self.browser_driver, self.wait_tool)
        self.LoginPage.login_via_valid_mail_and_password(self.navigator.user_mail,
                                                         self.navigator.user_password)
        self.HomePage = HomePage(self.browser_driver, self.wait_tool)

    def test_searching_on_products_by_keyword(self):
        self.assertTrue(self.HomePage.search_on_products_by_keyword(self.navigator.keyword))

    def test_opening_second_page(self):
        self.assertEqual(self.HomePage.open_second_page(), 'http://127.0.0.1:8000/#/?keyword=&page=2')

    def tearDown(self):
        self.navigator.terminate_browser()
