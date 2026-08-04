from sqlalchemy import select

from app.database.database import SessionLocal
from app.models import User
from app.models import Account

# Open a database session.
# It will automatically close when we leave the "with" block.
with SessionLocal() as session:

    # Find our existing user.
    statement = select(User).where(
        User.email == "example@example.com"
    )

    user = session.execute(
        statement
    ).scalar_one_or_none()


    # Handle the case where the user doesn't exist.
    if user is None:
        print("User not found.")
        raise SystemExit


    print(
        f"User: {user.first_name} {user.last_name}"
    )


    # Access the SQLAlchemy relationship.
    
    # SQLAlchemy knows:
    
    # users.id -> accounts.user_id
    
    # and retrieves accounts belonging to this user.
    for account in user.accounts:

        print(
            f"Account: {account.account_number}"
        )

        print(
            f"Currency: {account.currency}"
        )

        print(
            f"Balance: {account.balance}"
        )

        print(
            f"Status: {account.status}"
        )