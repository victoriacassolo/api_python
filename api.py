from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

movies = [
    {"id": 1, "nome": "The Avengers", "nota": 10},
    {"id": 2, "nome": "Fast and Furious", "nota": 7},
    {"id": 3, "nome": "Inside Out", "nota": 9},
]

@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(movies)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
