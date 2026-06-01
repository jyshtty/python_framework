# Async FastAPI CRUD

Async CRUD API built with FastAPI using `async def` route handlers and an `asyncio.Lock` for safe concurrent access.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn async_fastapi_crud:app --reload
```

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | /items | Create an item |
| PUT | /items/{id} | Update an item |
| GET | /items | List all items |
| GET | /items/{id} | Get an item |
| DELETE | /items/{id} | Delete an item |

## How It Works

**`async def` handlers** — All route handlers are defined with `async def`, allowing FastAPI to handle them concurrently via an event loop. While one request is awaiting I/O (e.g. a DB call), others can be processed.

**`asyncio.Lock`** — Since the in-memory dict is shared state, an `asyncio.Lock` prevents race conditions under concurrent requests. Each handler acquires the lock before reading or writing.

**When to use async** — Async shines when handlers do I/O-bound work (DB queries, HTTP calls, file reads). For CPU-bound work, use background tasks or a process pool instead.

> Key difference vs the sync FastAPI version: route handlers are `async def` and shared state is protected with `asyncio.Lock` instead of relying on the GIL.

## Example

```bash
curl -X POST http://localhost:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Widget", "price": 9.99}'
```
