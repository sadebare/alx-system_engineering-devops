#!/usr/bin/python3
"""
Querries the Reddit API and returns a list of the titles of all hot posts
listed for a given subreddit
"""

import json
import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    """Return a list of the titles of all hot posts listed for a subreddit"""
    headers = {"user-agent": "holberton"}
    params = {"after": after}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    subdata = requests.get(url, headers=headers, params=params)
    if subdata.status_code != 200:
        return None
    data = json.loads(subdata.text).get('data').get('children')
    after = json.loads(subdata.text).get('data').get('after')
    if data is None:
        if len(hot_list) == 0:
            print("")
            return
        word_count = {}
        word_list = list(set([word.lower() for word in word_list]))
        for word in word_list:
            word_count[word] = 0
        for word in word_list:
            for title in hot_list:
                for t in title.split():
                    if word == t.lower():
                        word_count[word] = word_count[word] + 1
        sort_word_count = sorted(word_count.items(), key=lambda x: x[1],
                                 reverse=True)
        for i in sort_word_count:
            if i[1] > 0:
                print("{}: {}".format(i[0], i[1]))
    else:
        for item in data:
            hot_list.append(item.get('data').get('title'))
    if after is None:
        if len(hot_list) == 0:
            print("")
            return
        word_count = {}
        word_list = list(set([word.lower() for word in word_list]))
        for word in word_list:
            word_count[word] = 0
        for word in word_list:
            for title in hot_list:
                for t in title.split():
                    if word.lower() == t.lower():
                        word_count[word] = word_count[word] + 1
        sort_word_count = sorted(word_count.items(), key=lambda x: x[1],
                                 reverse=True)
        for i in sort_word_count:
            if i[1] > 0:
                print("{}: {}".format(i[0], i[1]))
    else:
        return count_words(subreddit, word_list, hot_list, after)
