import praw
import config
import time
import csv
import random
import os

def bot_login():
	print("Logging in...")
	r = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = "Bollywood-bot v1.0")
	print("Logged in!")

	return r

def run_bot(r, comments_replied_to):
	print("Bot started")
	keywords = ["Bollywood", " Bollywood ","Bollywood ", "bollywood", " bollywood ", "bollywood "]

	for comment in r.subreddit('indiasocial+Chodi+delhi+IndiaSpeaks+bollywoodbottest').stream.comments(skip_existing=True):
		for keyword in keywords:
			if keyword in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
				print("Comment found consisting of a keyword")
				with open('file.csv') as f:
					reader = csv.reader(f)
					chosen_row = random.choice(list(reader))
					comment.reply(chosen_row)
					comments_replied_to=list(filter(None, comments_replied_to))
					comments_replied_to.append(comment.id)
					with open ("comments_replied_to.txt", "a") as f:
						f.write(comment.id + "\n")
				print("Sleeping for 10 seconds...")
				#Sleep for 10 seconds...		
				time.sleep(10)

def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = filter(None, comments_replied_to)


	return comments_replied_to


r = bot_login()
comments_replied_to = get_saved_comments()
print(comments_replied_to)

while True:
	run_bot(r, comments_replied_to)
