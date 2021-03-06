from typing import List

class Post():
    allow_live_comments: bool
    allow_live_comments: bool
    author: str
    created_utc : int
    domain: str
    gilded: int
    gildings: List[int] # Index 0 is silver, 1 is gold, 2 is platinum
    id: str
    is_meta: bool
    is_original_content: bool
    is_self: bool
    is_video: bool
    locked: bool
    num_comments: int
    num_crossposts: int
    over_18: bool
    permalink: str
    score: int
    spoiler: bool
    subreddit_name_prefixed: str
    subreddit_id: str
    subreddit_subscribers: int
    title: str
    total_awards_received: int
    upvote_ratio: float
    url: str
