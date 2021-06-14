from datetime import datetime
import pydantic

class Post(pydantic.BaseModel):
    """Post info stored in database"""
    class Config:
        extra = 'ignore'

    id: int
    title: str
    author: str
    created_utc : int
    score: int
    upvote_ratio: float
    num_comments: int
    num_crossposts: int
    total_awards_received: int
    subreddit_name: str
    subreddit_id: str
    subreddit_subscribers: int
    domain: str
    permalink: str
    url: str
    gilded: int
    gilded_silver: int
    gilded_gold: int
    gilded_platinum: int
    is_locked: bool
    is_meta: bool
    is_nsfw: bool
    is_oc: bool
    is_self: bool
    is_spoiler: bool
    is_video: bool