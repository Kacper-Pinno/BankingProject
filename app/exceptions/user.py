class UserNotFoundError(Exception):
    """
    Raised when the requested user does not exist.
    """

    pass


class UserAlreadyExistsError(Exception):
    """
    Raised when attempting to create a user
    with an email that already exists.
    """

    pass