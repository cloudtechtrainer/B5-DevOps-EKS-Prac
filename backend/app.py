from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route('/')
def serve_frontend():
    return send_from_directory('', 'index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hello from the backend!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
