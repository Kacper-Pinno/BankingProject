from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import User


def get_user_by_email(session: Session, email: str,) -> User | None:
    """
    Find a user by their email address.

    Returns:
        User  -> if found
        None  -> if no matching user exists
    """
    #Build: SELECT * FROM users WHERE email = ...

    statement = select(User).where(User.email == email)

    #Execute the query and return the first result, or None if not found.
    return session.execute(statement).scalar_one_or_none()



def get_user_by_id(session: Session, user_id: int,) -> User | None:
    #Find a user by primary key

    return session.get(User, user_id,)



def create_user(session: Session, email: str, first_name: str, last_name: str,) -> User:
    """
    Create a new User object and add it
    to the current SQLAlchemy Session.

    IMPORTANT:
    This function does NOT commit.
    """
    user = User(email=email, first_name=first_name, last_name=last_name)
    session.add(user)

    # Send INSERT so generated values such as user.id become available.

    session.flush()

    return user


