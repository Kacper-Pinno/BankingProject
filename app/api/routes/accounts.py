from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.account import (
    AccountCreate,
    AccountResponse,
)
from app.services.account_service import (
    get_account,
    open_account,
)

from app.exceptions.account import (
    AccountNotFoundError,
    AccountNumberCollisionError,
)

from app.exceptions.user import (
    UserNotFoundError,
)


# --------------------------------------------------
# ACCOUNT ROUTER
# --------------------------------------------------
# Groups all account-related API endpoints.
#
# Because prefix="/accounts", an endpoint defined
# as @router.post("") becomes:
#
# POST /accounts
#
router = APIRouter(
    prefix="/accounts",
    tags=["accounts"],
)


# --------------------------------------------------
# CREATE ACCOUNT
# --------------------------------------------------

@router.post(
    "",
    response_model=AccountResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_account_endpoint(
    account_data: AccountCreate,
    session: Session = Depends(get_db),
) -> AccountResponse:
    """
    Open a new bank account for an existing user.
    """

    try:
        # Everything inside this block belongs
        # to one database transaction.
        with session.begin():

            account = open_account(
                session=session,
                user_id=account_data.user_id,
                currency=account_data.currency,
            )

        return AccountResponse.model_validate(account)

    except UserNotFoundError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error



@router.get(
    "/{account_id}",
    response_model=AccountResponse,
)
def get_account_endpoint(
    account_id: int,
    session: Session = Depends(get_db),
) -> AccountResponse:
    """
    Retrieve one bank account by ID.
    """

    try:

        account = get_account(
            session=session,
            account_id=account_id,
        )

        # Convert SQLAlchemy Account
        # into our API response schema.
        return AccountResponse.model_validate(
            account
        )

    except AccountNotFoundError as error:

        # The requested account doesn't exist,
        # so HTTP 404 is appropriate.
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error),
        ) from error