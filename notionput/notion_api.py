import os

from notionput.console import print_error

class GetToken:
    def __init__(self):
        self.token = self._get_env_variable()

    def _get_env_variable(self):
        try:
            return os.environ["NOTION_TOKEN"]
        except:
            print_error("Notion Integration Token is not found")
            print(
            """
                Welcome to notionput!

                To get started, you need to save your Notion Integration Token.
                Find your token at
                    https://www.notion.so/my-integrations
                Then run shell command:
                    $export NOTION_TOKEN="<Your Token>"
                
                If you want to save this environment variable after reboot,
                put upper command in your shell resource(ex: .bashrc or .zshrc)
            """
            )
            exit(1)