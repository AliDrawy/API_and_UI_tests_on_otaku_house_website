from infra.ui_infra.browser_wrapper import WebBrowser
class WebPageBase:

    def __init__(self, browser, wait_condition):
        self.browser_driver = browser
        self.wait_condition = wait_condition
        # self.web_browser = WebBrowser()

    def retrieve_page_title(self):
        return self.browser_driver.title
