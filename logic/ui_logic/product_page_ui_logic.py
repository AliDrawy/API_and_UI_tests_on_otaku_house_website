from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from infra.ui_infra.page_base import WebPageBase


class ProductPage(WebPageBase):
    PRODUCT = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/div')
    ADD_TO_CART_BTN = (By.XPATH, '//*[@id="root"]/div/main/div/div/div[1]/div[3]/div/div/div[4]/button')
    RATING_BOX = (By.XPATH, '//*[@id="root"]/div/main/div/div/div[2]/div/div/div[1]/div')

    def get_product_page(self):
        product = self.wait_condition.until(EC.element_to_be_clickable(self.PRODUCT))
        product.click()
        return True

    def scroll_down(self):
        cm_to_inches = 10 / 2.54
        dpi = 100
        scroll_distance_inches = cm_to_inches
        scroll_distance_pixels = int(scroll_distance_inches * dpi)
        while True:
            self.browser_driver.execute_script(f"window.scrollBy(0, {scroll_distance_pixels});")
            WebDriverWait(self.browser_driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            if self.browser_driver.execute_script(
                    "return window.innerHeight + window.scrollY >= document.body.scrollHeight"):
                break

    def check_review(self):
        self.scroll_down()
        WebDriverWait(self.browser_driver, 10).until(EC.presence_of_element_located(self.RATING_BOX))
        return True
