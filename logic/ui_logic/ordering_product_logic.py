from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from infra.ui_infra.page_base import WebPageBase
from selenium.webdriver.support.ui import Select


class OrderingProduct(WebPageBase):
    PRODUCT = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/div/a')
    PRODUCT_TO_CART = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/div')
    ADD_TO_CART_BTN = (By.XPATH, '//*[@id="root"]/div/main/div/div/div[1]/div[3]/div/div/div[4]/button')
    CHEK_OUT_BTN = (By.XPATH, '//*[@id="root"]/div/main/div/div[2]/div/div[2]/button')
    SHIPPING_TITLE = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/h1')
    ADDRESS_INPUT = (By.XPATH, '//*[@id="address"]')
    CITY_INPUT = (By.XPATH, '//*[@id="city"]')
    POSTAL_CODE_INPUT = (By.XPATH, '//*[@id="postalCode"]')
    COUNTRY_INPUT = (By.XPATH, '//*[@id="country"]')
    CONTINUE_BTN = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/button')
    PAYMENT_METHOD = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/legend')
    PLACE_ORDER_BTN = (By.XPATH, '//*[@id="root"]/div/main/div/div[2]/div[2]/div/div/div[7]/button')
    PAYMENT_METHOD_BTN = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/button')
    PAY_VIA_VISA_BTN = (By.XPATH, '//*[@id="buttons-container"]/div/div[2]')
    VISA_INPUT = (By.XPATH, '//*[@id="credit-card-number"]')
    IFRAM_1 = (By.XPATH, "//*[starts-with(@name, '__zoid__paypal_buttons__')]")
    IFRAM_2 = (By.XPATH, "//*[starts-with(@name, '__zoid__paypal_card_form__')]")
    BUTTONS_CONTAINER = (By.XPATH, '//*[@id="buttons-container"]/div/div[2]/div')
    CVV = (By.XPATH, '//*[@id="credit-card-security"]')
    EX_DATE = (By.XPATH, '//*[@id="expiry-date"]')
    FIRST_NAME = (By.XPATH, '//*[@id="billingAddress.givenName"]')
    LAST_NAME = (By.XPATH, '//*[@id="billingAddress.familyName"]')
    ADDRESS_LINE = (By.XPATH, '//*[@id="billingAddress.line1"]')
    CITY_LINE = (By.XPATH, '//*[@id="billingAddress.city"]')
    POSTAL_CODE = (By.XPATH, '//*[@id="billingAddress.postcode"]')
    MOBILE_NUM = (By.XPATH, '//*[@id="phone"]')
    MAIL_INPUT = (By.XPATH, '//*[@id="email"]')
    BUY_BUTTON = (By.XPATH, '//*[@id="submit-button"]')
    SELECT_INPUT = (By.XPATH, '//*[@id="billingAddress.state"]')
    PAID_CONFIRMED = (By.XPATH, '//*[@id="root"]/div/main/div/div/div[1]/div/div[2]/div/text()[1]')
    ORDER_ID = (By.XPATH, '//*[@id="root"]/div/main/div/h1/text()[2]')

    def get_product_page(self):
        product = self.wait_condition.until(EC.element_to_be_clickable(self.PRODUCT))
        product.click()
        return True

    def get_product_for_cart(self):
        product = self.wait_condition.until(EC.element_to_be_clickable(self.PRODUCT_TO_CART))
        product.click()
        return True

    def add_product_to_cart(self):
        add_product = self.wait_condition.until(EC.element_to_be_clickable(self.ADD_TO_CART_BTN))
        add_product.click()
        return True

    def proceed_to_checkout(self):
        checkout = self.wait_condition.until(EC.element_to_be_clickable(self.CHEK_OUT_BTN))
        checkout.click()
        WebDriverWait(self.browser_driver, 3).until(EC.visibility_of_element_located(self.SHIPPING_TITLE))
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

    def scroll_down2(self):
        cm_to_inches = 5 / 2.54
        dpi = 100
        scroll_distance_inches = cm_to_inches
        scroll_distance_pixels = int(scroll_distance_inches * dpi)
        self.browser_driver.execute_script(f"window.scrollBy(0, {scroll_distance_pixels});")

    def add_shipping_address(self, address, city, postal_code, country):
        self.scroll_down()
        address_input = self.wait_condition.until(EC.element_to_be_clickable(self.ADDRESS_INPUT))
        address_input.click()
        address_input.send_keys(address)
        city_input = self.wait_condition.until(EC.element_to_be_clickable(self.CITY_INPUT))
        city_input.click()
        city_input.send_keys(city)
        postal_code_input = self.wait_condition.until(EC.element_to_be_clickable(self.POSTAL_CODE_INPUT))
        postal_code_input.click()
        postal_code_input.send_keys(postal_code)
        country_input = self.wait_condition.until(EC.element_to_be_clickable(self.COUNTRY_INPUT))
        country_input.click()
        country_input.send_keys(country)
        continue_btn = self.wait_condition.until(EC.element_to_be_clickable(self.CONTINUE_BTN))
        continue_btn.click()
        WebDriverWait(self.browser_driver, 3).until(EC.visibility_of_element_located(self.PAYMENT_METHOD))
        return True

    def send_key_to_input(self, key, xpath):
        el = WebDriverWait(self.browser_driver, 10).until(
            EC.visibility_of_element_located(xpath))
        el.click()
        el.send_keys(key)

    def fill_payment_details(self, visa_number, cvv, postal_code, expires_date, name, street_address, city, mobile,
                             mail, country):
        self.scroll_down()
        ifram_element = WebDriverWait(self.browser_driver, 10).until(
            EC.visibility_of_element_located(self.IFRAM_1))
        self.browser_driver.switch_to.frame(ifram_element)
        el = WebDriverWait(self.browser_driver, 10).until(
            EC.visibility_of_element_located(self.BUTTONS_CONTAINER))
        el.click()
        method_btn = self.wait_condition.until(EC.visibility_of_element_located(self.PAY_VIA_VISA_BTN))
        method_btn.click()
        ifram_element2 = WebDriverWait(self.browser_driver, 10).until(
            EC.visibility_of_element_located(self.IFRAM_2))
        self.browser_driver.switch_to.frame(ifram_element2)

        self.send_key_to_input(visa_number, self.VISA_INPUT)
        try:
            self.send_key_to_input(cvv, self.CVV)
        except:
            self.send_key_to_input(cvv, self.CVV)
        try:
            self.send_key_to_input(expires_date, self.EX_DATE)
        except:
            self.send_key_to_input(expires_date, self.EX_DATE)
        try:
            self.send_key_to_input(name, self.FIRST_NAME)
        except:
            try:
                self.send_key_to_input(name, self.FIRST_NAME)
            except:
                self.send_key_to_input(name, self.FIRST_NAME)
        try:
            self.send_key_to_input(name, self.LAST_NAME)
        except:
            self.send_key_to_input(name, self.LAST_NAME)
        try:
            self.send_key_to_input(street_address, self.ADDRESS_LINE)
        except:
            self.send_key_to_input(street_address, self.ADDRESS_LINE)
        try:
            self.send_key_to_input(city, self.CITY_LINE)
        except:
            self.send_key_to_input(city, self.CITY_LINE)
        try:
            select_element = WebDriverWait(self.browser_driver, 2).until(
                EC.visibility_of_element_located((self.SELECT_INPUT)))
            select = Select(select_element)
            select.select_by_visible_text(country)
        except:
            select_element = WebDriverWait(self.browser_driver, 2).until(
                EC.visibility_of_element_located(self.SELECT_INPUT))
            select = Select(select_element)
            select.select_by_visible_text(country)
        try:
            self.send_key_to_input(postal_code, self.POSTAL_CODE)
        except:
            self.send_key_to_input(postal_code, self.POSTAL_CODE)
        try:
            self.send_key_to_input(mobile, self.MOBILE_NUM)
        except:
            self.send_key_to_input(mobile, self.MOBILE_NUM)
        try:
            self.send_key_to_input(mail, self.MAIL_INPUT)
        except:
            self.send_key_to_input(mail, self.MAIL_INPUT)
        try:
            buy_button = WebDriverWait(self.browser_driver, 2).until(
                EC.visibility_of_element_located(self.BUY_BUTTON))
            buy_button.click()
        except:
            buy_button = WebDriverWait(self.browser_driver, 2).until(
                EC.visibility_of_element_located(self.BUY_BUTTON))
            buy_button.click()

        self.browser_driver.switch_to.default_content()

        return True

    def place_order(self):
        method_btn = self.wait_condition.until(EC.element_to_be_clickable(self.PAYMENT_METHOD_BTN))
        method_btn.click()
        self.scroll_down()
        place_order_btn = self.wait_condition.until(EC.element_to_be_clickable(self.PLACE_ORDER_BTN))
        place_order_btn.click()

        return True
