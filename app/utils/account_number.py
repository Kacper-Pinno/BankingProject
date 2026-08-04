import secrets


def generate_account_number() -> str:
    """
    Generate a simple account number for the project.

    This is NOT yet a real IBAN.
    """

    # Generate 14 random digits.
    random_part = "".join(
        str(secrets.randbelow(10))
        for _ in range(14)
    )

    # Example:
    # PL83910472518374
    return f"PL{random_part}"