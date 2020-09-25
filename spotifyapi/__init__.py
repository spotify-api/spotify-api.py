from .Util import AttrDict as objectify

from .Oauth import Auth
from .Track import Track
from .Artist import Artist
from .User import User
from .Album import Album

class Client():

  def __init__(self, token:str):
    self.token = token
    self.oauth = Auth(self.token)
    self.track = Track(self.token)
    self.artist = Artist(self.token)
    self.user = User(self.token)
    self.album = Album(self.token)

__version__ = '0.0.1'
