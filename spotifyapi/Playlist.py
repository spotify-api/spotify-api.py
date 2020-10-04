# Import Packages
from .Util import encodeURIComponent
from .Exception import *
import requests

# Playlist Class
class Playlist():
    def __init__(self, token: str):
        self.token = token

    def get(self, PlaylistID: str):
        return requests.request(
            'GET',
            'https://api.spotify.com/v1/playlists/' + PlaylistID,
            headers={'Authorization': 'Bearer ' + self.token},
            params={
                'market': 'US'
            }
        ).json()

    def tracks(self, PlaylistID: str, limit: int = 1):
        if not 0 < limit < 50:
            raise LimitOutOfRangeError('limit must be under 50')
        
        return requests.request(
            'GET',
            'https://api.spotify.com/v1/playlists/' + PlaylistID + '/tracks',
            headers={'Authorization': 'Bearer ' + self.token},
            params={
                'market': 'US',
                'limit': limit
            }
        ).json()
