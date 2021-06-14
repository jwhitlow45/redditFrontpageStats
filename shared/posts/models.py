from sqlalchemy import Column
from sqlalchemy import Integer, Float, Boolean, String, DateTime

from shared.core.db import Base

class Post(Base):
    __tablename__ = 'Posts'

    id = Column(Integer, primary_key=True)      # unique id 
    title = Column(String)                      # title 
    author = Column(String)                     # author 
    created_utc = Column(DateTime)              # time of creation in utc
    score = Column(Integer)                     # score 
    upvote_ratio = Column(Float)                # upvote ratio (upvote/total votes)
    num_comments = Column(Integer)              # number of comments on post
    num_crossposts = Column(Integer)            # number of crossposts 
    total_awards_received = Column(Integer)     # total number of received awards
    subreddit_name = Column(String)             # name of subreddit (r/subreddit)
    subreddit_id = Column(String)               # unique id of subreddit
    subreddit_subscribers = Column(Integer)     # number of subscribers to subreddit
    domain = Column(String)                     # domain hosting content
    permalink = Column(String)                  # permalink to post
    url = Column(String)                        # url of the content
    gilded = Column(Integer)                    # number of total gildings 
    gilded_silver = Column(Integer)             # number of silver awards
    gilded_gold = Column(Integer)               # number of gold awards
    gilded_platinum = Column(Integer)           # number of platinum awards
    is_locked = Column(Boolean)                 # is the post locked
    is_meta = Column(Boolean)                   # is the post meta
    is_nsfw = Column(Boolean)                   # is the post nsfw
    is_oc = Column(Boolean)                     # is the post oc
    is_self = Column(Boolean)                   # is the post a self post
    is_spoiler = Column(Boolean)                # is the post a spoiler
    is_video = Column(Boolean)                  # is the post a video