from flask import Flask, jsonify, request

app = Flask(__name__)

# Stockage en mémoire pour les items
items = []

@app.route("/", methods=["GET"])
def home():
    return "Hello World!", 200

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items), 200

@app.route("/items", methods=["POST"])
def add_item():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Item must have a name"}), 400
    items.append(data)
    return jsonify({"message": f"Item '{data['name']}' added!"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
