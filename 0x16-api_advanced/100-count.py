#!/usr/bin/python3
"""a function that prints the titles of posts
"""

from requests import get


def count_words(subreddit, word_list, found_list=[], after=None):
    """ a recursive function that queries the Reddit API,
    parses the title of all hot articles
    """

    headers = {'User-Agent': 'NENENAFE1'}
    url_post = get('https://www.reddit.com/r/{}/hot.json?after={}'
                   .format(subreddit, after), headers=headers)
    if after is None:
        word_list = [word.lower() for word in word_list]

    if url_post.status_code == 200:
        url_post = url_post.json()['data']
        then = url_post['after']
        url_post = url_post['children']
        for post in url_post:
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    found_list.append(word)
        if then is not None:
            count_words(subreddit, word_list, found_list, then)
        else:
            results = {}
            for word in found_list:
                if word.lower() in results.keys():
                    results[word.lower()] += 1
                else:
                    results[word.lower()] = 1
            for key, value in sorted(results.items(), key=lambda item: item[1],
                                     reverse=True):
                print('{}: {}'.format(key, value))
    else:
        return
