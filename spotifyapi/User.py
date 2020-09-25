import requests

class User():

  def __init__(self, token: str):
    self.token = token

  def get(self, userID: str):
    link = 'https://api.spotify.com/v1/users/' + userID
    header = {'Authorization': 'Bearer ' + self.token}

    return requests.request(
      'GET',
      link,
      headers=header
    ).json()
