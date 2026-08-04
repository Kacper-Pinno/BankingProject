class AccountNotFoundError(Exception):
    """
    Raised when the requested account does not exist.
    """

    pass


class AccountNumberCollisionError(Exception):
    """
    Raised if a generated account number
    already exists.
    """

    pass