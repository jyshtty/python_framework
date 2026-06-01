from flask import Flask, jsonify, request, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

# In-memory storage
items: dict[int, dict] = {}
next_id = 1


def item_or_404(item_id: int) -> dict:
    if item_id not in items:
        abort(404, description="Item not found")
    return items[item_id]


@app.get("/items")
def list_items():
    return jsonify([{"id": k, **v} for k, v in items.items()])


@app.get("/items/<int:item_id>")
def get_item(item_id: int):
    return jsonify({"id": item_id, **item_or_404(item_id)})


@app.post("/items")
def create_item():
    global next_id
    data = request.get_json()
    if not data or "name" not in data or "price" not in data:
        abort(400, description="name and price are required")
    items[next_id] = {
        "name": data["name"],
        "description": data.get("description"),
        "price": float(data["price"]),
    }
    response = jsonify({"id": next_id, **items[next_id]})
    next_id += 1
    return response, 201


@app.put("/items/<int:item_id>")
def update_item(item_id: int):
    item_or_404(item_id)
    data = request.get_json() or {}
    for field in ("name", "description", "price"):
        if field in data and data[field] is not None:
            items[item_id][field] = data[field]
    return jsonify({"id": item_id, **items[item_id]})


@app.delete("/items/<int:item_id>")
def delete_item(item_id: int):
    item_or_404(item_id)
    del items[item_id]
    return "", 204


if __name__ == "__main__":
    app.run(debug=True, port=8000)
