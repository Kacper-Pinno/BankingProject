from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy ORM models.

    Every database model in our application will inherit
    from this class.

    SQLAlchemy uses Base.metadata to keep track of all
    tables that our Python models describe.
    """
    pass
