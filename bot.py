import praw
import os

user = os.environ.get("REDDIT_RESIGN_USER")
pw = os.environ.get("REDDIT_RESIGN_PASSWORD")
cid = os.environ.get("CLIENT_ID")
csecret= os.environ.get("CLIENT_SECRET")

reddit = praw.Reddit(user_agent='resign_bot (by /u/hardy_v1)',
                     client_id=cid, client_secret=csecret,
                    username=user, password=pw)

print("Logged in successfully: ",user," ", pw, " ", cid, " ", csecret)

subreddit = reddit.subreddit('nba')
for comment in subreddit.stream.comments(skip_existing=True):
    lowcom = comment.body.lower()
    if "resign" in lowcom and comment.author != "resign_bot":
    	comment.reply("Did you mean **re-sign**? \n\n ^Beep ^boop, ^I'm ^a ^bot. ^You ^can ^contact ^me ^[here](https://www.reddit.com/message/compose/?to=hardy_v1&subject=/u/resign_bot)")
    	print("Commented on ", comment.author, "who said '", comment.body, "'")

