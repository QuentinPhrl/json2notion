import json

import requests

from json2notion.__init__ import NOTION_VERSION
from json2notion.console import print_error

class Request:
    def __init__(self, url, integrations_token):
        """
        init
        :param url: Notion API URL
        :param integrations_token: Notion Internal Integration Token
        """
        self.NOTION_KEY = integrations_token
        self.HEADER = {"Authorization": f"Bearer {self.NOTION_KEY}",
                       "Content-Type": "application/json",
                       "Notion-Version": NOTION_VERSION}
        self.url = url

    def call_api_post(self, url, body):
        """
        request post
        :param url:
        :param body:
        :return:
        """
        r = requests.post(url, data=json.dumps(body), headers=self.HEADER).json()
        
        if r["object"] == "error":
            print_error(f'Notion API : {r["message"]}')
            exit(1)
        else:
            return r

    def call_api_get(self, url):
        """
        request get
        :param url:
        :return:
        """
        r = requests.get(url, headers=self.HEADER).json()

        if r["object"] == "error":
            print_error(f'Notion API : {r["message"]}')
            exit(1)
        else:
            return r

    def call_api_patch(self, url, body):
        """
        request patch
        :param url:
        :param body:
        :return:
        """
        r = requests.patch(url, data=json.dumps(body), headers=self.HEADER).json()
        
        if r["object"] == "error":
            print_error(f'Notion API : {r["message"]}')
            exit(1)
        else:
            return r