# Import Packages
from .Util import encodeURIComponent
from .Exception import *
import requests

# Track Class
class Track():

    def __init__(self, token: str):
        self.token = token

    def search(self, query: str, limit: int = 1):
        link = 'https://api.spotify.com/v1/search'
        header = {'Authorization': 'Bearer ' + self.token}

        if not 0 < limit < 50:
            raise LimitOutOfRangeError('limit must be under 50')

        return requests.request(
            'GET',
            link,
            headers=header,
            params={
                'q': encodeURIComponent(query),
                'type': 'track',
                'limit': limit,
                'market': 'US'
            }
        ).json()

    def get(self, trackID: str, advanced: bool = False):
        data = requests.request(
            'GET',
            'https://api.spotify.com/v1/tracks/' + trackID,
            headers={'Authorization': 'Bearer ' + self.token}
        ).json()

        if advanced:
            data['code_img'] = 'https://scannables.scdn.co/uri/plain/jpeg/1db954/white/1080/spotify:track:' + trackID

        return data

    def auido_features(self, trackID: str):
        link = 'https://api.spotify.com/v1/audio-features/' + trackID

        return requests.request(
            'GET',
            link,
            headers={'Authorization': 'Bearer ' + self.token}
        ).json()

    def auido_analysis(self, trackID: str):
        link = 'https://api.spotify.com/v1/audio-analysis/' + trackID
    
        return requests.request(
            'GET',
            link,
            headers={'Authorization': 'Bearer ' + self.token}
        ).json()
