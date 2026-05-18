 # 🔐 Secured Auth API

A production-style asynchronous authentication backend built with **FastAPI**, **PostgreSQL**, and **Redis** implementing:

- OAuth2 Password Flow
- JWT Access & Refresh Tokens
- Dual Token Rotation
- Instant Logout with Redis Blacklist
- Fully Async Architecture
- Automated Testing
- GitHub Actions CI Pipeline
- Linting & Security Scanning

---

# 🚀 Features

✅ Fully asynchronous FastAPI backend  
✅ PostgreSQL with SQLAlchemy Async ORM  
✅ Redis-based token blacklist system  
✅ Access token + Refresh token flow  
✅ Refresh token rotation  
✅ Instant logout token revocation  
✅ Protected authenticated routes  
✅ Password hashing using bcrypt  
✅ Async automated tests with Pytest  
✅ Ruff linting integration  
✅ Bandit security scanning  
✅ GitHub Actions CI pipeline  

---

# 🛠 Tech Stack

| Technology | Purpose |
|---|---|
| FastAPI | Backend framework |
| PostgreSQL | Primary database |
| SQLAlchemy Async | Async ORM |
| Redis | Token blacklist storage |
| Docker | Redis container |
| JWT | Authentication tokens |
| Passlib + bcrypt | Password hashing |
| Pytest | Automated testing |
| Ruff | Linting |
| Bandit | Security scanning |
| GitHub Actions | CI pipeline |

---

# 📂 Project Structure

```text
secured-auth/
│
├── app/
│   ├── api/
│   │   ├── routes/
│   │   └── dependencies.py
│   │
│   ├── core/
│   │   └── config.py
│   │
│   ├── db/
│   │   ├── base.py
│   │   ├── redis.py
│   │   └── session.py
│   │
│   ├── models/
│   │   └── user.py
│   │
│   ├── schemas/
│   │   ├── token.py
│   │   └── user.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── token_blacklist_service.py
│   │   └── user_service.py
│   │
│   ├── utils/
│   │   ├── password.py
│   │   └── token.py
│   │
│   └── main.py
│
├── tests/
│   ├── conftest.py
│   └── test_auth_flow.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── create_tables.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

# ⚙️ Environment Variables

Create a `.env` file in the project root:

```env
APP_NAME=Secured Auth API
APP_ENV=development

DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/secured_auth_db

ACCESS_TOKEN_SECRET=your-super-secret-access-key
REFRESH_TOKEN_SECRET=your-super-secret-refresh-key

JWT_ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7

REDIS_URL=redis://localhost:6379/0
```

---

# 🐘 PostgreSQL Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE secured_auth_db;
```

---

# 🐳 Redis Setup with Docker

## Pull and Run Redis

```powershell
docker run --name secured-auth-redis -p 6379:6379 -d redis:7
```

## Verify Redis

```powershell
docker exec -it secured-auth-redis redis-cli ping
```

Expected output:

```text
PONG
```

---

# 📦 Installation

## Clone Repository

```bash
git clone <your-repository-url>
cd secured-auth
```

## Create Virtual Environment

### Windows

```powershell
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

# 📥 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄 Create Database Tables

```bash
python create_tables.py
```

---

# ▶️ Run Application

```bash
uvicorn app.main:app --reload
```

Application will run on:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# 🔑 Authentication Flow

## 1. Register User

```http
POST /auth/register
```

Request:

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

---

## 2. Login

```http
POST /auth/login
```

Form Data:

```text
username=user@example.com
password=password123
```

Response:

```json
{
  "access_token": "jwt_access_token",
  "refresh_token": "jwt_refresh_token",
  "token_type": "bearer"
}
```

---

## 3. Access Protected Route

```http
GET /users/me
```

Headers:

```text
Authorization: Bearer <access_token>
```

---

## 4. Refresh Tokens

```http
POST /auth/refresh
```

Request:

```json
{
  "refresh_token": "your_refresh_token"
}
```

Returns a new token pair.

---

## 5. Logout

```http
POST /auth/logout
```

Headers:

```text
Authorization: Bearer <access_token>
```

The access token gets blacklisted instantly in Redis.

---

# 🧪 Running Tests

Make sure Redis is running first.

Run tests:

```bash
pytest
```

Expected:

```text
4 passed
```

---

# 🧹 Ruff Linting

Run lint checks:

```bash
ruff check .
```

Auto-fix issues:

```bash
ruff check . --fix
```

---

# 🔒 Bandit Security Scan

Run security scan:

```bash
bandit -r app
```

---

# ⚡ GitHub Actions CI

The project includes automated CI pipeline with:

- PostgreSQL service
- Redis service
- Ruff linting
- Bandit security scan
- Pytest async tests

Workflow file:

```text
.github/workflows/ci.yml
```

---

# 📌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Register new user |
| POST | `/auth/login` | Login user |
| POST | `/auth/refresh` | Rotate tokens |
| POST | `/auth/logout` | Logout user |
| GET | `/users/me` | Get current authenticated user |

---

# 🔐 Security Features

- Password hashing with bcrypt
- JWT token authentication
- Separate access & refresh secrets
- Refresh token rotation
- Redis token blacklist
- Protected route authorization
- Token expiration handling
- Async-safe database architecture
