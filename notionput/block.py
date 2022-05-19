from notionput.request_notion import Request

class Block:
    def __init__(self, integrations_token):
        """
        init
        :param integrations_token: Notion Internal Integration Token
        """
        self.url = 'https://api.notion.com/v1/blocks'
        self.result = {}
        self.request = Request(self.url, integrations_token=integrations_token)
    
    def retrieve_blocks(self,page_id):

        self.result = self.request.call_api_get(self.url + "/" + page_id + "/children")

    def update_block(self,block_id,children):

        self.result = self.request.call_api_patch(self.url + "/" + block_id, body=children[0])
    