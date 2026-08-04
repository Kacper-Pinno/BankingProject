from decimal import Decimal

from sqlalchemy import select

from app.database.database import SessionLocal
from app.models import User
from app.models import Account


# "with" automatically closes the session when we're done.
with SessionLocal() as session:

    # ---------------------------------------------------------
    # 1. BUILD THE QUERY
    # ---------------------------------------------------------

    # This doesn't execute SQL yet.
    # Rough SQL equivalent:
    # SELECT *
    # FROM users
    # WHERE email = 'john@example.com';
    statement = select(User).where(
        User.email == "example@example.com"
    )


    # ---------------------------------------------------------
    # 2. EXECUTE THE QUERY
    # ---------------------------------------------------------

    result = session.execute(statement)


    # We expect exactly one user with this email.
    user = result.scalar_one()

    print(f"Found user: {user.first_name} {user.last_name}")
    print(f"User ID: {user.id}")


    # ---------------------------------------------------------
    # 3. CREATE AN ACCOUNT
    # ---------------------------------------------------------

    account = Account(
        # Foreign key → users.id
        user_id=user.id,

        account_number="PL001234567890",

        currency="PLN",

        # Always use Decimal for money.
        balance=Decimal("1000.00"),
    )


    # Tell SQLAlchemy to track this new account.
    session.add(account)


    # Permanently save it.
    session.commit()


    print("Account created!")
    print(f"Account ID: {account.id}")