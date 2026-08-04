# Banking App
A backend banking application built with **Python**, **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **Alembic**, and **Docker**.

The project is currently under active development and is being built to explore backend development, relational database design, transaction processing, database migrations, containerization, and modern software engineering practices.

> Project Status: Early Development

---

## Project Goal
The goal of this project is to build a backend system that models the core functionality of a banking application.

The project will gradually include features such as:

- User management
- Bank accounts
- Account balances
- Money transfers
- Transaction history
- Database transaction integrity
- API endpoints
- Authentication and authorization
- Automated database migrations
- Containerized development environment

---

# Tech Stack

## Backend

- **Python** — primary programming language
- **FastAPI** — REST API framework
- **SQLAlchemy** — ORM and database interaction
- **Alembic** — database schema migrations

## Database

- **PostgreSQL 17** — relational database

## Infrastructure & Development

- **Docker** — containerization
- **Docker Compose** — local service orchestration
- **Git** — version control
- **GitHub** — source code repository

---

# Current Architecture
The application follows a layered architecture:

```
USER / CLIENT
      │
      │ HTTP Request
      ▼
┌───────────────┐
│    FastAPI    │
│    Backend    │
└───────┬───────┘
        │
        │ Python objects / queries
        ▼
┌───────────────┐
│  SQLAlchemy   │
│      ORM      │
└───────┬───────┘
        │
        │ SQL
        ▼
┌───────────────┐
│  PostgreSQL   │
│   Database    │
└───────────────┘
```

Database schema changes are managed separately through **Alembic migrations**.

```
SQLAlchemy Models
        │
        ▼
     Alembic
        │
        ▼
Migration Files
        │
        ▼
   PostgreSQL
```

---

# Current Project Structure
Current project structure:

```
Banking_APP/
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── app/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── accounts.py
│   │   │   └── users.py
│   │   └── __init__.py
│   ├── database/
│   │   ├── base.py
│   │   ├── database.py
│   │   ├── dependencies.py
│   │   └── __init__.py
│   ├── exceptions/
│   │   ├── account.py
│   │   ├── user.py
│   │   └── __init__.py
│   ├── models/
│   │   ├── account.py
│   │   ├── user.py
│   │   └── __init__.py
│   ├── repositories/
│   │   ├── account_repository.py
│   │   └── user_repository.py
│   ├── schemas/
│   │   ├── account.py
│   │   ├── customer.py
│   │   ├── user.py
│   │   └── __init__.py
│   ├── scripts/
│   │   ├── test_account_owner.py
│   │   ├── test_account_repository.py
│   │   ├── test_database.py
│   │   ├── test_relationships.py
│   │   ├── test_schemas.py
│   │   ├── test_transaction.py
│   │   └── test_user_repository.py
│   ├── services/
│   │   ├── account_service.py
│   │   └── user_service.py
│   ├── utils/
│   │   ├── account_number.py
│   │   └── __init__.py
│   ├── main.py
│   └── __init__.py
│
├── alembic.ini
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```
The structure will evolve as additional banking functionality is implemented.

---

# Current Project State

## What is implemented
- FastAPI entry point in `app/main.py`
- Health check endpoint: `GET /health`
- User registration endpoint: `POST /users`
- Account creation endpoint: `POST /accounts`
- Account retrieval endpoint: `GET /accounts/{account_id}`
- User account list endpoint: `GET /users/{user_id}/accounts`
- Database integration using SQLAlchemy ORM and request-scoped sessions
- Pydantic schemas for request validation and response serialization
- Repository layer for user and account database operations
- Service layer for business rules and domain validation
- Alembic migration scaffolding for schema changes
- Environment variable support via `.env` for database configuration

## What works today
- Create a new user with unique email validation
- Open a new bank account for an existing user
- Retrieve account details by account ID
- List all accounts belonging to a given user

---

# PostgreSQL
PostgreSQL is used as the primary relational database.

The database can run inside Docker using the official PostgreSQL 17 image.

The `docker-compose.yml` service is configured as:

