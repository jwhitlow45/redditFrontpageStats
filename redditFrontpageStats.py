import praw
import pprint

# Config containing personal use script and secret token
from config import Client

reddit = praw.Reddit(
    client_id=Client.ID,
    client_secret=Client.SECRET,
    user_agent=Client.AGENT
)

subreddit = reddit.subreddit('all')

for submission in subreddit.hot(limit=4):
    pprint.pprint(vars(submission))