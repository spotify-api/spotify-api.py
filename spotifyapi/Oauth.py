# Import Packages
import requests
from .Util import b64

# Read Class
class Auth():

  def __init__(self, oauth: str):
    self.token = oauth

  def get(self, client_id: str, client_secret: str):
    header_data = b64(str(client_id) + ':' + str(client_secret))
    header = {
      'Authorization': 'Basic {}'.format(header_data)
    }

    return requests.request(
      'POST',
      'https://accounts.spotify.com/api/token',
      data={
        'grant_type': 'client_credentials'
      },
      headers=header
    ).json()
