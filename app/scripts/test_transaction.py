from decimal import Decimal

from app.database.database import SessionLocal
from app.models import User
from app.models import Account


# Opening the Session using "with" ensures that
# the Session is closed when we're finished.
with SessionLocal() as session:

    # Everything inside session.begin() belongs
    # to ONE database transaction.
    #
    # Success   → COMMIT
    # Exception → ROLLBACK
    with session.begin():

        # ------------------------------------------
        # 1. CREATE USER
        # ------------------------------------------

        user = User(
            email="bob@example.com",
            first_name="Bob",
            last_name="Smith",
                    )

        session.add(user)


        # ------------------------------------------
        # 2. FLUSH
        # ------------------------------------------

        # Send pending SQL to PostgreSQL.
        #
        # This allows PostgreSQL to generate
        # the user's primary key.
        #
        # IMPORTANT:
        # flush() does NOT commit the transaction.
        session.flush()

        print(f"Generated user ID: {user.id}")


        # ------------------------------------------
        # 3. CREATE ACCOUNT
        # ------------------------------------------

        account = Account(
            user_id=user.id,

            # Intentionally duplicate John's account number.
            account_number="PL001234567890",

            currency="PLN",
            balance=Decimal("0.00"),
        )

        session.add(account)


# If no exception happened inside session.begin(),
# SQLAlchemy commits automatically.

print("User and account created successfully!")