# Import packages
from .Exception import *
import requests

# Shows class
class Shows():
    
    def __init__(self, token):
        self.token = token

    def all(self, ids: list):
        return requests.request(
            'GET',
            'https://api.spotify.com/v1/shows/',
            headers={'Authorization': 'Bearer ' + self.token},
            params={
                'ids': ','.join(ids)
            }
        ).json()

    def get(self, showID: str):
        return requests.request(
            'GET',
            'https://api.spotify.com/v1/shows/' + showID,
            headers={'Authorization': 'Bearer ' + self.token}
        ).json() 

    def episodes(self, showID: str, limit: int = 20):
        if not 0 < limit < 50:
            raise LimitOutOfRangeError('limit must be under 50')

        return requests.request(
            'GET',
            'https://api.spotify.com/v1/shows/' + showID + '/episodes',
            headers={'Authorization': 'Bearer ' + self.token},
            params={
                'limit': limit
            }
        ).json() 
