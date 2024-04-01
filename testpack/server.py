from flask import Flask, jsonify

from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/api/data", methods=['GET'])
def get_data():
    data = {"name": "test", "age": 20}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)