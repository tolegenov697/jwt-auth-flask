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
git clone https://github.com/your-username/jwt-auth-app.git
cd jwt-auth-app
```
### Step 2: Start services
```bash
docker-compose up --build
```
API will be available at: http://localhost:5000


### ➕ Register a User

```bash
curl -X POST http://localhost:5000/register \
  -H "Content-Type: application/json" \
  -d '{"username":"admin", "password":"1234"}'
```

Expected response:
```bash
{"msg":"User created successfully"}
```


### 🔑 Login to Get JWT Token
```bash
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin", "password":"1234"}'
```
Expected response:
```bash
{
  "access_token": "your-jwt-token-here"
}
```

