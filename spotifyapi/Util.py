# Import Packages
import base64
import urllib

# Text to base64
def b64(text: str) -> str:
    text = text.encode('ascii')
    return base64.b64encode(text).decode('ascii')

# Parsing text to uri component like in js
def encodeURIComponent(text: str) -> str:
    text = text.encode('utf-8')
    return urllib.parse.quote(text)

# All types of search
search_types = ['track', 'artist', 'album']
