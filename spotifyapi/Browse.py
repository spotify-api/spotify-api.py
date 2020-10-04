"""
This file is not stable!
Try to contribute in github
"""

# Import packages
from .Exception import *
import requests

# Category sub class
class Category():

    def __init__(self, token):
        self.token = token

    def all(self):
        return requests.request(
            'GET',
            'https://api.spotify.com/v1/browse/categories/',
            headers={'Authorization': 'Bearer ' + self.token}
        ).json()

    def get(self, categoryId: str):
        return requests.request(
            'GET',
            'https://api.spotify.com/v1/browse/categories/' + categoryId,
            headers={'Authorization': 'Bearer ' + self.token}
        ).json()

    def playlists(self, categoryId: str, limit: int = 1):
        if not 0 < limit < 50:
            raise LimitOutOfRangeError('limit must be under 50')

        return requests.request(
            'GET',
            'https://api.spotify.com/v1/browse/categories/' + categoryId + '/playlists',
            headers={'Authorization': 'Bearer ' + self.token}
        ).json()

# Browse class
class Browse():

    def __init__(self, token):
        self.token = token
        self.categories = Category(self.token)

    def featured_playlists(self, limit: int = 20):
        if not 0 < limit < 50:
            raise LimitOutOfRangeError('limit must be under 50')

        return requests.request(
            'GET',
            'https://api.spotify.com/v1/browse/featured-playlists',
            headers={'Authorization': 'Bearer ' + self.token},
            params={
                'limit': limit
            }
        ).json()

    def new_releases(self, limit: int = 20):
        if not 0 < limit < 50:
            raise LimitOutOfRangeError('limit must be under 50')

        return requests.request(
            'GET',
            'https://api.spotify.com/v1/browse/new-releases',
            headers={'Authorization': 'Bearer ' + self.token},
            params={
                'limit': str(limit)
            }
        ).json()

    def recommendations(self, limit: int = 20):
        if not 0 < limit < 100:
            raise LimitOutOfRangeError('limit must be under 100')

        return requests.request(
            'GET',
            'https://api.spotify.com/v1/browse/recommendations',
            headers={'Authorization': 'Bearer ' + self.token},
            params={
                'limit': limit
            }
        ).text
