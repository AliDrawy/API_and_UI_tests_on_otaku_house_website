from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from infra.ui_infra.page_base import WebPageBase
from selenium.common.exceptions import TimeoutException


class LoginPage(WebPageBase):
    EMAIL_INPUT = (By.XPATH, '//*[@id="email"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="password"]')
    SIGN_IN_BUTTON = (By.XPATH, '//button[text()="Sign In"]')
    REGISTER_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/div/a')#fix path of all loctor
    PRODUCTS_LIST_TITLE = (By.XPATH, '//*[@id="root"]/div/main/div/h1')
    REGISTER_TITLE = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/h1')
    NEW_NAME = (By.XPATH, '//*[@id="name"]')
    CONFIRM_PASSWORD = (By.XPATH, '// *[ @ id = "passwordConfirm"]')
    REGISTER = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/button')

    def click_on_mail_btn(self,mail):
        mail_btn = self.wait_condition.until(EC.element_to_be_clickable(self.EMAIL_INPUT))
        mail_btn.click()
        mail_btn.send_keys(mail)

    def login_via_valid_mail_and_password(self, mail, password):
        self.click_on_mail_btn(mail)
        password_btn = self.wait_condition.until(EC.element_to_be_clickable(self.PASSWORD_INPUT))
        password_btn.click()
        password_btn.send_keys(password)
        sign_in = self.wait_condition.until(EC.element_to_be_clickable(self.SIGN_IN_BUTTON))
        sign_in.click()
        try:# do it in other function
            WebDriverWait(self.browser_driver, 2).until(EC.visibility_of_element_located(self.PRODUCTS_LIST_TITLE))
            return True
        except:
            return False

    def register_via_mail_and_password(self, name, mail, password):
        register_btn = self.wait_condition.until(EC.element_to_be_clickable(self.REGISTER_BUTTON))
        register_btn.click()
        WebDriverWait(self.browser_driver, 5).until(EC.visibility_of_element_located(self.REGISTER_TITLE))
        name_input = self.wait_condition.until(EC.element_to_be_clickable(self.NEW_NAME))
        name_input.send_keys(name)
        mail_input = self.wait_condition.until(EC.element_to_be_clickable(self.EMAIL_INPUT))
        mail_input.send_keys(mail)
        password_input = self.wait_condition.until(EC.element_to_be_clickable(self.PASSWORD_INPUT))
        password_input.send_keys(password)
        conf_password_input = self.wait_condition.until(EC.element_to_be_clickable(self.CONFIRM_PASSWORD))
        conf_password_input.send_keys(password)

        cm_to_inches = 4 / 2.54
        dpi = 100
        scroll_distance_inches = cm_to_inches
        scroll_distance_pixels = int(scroll_distance_inches * dpi)
        self.browser_driver.execute_script(f"window.scrollBy(0, {scroll_distance_pixels});")
        register_btn = self.wait_condition.until(EC.element_to_be_clickable(self.REGISTER))
        WebDriverWait(self.browser_driver, 5).until(EC.visibility_of_element_located(self.REGISTER))
        register_btn.click()
        try:
            WebDriverWait(self.browser_driver, 2).until(EC.visibility_of_element_located(self.PRODUCTS_LIST_TITLE))
            return True
        except:
            return False

