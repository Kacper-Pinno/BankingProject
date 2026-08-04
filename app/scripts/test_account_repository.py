from app.database.database import SessionLocal

from app.repositories.account_repository import (
    get_account_by_id,
    get_account_by_number,
    get_accounts_by_user_id,
)


with SessionLocal() as session:

    # ------------------------------------------
    # FIND ACCOUNT BY NUMBER
    # ------------------------------------------

    account = get_account_by_number(
        session,
        "PL001234567890",
    )

    if account is None:
        print("Account not found.")
        raise SystemExit

    print("Found by account number:")
    print(
        f"{account.id} | "
        f"{account.account_number} | "
        f"{account.balance} {account.currency}"
    )


    # ------------------------------------------
    # FIND ACCOUNT BY ID
    # ------------------------------------------

    same_account = get_account_by_id(
        session,
        account.id,
    )

    if same_account is None:
        print("Account not found by ID.")
        raise SystemExit

    print()
    print("Found by ID:")
    print(
        f"{same_account.id} | "
        f"{same_account.account_number}"
    )


    # ------------------------------------------
    # FIND ALL ACCOUNTS FOR USER
    # ------------------------------------------

    accounts = get_accounts_by_user_id(
        session,
        account.user_id,
    )

    print()
    print("User accounts:")

    for user_account in accounts:
        print(
            f"- {user_account.account_number} | "
            f"{user_account.balance} "
            f"{user_account.currency}"
        )