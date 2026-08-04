from decimal import Decimal
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field




SupportedCurrency = Literal[
    "PLN",
    "EUR",
    "GBP",
    "USD",
]

class AccountCreate(BaseModel):

    #Data required to create a bank account.

    user_id: int

    #ISO-style 3-letter currency code.
    currency: SupportedCurrency

class AccountResponse(BaseModel):

    # Account data returned to the client.

    # Allows Pydentic to read attributes directly from SQLAlchemy Account objects.

    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    account_number: str
    currency: str
    balance: Decimal
    status: str


