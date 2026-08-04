from pydantic import ValidationError

from app.schemas.user import UserCreate


# --------------------------------------------
# VALID DATA
# --------------------------------------------

valid_user = UserCreate(
    email="mike@example.com",
    first_name="Mike",
    last_name="Smith",
)

print("Valid user:")
print(valid_user)


# --------------------------------------------
# INVALID DATA
# --------------------------------------------

try:

    invalid_user = UserCreate(
        email="not-an-email",
        first_name="Mike",
        last_name="Smith",
    )

except ValidationError as error:

    print()
    print("Validation failed:")
    print(error)