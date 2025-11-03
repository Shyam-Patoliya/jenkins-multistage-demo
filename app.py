from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database for demonstration
inventory = [
    {"id": 1, "name": "Laptop", "quantity": 10},
    {"id": 2, "name": "Mouse", "quantity": 50},
    {"id": 3, "name": "Keyboard", "quantity": 30},
]

@app.route('/')
def hello():
    # Keep the original route
    return "Inventory API running successfully!"

@app.route('/inventory', methods=['GET'])
def get_inventory():
    """Returns the entire inventory list as JSON."""
    return jsonify(inventory)

@app.route('/inventory', methods=['POST'])
def add_item():
    """Adds a new item to the inventory."""
    # Get the new item data from the request body (as JSON)
    new_item = request.json
    
    if not new_item or 'id' not in new_item or 'name' not in new_item or 'quantity' not in new_item:
        # Return an error if the data is incomplete
        return jsonify({"error": "Invalid data. Requires 'id', 'name', and 'quantity'."}), 400

    inventory.append(new_item)
    
    # Return the new item and a 201 (Created) status code
    return jsonify(new_item), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
