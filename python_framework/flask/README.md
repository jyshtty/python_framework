# Flask CRUD

Simple CRUD API built with Flask. Uses in-memory storage.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python flask_crud.py
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

**App & routing** — A `Flask()` instance is created and routes are defined using decorators like `@app.post("/items")`. Flask maps each decorator to an HTTP method and path.

**Request parsing** — Unlike FastAPI, there are no model classes. `request.get_json()` returns a raw dict and fields are accessed manually. Missing or invalid fields must be checked explicitly.

**`item_or_404` helper** — A small helper that looks up an item by ID and calls `abort(404)` if not found, keeping the route handlers clean.

**In-memory storage** — Items are stored in a plain dict `items: dict[int, dict]` with an auto-incrementing `next_id`. Data is lost on restart.

**Responses** — All responses are wrapped in `jsonify()` to serialize dicts to JSON. Status codes are returned as a second value in a tuple (e.g. `return response, 201`).

> Key difference vs FastAPI/Django: Flask is the most minimal of the three — no validation, no ORM, no auto-generated docs. You wire everything up yourself.

## Example

```bash
curl -X POST http://localhost:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Widget", "price": 9.99}'
```
