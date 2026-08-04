from decimal import Decimal

from sqlalchemy.orm import Session

from app.models import Account

from app.repositories.account_repository import (
    create_account,
    get_account_by_id,
    get_account_by_number,
    get_accounts_by_user_id,
)

from app.repositories.user_repository import (
    get_user_by_id,
)

from app.utils.account_number import (
    generate_account_number,
)

from app.exceptions.account import (
    AccountNotFoundError,
    AccountNumberCollisionError,
)

from app.exceptions.user import (
    UserNotFoundError,
)



def open_account(session: Session, user_id: str, currency: str) -> Account:
    #Open new bank account for an existing user.

    #BUSINESS RULE 1: User must exist.

    user = get_user_by_id(session, user_id)

    if user is None:
        raise UserNotFoundError("User does not exist.")


    #Generate Account Number
    account_number = generate_account_number()

    #Account Number Must Be Unique
    existing_account = get_account_by_number(session, account_number)

    if existing_account is not None:
        raise AccountNumberCollisionError("Generated account number already exists.")


    #Create Account

    account = create_account(session=session,
                             user_id=user_id,
                             account_number=account_number,
                             currency=currency,
                             balance=Decimal("0.00")
                             )
    
    return account


def get_account(
    session: Session,
    account_id: int,
) -> Account:
    """
    Retrieve an account by ID.

    The repository performs the database lookup.
    The service decides what should happen if
    the account doesn't exist.
    """

    # Ask repository to find the account.
    account = get_account_by_id(
        session,
        account_id,
    )

    # Repository returns None if nothing was found.
    if account is None:
        raise AccountNotFoundError(
            "Account does not exist."
        )

    return account


def get_user_accounts(
    session: Session,
    user_id: int,
) -> list[Account]:
    """
    Return all accounts belonging to a user.

    First verify that the user actually exists.
    """

    # ------------------------------------------
    # CHECK USER
    # ------------------------------------------

    user = get_user_by_id(
        session,
        user_id,
    )

    if user is None:
        raise UserNotFoundError(
            "User does not exist."
        )


    # ------------------------------------------
    # GET USER'S ACCOUNTS
    # ------------------------------------------

    accounts = get_accounts_by_user_id(
        session,
        user_id,
    )

    return accounts