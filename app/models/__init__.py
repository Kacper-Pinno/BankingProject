"""
SQLAlchemy model registry.

Import every ORM model here so that SQLAlchemy knows about
all mapped classes when the application starts.
"""

from app.models.user import User
from app.models.account import Account


__all__ = [
    "User",
    "Account",
]