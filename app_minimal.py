#!/usr/bin/env python3
import os
import random
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for created items
movies_storage = [
    {
        'id': 1,
        'title': 'Avengers: Endgame',
        'description': 'The epic conclusion to the Infinity Saga',
        'duration': 181,
        'release_date': '2019-04-26',
        'genre': 'Action',
        'language': 'English'
    },
    {
        'id': 2,
        'title': 'The Dark Knight',
        'description': 'Batman faces the Joker in this acclaimed sequel',
        'duration': 152,
        'release_date': '2008-07-18',
        'genre': 'Action',
        'language': 'English'
    },
    {
        'id': 3,
        'title': 'Inception',
        'description': 'A mind-bending thriller about dreams within dreams',
        'duration': 148,
        'release_date': '2010-07-16',
        'genre': 'Sci-Fi',
        'language': 'English'
    },
    {
        'id': 4,
        'title': 'Parasite',
        'description': 'A masterpiece of social commentary',
        'duration': 132,
        'release_date': '2019-05-30',
        'genre': 'Thriller',
        'language': 'Korean'
    },
    {
        'id': 5,
        'title': 'Interstellar',
        'description': 'A visually stunning space epic',
        'duration': 169,
        'release_date': '2014-11-07',
        'genre': 'Sci-Fi',
        'language': 'English'
    }
]

