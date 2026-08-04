from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Account

from decimal import Decimal


def get_account_by_id(session: Session, account_id: int,) -> Account | None:

    """
    Find an account using its primary key.
    """

    return session.get(Account, account_id)


def get_account_by_number(session: Session, account_number: str,) -> Account | None:

    """
    Find an account using its unique account number.
    """

    statement = select(Account).where(Account.account_number == account_number)

    return session.execute(statement).scalar_one_or_none()


def get_accounts_by_user_id(session: Session, user_id: int,) -> list[Account]:

    """
    Return all accounts belonging to a user.
    """
    statement = select(Account).where(Account.user_id == user_id)

    return list(session.scalars(statement).all())


def create_account(session: Session, user_id: int, account_number: str, currency: str, balance: Decimal,) -> Account:
    """
    Create an account inside the current transaction.

    This function does NOT commit.
    """
    account = Account(user_id=user_id, account_number=account_number, currency=currency, balance=balance)

    session.add(account)

    # Send the INSERT to PostgreSQL so generated
    # values such as account.id are available.
    # This does NOT commit.
    session.flush()

    return account


