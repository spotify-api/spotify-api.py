# Import Packages
import requests

# User Class
class User():

    def __init__(self, token: str):
        self.token = token

    def get(self, userID: str):
        return requests.request(
            'GET',
            'https://api.spotify.com/v1/users/' + userID,
            headers={'Authorization': 'Bearer ' + self.token}
        ).json()
