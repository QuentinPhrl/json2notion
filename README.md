## About Notionput

Notion put is a generic script that allows to insert data from a json file in a Notion database. The interest of this script is that during the update of the data the information in the database is simply updated on the page which allows to keep the already existing backlink to other Notion page

## API Key(Token)

- Before getting started, create [an integration and find the token](https://www.notion.so/my-integrations). → [Learn more about authorization](https://developers.notion.com/docs/authorization).

- Then save your api key(token) as your os environment variable

```Bash
$ export NOTION_TOKEN_PUT_EXPERIMENT="{your integration token key}"
```

## Usage: Shell Command

- Notionput requires `db_id` of the Notion database
- Notionput requires `json_file` formatted as in the example below
```Json
{
    "entries": [{
        "_id": "tweetid1",
        "type": "Twitter",
        "fields": {
            "message": "blah blah",
            "author": "Elon",
            "location": "paris"
        },
        "body": {
            "type": "embed",
            "content": "<tweet_url>"
        }
    }]
}
```
- The keys between the braces of `fields` can be modified but the same name must be assigned to the column in the database
- Example of use of the script : 

```Bash
    python3 main.py -d d08f397181941f990c7ed767a653 -f data.json
```

## Restrictions
- If you want to increase the number of input data, you must first delete the elements in the database from the same source.





