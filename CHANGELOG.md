# Change log

## v1.2

** New Features **
- Recovering twitter usernames from column titles
- Protection against errors caused by a Twitter username that does not exist and against column titles of the wrong type

** Changed **
- Update of the 'README.md' file 

** Feature Change **
- Taking into account the number of columns in the page Notion in a dynamic way

** Added: **
- Added "checkTwitterUsername" function that checks if a Twitter user exists 
- Added "getUsernames" function that retrieves the username in the column title of the Notion page 
- Added function "aggColumnUsername" which calls sub-functions that check that the username exists on twitter and that the title of the column is of type "heading_1
- File ’CHANGELOG.md’

## v1.1

** New Features **
- Display of four twitter accounts on one page Notion

** Changed **
- Changed of the "main" function to call the different functions and add the tweets in each column
- Changed of the "appendEmbed" function so that it adds a block containing a tweet generated via the variables in parameters.

** Added: **
- Added a "getTweet" function that retrieves the id of a user's tweets   
- Added "getColumnIDs" function which retrieves the columns id of the Notion page
- File ’README.md’
- File ’main.py’

## v1.0 

Initial release.

** Added: **
- Added the "appendEmbed" function which adds a block of type "Embed" which contains the url of a tweet
- Added the "apiCall" function which retrieves the content of the Notion page 
- File ’__init__.py’
- File ’main.py’