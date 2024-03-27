import unittest
from infra.ui_infra.browser_wrapper import WebBrowser
from logic.ui_logic.login_page_logic_ui import LoginPage
from logic.ui_logic.profil_page_ui import ProfilePage


class APIAndUI(unittest.TestCase):
    def setUp(self):
        self.navigator = WebBrowser()
        self.browser_driver = self.navigator.launch_browser("chrome")
        self.wait_tool = self.navigator.wait()
        self.LoginPage = LoginPage(self.browser_driver, self.wait_tool)
        self.LoginPage.login_via_valid_mail_and_password(self.navigator.user_mail,
                                                         self.navigator.user_password)
        self.result = None
        self.ProfilePage = ProfilePage(self.browser_driver, self.wait_tool)
        self.error_msg = None

    def test_update_profile_page(self):
        self.result = self.ProfilePage.navigate_to_profile_page()
        self.result = self.ProfilePage.update_profile_page(self.navigator.new_user_name,
                                                           self.navigator.register_mail,
                                                           self.navigator.user_password)
        self.error_msg = "the profile details not updated successfully"
        self.assertEqual(self.result, self.navigator.new_user_name, self.error_msg)

    def tearDown(self):
        if self.result != self.navigator.new_user_name:
            print(self.navigator.create_issue("Test update profile page via UI",
                                              self.error_msg, 'EP'))

        self.navigator.terminate_browser()
