#!/usr/bin/env python3
"""
Fix backend data to match frontend expectations
"""

import os
import random
from flask import Flask, jsonify, request

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
        {
            'id': 1,
            'title': 'Avengers: Endgame',
            'description': 'The epic conclusion to the Infinity Saga that became a defining moment in cinema history.',
            'duration': 181,
            'release_date': '2019-04-26',
            'genre': 'Action',
            'language': 'English'
        },
        {
            'id': 2,
            'title': 'The Dark Knight',
            'description': 'Batman faces the Joker in this acclaimed sequel that redefined superhero cinema.',
            'duration': 152,
            'release_date': '2008-07-18',
            'genre': 'Action',
            'language': 'English'
        },
        {
            'id': 3,
            'title': 'Inception',
            'description': 'A mind-bending thriller about dreams within dreams from Christopher Nolan.',
            'duration': 148,
            'release_date': '2010-07-16',
            'genre': 'Sci-Fi',
            'language': 'English'
        },
        {
            'id': 4,
            'title': 'Parasite',
            'description': 'A masterpiece of social commentary that won the Academy Award for Best Picture.',
            'duration': 132,
            'release_date': '2019-05-30',
            'genre': 'Thriller',
            'language': 'Korean'
        },
        {
            'id': 5,
            'title': 'Interstellar',
            'description': 'A visually stunning space epic about love, sacrifice, and the survival of humanity.',
            'duration': 169,
            'release_date': '2014-11-07',
            'genre': 'Sci-Fi',
            'language': 'English'
        }
    ])

@app.route('/api/theaters')
def theaters():
    return jsonify([
        {
            'id': 1,
            'name': 'PVR Cinemas Phoenix',
            'address': 'Phoenix Marketcity, Kurla West',
            'city': 'Mumbai',
            'state': 'Maharashtra',
            'country': 'India',
            'pincode': '400070',
            'halls': [
                {
                    'id': 1, 
                    'name': 'Screen 1', 
                    'total_seats': 180, 
                    'type': 'Premium',
                    'rows': [
                        {'id': 1, 'row_number': 1, 'seat_count': 15},
                        {'id': 2, 'row_number': 2, 'seat_count': 15},
                        {'id': 3, 'row_number': 3, 'seat_count': 18},
                        {'id': 4, 'row_number': 4, 'seat_count': 18},
                        {'id': 5, 'row_number': 5, 'seat_count': 18},
                        {'id': 6, 'row_number': 6, 'seat_count': 18},
                        {'id': 7, 'row_number': 7, 'seat_count': 18},
                        {'id': 8, 'row_number': 8, 'seat_count': 18},
                        {'id': 9, 'row_number': 9, 'seat_count': 18},
                        {'id': 10, 'row_number': 10, 'seat_count': 18}
                    ]
                },
                {
                    'id': 2, 
                    'name': 'Screen 2', 
                    'total_seats': 150, 
                    'type': 'Standard',
                    'rows': [
                        {'id': 11, 'row_number': 1, 'seat_count': 12},
                        {'id': 12, 'row_number': 2, 'seat_count': 12},
                        {'id': 13, 'row_number': 3, 'seat_count': 15},
                        {'id': 14, 'row_number': 4, 'seat_count': 15},
                        {'id': 15, 'row_number': 5, 'seat_count': 15},
                        {'id': 16, 'row_number': 6, 'seat_count': 15},
                        {'id': 17, 'row_number': 7, 'seat_count': 15},
                        {'id': 18, 'row_number': 8, 'seat_count': 15},
                        {'id': 19, 'row_number': 9, 'seat_count': 15},
                        {'id': 20, 'row_number': 10, 'seat_count': 21}
                    ]
                }
            ]
        },
        {
            'id': 2,
            'name': 'INOX R City',
            'address': 'R City Mall, Ghatkopar West',
            'city': 'Mumbai',
            'state': 'Maharashtra',
            'country': 'India',
            'pincode': '400086',
            'halls': [
                {
                    'id': 4, 
                    'name': 'Screen A', 
                    'total_seats': 200, 
                    'type': 'IMAX',
                    'rows': [
                        {'id': 31, 'row_number': 1, 'seat_count': 16},
                        {'id': 32, 'row_number': 2, 'seat_count': 16},
                        {'id': 33, 'row_number': 3, 'seat_count': 20},
                        {'id': 34, 'row_number': 4, 'seat_count': 20},
                        {'id': 35, 'row_number': 5, 'seat_count': 20},
                        {'id': 36, 'row_number': 6, 'seat_count': 20},
                        {'id': 37, 'row_number': 7, 'seat_count': 20},
                        {'id': 38, 'row_number': 8, 'seat_count': 20},
                        {'id': 39, 'row_number': 9, 'seat_count': 24},
                        {'id': 40, 'row_number': 10, 'seat_count': 24}
                    ]
                }
            ]
        }
    ])

