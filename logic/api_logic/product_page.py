from infra.api_infra.api_wrapper import OtakuHouseAPI


class OtakuHouseProductPage(OtakuHouseAPI):
    def __init__(self):  # Constructor method to initialize class attributes
        super().__init__()
        self.json_data = None

    def check_product_id(self, product_id, product):
        if product_id == product['_id']:
            return True
        return False

    def get_product(self, product_id):
        return self.api_get_request(f'{self.url}api/products/{product_id}/')

    def send_review_about_product(self, rating_list, review, product_id):
        rating = self.choose_random_value(rating_list)
        self.json_data = {"rating": rating, "comment": review}
        self.response = self.request.post(f'{self.url}api/products/{product_id}/reviews/', json=self.json_data,
                                          headers=self.headers)
        return self.response

    # def add_product_to_cart(self, product_id):
    #     return  self.api_get_request(f'{self.url[:-2]}api/products/{product_id}/')
# http://127.0.0.1:8000/api/products/26/