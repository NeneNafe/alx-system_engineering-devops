#!/usr/bin/python3
"""a function that queries Reddit API and return the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """returns reddit subscribers
    """

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        "User-Agent": "vscode:0x16.api.advanced:v1.0. (by /NENENAFE1_)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return (0)
    results = response.json().get("data")
    return results.get("subscribers")
