from sqlalchemy.orm import Session

from app.models import User
from app.repositories.user_repository import (
    create_user,
    get_user_by_email,
)
from app.exceptions.user import (
    UserAlreadyExistsError,
)


def register_user(session: Session, email: str, first_name: str, last_name: str,) -> User:
    """
    Register a new user.

    Business rules belong here.
    """
    # ------------------------------------------
    # BUSINESS RULE:
    # Email must not already exist.
    # ------------------------------------------
    existing_user = get_user_by_email(session, email)

    if existing_user is not None:
        raise UserAlreadyExistsError(
            "A user with this email already exists."
        )

    # ------------------------------------------
    # CREATE USER
    # ------------------------------------------

    user = create_user(session=session, email=email, first_name=first_name, last_name=last_name)

    return user
