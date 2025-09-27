#!/usr/bin/env python3
"""
Simple Flask app for Movie Ticket Booking
Minimal version to ensure deployment works
"""

import os
from flask import Flask, jsonify
from flask_cors import CORS

# Create Flask app
app = Flask(__name__)

# Configure CORS
CORS(app, origins=[
    'https://dashing-horse-e44477.netlify.app',
    'https://*.netlify.app',
    'http://localhost:5173',
    'http://localhost:3000'
])

# Root route
@app.route('/')
def root():
    return jsonify({
        'message': 'Movie Ticket Booking System',
        'status': 'running',
        'version': '1.0.0'
    })

# API routes
@app.route('/api/')
def api_root():
    return jsonify({
        'message': 'Movie Ticket Booking API',
        'version': '1.0.0',
        'endpoints': ['/health', '/movies', '/theaters', '/shows']
    })

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'message': 'API is running'
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
            'language': 'English'
        },
        {
            'id': 2,
            'title': 'The Dark Knight',
            'genre': 'Action',
            'duration': 152,
            'language': 'English'
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
            'halls': [
                {'id': 1, 'name': 'Screen 1', 'total_seats': 100},
                {'id': 2, 'name': 'Screen 2', 'total_seats': 150}
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
            'price': 250.0
        }
    ])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
