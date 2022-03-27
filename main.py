import os

token = os.environ["NOTION_TOKEN_PUT"]
BEARER_TOKEN = os.environ["NOTION_BEARER_TOKEN"]

main_page_id = 'fa2142e7178a4af980ef0bc2bcde14ec'

headers = {
    "Accept": "application/json",
    "Notion-Version": "2021-08-16",
    "Content-Type": "application/json",
    "Authorization": "Bearer " + token
}

def main():
    print("main")

if __name__ == '__main__':
    main()