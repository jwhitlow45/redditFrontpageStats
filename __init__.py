import pydantic
from shared.posts.models import Post
import praw
import pprint


import shared.core.db as db
from shared.core.config import Client
from shared.posts.post import Post
from shared.posts import utils

reddit = praw.Reddit(
    client_id=Client.ID,
    client_secret=Client.SECRET,
    user_agent=Client.AGENT
)

subreddit = reddit.subreddit('all')

with db.session_manager() as session:
    pass

for submission in subreddit.hot(limit=1):
    curr_post = pydantic.parse_raw_as(Post, submission)