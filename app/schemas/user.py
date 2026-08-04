from pydantic import BaseModel, EmailStr, ConfigDict

class UserCreate(BaseModel):
    """
    Data required from the client
    when creating a new user.
    """

    email: EmailStr
    first_name: str
    last_name: str


class UserResponse(BaseModel):
    """
    Data returned to the client
    when a user is created or retrieved.
    """

    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    first_name: str
    last_name: str

    