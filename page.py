
from sre_constants import CH_LOCALE
from children import Children
from properties import Properties
from request_notion import Request
from block import Block


class Page:
    def __init__(self, integrations_token):
        """
        init
        :param integrations_token: Notion Internal Integration Token
        """
        self.url = 'https://api.notion.com/v1/pages'
        self.result = {}
        self.request = Request(self.url, integrations_token=integrations_token)
        self.block =  Block(integrations_token=integrations_token)

    def create_page(self, database_id, properties=None, children=None):
        """
        Create a page
        :param database_id: Identifier for a Notion database
        :param properties: Property values of this page
        :return:
        """
        if children is None:
            children = Children()
        if properties is None:
            properties = Properties()
            
        children = children
        properties = properties

        body = {
            "parent": {
                "database_id": database_id
            },
            "properties": properties.result,
            "children": children.result
        }
        self.result = self.request.call_api_post(self.url, body)
    
    def update_page(self, page_id, properties=None,children=None):
        """
        Update page parameter
        :param page_id: Identifier for a Notion page
        :param properties: Property values to update for this page
        :return:
        """
        if properties is None:
            properties = Properties()

        body = {
            "properties": properties.result,
        }
        self.result = self.request.call_api_patch(self.url + "/" + page_id, body)
        
        if children is not None:
            self.update_page_content(page_id,children=children)

    def update_page_content(self,page_id,children):
        """
        Updates the block that corresponds to the data type in the children variable
        :param page_id: Identifier for a Notion page
        :param children: Value to update 
        :return:
        """
        
        self.block.retrieve_blocks(page_id=page_id)
        
        for block_unit in self.block.result["results"]:

            if block_unit["type"] == children.result[0]["type"]:
                self.block.update_block(block_id=block_unit["id"],children=children.result)
        



