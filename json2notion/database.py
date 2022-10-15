from json2notion.request_notion import Request
from json2notion.console import print_error

class Database:
    def __init__(self, integrations_token):
        """
        init
        :param integrations_token: Notion Internal Integration Token
        """
        self.type_list = []
        self.url = 'https://api.notion.com/v1/databases'
        self.result = {}
        self.request = Request(self.url, integrations_token=integrations_token)
    
    def retrive_column_type (self, database_id, fields_key):
        """
        Get properties 
        :param database_id: Identifier for a Notion database
        :param fields_key: List of column names to identify their type 
        :return:
        """
        type_list = []

        self.result = self.request.call_api_get(self.url + "/" + database_id)
        try:
            for field_key in fields_key:
                type_list.append(self.result["properties"][field_key]["type"])

            self.type_list=type_list

        except KeyError as missing:
            print_error(f"Column name {missing} not found in the Notion page")
            exit(1)

    def query_database_filter(self, database_id, column_name, content):

        self.retrive_column_type(database_id,[column_name])

        body = {
            "filter": {
                "property": column_name,
                self.type_list[0]: {"equals": content}
            }
        }

        self.result = self.request.call_api_post(self.url + "/" + database_id + "/query", body)
