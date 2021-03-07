import praw
import pprint
import shared.core.db as db

# Config containing personal use script and  secret token
from shared.core.config import Client

reddit = praw.Reddit(
    client_id=Client.ID,
    client_secret=Client.SECRET,
    user_agent=Client.AGENT
)

subreddit = reddit.subreddit('all')

with db.session_manager() as session:
    pass

for submission in subreddit.hot(limit=4):
    pprint.pprint(vars(submission))