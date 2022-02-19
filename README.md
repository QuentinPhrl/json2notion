# notionput
Various scripts to edit a Notion based on external sources


## Progress of the script :

- [x] Retrieve tweets of a user with his id
- [x] Saves tweets in columns on the dashboard notion
- [x] Automatically retrieve the user's name from the notion dashboard
- [x] Taking into account the number of columns in the page Notion in a dynamic way
- [ ] Reverse the order of tweets on the notion dashboard (Newest first)
- [ ] Other suggestions

## How to use this script : 

Create a developer twitter account and get this "BEARER_TOKEN".
Add this token as environment variable "NOTION_BEARER_TOKEN"
Create an integration in notion and get the token, don't forget to share the document with the integration.
Add this token as environment variable "NOTION_TOKEN_PUT"

Add the id of the notion page in the main_page_id variable

Finally, write in the "Usernames" table the @ of the users whose tweets you want to retrieve

### Exemple after execution : 

![Notion page with some tweets](Exemple.png)





