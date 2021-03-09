from typing import Any, List, Optional
import pydantic

class Post(pydantic.BaseModel):
    """Post info stored in database"""
    class Config:
        extra = 'ignore'

    id: str
    title: str
    author: str
    created_utc : int
    score: int
    upvote_ratio: float
    num_comments: int
    num_crossposts: int
    total_awards_received: int
    subreddit_name_prefixed: bool
    subreddit_id: str
    subreddit_subscribers: int
    domain: str
    permalink: str
    url: str
    gilded: int
    gildings: List[int]
    locked: bool
    is_meta: bool
    over_18: bool
    is_original_content: bool
    is_self: bool
    spoiler: bool
    is_video: bool