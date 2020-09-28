"""
Spotify-Api.py

Simple Spotify Wrapper written in python
By abh80 and science spot(scientific-guy)
v0.0.2 MIT License
"""

# Import all lib files
from .Oauth import Auth
from .Track import Track
from .Artist import Artist
from .User import User
from .Album import Album
from .Playlist import Playlist

# Client Class


class Client():

    def __init__(self, token: str):
        self.token = token
        self.oauth = Auth(self.token)
        self.track = Track(self.token)
        self.artist = Artist(self.token)
        self.user = User(self.token)
        self.album = Album(self.token)
        self.playlist = Playlist(self.token)


# Version v0.0.2
__version__ = '0.0.2'
