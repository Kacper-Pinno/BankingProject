from typing import TYPE_CHECKING
from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.models import User


class Account(Base):
    """
    Represents a bank account owned by a user.

    Each account must belong to an existing user.
    """

    __tablename__ = "accounts"

    #Internal database identifier
    id: Mapped[int] = mapped_column(primary_key=True)

    # Foreign key connecting this account to users.id.
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)

    # Public-facing account identifier.
    # Keeping this generic for now rather than implementing IBAN yet.
    account_number: Mapped[str] = mapped_column(String(34), unique=True, nullable=False)

    # ISO-style currency code:
    # PLN, EUR, GBP, USD, etc.
    currency: Mapped[str] = mapped_column(String(3), nullable=False)

    # NUMERIC is used instead of FLOAT for financial values.
    # NUMERIC is exact, while FLOAT is approximate.
    balance: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False, default=Decimal("0.00"), server_default=text("0.00"))


    # Examples: active, frozen, closed
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="active", server_default=text("'active'"))

    # Python/ORM-level relationship.
    # Allows: account.owner
    # instead of manually querying users using user_id.
    owner: Mapped["User"] = relationship(back_populates="accounts")


