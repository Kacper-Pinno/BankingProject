from app.database.database import SessionLocal
from app.repositories.user_repository import (
    get_user_by_email,
    get_user_by_id,
)


with SessionLocal() as session:

    # ----------------------------------------
    # FIND BY EMAIL
    # ----------------------------------------

    user = get_user_by_email(
        session,
        "example@example.com",
    )

    if user is None:
        print("User not found.")
        raise SystemExit


    print("Found by email:")
    print(
        f"{user.id} | "
        f"{user.first_name} "
        f"{user.last_name}"
    )


    # ----------------------------------------
    # FIND BY ID
    # ----------------------------------------

    same_user = get_user_by_id(
        session,
        user.id,
    )


    if same_user is None:
        print("User not found by ID.")
        raise SystemExit


    print()
    print("Found by ID:")
    print(
        f"{same_user.id} | "
        f"{same_user.email}"
    )