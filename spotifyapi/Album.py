# Import Packages
import requests
from .Util import encodeURIComponent
from .Exception import *

# Album Class
class Album():

    def __init__(self, token: str):
        self.token = token

    def search(self, query: str, limit: int = 1):
        if not 0 < limit < 50:
            raise LimitOutOfRangeError('limit must be under 50')

        return requests.request(
            'GET',
            'https://api.spotify.com/v1/search',
            headers={'Authorization': 'Bearer ' + self.token},
            params={
                'q': encodeURIComponent(query),
                'type': 'album',
                'limit': limit,
                'market': 'US'
            }
        ).json()

    def get(self, albumID: str):
        return requests.request(
            'GET',
            'https://api.spotify.com/v1/albums/' + albumID,
            headers={'Authorization': 'Bearer ' + self.token}
        ).json()

    def get_multiple(self, albumIDs: list): 
        return requests.request(
            'GET',
            'https://api.spotify.com/v1/albums',
            headers={'Authorization': 'Bearer ' + self.token},
            params={
                'ids': albumIDs
            }
        ).json()

    def get_tracks(self, albumID: str, limit: int = 1):
        if not 0 < limit < 50:
            raise LimitOutOfRangeError('limit must be under 50')

        return requests.request(
            'GET',
            'https://api.spotify.com/v1/albums/' + albumID + '/tracks',
            headers={'Authorization': 'Bearer ' + self.token},
            params={
                'offset': 0,
                'limit': limit,
                'market': 'US'
            }
        ).json()
