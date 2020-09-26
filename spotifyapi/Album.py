# Import Packages
import requests
from .Util import encodeURIComponent
from .exceptions import LimitOutOfRangeError


# Album Class
class Album():

  def __init__(self, token: str):
    self.token = token

  def search(self, query: str, limit: int = 1):
    link = 'https://api.spotify.com/v1/search'
    header = {'Authorization': 'Bearer ' + self.token}

    if not 0 < limit < 50:
      raise LimitOutOfRangeError('Limit must be under 50.')

    return requests.request(
      'GET',
      link,
      headers=header,
      params={
        'q': encodeURIComponent(query),
        'type': 'album',
        'limit': limit,
        'market': 'US'
      }
    ).json()

  def get(self, albumID: str):
    link = 'https://api.spotify.com/v1/albums/' + albumID
    header = {'Authorization': 'Bearer ' + self.token}

    return requests.request(
      'GET',
      link,
      headers=header
    ).json()

  def get_tracks(self, albumID: str, limit: int = 1):
    link = 'https://api.spotify.com/v1/albums/' + albumID + '/tracks'
    header = {'Authorization': 'Bearer ' + self.token}

    if not 0 < limit < 50:
      raise LimitOutOfRangeError('Limit must be under 50.')

    return requests.request(
      'GET',
      link,
      headers=header,
      params={
        'offset': 0,
        'limit': limit,
        'market': 'US'
      }
    ).json()
