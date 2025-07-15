from flask import Flask, request, jsonify
from insert import insert_data
from display import get_items

app = Flask(__name__)

@app.route('/insert', methods=['POST'])
def insert_route():
    try:
        data = request.get_json()
        result = insert_data(data)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/display', methods=['GET'])
def display_route():
    try:
        items = get_items()
        return jsonify(items), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
