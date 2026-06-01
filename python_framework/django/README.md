# Django CRUD

Self-contained CRUD API built with Django and Django REST Framework. Uses an in-memory SQLite database.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python django_crud.py runserver
```

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | /items/ | List all items |
| GET | /items/{id}/ | Get an item |
| POST | /items/ | Create an item |
| PUT | /items/{id}/ | Update an item |
| DELETE | /items/{id}/ | Delete an item |

## How It Works

**Configuration** — Django settings are configured in-code via `settings.configure()` instead of a separate `settings.py`. Sets up an in-memory SQLite DB, installs `rest_framework`, and wires up middleware.

**Model** — Defines the `Item` table with `name`, `description`, and `price` fields. Django maps this to SQLite automatically on startup.

**Serializer** — `ItemSerializer` handles converting `Item` model instances to/from JSON.

**ViewSet** — `ModelViewSet` auto-generates all 5 CRUD endpoints — no need to write individual route handlers like in Flask or FastAPI.

**Router** — `router.register(r"items", ItemViewSet)` auto-generates URLs: `GET/POST /items/` and `GET/PUT/DELETE /items/{id}/`.

**Startup** — Runs migrations to create the DB schema, then starts the dev server — all from `python django_crud.py runserver`.

> Key difference vs Flask/FastAPI: one `ModelViewSet` replaces ~50 lines of manual route handlers, but it's also the most opinionated and heavyweight of the three.

## Example

```bash
curl -X POST http://localhost:8000/items/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Widget", "price": 9.99}'
```
