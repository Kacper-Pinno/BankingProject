
from typing import TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

# Only imported for Python type checking
# This helps avoid circular imports at runtime

if TYPE_CHECKING:
    from app.models import Account

class User(Base):
    """
    Represents a user/customer in the banking system.

    This Python class maps to the PostgreSQL table called "users".
    """
    __tablename__ = "users"

    #Primary key uniquly indentifies every user
    id: Mapped[int] = mapped_column(primary_key=True)

    #Email will be required and must be unique
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    #Store names separately for better flexibility
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)

    #One user can own multiple accounts.
    accounts: Mapped[list["Account"]] = relationship(back_populates="owner")
