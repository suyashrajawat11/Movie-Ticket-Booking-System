#!/usr/bin/env python3
"""
Simple Flask app for Movie Ticket Booking
Minimal version to ensure deployment works
"""

import os
from flask import Flask, jsonify, make_response
from flask_cors import CORS

# Create Flask app
app = Flask(__name__)

# Configure CORS - Allow all origins
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# Add CORS headers to all responses
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

# Root route
@app.route('/')
def root():
    return jsonify({
        'message': 'Movie Ticket Booking System',
        'status': 'running',
        'version': '1.0.0'
    })

# Handle preflight OPTIONS requests
@app.route('/api/<path:path>', methods=['OPTIONS'])
@app.route('/api/', methods=['OPTIONS'])
@app.route('/api', methods=['OPTIONS'])
def handle_options(path=None):
    response = make_response()
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

# API routes
@app.route('/api')
@app.route('/api/')
def api_root():
    return jsonify({
        'message': 'Movie Ticket Booking API',
        'version': '1.0.0',
        'endpoints': ['/api/health', '/api/movies', '/api/theaters', '/api/shows'],
        'status': 'API is working'
    })

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'message': 'API is running',
        'timestamp': '2024-01-01T12:00:00Z'
    })

@app.route('/api/movies')
def movies():
    # Sample movie data
    return jsonify([
        {
            'id': 1,
            'title': 'Avengers: Endgame',
            'genre': 'Action',
            'duration': 180,
            'language': 'English',
            'description': 'The epic conclusion to the Infinity Saga'
        },
        {
            'id': 2,
            'title': 'The Dark Knight',
            'genre': 'Action',
            'duration': 152,
            'language': 'English',
            'description': 'Batman faces the Joker in this acclaimed sequel'
        },
        {
            'id': 3,
            'title': 'Inception',
            'genre': 'Sci-Fi',
            'duration': 148,
            'language': 'English',
            'description': 'A mind-bending thriller about dreams within dreams'
        }
    ])

@app.route('/api/theaters')
def theaters():
    # Sample theater data
    return jsonify([
        {
            'id': 1,
            'name': 'PVR Cinemas',
            'city': 'Mumbai',
            'address': 'Phoenix Mall, Lower Parel',
            'halls': [
                {'id': 1, 'name': 'Screen 1', 'total_seats': 100},
                {'id': 2, 'name': 'Screen 2', 'total_seats': 150}
            ]
        },
        {
            'id': 2,
            'name': 'INOX',
            'city': 'Mumbai',
            'address': 'R City Mall, Ghatkopar',
            'halls': [
                {'id': 3, 'name': 'Screen A', 'total_seats': 120},
                {'id': 4, 'name': 'Screen B', 'total_seats': 80}
            ]
        }
    ])

@app.route('/api/shows')
def shows():
    # Sample show data
    return jsonify([
        {
            'id': 1,
            'movie_id': 1,
            'hall_id': 1,
            'start_time': '2024-01-01T18:00:00',
            'end_time': '2024-01-01T21:00:00',
            'price': 250.0
        },
        {
            'id': 2,
            'movie_id': 2,
            'hall_id': 2,
            'start_time': '2024-01-01T15:00:00',
            'end_time': '2024-01-01T17:32:00',
            'price': 200.0
        },
        {
            'id': 3,
            'movie_id': 3,
            'hall_id': 3,
            'start_time': '2024-01-01T20:00:00',
            'end_time': '2024-01-01T22:28:00',
            'price': 300.0
        }
    ])

# Debug route to list all routes
@app.route('/debug/routes')
def list_routes():
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append({
            'endpoint': rule.endpoint,
            'methods': list(rule.methods),
            'rule': str(rule)
        })
    return jsonify({'routes': routes})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    print(f"🚀 Starting Flask app on port {port}")
    print("📋 Available routes:")
    for rule in app.url_map.iter_rules():
        print(f"  {rule}")
    app.run(host='0.0.0.0', port=port, debug=False)
