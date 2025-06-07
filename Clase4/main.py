from flask import Flask, request, jsonify

app = Flask(__name__)

items = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Bad Request', 'message': "Field 'name' is required."}), 400

    item = {
        'id': len(items) + 1,
        'name': data['name']
    }
    items.append(item)
    return jsonify(item), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
