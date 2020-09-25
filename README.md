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
The Track class has 4 functions which are listed below the codeblock -
- Getting the **Track** class - 
```py
from spotifyapi import Client

client = Client(
  token='NO TOKEN' # Leave it like this
)
client.track; # here you will be able to access the track class!!
```
### Functions
Here is a quick example of some functions of the **Track** class.
```py
client.track.search("song",1) # searching for song the second param is the limit

client.track.get('songid',true) # getting a song from track id using the advanced method
```
