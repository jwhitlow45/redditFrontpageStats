from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, Float, String, Boolean
from sqlalchemy.sql.sqltypes import Time

import shared.core.config

engine = create_engine(shared.core.config.SQLEngine.CONNECTION_STR, echo=True)
meta=MetaData()

posts = Table(
    'posts', meta,
    Column('id', String, primary_key=True),     # unique id 
    Column('title', String),                    # title 
    Column('author', String),                   # author 
    Column('created_utc', Time),                # time of creation in utc
    Column('score', Integer),                   # score 
    Column('upvote_ratio', Float),              # upvote ratio (upvote/total votes)
    Column('num_comments', Integer),            # number of comments on post
    Column('num_crossposts', Integer),          # number of crossposts 
    Column('total_awards_received', Integer),   # total number of received awards
    Column('subreddit_name', String),           # name of subreddit (r/subreddit)
    Column('subreddit_id', String),             # unique id of subreddit
    Column('subreddit_subscribers', Integer),   # number of subscribers to subreddit
    Column('domain', String),                   # domain hosting content
    Column('permalink', String),                # permalink to post
    Column('url', String),                      # url of the content
    Column('gilded', Integer),                  # number of total gildings 
    Column('gilded_silver', Integer),           # number of silver awards
    Column('gilded_gold', Integer),             # number of gold awards
    Column('gilded_platinum', Integer),         # number of platinum awards
    Column('is_locked', Boolean),               # is the post locked
    Column('is_meta', Boolean),                 # is the post meta
    Column('is_nsfw', Boolean),                 # is the post nsfw
    Column('is_oc', Boolean),                   # is the post oc
    Column('is_self', Boolean),                 # is the post a self post
    Column('is_spoiler', Boolean),              # is the post a spoiler
    Column('is_video', Boolean)                 # is the post a video
)