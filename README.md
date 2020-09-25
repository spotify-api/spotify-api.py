# Spotify-Api.py

Simple wrapper for Spotify api written in python by the [@spotify-api](https://github.com/spotify-api) Organization!


# Quick Docs

## Client Class

Client class will be the main class to access other classes!

```py
from spotifyapi import Client

client = Client(
  token='your-token'
)
```

Now as the Spotify Token Regenerates for every 5 minutes you can get a new token by Client ID and Client Secret!

```py
# You can use set interval if u want

from spotifyapi import Client

client = Client(
  token='NO TOKEN' # Leave it like this
)

my_auth = client.oauth.get(
  client_id='your-id',
  client_secret='your-secret'
)

print(my_auth['access_token']) # Will print token. If you find errors, you can create an issue in Github repo
```

## Track Class 
Track class will let you to find, get and configure your search. You have to load `client`. Example given above 

First define tracks if needed
```py
track = client.track

# or

from spotifyapi.Track import Track
track = Track('some-token')
```

### Functions

| Name           | Params                     | Example                           |
|----------------|----------------------------|-----------------------------------|
| search         | `query: str`, `limit: int` | `track.get('some query', 5)`      |
| get            | `trackID: str`             | `track.get('some-id')`            |
| audio_features | `trackID: str`             | `track.audio_features('some-id')` |
| audio_analysis | `trackID: str`             | `track.audio_analysis('some-id')` |
