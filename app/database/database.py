import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    echo=True,
)

# SessionLocal is a SESSION FACTORY.

# It does NOT represent one database session.
# Calling SessionLocal() creates a new session.

SessionLocal = sessionmaker(
    bind=engine,

    # don't automatically commit changes.
    # Explicit control over transactions.
    autoflush=False,

    # Keep ORM objects usable after commit without immediately reloading them.
    expire_on_commit=False,
)
