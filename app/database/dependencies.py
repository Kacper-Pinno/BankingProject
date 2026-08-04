from collections.abc import Generator
from sqlalchemy.orm import Session

from app.database.database import SessionLocal


def get_db() -> Generator[Session, None, None]:
    """
    Create one SQLAlchemy Session for a request.

    The Session is automatically closed
    when the request finishes.
    """

    with SessionLocal() as session:
        yield session
