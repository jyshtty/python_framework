# FastAPI CRUD

Simple CRUD API built with FastAPI and Pydantic. Uses in-memory storage.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn fastapi_crud:app --reload
```

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | /items | List all items |
| GET | /items/{id} | Get an item |
| POST | /items | Create an item |
| PUT | /items/{id} | Update an item |
| DELETE | /items/{id} | Delete an item |

## How It Works

**App & routing** — A `FastAPI()` instance is created and routes are defined using decorators like `@app.post("/items")`. FastAPI maps each decorator directly to an HTTP method and path.

**Pydantic models** — `ItemCreate`, `ItemUpdate`, and `ItemResponse` are Pydantic models that handle request validation and response serialization automatically. Invalid payloads are rejected with a 422 before reaching the route handler.

**In-memory storage** — Items are stored in a plain dict `items: dict[int, dict]` with an auto-incrementing `next_id`. Data is lost on restart.

**Route handlers** — Each handler is a plain Python function. FastAPI injects path params, request bodies, and query params based on type annotations — no manual parsing needed.

> Key difference vs Flask/Django: FastAPI gives you automatic request validation, response serialization, and interactive docs (at `/docs`) out of the box with minimal boilerplate.

## Example

```bash
curl -X POST http://localhost:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Widget", "price": 9.99}'
```
