#!/usr/bin/python3
"""a function that prints the titles of posts
"""

from requests import get
import sys
after = None


def recurse(subreddit, hot_list=[]):
    """recursively return a list of 10 hot posts form subreddit
    """
    global after
    headers = {'User-Agent': 'alinanene'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}
    response = get(url, headers=headers, params=params)

    if response.status_code == 200:
        then_ = response.json()['data']['after']
        if then_ is not None:
            after = then_
            recurse(subreddit, hot_list)
        list_titles = response.json()['data']['children']
        for title_ in list_titles:
            hot_list.append(title_['data']['title'])
        return hot_list
    else:
        return (None)
