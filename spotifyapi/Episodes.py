# Import packages
from .Exception import *
import requests

# Episodes class
class Episodes():

    def __init__(self, token):
        self.token = token

    def all(self, ids: list):
        return requests.request(
            'GET',
            'https://api.spotify.com/v1/episodes/',
            headers={'Authorization': 'Bearer ' + self.token},
            params={
                'ids': ','.join(ids)
            }
        ).json()

    def get(self, episodeID: str):
        return requests.request(
            'GET',
            'https://api.spotify.com/v1/episodes/' + episodeID,
            headers={'Authorization': 'Bearer ' + self.token}
        ).json() 
