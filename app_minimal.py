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

@app.route('/api/analytics/overview')
def analytics_overview():
    return jsonify({
        'total_bookings': 150,
        'total_revenue': 45000,
        'popular_movies': [
            {'title': 'Avengers: Endgame', 'bookings': 85},
            {'title': 'The Dark Knight', 'bookings': 65}
        ],
        'daily_revenue': [
            {'date': '2024-01-01', 'revenue': 15000},
            {'date': '2024-01-02', 'revenue': 18000},
            {'date': '2024-01-03', 'revenue': 12000}
        ]
    })

@app.route('/api/analytics/movie/<int:movie_id>')
def movie_analytics(movie_id):
    return jsonify({
        'movie_id': movie_id,
        'total_bookings': 85,
        'total_revenue': 21250,
        'average_rating': 4.5,
        'booking_trends': [
            {'date': '2024-01-01', 'bookings': 25},
            {'date': '2024-01-02', 'bookings': 35},
            {'date': '2024-01-03', 'bookings': 25}
        ]
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
