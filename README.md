<div align="center"><img src="https://socialify.git.ci/Bollywood-Bot/reddit/image?description=1&descriptionEditable=A%20Bot%20that%20replied%20to%20you%20with%20a%20cheeky%20and%20typical%20Bollywood%20dialogue%20everytime%20you%20mention%20it.%20&font=Inter&forks=1&issues=1&language=1&owner=1&pulls=1&stargazers=1&theme=Light" width="600"></div>

# Bollywood Bot - Reddit Version
This [reddit bot](https://www.reddit.com/user/Bollywood-Bot) is live deployed.</br> 
So, if you want to test it go to any subreddit, <br>
and comment under any post with (bollywood/Bollywood) word with in your comment.
  - [r/indiasocial](https://www.reddit.com/r/indiasocial/)
  - [r/Chodi](https://www.reddit.com/r/Chodi)
  - [r/IndiaSpeaks](https://www.reddit.com/r/IndiaSpeaks/) </br>
</br>

### How to use this
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

### Contribution
Fork this Repository for any kind of contribution,</br>
All kind of contributions, issues and feature requests are welcome ❤️
