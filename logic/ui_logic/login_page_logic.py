from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from infra.ui_infra.page_base import WebPageBase
from selenium.common.exceptions import TimeoutException


class LoginPage(WebPageBase):
    EMAIL_INPUT = (By.XPATH, '//*[@id="email"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="password"]')
    SIGN_IN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/button')
    REGISTER_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/div/a')

    def login_by_valid_mail_and_password(self, mail, password):
        full_screen_btn = self.wait_condition.until(EC.element_to_be_clickable(self.EMAIL_INPUT))
        full_screen_btn.click()
        full_screen_btn.send_keys(mail)
        full_screen_btn = self.wait_condition.until(EC.element_to_be_clickable(self.PASSWORD_INPUT))
        full_screen_btn.click()
        full_screen_btn.send_keys(password)
        full_screen_btn = self.wait_condition.until(EC.element_to_be_clickable(self.SIGN_IN_BUTTON))
        full_screen_btn.click()
        return True

