#!/usr/bin/python3

"""
Querries the Reddit API and returns the total number of subscribers for a
given subreddit.
If an invalid subreddit is given, return 0.
"""
import json
import requests


def number_of_subscribers(subreddit):
    """Querries Reddit API and returns total subscribers for a given subreddit,
       or 0 if invalid subreddit given.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        "User-Agent": "holberton"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
