# Import packages
from .Exception import *
from .Util import encodeURIComponent, search_types
import requests

# Search Class
class Search():

    def __init__(self, token):
        self.token = token

    def search(self, query: str, limit: int = 1, market: str = 'US', search_type: list = search_types):
        if not 0 < limit < 50:
            raise LimitOutOfRangeError('limit must be under 50')

        return requests.request(
            'GET',
            'https://api.spotify.com/v1/search',
            headers={'Authorization': 'Bearer ' + self.token},
            params={
                'q': encodeURIComponent(query),
                'type': ','.join(search_type),
                'limit': limit,
                'market': market
            }
        ).json()
