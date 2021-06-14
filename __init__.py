import pydantic
from shared.posts.models import Post
import praw
import pprint

import shared.core.db as db
from shared.core.config import Client
from shared.posts import utils

reddit = praw.Reddit(
    client_id=Client.ID,
    client_secret=Client.SECRET,
    user_agent=Client.AGENT
)

# GLOBALS
POST_NUMBER = 25


def update_posts_from_frontpage():
    subreddit = reddit.subreddit('all')

    FrontpagePosts = []

    #for post in r/all
    for p in subreddit.hot(limit=POST_NUMBER):
        currPost = Post(
            id=utils.post_id_to_int(p.id),
            title=p.title,
            author=p.author,
            created_utc=int(p.created_utc),
            score=p.score,
            upvote_ratio=p.upvote_ratio,
            num_comments=p.num_comments,
            num_crossposts=p.num_crossposts,
            total_awards_received=p.total_awards_received,
            subreddit_name=p.subreddit_name_prefixed,
            subreddit_id=p.subreddit_id,
            subreddit_subscribers=p.subreddit_subscribers,
            domain=p.domain,
            permalink=p.permalink,
            url=p.url,
            gilded=p.gilded,
            gilded_silver=p.gildings['gid_1'] if 'gid_1' in p.gildings.keys() else 0,
            gilded_gold=p.gildings['gid_2'] if 'gid_2' in p.gildings.keys() else 0,
            gilded_platinum=p.gildings['gid_3'] if 'gid_3' in p.gildings.keys() else 0,
            is_locked=p.locked,
            is_meta=p.is_meta,
            is_nsfw=p.over_18,
            is_oc=p.is_original_content,
            is_self=p.is_self,
            is_spoiler=p.spoiler,
            is_video=p.is_video
        )
        FrontpagePosts.append(currPost)
        pass

    for post in FrontpagePosts:
        print_post(post)

    with db.session_manager() as session:
        pass



update_posts_from_frontpage()