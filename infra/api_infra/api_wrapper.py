import requests
import json
from os.path import dirname, join
from jira import JIRA
import os
import random
from dotenv import load_dotenv
load_dotenv("../../.env")

class OtakuHouseAPI:
    def __init__(self):
        self.response = None
        self.url = self.read_config_data("api_config.json")['url']
        self.jira_api = os.getenv("JIRA_API")
        self.jira_url = self.read_config_data("api_config.json")['jira_url']
        self.jira_mail = self.read_config_data("api_config.json")['mail']
        self.user_name = self.read_config_data("api_config.json")['user_name']
        self.user_mail = self.read_config_data("api_config.json")['login_mail']
        self.user_password = self.read_config_data("api_config.json")['login_password']
        self.new_user_mail = self.read_config_data("api_config.json")['invalid_login_mail']
        self.invalid_user_password = self.read_config_data("api_config.json")['invalid_login_password']
        self.searching_keyword = self.read_config_data("api_config.json")['keyword_for_search'].lower()
        self.product_id = self.read_config_data("api_config.json")['product_id']
        self.token = os.getenv("TOKEN")
        self.rating = self.read_config_data("api_config.json")['rating_product']
        self.review_txt = self.read_config_data("api_config.json")['review_text']
        self.order_id = self.read_config_data("api_config.json")['order_id']
        self.user_id = self.read_config_data("api_config.json")['user_id']
        self.headers = {"Authorization": self.token}
        self.request = requests
        self.parallel = True
        self.auth_jira = JIRA(basic_auth=(self.jira_mail, self.jira_api), options={'server': self.jira_url})

    def api_get_request(self, url):
        self.response = self.request.get(url)
        return self.response

    def read_config_data(self, file):
        here = dirname(__file__)
        filename = join(here, file)
        with open(filename, 'r') as file:
            config = json.load(file)
            return config

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
