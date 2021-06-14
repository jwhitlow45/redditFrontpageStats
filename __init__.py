import pydantic
import praw
from typing import List

import shared.core.db as db
from shared.core.config import Client
from shared.posts import models
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
        currPost = models.Post(
            id=utils.post_id_to_int(p.id),
            title=p.title,
            author=str(p.author),
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

    with db.session_manager() as session:
        for post in FrontpagePosts:
            session.merge(post)
        session.commit()
        pass

def print_post(p):
    print("id: " + str(p.id))
    print("title: " + str(p.title))
    print("author: " + str(p.author))
    print("created_utc: " + str(p.created_utc))
    print("score: " + str(p.score))
    print("upvote_ratio: " + str(p.upvote_ratio))
    print("num_comments: " + str(p.num_comments))
    print("num_crossposts: " + str(p.num_crossposts))
    print("total_awards_received: " + str(p.total_awards_received))
    print("subreddit_name: " + str(p.subreddit_name))
    print("subreddit_id: " + str(p.subreddit_id))
    print("subreddit_subscribers: " + str(p.subreddit_subscribers))
    print("domain: " + str(p.domain))
    print("permalink: " + str(p.permalink))
    print("url: " + str(p.url))
    print("gilded: " + str(p.gilded))
    print("gilded_silver: " + str(p.gilded_silver))
    print("gilded_gold: " + str(p.gilded_gold))
    print("gilded_platinum: " + str(p.gilded_platinum))
    print("is_locked: " + str(p.is_locked))
    print("is_meta: " + str(p.is_meta))
    print("is_nsfw: " + str(p.is_nsfw))
    print("is_oc: " + str(p.is_oc))
    print("is_self: " + str(p.is_self))
    print("is_spoiler: " + str(p.is_spoiler))
    print("is_video: " + str(p.is_video))
    print("")

update_posts_from_frontpage()