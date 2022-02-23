from turtle import color
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

def main():

    tweet_ids_by_user = []

    agg_Col = aggColumnUsername()
    ColumnIDs = agg_Col[0]
    Usernames = agg_Col[1]
    
    for username in Usernames:
        tweet_ids_by_user.append(getTweet(username))
    
    for index,tweet_ids_list in enumerate(tweet_ids_by_user):
        for tweet in tweet_ids_list:
            Code = appendEmbed(tweet,Usernames[index],ColumnIDs[index])
            print(Code)

#Calling all the blocks of the page via the page id  
"""
def apiCall():

    colomun_list_id = "314ce5cb-6882-49e0-8034-6d04ea360edb"

    url_block_page = f"https://api.notion.com/v1/blocks/{colomun_list_id}/children"

    response = requests.request("GET", url_block_page, headers=headers)

    return json.loads(response.text)
"""
#Updates the link of the tweet in the block "embed" via its id (block_id)
'''
def updateEmbed():
    
    updateData = {
        "embed":{
             "url":"https://twitter.com/NotionAPI/status/1430576039650942976?s=20&t=R92L0tBPzRXD42TS-Yyalw"
          }
    }

    return requests.request("PATCH", url, json=updateData, headers=headers)
'''
#Create a new "embed" block that contains the link to the tweet

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

#Function that retrieves the id of the blocks that contain a tweet and deletes them 
def deleteEmbed(columns_id):

    
    embed_blocks_id = []
        # Get the id of the 'embed' blocks that contain a twitter link 
    for column_id in columns_id:
        url_block_column = f"https://api.notion.com/v1/blocks/{column_id}/children"
        blocks = json.loads(requests.request("GET", url_block_column, headers=headers).text)

        for block in blocks["results"]:
                # If the type of the block is "embed" and the url it contains starts with 'https://twitter.com/' then we copy its id
            if block["type"] == "embed" and block["embed"]["url"].startswith('https://twitter.com/'):
                embed_blocks_id.append(block["id"])

    for embed_block_id in embed_blocks_id:

        url_block_embed = f"https://api.notion.com/v1/blocks/{embed_block_id}"

        requests.request("DELETE", url_block_embed, headers=headers)
    
#Function that checks if the column title is heading 1 and if the twitter username exists
#if this is not the case the id of the column is not kept.  

def aggColumnUsername():

    agg_return = [[],[]]

    ColumnIDs = getColumnIDs()
    deleteEmbed(ColumnIDs)
    Usernames = getUsernames(ColumnIDs)

    for index,username in enumerate(Usernames):

        if username != "%wrong_type%" and checkTwitterUsername(username) == "user_exists":
            agg_return[0].append(ColumnIDs[index])
            agg_return[1].append(Usernames[index])

    return agg_return
        
# Function which retrieves the columns id of the Notion page

def getColumnIDs():

    column_id_return = []
        #We get the id of the block "column_list" which is a child of the id of the page
    url_block_page_main = f"https://api.notion.com/v1/blocks/{main_page_id}/children"

    block_column_list_id = json.loads(requests.request("GET", url_block_page_main, headers=headers).text)
    block_column_list_id = block_column_list_id["results"][0]["id"]
         #Then we get the id of the x columns of the page
    url_block_page_column = f"https://api.notion.com/v1/blocks/{block_column_list_id}/children"

    columns_id = json.loads(requests.request("GET", url_block_page_column, headers=headers).text)

    for column_id in columns_id["results"]:
        column_id_return.append(column_id["id"])

    return column_id_return

# Function that retrieves the username in the column title (heading_1) of the Notion page 
def getUsernames(columns_id):

    username_return = []
    
    for column_id in columns_id:
        url_block_column = f"https://api.notion.com/v1/blocks/{column_id}/children"
        usernames = json.loads(requests.request("GET", url_block_column, headers=headers).text)
            #If the type field of the first element of the column is a "heading_1" then we retrieve its content and add it to the table in return
        if usernames["results"][0]["type"] == "heading_1":
            username_return.append(usernames["results"][0]["heading_1"]["text"][0]["text"]["content"])
            #Otherwise we add the string "%wrong_type%" in the return array.
        else:
            username_return.append("%wrong_type%")
    return username_return

# Function that checks if a Twitter user exists 

def checkTwitterUsername(username): 

    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    if not (client.get_user(username=username)).errors:
        return 'user_exists'
    else: 
        print(client.get_user(username=username).errors[0]['detail'])
        return 'User does not exist'

#function that retrieves the id of a user's tweets  
def getTweet(username):

    ids = []

    client = tweepy.Client(bearer_token=BEARER_TOKEN)

        #We get the user's Twitter id

    UserID = (client.get_user(username=username)).data.id

        #We display his last 5 tweets
    tweets = client.get_users_tweets(id=UserID, max_results=5)
    for tweet in tweets.data:
        ids.append(tweet.id)

    return ids

if __name__ == '__main__':
    main()