# Import Packages
import requests
from .Util import encodeURIComponent

# Artist Class
class Artist():

  def __init__(self, token: str):
    self.token = token

  def search(self, query: str, limit: int = 1):
    link = 'https://api.spotify.com/v1/search'
    header = {'Authorization': 'Bearer ' + self.token}

    if limit not in range(50):
      raise TypeError('limit must be under 50')

    return requests.request(
      'GET',
      link,
      headers=header,
      params={
        'q': encodeURIComponent(query),
        'type': 'artist',
        'limit': limit,
        'market': 'US'
      }
    ).json()

  def get(self, artistID: str):
    link = 'https://api.spotify.com/v1/artists/' + artistID
    header = {'Authorization': 'Bearer ' + self.token}

    return requests.request(
      'GET',
      link,
      headers=header
    ).json()

  def albums(self, artistID: str, limit: int = 1):
    link = 'https://api.spotify.com/v1/artists/' + artistID + '/albums'
    header = {'Authorization': 'Bearer ' + self.token}

    if limit not in range(50):
      raise TypeError('limit must be under 50')

    return requests.request(
      'GET',
      link,
      headers=header,
      params={
        'include_groups': 'single',
        'limit': limit,
        'market': 'US'
      }
    ).json()

  def top_tracks(self, artistID: str):
    link = 'https://api.spotify.com/v1/artists/' + artistID + '/top-tracks'
    header = {'Authorization': 'Bearer ' + self.token}

    return requests.request(
      'GET',
      link,
      headers=header,
      params={
        'country': 'US'
      }
    ).json()

  def related_artists(self, artistID: str):
    link = 'https://api.spotify.com/v1/artists/' + artistID + '/related-artists'
    header = {'Authorization': 'Bearer ' + self.token}

    return requests.request(
      'GET',
      link,
      headers=header
    ).json()