@app.route('/api/shows')
def shows():
    return jsonify([
        {'id': 1, 'movie_id': 1, 'hall_id': 1, 'start_time': '2024-01-15T10:00:00', 'end_time': '2024-01-15T13:01:00', 'price': 350.0},
        {'id': 2, 'movie_id': 1, 'hall_id': 1, 'start_time': '2024-01-15T14:00:00', 'end_time': '2024-01-15T17:01:00', 'price': 400.0},
        {'id': 3, 'movie_id': 1, 'hall_id': 1, 'start_time': '2024-01-15T18:30:00', 'end_time': '2024-01-15T21:31:00', 'price': 450.0},
        {'id': 4, 'movie_id': 2, 'hall_id': 4, 'start_time': '2024-01-15T11:00:00', 'end_time': '2024-01-15T13:32:00', 'price': 500.0},
        {'id': 5, 'movie_id': 2, 'hall_id': 4, 'start_time': '2024-01-15T15:00:00', 'end_time': '2024-01-15T17:32:00', 'price': 550.0}
    ])

@app.route('/api/health')
def health():
    return jsonify({'status': 'healthy', 'message': 'API working'})

@app.route('/api/bookings/availability')
def booking_availability():
    show_id = request.args.get('show_id')
    if not show_id:
        return jsonify({'error': 'show_id is required'}), 400
    
    # Generate realistic seat availability
    show_hall_map = {
        '1': 1, '2': 1, '3': 1,  # Hall 1 
        '4': 4, '5': 4,  # Hall 4 (IMAX)
    }
    
    hall_id = show_hall_map.get(show_id, 1)
    
    # Define seat layouts for each hall
    hall_layouts = {
        1: [15, 15, 18, 18, 18, 18, 18, 18, 18, 18],  # Hall 1
        4: [16, 16, 20, 20, 20, 20, 20, 20, 24, 24],  # Hall 4 (IMAX)
    }
    
    layout = hall_layouts.get(hall_id, [15, 15, 18, 18, 18, 18, 18, 18, 18, 18])
    
    # Generate seat availability
    availability = []
    
    for row_idx, seat_count in enumerate(layout):
        row_number = row_idx + 1
        for seat_num in range(1, seat_count + 1):
            # Randomly make some seats booked (30% chance)
            is_booked = random.random() < 0.3
            availability.append({
                'row_number': row_number,
                'seat_number': seat_num,
                'status': 'booked' if is_booked else 'available',
                'seat_id': f"R{row_number}S{seat_num}"
            })
    
    return jsonify({
        'show_id': int(show_id),
        'hall_id': hall_id,
        'availability': availability
    })

@app.route('/api/bookings', methods=['POST'])
def create_booking():
    data = request.get_json()
    
    # Simulate booking creation
    booking_id = random.randint(1000, 9999)
    
    return jsonify({
        'booking_id': booking_id,
        'show_id': data.get('show_id'),
        'seats': data.get('seats', []),
        'total_price': data.get('total_price', 0),
        'status': 'confirmed',
        'booking_reference': f"BK{booking_id}",
        'message': 'Booking confirmed successfully!'
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
