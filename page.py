
from properties import Properties
from request_notion import Request


class Page:
    def __init__(self, integrations_token):
        """
        init
        :param integrations_token: Notion Internal Integration Token
        """
        self.url = 'https://api.notion.com/v1/pages'
        self.result = {}
        self.request = Request(self.url, integrations_token=integrations_token)

    def create_page(self, database_id, properties=None):
        """
        Create a page
        :param database_id: Identifier for a Notion database
        :param properties: Property values of this page
        :param children: Page content for the new page
        :return:
        """
        if properties is None:
            properties = Properties()
        properties = properties

        body = {
            "parent": {
                "database_id": database_id
            },
            "properties": properties.result,
        }
        self.result = self.request.call_api_post(self.url, body)