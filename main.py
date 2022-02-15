import requests
import json
import os

token = os.environ["NOTION_TOKEN_PUT"]

block_id = 'e42cdf2c-ef06-4059-b88c-2b159415c902'
block_page_id = 'fa2142e7178a4af980ef0bc2bcde14ec'

url_block_page = f"https://api.notion.com/v1/blocks/{block_page_id}/children"
url = f"https://api.notion.com/v1/blocks/{block_id}"

headers = {
    "Accept": "application/json",
    "Notion-Version": "2021-08-16",
    "Content-Type": "application/json",
    "Authorization": "Bearer " + token
}


def main():

    #print(updateEmbed())
    
    print(appendEmbed())
    
# Appel de l'ensemble des blocks de la page via l'id de page    

def apiCall():

    response = requests.request("GET", url_block_page, headers=headers)

    return json.loads(response.text)

#Met à jour le lien du tweet dans le block "embed" via son id (block_id)

def updateEmbed():
    
    updateData = {
        "embed":{
             "url":"https://twitter.com/NotionAPI/status/1430576039650942976?s=20&t=R92L0tBPzRXD42TS-Yyalw"
          }
    }

    return requests.request("PATCH", url, json=updateData, headers=headers)

#Créer un nouveau block "embed" qui contient le lien vers le tweet

def appendEmbed():

    appData = [{
            "object": "block",
            "type": "embed",
            "embed": {
                "url": "https://twitter.com/ZeratoR/status/1493276555052826624?s=20&t=UFnSjZGiFRcZQ9lHUv0JtA"
            }
        }
    ]
    
    return requests.request("PATCH", url_block_page, json={"children": appData}, headers=headers)


if __name__ == '__main__':
    main()