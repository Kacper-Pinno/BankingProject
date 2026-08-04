from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import register_user
from app.schemas.account import AccountResponse
from app.services.account_service import get_user_accounts

from app.exceptions.user import (
    UserAlreadyExistsError,
    UserNotFoundError,
)


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user_data: UserCreate,
    session: Session = Depends(get_db),
) -> UserResponse:
    """
    Register a new user.
    """

    try:

        # Start ONE transaction for the registration.
        with session.begin():

            user = register_user(
                session=session,
                email=str(user_data.email),
                first_name=user_data.first_name,
                last_name=user_data.last_name,
            )

        return UserResponse.model_validate(user)

    except UserAlreadyExistsError as error:

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        ) from error


@router.get(
    "/{user_id}/accounts",
    response_model=list[AccountResponse],
)
def get_user_accounts_endpoint(
    user_id: int,
    session: Session = Depends(get_db),
) -> list[AccountResponse]:
    """
    Return every bank account belonging to a user.
    """

    try:

        accounts = get_user_accounts(
            session=session,
            user_id=user_id,
        )

        # Convert each SQLAlchemy Account object
        # into an AccountResponse schema.
        return [
            AccountResponse.model_validate(account)
            for account in accounts
        ]

    except UserNotFoundError as error:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error),
        ) from error