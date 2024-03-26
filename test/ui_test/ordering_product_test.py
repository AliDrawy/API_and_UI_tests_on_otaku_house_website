import unittest
from infra.ui_infra.browser_wrapper import WebBrowser
from logic.ui_logic.login_page_logic_ui import LoginPage
from logic.ui_logic.home_page_logic_ui import HomePage
from logic.ui_logic.ordering_product_logic import OrderingProduct


class OrderingProductTests(unittest.TestCase):
    def setUp(self):
        self.navigator = WebBrowser()
        self.browser_driver = self.navigator.launch_browser("chrome")
        self.wait_tool = self.navigator.wait()
        self.HomePage = HomePage(self.browser_driver, self.wait_tool)
        self.LoginPage = LoginPage(self.browser_driver, self.wait_tool)
        self.LoginPage.login_via_valid_mail_and_password(self.navigator.user_mail,
                                                         self.navigator.user_password)
        self.result = None
        self.order_product = OrderingProduct(self.browser_driver, self.wait_tool)

    def test_ordering_product(self):
        self.result = self.HomePage.search_on_products_by_keyword(self.navigator.keyword_for_cart)
        self.result = self.order_product.get_product_for_cart()
        self.result = self.order_product.add_product_to_cart()
        self.result = self.order_product.proceed_to_checkout()
        self.result = self.order_product.add_shipping_address(self.navigator.address, self.navigator.city,
                                                              self.navigator.postal_code, self.navigator.country)
        self.result = self.order_product.place_order()
        self.result = self.order_product.fill_payment_details(self.navigator.visa, self.navigator.cvv,
                                                              self.navigator.postal_code, self.navigator.ex_date,
                                                              self.navigator.user_name, self.navigator.address,
                                                              self.navigator.city,
                                                              self.navigator.phone,
                                                              self.navigator.user_mail,self.navigator.country)
        self.assertTrue(self.result)

    def tearDown(self):
        self.navigator.terminate_browser()
