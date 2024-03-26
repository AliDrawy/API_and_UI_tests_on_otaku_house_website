import unittest
from infra.ui_infra.browser_wrapper import WebBrowser
from logic.ui_logic.home_page_logic_ui import HomePage
from logic.ui_logic.login_page_logic_ui import LoginPage
from logic.api_logic.login_logic import OtakuHouseLoginPage
from logic.api_logic.product_page import OtakuHouseProductPage
from logic.ui_logic.product_page_ui_logic import ProductPage


class APIAndUI(unittest.TestCase):
    def setUp(self):
        self.navigator = WebBrowser()
        self.browser_driver = self.navigator.launch_browser("chrome")
        self.wait_tool = self.navigator.wait()
        self.LoginPage = LoginPage(self.browser_driver, self.wait_tool)
        self.otaku_house = OtakuHouseLoginPage()
        self.product_page = OtakuHouseProductPage()
        self.product_page_ui = ProductPage(self.browser_driver, self.wait_tool)
        self.HomePage = HomePage(self.browser_driver, self.wait_tool)
        self.response = None

    def test_creat_account_via_api_and_login_via_ui(self):
        self.response = self.otaku_house.register_account(self.otaku_house.user_name, self.otaku_house.new_user_mail,
                                                          self.otaku_house.user_password)
        self.response = self.LoginPage.login_via_valid_mail_and_password(self.navigator.user_mail,
                                                                         self.navigator.user_password)
        self.assertTrue(self.response)

    def test_send_review_via_api_and_test_via_ui(self):
        self.response = self.LoginPage.login_via_valid_mail_and_password(self.navigator.user_mail,
                                                                         self.navigator.user_password)
        self.response = self.product_page.send_review_about_product(self.product_page.rating,
                                                                    self.product_page.review_txt,
                                                                    self.product_page.product_id)
        self.response = self.HomePage.search_on_products_by_keyword(self.navigator.keyword)
        self.response = self.product_page_ui.get_product_page()
        self.response = self.product_page_ui.check_review()
        self.assertTrue(self.response)

    def tearDown(self):
        self.navigator.terminate_browser()
