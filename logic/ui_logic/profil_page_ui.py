from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from infra.ui_infra.page_base import WebPageBase


class ProfilePage(WebPageBase):
    USER_BTN = (By.XPATH, '//*[@id="username"]')
    PROFILE_BTN = (By.XPATH, '//*[@id="navbarScroll"]/div/div/div/a[1]')
    USER_PROFILE_TITLE = (By.XPATH, '//*[@id="root"]/div/main/div/div[1]/h2')
    NAME_INPUT = (By.XPATH, '//*[@id="name"]')
    MAIL_INPUT = (By.XPATH, '//*[@id="email"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="password"]')
    CONFIRM_PASSWORD_INPUT = (By.XPATH, '// *[ @ id = "passwordConfirm"]')
    UPDATE_BTN = (By.XPATH, '//*[@id="root"]/div/main/div/div[1]/form/button')
    OTAKU_HOUSE_TITLE = (By.XPATH, '//*[@id="root"]/header/nav/div/a')

    def navigate_to_profile_page(self):
        user_btn = self.wait_condition.until(EC.element_to_be_clickable(self.USER_BTN))
        user_btn.click()
        profile_btn = self.wait_condition.until(EC.element_to_be_clickable(self.PROFILE_BTN))
        profile_btn.click()
        WebDriverWait(self.browser_driver, 10).until(EC.visibility_of_element_located(self.USER_PROFILE_TITLE))
        return True

    def scroll_up(self):
        cm_to_inches = 5 / 2.54
        dpi = 100
        scroll_distance_inches = cm_to_inches
        scroll_distance_pixels = int(scroll_distance_inches * dpi)
        self.browser_driver.execute_script(f"window.scrollBy(0, -{scroll_distance_pixels});")

    def scroll_down(self):
        cm_to_inches = 5 / 2.54
        dpi = 100
        scroll_distance_inches = cm_to_inches
        scroll_distance_pixels = int(scroll_distance_inches * dpi)
        self.browser_driver.execute_script(f"window.scrollBy(0, {scroll_distance_pixels});")

    def update_profile_page(self, user_name, mail, password):
        name_input = self.wait_condition.until(EC.element_to_be_clickable(self.NAME_INPUT))
        name_input.clear()
        name_input.send_keys(user_name)
        mail_input = self.wait_condition.until(EC.element_to_be_clickable(self.MAIL_INPUT))
        mail_input.clear()
        mail_input.send_keys(mail)
        password_input = self.wait_condition.until(EC.element_to_be_clickable(self.PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(password)
        conf_password_input = self.wait_condition.until(EC.element_to_be_clickable(self.CONFIRM_PASSWORD_INPUT))
        conf_password_input.clear()
        conf_password_input.send_keys(password)
        self.scroll_down()
        update_btn = self.wait_condition.until(EC.element_to_be_clickable(self.UPDATE_BTN))
        update_btn.click()
        self.scroll_up()
        otaku_house_nav = self.wait_condition.until(EC.element_to_be_clickable(self.OTAKU_HOUSE_TITLE))
        otaku_house_nav.click()
        user_name = WebDriverWait(self.browser_driver, 5).until(EC.visibility_of_element_located(self.USER_BTN)).text
        return user_name.lower()
