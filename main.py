import requests
import tweepy
import json
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

Usernames = ['NotionAPI','berty','DFintelligence','moul']


def main():

    tweet_ids_by_user = []

    ColumnIDs = getColumnIDs()

    for username in Usernames:
        tweet_ids_by_user.append(getTweet(username))
    
    for index,tweet_ids_list in enumerate(tweet_ids_by_user):
        for tweet in tweet_ids_list:
            appendEmbed(tweet,Usernames[index],ColumnIDs[index])
            
"""
# Appel de l'ensemble des blocks de la page via l'id de page    

def apiCall():

    response = requests.request("GET", url_block_page, headers=headers)

    return json.loads(response.text)
"""
#Met à jour le lien du tweet dans le block "embed" via son id (block_id)
'''
def updateEmbed():
    
    updateData = {
        "embed":{
             "url":"https://twitter.com/NotionAPI/status/1430576039650942976?s=20&t=R92L0tBPzRXD42TS-Yyalw"
          }
    }

    return requests.request("PATCH", url, json=updateData, headers=headers)
'''
#Créer un nouveau block "embed" qui contient le lien vers le tweet

def appendEmbed(tweet_ids,username,column_id):

    url_block_column = f"https://api.notion.com/v1/blocks/{column_id}/children"

    appData = [{
            "object": "block",
            "type": "embed",
            "embed": {
                "url": f"https://twitter.com/{username}/status/{tweet_ids}"
            }
        }
    ]

    ReturnCode = requests.request("PATCH", url_block_column, json={"children": appData}, headers=headers)
        
    return ReturnCode


def getColumnIDs():

    column_id_return = []
        #On récupére l'id du block "column_list" qui est un enfant de l'id de la page
    url_block_page_main = f"https://api.notion.com/v1/blocks/{main_page_id}/children"

    block_column_list_id = json.loads(requests.request("GET", url_block_page_main, headers=headers).text)
    block_column_list_id = block_column_list_id["results"][0]["id"]
        #Puis on récupére l'id des x colonnes de la page
    url_block_page_column = f"https://api.notion.com/v1/blocks/{block_column_list_id}/children"

    columns_id = json.loads(requests.request("GET", url_block_page_column, headers=headers).text)

    for column_id in columns_id["results"]:
        column_id_return.append(column_id["id"])

    return column_id_return


def getTweet(username):

    ids = []

    client = tweepy.Client(bearer_token=BEARER_TOKEN)

        #On récupére l'id Twitter de l'utilisateur
    UserID = (client.get_user(username=username)).data.id

        #On affiche ses 5 derniers tweets
    tweets = client.get_users_tweets(id=UserID, max_results=5)
    for tweet in tweets.data:
        ids.append(tweet.id)

    return ids

if __name__ == '__main__':
    main()