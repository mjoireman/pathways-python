class AuthenticationError(Exception):
    """This exception is raised when a problem is encountered during authentication.
    """
    def __init__(self, message):
        super(AuthenticationError, self).__init__(message)