theaters_storage = [
    {
        'id': 1,
        'name': 'PVR Cinemas Phoenix',
        'address': 'Phoenix Marketcity, Kurla West',
        'city': 'Mumbai',
        'state': 'Maharashtra',
        'country': 'India',
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
]

shows_storage = [
    {'id': 1, 'movie_id': 1, 'hall_id': 1, 'start_time': '2024-01-15T10:00:00', 'end_time': '2024-01-15T13:01:00', 'price': 350.0},
    {'id': 2, 'movie_id': 1, 'hall_id': 1, 'start_time': '2024-01-15T14:00:00', 'end_time': '2024-01-15T17:01:00', 'price': 400.0},
    {'id': 3, 'movie_id': 1, 'hall_id': 1, 'start_time': '2024-01-15T18:30:00', 'end_time': '2024-01-15T21:31:00', 'price': 450.0},
    {'id': 4, 'movie_id': 2, 'hall_id': 4, 'start_time': '2024-01-15T11:00:00', 'end_time': '2024-01-15T13:32:00', 'price': 500.0},
    {'id': 5, 'movie_id': 2, 'hall_id': 4, 'start_time': '2024-01-15T15:00:00', 'end_time': '2024-01-15T17:32:00', 'price': 550.0},
    {'id': 6, 'movie_id': 3, 'hall_id': 2, 'start_time': '2024-01-15T12:00:00', 'end_time': '2024-01-15T14:28:00', 'price': 320.0},
    {'id': 7, 'movie_id': 3, 'hall_id': 2, 'start_time': '2024-01-15T16:00:00', 'end_time': '2024-01-15T18:28:00', 'price': 380.0},
    {'id': 8, 'movie_id': 4, 'hall_id': 4, 'start_time': '2024-01-15T13:30:00', 'end_time': '2024-01-15T15:42:00', 'price': 280.0},
    {'id': 9, 'movie_id': 5, 'hall_id': 1, 'start_time': '2024-01-15T19:30:00', 'end_time': '2024-01-15T22:19:00', 'price': 600.0},
    {'id': 10, 'movie_id': 5, 'hall_id': 2, 'start_time': '2024-01-15T21:00:00', 'end_time': '2024-01-15T23:49:00', 'price': 550.0}
]

# Simple CORS handling
@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

@app.route('/')
def home():
    return jsonify({'message': 'Movie Booking API', 'status': 'running'})

# Movies endpoint with CRUD
@app.route('/api/movies', methods=['GET', 'POST'])
def movies():
    if request.method == 'POST':
        data = request.get_json()
        new_movie = {
            'id': max([m['id'] for m in movies_storage] + [0]) + 1,
            'title': data.get('title', 'New Movie'),
            'description': data.get('description', 'A great movie'),
            'duration': data.get('duration', 120),
            'release_date': data.get('release_date', '2024-01-01'),
            'genre': data.get('genre', 'Drama'),
            'language': data.get('language', 'English')
        }
        movies_storage.append(new_movie)
        return jsonify(new_movie)
    
    return jsonify(movies_storage)

# Theaters endpoint with CRUD
@app.route('/api/theaters', methods=['GET', 'POST'])
def theaters():
    if request.method == 'POST':
        data = request.get_json()
        new_theater = {
            'id': max([t['id'] for t in theaters_storage] + [0]) + 1,
            'name': data.get('name', 'New Theater'),
            'address': data.get('address', 'New Address'),
            'city': data.get('city', 'Mumbai'),
            'state': data.get('state', 'Maharashtra'),
            'country': data.get('country', 'India'),
            'halls': data.get('halls', [])
        }
        theaters_storage.append(new_theater)
        return jsonify(new_theater)
    
    return jsonify(theaters_storage)

# Shows endpoint with CRUD
@app.route('/api/shows', methods=['GET', 'POST'])
def shows():
    if request.method == 'POST':
        data = request.get_json()
        new_show = {
            'id': max([s['id'] for s in shows_storage] + [0]) + 1,
            'movie_id': data.get('movie_id', 1),
            'hall_id': data.get('hall_id', 1),
            'start_time': data.get('start_time', '2024-01-15T18:00:00'),
            'end_time': data.get('end_time', '2024-01-15T20:00:00'),
            'price': data.get('price', 300.0)
        }
        shows_storage.append(new_show)
        return jsonify(new_show)
    
    return jsonify(shows_storage)

@app.route('/api/health')
def health():
    return jsonify({'status': 'healthy', 'message': 'API working'})

@app.route('/api/bookings/availability')
def booking_availability():
    show_id = request.args.get('show_id')
    if not show_id:
        return jsonify({'error': 'show_id is required'}), 400
    
    # Map shows to halls
    show_hall_map = {
        '1': 1, '2': 1, '3': 1, '9': 1,  # Hall 1 
        '4': 4, '5': 4, '8': 4,  # Hall 4 (IMAX)
        '6': 2, '7': 2, '10': 2,  # Hall 2
    }
    
    hall_id = show_hall_map.get(show_id, 1)
    
    # Define seat layouts for each hall
    hall_layouts = {
        1: [15, 15, 18, 18, 18, 18, 18, 18, 18, 18],  # Hall 1
        2: [12, 12, 15, 15, 15, 15, 15, 15, 15, 21],  # Hall 2
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

@app.route('/api/analytics/overview')
def analytics_overview():
    return jsonify({
        'total_bookings': 2847,
        'total_revenue': 1245680,
        'total_theaters': 2,
        'total_movies': 5,
        'popular_movies': [
            {'title': 'Avengers: Endgame', 'bookings': 485, 'revenue': 195400},
            {'title': 'The Dark Knight', 'bookings': 412, 'revenue': 226600},
            {'title': 'Interstellar', 'bookings': 298, 'revenue': 268200},
            {'title': 'Inception', 'bookings': 356, 'revenue': 134280},
            {'title': 'Parasite', 'bookings': 267, 'revenue': 81360}
        ],
        'theater_performance': [
            {'name': 'PVR Cinemas Phoenix', 'bookings': 645, 'revenue': 287250},
            {'name': 'INOX R City', 'bookings': 598, 'revenue': 329400}
        ],
        'daily_revenue': [
            {'date': '2024-01-08', 'revenue': 156780, 'bookings': 387},
            {'date': '2024-01-09', 'revenue': 189450, 'bookings': 445},
            {'date': '2024-01-10', 'revenue': 167890, 'bookings': 398},
            {'date': '2024-01-11', 'revenue': 198760, 'bookings': 467},
            {'date': '2024-01-12', 'revenue': 234560, 'bookings': 523},
            {'date': '2024-01-13', 'revenue': 298240, 'bookings': 628},
            {'date': '2024-01-14', 'revenue': 312890, 'bookings': 645}
        ],
        'genre_distribution': [
            {'genre': 'Action', 'count': 2, 'revenue': 422000},
            {'genre': 'Sci-Fi', 'count': 2, 'revenue': 402480},
            {'genre': 'Thriller', 'count': 1, 'revenue': 81360}
        ]
    })

@app.route('/api/analytics/movie/<int:movie_id>')
def movie_analytics(movie_id):
    movie_data = {
        1: {'title': 'Avengers: Endgame', 'bookings': 485, 'revenue': 195400, 'rating': 4.8},
        2: {'title': 'The Dark Knight', 'bookings': 412, 'revenue': 226600, 'rating': 4.9},
        3: {'title': 'Inception', 'bookings': 356, 'revenue': 134280, 'rating': 4.7},
        4: {'title': 'Parasite', 'bookings': 267, 'revenue': 81360, 'rating': 4.6},
        5: {'title': 'Interstellar', 'bookings': 298, 'revenue': 268200, 'rating': 4.8}
    }
    
    data = movie_data.get(movie_id, {'title': 'Unknown Movie', 'bookings': 150, 'revenue': 45000, 'rating': 4.0})
    
    return jsonify({
        'movie_id': movie_id,
        'title': data['title'],
        'total_bookings': data['bookings'],
        'total_revenue': data['revenue'],
        'average_rating': data['rating'],
        'booking_trends': [
            {'date': '2024-01-08', 'bookings': int(data['bookings'] * 0.12)},
            {'date': '2024-01-09', 'bookings': int(data['bookings'] * 0.15)},
            {'date': '2024-01-10', 'bookings': int(data['bookings'] * 0.13)},
            {'date': '2024-01-11', 'bookings': int(data['bookings'] * 0.16)},
            {'date': '2024-01-12', 'bookings': int(data['bookings'] * 0.18)},
            {'date': '2024-01-13', 'bookings': int(data['bookings'] * 0.14)},
            {'date': '2024-01-14', 'bookings': int(data['bookings'] * 0.12)}
        ],
        'show_performance': [
            {'time': '10:00-13:00', 'bookings': int(data['bookings'] * 0.25), 'revenue': int(data['revenue'] * 0.22)},
            {'time': '14:00-17:00', 'bookings': int(data['bookings'] * 0.35), 'revenue': int(data['revenue'] * 0.38)},
            {'time': '18:00-21:00', 'bookings': int(data['bookings'] * 0.40), 'revenue': int(data['revenue'] * 0.40)}
        ]
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
