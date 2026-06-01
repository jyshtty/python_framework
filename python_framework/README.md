# Python Framework Comparison

Simple CRUD API implemented in three Python web frameworks for comparison.

## Structure

| Directory | Framework | Docs |
|-----------|-----------|------|
| `fastapi/` | FastAPI + Pydantic | [README](fastapi/README.md) |
| `flask/` | Flask | [README](flask/README.md) |
| `django/` | Django + Django REST Framework | [README](django/README.md) |

## How It Works

All three apps implement the same `/items` CRUD API with identical endpoints, but differ in how much they do for you:

| | FastAPI | Flask | Django |
|---|---|---|---|
| Request validation | Automatic (Pydantic) | Manual | Automatic (DRF serializers) |
| Response serialization | Automatic | `jsonify()` | Automatic |
| Routing | Decorators + type hints | Decorators | ViewSet + Router |
| Storage | In-memory dict | In-memory dict | SQLite (in-memory) |
| Auto-generated docs | Yes (`/docs`) | No | No |
| Boilerplate | Low | Lowest | Highest |

**FastAPI** is the most modern — type annotations drive validation, serialization, and docs automatically.

**Flask** is the most minimal — you control everything manually, making it simple but verbose for larger apps.

**Django** is the most full-featured — `ModelViewSet` auto-generates all endpoints, but requires the most setup and is the most opinionated.

## Quickstart

Each app exposes the same `/items` CRUD endpoints. Navigate into a subdirectory and follow its README to install dependencies and run the server.
