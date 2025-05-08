# 🛡️ JWT Auth App with Flask + PostgreSQL + Docker

A simple Flask API with user registration, login, and JWT-protected routes. Powered by Flask-JWT-Extended, SQLAlchemy, PostgreSQL, and Docker.

## 🚀 Features

- User registration & login
- JWT token generation
- Protected routes using `@jwt_required`
- PostgreSQL database integration
- Dockerized backend & DB
- Ready for CI/CD and testing

## 🐳 Run with Docker

### Step 1: Clone the repo

```bash
git clone https://github.com/tolegenov697/jwt-auth-flask.git
cd jwt-auth-flask
```
### Step 2: Start services
```bash
docker-compose up --build
```
API will be available at: http://localhost:5000


### ➕ Register a User

```bash 
curl -X POST http://localhost:5000/register -H "Content-Type: application/json" -d "{\"username\": \"admin\", \"password\": \"1234\"}"
```

Expected response:
```bash
{"msg":"User created successfully"}
```


### 🔑 Login to Get JWT Token
```bash
curl -X POST http://localhost:5000/login -H "Content-Type: application/json" -d "{\"username\": \"admin\", \"password\": \"1234\"}"
```
Expected response:
```bash
{
  "access_token": "your-jwt-token-here"
}
```

### 🔐 Access Protected Route
Replace <your-jwt-token> with the token from the login response.
```bash
curl -X GET http://localhost:5000/protected -H "Authorization: Bearer <your-jwt-token>"
```
Expected response:
```bash
{
  "logged_in_as": "admin"
}
```

### 🧪 Run Tests (if using CI/CD or local testing)
Inside backend/, you can run:
```bash
pytest
```
Expected response:
```bash
================================================= test session starts =================================================
platform win32 -- Python 3.11.9, pytest-8.3.5, pluggy-1.5.0
rootdir: C:\{...}\jwt-auth-flask\backend
plugins: anyio-4.6.2.post1
collected 1 item

test_auth.py .                                                                                                   [100%]

================================================== 1 passed in 1.09s ==================================================
```
### 📦 Project Structure
```bash
jwt-auth-flask/
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── auth.py
│   ├── test_auth.py
│   └── Dockerfile
├── db/
│   └── init.sql
├── docker-compose.yml
└── README.md
```

### ✅ Final Project Criteria
#### ✔ Dockerized Flask + PostgreSQL
#### ✔ Connected services (backend ↔ db)
#### ✔ Auth system (JWT)
#### ✔ CI/CD ready with test
#### ✔ Bash command examples
