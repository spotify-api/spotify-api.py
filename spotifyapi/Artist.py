# Import Packages
import requests
from .Util import encodeURIComponent
from .Exception import *

# Artist Class
class Artist():

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
                'type': 'artist',
                'limit': limit,
                'market': 'US'
            }
        ).json()

    def get(self, artistID: str):
        return requests.request(
            'GET',
            'https://api.spotify.com/v1/artists/' + artistID,
            headers={'Authorization': 'Bearer ' + self.token}
        ).json()

    def albums(self, artistID: str, limit: int = 1):
        if not 0 < limit < 50:
            raise LimitOutOfRangeError('limit must be under 50')

        return requests.request(
            'GET',
            'https://api.spotify.com/v1/artists/' + artistID + '/albums',
            headers={'Authorization': 'Bearer ' + self.token},
            params={
                'include_groups': 'single',
                'limit': limit,
                'market': 'US'
            }
        ).json()

    def top_tracks(self, artistID: str):
        return requests.request(
            'GET',
            'https://api.spotify.com/v1/artists/' + artistID + '/top-tracks',
            headers={'Authorization': 'Bearer ' + self.token},
            params={'country': 'US'}
        ).json()

    def related_artists(self, artistID: str):
        return requests.request(
            'GET',
            'https://api.spotify.com/v1/artists/' + artistID + '/related-artists',
            headers={'Authorization': 'Bearer ' + self.token}
        ).json()
