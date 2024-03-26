from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from infra.ui_infra.page_base import WebPageBase
from selenium.common.exceptions import TimeoutException


class HomePage(WebPageBase):
    PRODUCTS_LIST = (By.XPATH, '//*[@class="col-xl-3 col-lg-4 col-md-6 col-sm-12"]')
    SEARCH_BAR = (By.XPATH, '//*[@id="navbarScroll"]/form/input')
    SEARCH_BTN = (By.XPATH, '//*[@id="navbarScroll"]/form/button')
    SECOND_PAGE_BTN = (By.XPATH, '//*[@id="root"]/div/main/div/div[2]/ul/li[2]/a')

    def search_on_products_by_keyword(self, keyword):

        mail_btn = self.wait_condition.until(EC.element_to_be_clickable(self.SEARCH_BAR))
        mail_btn.click()
        mail_btn.send_keys(keyword)
        sign_in = self.wait_condition.until(EC.element_to_be_clickable(self.SEARCH_BTN))
        sign_in.click()
        WebDriverWait(self.browser_driver, 10).until(EC.visibility_of_element_located(self.PRODUCTS_LIST))
        products_list = self.browser_driver.find_elements(*self.PRODUCTS_LIST)

        for product in products_list:
            text = WebDriverWait(self.browser_driver, 20).until(EC.visibility_of(product)).text
            if keyword.lower() not in text.lower():
                return False
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

    def open_second_page(self):
        self.scroll_down()
        sign_in = self.wait_condition.until(EC.element_to_be_clickable(self.SECOND_PAGE_BTN))
        sign_in.click()
        return self.browser_driver.current_url
