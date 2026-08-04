from fastapi import FastAPI
from app.api.routes.users import router as users_router
from app.api.routes.accounts import router as accounts_router




app = FastAPI(title="Banking API", version="0.1.0")


#Regsiter the user endpoints.
app.include_router(users_router)
app.include_router(accounts_router)


@app.get("/health")
def health_check() -> dict[str, str]:
    """
    Simple endpoint used to verify
    that the API is running.
    """
    return {"status": "ok"}
