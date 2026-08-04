from typing import Literal

from pydantic import BaseModel, EmailStr

from app.schemas.account import AccountResponse
from app.schemas.user import UserResponse


SupportedCurrency = Literal[
    "PLN",
    "EUR",
    "GBP",
    "USD",
]


class CustomerRegister(BaseModel):
    """
    Information required to register a new customer.
    """

    email: EmailStr
    first_name: str
    last_name: str
    currency: SupportedCurrency


class CustomerRegisterResponse(BaseModel):
    """
    Complete response after customer registration.
    """

    user: UserResponse
    account: AccountResponse