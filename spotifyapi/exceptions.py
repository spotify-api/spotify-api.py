class SpotifyError(Exception):
    """
    Generic base class for exceptions.
    """
    def __init__(self, message):
        self.message = message 

    def __str__(self):
        class_name = self.__class__.__name__
        return f"{class_name}: {self.message}"

class LimitOutOfRangeError(SpotifyError):
    def __init__(self, message):
        super().__init__(message)

class InvalidTrackIdError(SpotifyError):
    def __init__(self, message):
        super().__init__(message)

