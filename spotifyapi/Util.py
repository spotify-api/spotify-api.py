class AttrDict():
  def __init__(self, dictionary: dict):
    for key in dictionary.keys():
      setattr(self, key, dictionary[key])

import base64

def b64(text: str):
  text = text.encode('ascii')
  return base64.b64encode(text).decode('ascii')

import urllib

def encodeURIComponent(text: str):
  text = text.encode('utf-8')
  return urllib.parse.quote(text)
