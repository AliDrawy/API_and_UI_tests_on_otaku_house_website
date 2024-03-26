from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import requests
import os
import json
from os.path import dirname, join
from jira import JIRA
import random
from dotenv import load_dotenv

load_dotenv("../.env")


class WebBrowser:
    def __init__(self):
        self.timeout = None
        self.web_driver = None
        self.parallel = True
        self.serial = False
        self.url = self.read_config_data("ui_config.json")['url']
        self.jira_api = os.getenv("JIRA_API")
        self.jira_url = self.read_config_data("ui_config.json")['jira_url']
        self.jira_mail = os.getenv("MAIL")
        self.auth_jira = JIRA(basic_auth=(self.jira_mail, self.jira_api), options={'server': self.jira_url})
        self.user_name = self.read_config_data("ui_config.json")['user_name']
        self.new_user_name = self.read_config_data("ui_config.json")['new_user_name']
        self.user_mail = self.read_config_data("ui_config.json")['login_mail']
        self.user_password = self.read_config_data("ui_config.json")['login_password']
        self.invalid_mail = self.read_config_data("ui_config.json")['invalid_login_mail']
        self.invalid_user_password = self.read_config_data("ui_config.json")['invalid_login_password']
        self.register_mail = self.read_config_data("ui_config.json")['register_mail']
        self.keyword = self.read_config_data("ui_config.json")['keyword_for_search']
        self.keyword_for_cart = self.read_config_data("ui_config.json")['keyword_for_cart']
        self.city = self.read_config_data("ui_config.json")['city']
        self.visa = self.read_config_data("ui_config.json")['visa']
        self.cvv = self.read_config_data("ui_config.json")['cvv']
        self.phone = self.read_config_data("ui_config.json")['phone']
        self.country = self.read_config_data("ui_config.json")['country']
        self.postal_code = self.read_config_data("ui_config.json")['postal_code']
        self.address = self.read_config_data("ui_config.json")['address']
        self.ex_date = self.read_config_data("ui_config.json")['ex_date']

    def read_config_data(self, file):
        here = dirname(__file__)
        filename = join(here, file)
        with open(filename, 'r') as file:
            config = json.load(file)
            return config

    def launch_browser(self, browser):
        self.web_driver = self.get_driver(browser)
        self.open_website(f'{self.url}login')
        self.web_driver.maximize_window()#move to infra
        return self.web_driver

    def wait(self, timeout=50):
        self.timeout = timeout
        return WebDriverWait(self.web_driver, self.timeout)

    def open_website(self, website_url):
        self.web_driver.get(website_url)

    def login_page(self):
        self.open_website(f'{self.url}login')

    # def open_video(self):
    #     self.open_website(self.url)

    def terminate_browser(self):
        if self.web_driver:
            self.web_driver.quit()

    def get_driver(self, browser):
        browser_type = browser
        if self.parallel:
            options = self.set_up_capabilities(browser_type)
            self.web_driver = webdriver.Remote(command_executor="http://192.168.217.1:4444", options=options)
        else:
            if browser.lower() == 'chrome':
                self.web_driver = webdriver.Chrome()
            elif browser.lower() == 'firefox':
                self.web_driver = webdriver.Firefox()
            elif browser.lower() == 'edge':
                self.web_driver = webdriver.Edge()
        self.open_website(f'{self.url}login')

        return self.web_driver

    def set_up_capabilities(self, browser_type):
        options = ''
        if browser_type.lower() == 'chrome':
            options = webdriver.ChromeOptions()
        elif browser_type.lower() == 'firefox':
            options = webdriver.FirefoxOptions()
        elif browser_type.lower() == 'edge':
            options = webdriver.EdgeOptions()
        # options.add_argument("--headless")
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f'--platformName=windows')
        return options

    def get_browsers(self):
        return ["chrome", "edge"]

    def create_issue(self, summery, description, project_key, issue_type="Bug"):
        issue_dict = {
            'project': {'key': project_key},
            'summary': f'failed test: {summery}',
            'description': description,
            'issuetype': {'name': issue_type},
        }
        new_issue = self.auth_jira.create_issue(fields=issue_dict)
        return new_issue.key

    def choose_random_value(self, list_value):
        if not list_value:
            return None
        return random.choice(list_value)
    # def is_grid(self):
    #     return ["chrome", "edge"]

    # def get_browser(self):
    #     return "chrome"
