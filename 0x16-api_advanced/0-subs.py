#!/usr/bin/python3
""" returns the number of subscribers """
import json
import requests


def number_of_subscribers(subreddit):
    """ return the total number of subscribers of a subreddit """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'Hajar-Zait'},
                            allow_redirects=False)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0
