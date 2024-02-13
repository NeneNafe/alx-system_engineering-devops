#!/usr/bin/python3
"""a function that prints the titles of posts
"""

from requests import get


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    params = {'limit': 10}
    headers = {
        "User-Agent": "vscode:0x16.api.advanced:v1.0"
    }

    response = get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return

    results = response.json()['data']['children']
    [print(post['data']['title']) for post in results]
