import unittest
from logic.api_logic.product_page import OtakuHouseProductPage


class TestOtakuHouseProductPage(unittest.TestCase):

    def setUp(self):
        self.product_page = OtakuHouseProductPage()
        self.response = None
        self.data = None

    def test_checking_received_product(self):
        self.response = self.product_page.get_product(self.product_page.product_id)
        self.data = self.response.json()
        self.response = self.product_page.check_product_id(self.product_page.product_id, self.data)
        self.assertTrue(self.response)

    def test_getting_product(self):
        self.response = self.product_page.get_product(self.product_page.product_id)
        self.data = self.response.json()
        self.assertEqual(self.response.status_code, 200)

    def test_send_review_about_product(self):
        self.response = self.product_page.send_review_about_product(self.product_page.rating,
                                                                    self.product_page.review_txt,
                                                                    self.product_page.product_id)
        self.assertEqual(self.response.status_code, 200)
