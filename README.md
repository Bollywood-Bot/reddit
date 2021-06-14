# Bollywood Bot - Reddit Version
This Reddit Comment Bot is a python-based auto-responder.
  - Pick a subreddit to scan
  - Designate a specific comment to search for
  - Set your bot's reply

### Requirements
  - [Python 3](https://www.python.org/downloads/)
  - [Praw](https://praw.readthedocs.io/en/latest/getting_started/installation.html)
  - A Reddit Account
  - A csv file with all the replies

### Setup
###### Reddit App:
1. [Navigate to the Apps page ](https://www.reddit.com/prefs/apps/)
2. Click *create an app*
3. **name:** Set a name for your app
4. **type:** Script
5. **description:** Optional
6. **about url:** Optional
7. **redirect uri:** http://localhost:8080
8. Note the outputted *client id* and *secret*

###### config.py:
1. **username:** your Reddit username
2. **password:** your Reddit password
3. **client_id:** the outputted client id
4. **client_secret:** the outputted secret

###### reddit_bot.py:

Set the subreddit to search (default = "r/test"):
```python
r.subreddit('test')
```
Comment search criteria (default = "sample user comment"):
```python
if "sample user comment"
```
Bot's comment reply 
```python
reader = csv.reader(f)
chosen_row = random.choice(list(reader)) #Chose a random row from csv file
comment.reply(chosen_row) #reply with that random row
```

### Usage

Navigate into the bot directory.
Run your bot:
```sh
$ python reddit_bot.py
```
