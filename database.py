from request_notion import Request

class Database:
    def __init__(self, integrations_token):
        """
        init
        :param integrations_token: Notion Internal Integration Token
        """
        self.properties_list = []
        self.url = 'https://api.notion.com/v1/databases'
        self.result = {}
        self.request = Request(self.url, integrations_token=integrations_token)
    

    def retrieve_database(self, database_id, fields_key):
        """
        Retrieve a database
        :param database_id: Identifier for a Notion database
        :param get_properties: Get properties_list trigger
        :return:
        """

        self.result = self.request.call_api_get(self.url + "/" + database_id)

        for field_key in fields_key:
            self.properties_list.append(self.result["properties"][field_key]["type"])


    