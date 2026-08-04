from sqlalchemy import select

from app.database.database import SessionLocal
from app.models import User
from app.models import Account


with SessionLocal() as session:

    # --------------------------------------------------
    # FIND THE ACCOUNT
    # --------------------------------------------------

    statement = select(Account).where(
        Account.account_number == "PL001234567890"
    )

    account = session.execute(
        statement
    ).scalar_one_or_none()


    # Always handle the possibility that nothing was found.
    if account is None:
        print("Account not found.")
        raise SystemExit


    print(f"Account number: {account.account_number}")
    print(f"Balance: {account.balance}")
    print(f"Currency: {account.currency}")


    # --------------------------------------------------
    # FOLLOW THE RELATIONSHIP
    # --------------------------------------------------

    # account.owner is NOT a column in PostgreSQL.
    #
    # It's a SQLAlchemy relationship that uses:
    #
    # accounts.user_id → users.id
    owner = account.owner


    print(f"Owner: {owner.first_name} {owner.last_name}")
    print(f"Email: {owner.email}")