```yaml
services:
    postgres:
        image: postgres:17
        container_name: banking_postgres

        environment:
            POSTGRES_USER: ${POSTGRES_USER}
            POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
            POSTGRES_DB: ${POSTGRES_DB}

        ports:
        - "5432:5432"

        volumes:
        - postgres_data:/var/lib/postgresql/data

volumes:
    postgres_data:
```

A Docker volume is used so that database data persists when the PostgreSQL container is restarted.

---

# Environment Variables
Database credentials are provided through environment variables rather than being stored directly in `docker-compose.yml`.

Create a local `.env` file:

```
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_DB=your_database
```

The `.env` file contains local credentials and must not be committed to Git.

It should be included in `.gitignore`:

```
.env
```

---

# Running PostgreSQL
Start the PostgreSQL container:

```
docker compose up -d
```

Check running containers:

```
docker ps
```

The PostgreSQL container should appear as:

```
banking_postgres
```

Stop the services:

```
docker compose down
```

Database data remains stored in the Docker volume.

---

# Database Migrations
Database schema changes are managed using **Alembic**.

Instead of manually modifying production database tables, schema changes are represented as migration files.

Create a new migration:

```
alembic revision --autogenerate -m "migration description"
```

Apply all migrations:

```
alembic upgrade head
```

View migration history:

```
alembic history
```

Roll back the most recent migration:

```
alembic downgrade -1
```

Migration files are stored inside:

```
alembic/versions/
```

These files should be committed to Git so that the database schema can be reproduced across environments.

---

# Python Dependencies
Python dependencies are stored in:

```
requirements.txt
```

Install them with:

```
pip install -r requirements.txt
```

---

# Local Development Setup

## 1. Clone the repository

```
git clone <repository-url>
cd Banking_APP
```

## 2. Create a virtual environment

```
python -m venv .venv
```

Activate it on Windows:

```
.venv\Scripts\activate
```

## 3. Install dependencies

```
pip install -r requirements.txt
```

## 4. Configure environment variables
Create a `.env` file and provide the required PostgreSQL configuration.

## 5. Start PostgreSQL

```
docker compose up -d
```

## 6. Apply database migrations

```
alembic upgrade head
```

## 7. Start the FastAPI application

```
uvicorn app.main:app --reload
```

---

# Development Workflow
A typical development workflow for the project is:

```
1. Modify Python / SQLAlchemy models
              ↓
2. Generate Alembic migration
              ↓
3. Review migration
              ↓
4. Apply migration to PostgreSQL
              ↓
5. Test application
              ↓
6. Commit changes with Git
              ↓
7. Push changes to GitHub
```

Example Git workflow:

```
git status
git add .
git commit -m "Describe the changes"
git push
```

---

# Security
Sensitive information such as:

- Database passwords
- API keys
- Authentication secrets
- Tokens
- Private credentials

should never be committed to the repository.

Secrets should be stored using environment variables or appropriate secret-management systems.

---

# Planned Development
The project is being developed incrementally.

Planned areas include:

- User database model
- Customer profile model
- Bank account model
- Transaction model
- Ledger system
- Money transfer logic
- Transaction integrity
- Database locking
- Idempotent transactions
- FastAPI endpoints
- Request/response validation
- Authentication
- Authorization
- Error handling
- Logging
- Automated tests
- API documentation
- CI/CD pipeline

---

# Concepts Explored
This project is also intended as a practical environment for learning and applying:

- REST API design
- Relational database modelling
- SQL
- Object Relational Mapping
- Database migrations
- ACID transactions
- Database locking
- Atomic operations
- Financial ledger design
- Idempotency
- Containerization
- Environment configuration
- Git workflows
- Backend architecture

---

# Disclaimer
This project is an educational backend banking application.

It is not intended for use as a real financial system and should not be considered production-ready banking software.

---

# Status
**Current stage:** Backend and database infrastructure setup.

PostgreSQL, Docker, SQLAlchemy, Alembic, and the initial FastAPI project environment are being established before implementing the core banking domain logic.
