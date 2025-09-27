from flask import Flask, jsonify
import os

app = Flask(__name__)

# Simple CORS handling - no external library
@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

@app.route('/')
def home():
    return jsonify({'message': 'Movie Booking API', 'status': 'running'})

@app.route('/api/movies')
def movies():
    return jsonify([
        {'id': 1, 'title': 'Avengers: Endgame', 'genre': 'Action', 'duration': 180},
        {'id': 2, 'title': 'The Dark Knight', 'genre': 'Action', 'duration': 152},
        {'id': 3, 'title': 'Inception', 'genre': 'Sci-Fi', 'duration': 148}
    ])

@app.route('/api/theaters')
def theaters():
    return jsonify([
        {'id': 1, 'name': 'PVR Cinemas', 'city': 'Mumbai'},
        {'id': 2, 'name': 'INOX', 'city': 'Mumbai'}
    ])

@app.route('/api/shows')
def shows():
    return jsonify([
        {'id': 1, 'movie_id': 1, 'hall_id': 1, 'start_time': '2024-01-01T18:00:00', 'price': 250},
        {'id': 2, 'movie_id': 2, 'hall_id': 2, 'start_time': '2024-01-01T15:00:00', 'price': 200}
    ])

@app.route('/api/health')
def health():
    return jsonify({'status': 'healthy', 'message': 'API working'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
