import unittest
from logic.api_logic.home_page_logic import OtakuHouseHomePage


class TestOtakuHouseHomePage(unittest.TestCase):

    def setUp(self):
        self.home_page = OtakuHouseHomePage()
        self.response = None

    def test_get_home_page(self):
        self.assertEqual(self.home_page.get_home_page().status_code, 200)

    def test_get_second_home_page(self):
        self.assertEqual(self.home_page.get_second_home_page().status_code, 200)

    def test_check_searched_product(self):
        self.response = self.home_page.search_on_product(self.home_page.searching_keyword)
        self.data = self.response.json()
        self.response = self.home_page.check_product_name(self.home_page.searching_keyword, self.data)
        self.assertTrue(self.response)

    def test_searching_on_product(self):
        self.assertEqual(self.home_page.search_on_product(self.home_page.searching_keyword).status_code, 200)
