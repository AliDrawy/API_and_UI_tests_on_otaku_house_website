from infra.api_infra.api_wrapper import OtakuHouseAPI


class OtakuHouseHomePage(OtakuHouseAPI):
    def __init__(self):  # Constructor method to initialize class attributes
        super().__init__()

    def get_home_page(self):
        return self.api_get_request(f'{self.url}')

    def get_second_home_page(self):
        return self.api_get_request(f'{self.url[:-2]}api/products/?keyword=&page=2')

    def search_on_product(self, keyword):
        return self.api_get_request(f'{self.url[:-2]}api/products/?keyword={keyword}')

    def check_product_name(self, keyword, products):
        for item in products['products']:
            if keyword not in item['name'].lower():
                return False

        return True
