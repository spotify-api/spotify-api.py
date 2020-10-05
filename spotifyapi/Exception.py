# Base Error Class
class SpotifyApiError(Exception):
    
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return self.message

# Limit out of range error
class LimitOutOfRangeError(SpotifyApiError):

    def __init__(self, message):
        super().__init__(message)

# Invalid Method error
class InvalidMethodError(SpotifyApiError):

    def __init__(self, message):
        super().__init__(message)
