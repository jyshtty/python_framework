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

## Example

```bash
curl -X POST http://localhost:8000/items/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Widget", "price": 9.99}'
```
