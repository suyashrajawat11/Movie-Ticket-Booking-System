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
        },
        {
            'id': 6,
            'title': 'The Godfather',
            'description': 'The timeless saga of the Corleone crime family and the transformation of Michael.',
            'duration': 175,
            'release_date': '1972-03-24',
            'genre': 'Crime',
            'language': 'English'
        },
        {
            'id': 7,
            'title': 'Pulp Fiction',
            'description': 'Quentin Tarantino\'s nonlinear masterpiece that revolutionized independent cinema.',
            'duration': 154,
            'release_date': '1994-10-14',
            'genre': 'Crime',
            'language': 'English'
        },
        {
            'id': 8,
            'title': 'Spirited Away',
            'description': 'Studio Ghibli\'s enchanting tale of a young girl in a magical spirit world.',
            'duration': 125,
            'release_date': '2001-07-20',
            'genre': 'Animation',
            'language': 'Japanese'
        },
        {
            'id': 9,
            'title': 'The Matrix',
            'description': 'A groundbreaking sci-fi action film that questioned the nature of reality.',
            'duration': 136,
            'release_date': '1999-03-31',
            'genre': 'Sci-Fi',
            'language': 'English'
        },
        {
            'id': 10,
            'title': 'Goodfellas',
            'description': 'Martin Scorsese\'s visceral portrayal of life in the mob through Henry Hill\'s eyes.',
            'duration': 146,
            'release_date': '1990-09-21',
            'genre': 'Crime',
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
                        {'id': 1, 'name': 'A', 'seats': 15},
                        {'id': 2, 'name': 'B', 'seats': 15},
                        {'id': 3, 'name': 'C', 'seats': 18},
                        {'id': 4, 'name': 'D', 'seats': 18},
                        {'id': 5, 'name': 'E', 'seats': 18},
                        {'id': 6, 'name': 'F', 'seats': 18},
                        {'id': 7, 'name': 'G', 'seats': 18},
                        {'id': 8, 'name': 'H', 'seats': 18},
                        {'id': 9, 'name': 'I', 'seats': 18},
                        {'id': 10, 'name': 'J', 'seats': 18}
                    ]
                },
                {
                    'id': 2, 
                    'name': 'Screen 2', 
                    'total_seats': 150, 
                    'type': 'Standard',
                    'rows': [
                        {'id': 11, 'name': 'A', 'seats': 12},
                        {'id': 12, 'name': 'B', 'seats': 12},
                        {'id': 13, 'name': 'C', 'seats': 15},
                        {'id': 14, 'name': 'D', 'seats': 15},
                        {'id': 15, 'name': 'E', 'seats': 15},
                        {'id': 16, 'name': 'F', 'seats': 15},
                        {'id': 17, 'name': 'G', 'seats': 15},
                        {'id': 18, 'name': 'H', 'seats': 15},
                        {'id': 19, 'name': 'I', 'seats': 15},
                        {'id': 20, 'name': 'J', 'seats': 21}
                    ]
                },
                {
                    'id': 3, 
                    'name': 'Screen 3', 
                    'total_seats': 120, 
                    'type': 'Standard',
                    'rows': [
                        {'id': 21, 'name': 'A', 'seats': 10},
                        {'id': 22, 'name': 'B', 'seats': 10},
                        {'id': 23, 'name': 'C', 'seats': 12},
                        {'id': 24, 'name': 'D', 'seats': 12},
                        {'id': 25, 'name': 'E', 'seats': 12},
                        {'id': 26, 'name': 'F', 'seats': 12},
                        {'id': 27, 'name': 'G', 'seats': 12},
                        {'id': 28, 'name': 'H', 'seats': 12},
                        {'id': 29, 'name': 'I', 'seats': 14},
                        {'id': 30, 'name': 'J', 'seats': 14}
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
                        {'id': 31, 'name': 'A', 'seats': 16},
                        {'id': 32, 'name': 'B', 'seats': 16},
                        {'id': 33, 'name': 'C', 'seats': 20},
                        {'id': 34, 'name': 'D', 'seats': 20},
                        {'id': 35, 'name': 'E', 'seats': 20},
                        {'id': 36, 'name': 'F', 'seats': 20},
                        {'id': 37, 'name': 'G', 'seats': 20},
                        {'id': 38, 'name': 'H', 'seats': 20},
                        {'id': 39, 'name': 'I', 'seats': 24},
                        {'id': 40, 'name': 'J', 'seats': 24}
                    ]
                },
                {
                    'id': 5, 
                    'name': 'Screen B', 
                    'total_seats': 160, 
                    'type': 'Premium',
                    'rows': [
                        {'id': 41, 'name': 'A', 'seats': 14},
                        {'id': 42, 'name': 'B', 'seats': 14},
                        {'id': 43, 'name': 'C', 'seats': 16},
                        {'id': 44, 'name': 'D', 'seats': 16},
                        {'id': 45, 'name': 'E', 'seats': 16},
                        {'id': 46, 'name': 'F', 'seats': 16},
                        {'id': 47, 'name': 'G', 'seats': 16},
                        {'id': 48, 'name': 'H', 'seats': 16},
                        {'id': 49, 'name': 'I', 'seats': 18},
                        {'id': 50, 'name': 'J', 'seats': 18}
                    ]
                },
                {
                    'id': 6, 
                    'name': 'Screen C', 
                    'total_seats': 140, 
                    'type': 'Standard',
                    'rows': [
                        {'id': 51, 'name': 'A', 'seats': 12},
                        {'id': 52, 'name': 'B', 'seats': 12},
                        {'id': 53, 'name': 'C', 'seats': 14},
                        {'id': 54, 'name': 'D', 'seats': 14},
                        {'id': 55, 'name': 'E', 'seats': 14},
                        {'id': 56, 'name': 'F', 'seats': 14},
                        {'id': 57, 'name': 'G', 'seats': 14},
                        {'id': 58, 'name': 'H', 'seats': 14},
                        {'id': 59, 'name': 'I', 'seats': 16},
                        {'id': 60, 'name': 'J', 'seats': 16}
                    ]
                }
            ]
        },
        {
            'id': 3,
            'name': 'Cinepolis Andheri',
            'address': 'Fun Republic Mall, Andheri West',
            'city': 'Mumbai',
            'state': 'Maharashtra',
            'country': 'India',
            'pincode': '400053',
            'halls': [
                {
                    'id': 7, 
                    'name': 'Audi 1', 
                    'total_seats': 170, 
                    'type': 'Premium',
                    'rows': [
                        {'id': 61, 'name': 'A', 'seats': 15},
                        {'id': 62, 'name': 'B', 'seats': 15},
                        {'id': 63, 'name': 'C', 'seats': 17},
                        {'id': 64, 'name': 'D', 'seats': 17},
                        {'id': 65, 'name': 'E', 'seats': 17},
                        {'id': 66, 'name': 'F', 'seats': 17},
                        {'id': 67, 'name': 'G', 'seats': 17},
                        {'id': 68, 'name': 'H', 'seats': 17},
                        {'id': 69, 'name': 'I', 'seats': 19},
                        {'id': 70, 'name': 'J', 'seats': 19}
                    ]
                },
                {
                    'id': 8, 
                    'name': 'Audi 2', 
                    'total_seats': 130, 
                    'type': 'Standard',
                    'rows': [
                        {'id': 71, 'name': 'A', 'seats': 11},
                        {'id': 72, 'name': 'B', 'seats': 11},
                        {'id': 73, 'name': 'C', 'seats': 13},
                        {'id': 74, 'name': 'D', 'seats': 13},
                        {'id': 75, 'name': 'E', 'seats': 13},
                        {'id': 76, 'name': 'F', 'seats': 13},
                        {'id': 77, 'name': 'G', 'seats': 13},
                        {'id': 78, 'name': 'H', 'seats': 13},
                        {'id': 79, 'name': 'I', 'seats': 15},
                        {'id': 80, 'name': 'J', 'seats': 15}
                    ]
                },
                {
                    'id': 9, 
                    'name': 'Audi 3', 
                    'total_seats': 110, 
                    'type': 'Standard',
                    'rows': [
                        {'id': 81, 'name': 'A', 'seats': 9},
                        {'id': 82, 'name': 'B', 'seats': 9},
                        {'id': 83, 'name': 'C', 'seats': 11},
                        {'id': 84, 'name': 'D', 'seats': 11},
                        {'id': 85, 'name': 'E', 'seats': 11},
                        {'id': 86, 'name': 'F', 'seats': 11},
                        {'id': 87, 'name': 'G', 'seats': 11},
                        {'id': 88, 'name': 'H', 'seats': 11},
                        {'id': 89, 'name': 'I', 'seats': 13},
                        {'id': 90, 'name': 'J', 'seats': 13}
                    ]
                }
            ]
        },
        {
            'id': 4,
            'name': 'Carnival Cinemas',
            'address': 'Wadala East, Near Eastern Express Highway',
            'city': 'Mumbai',
            'state': 'Maharashtra',
            'country': 'India',
            'pincode': '400037',
            'halls': [
                {
                    'id': 10, 
                    'name': 'Hall 1', 
                    'total_seats': 190, 
                    'type': 'Premium',
                    'rows': [
                        {'id': 91, 'name': 'A', 'seats': 17},
                        {'id': 92, 'name': 'B', 'seats': 17},
                        {'id': 93, 'name': 'C', 'seats': 19},
                        {'id': 94, 'name': 'D', 'seats': 19},
                        {'id': 95, 'name': 'E', 'seats': 19},
                        {'id': 96, 'name': 'F', 'seats': 19},
                        {'id': 97, 'name': 'G', 'seats': 19},
                        {'id': 98, 'name': 'H', 'seats': 19},
                        {'id': 99, 'name': 'I', 'seats': 21},
                        {'id': 100, 'name': 'J', 'seats': 21}
                    ]
                },
                {
                    'id': 11, 
                    'name': 'Hall 2', 
                    'total_seats': 155, 
                    'type': 'Standard',
                    'rows': [
                        {'id': 101, 'name': 'A', 'seats': 13},
                        {'id': 102, 'name': 'B', 'seats': 13},
                        {'id': 103, 'name': 'C', 'seats': 15},
                        {'id': 104, 'name': 'D', 'seats': 15},
                        {'id': 105, 'name': 'E', 'seats': 15},
                        {'id': 106, 'name': 'F', 'seats': 15},
                        {'id': 107, 'name': 'G', 'seats': 15},
                        {'id': 108, 'name': 'H', 'seats': 15},
                        {'id': 109, 'name': 'I', 'seats': 17},
                        {'id': 110, 'name': 'J', 'seats': 22}
                    ]
                }
            ]
        },
        {
            'id': 5,
            'name': 'MovieMax Bandra',
            'address': 'Linking Road, Bandra West',
            'city': 'Mumbai',
            'state': 'Maharashtra',
            'country': 'India',
            'pincode': '400050',
            'halls': [
                {
                    'id': 12, 
                    'name': 'Gold Class', 
                    'total_seats': 80, 
                    'type': 'Luxury',
                    'rows': [
                        {'id': 111, 'name': 'A', 'seats': 6},
                        {'id': 112, 'name': 'B', 'seats': 6},
                        {'id': 113, 'name': 'C', 'seats': 8},
                        {'id': 114, 'name': 'D', 'seats': 8},
                        {'id': 115, 'name': 'E', 'seats': 8},
                        {'id': 116, 'name': 'F', 'seats': 8},
                        {'id': 117, 'name': 'G', 'seats': 8},
                        {'id': 118, 'name': 'H', 'seats': 8},
                        {'id': 119, 'name': 'I', 'seats': 10},
                        {'id': 120, 'name': 'J', 'seats': 10}
                    ]
                },
                {
                    'id': 13, 
                    'name': 'Silver Screen', 
                    'total_seats': 145, 
                    'type': 'Standard',
                    'rows': [
                        {'id': 121, 'name': 'A', 'seats': 12},
                        {'id': 122, 'name': 'B', 'seats': 12},
                        {'id': 123, 'name': 'C', 'seats': 14},
                        {'id': 124, 'name': 'D', 'seats': 14},
                        {'id': 125, 'name': 'E', 'seats': 14},
                        {'id': 126, 'name': 'F', 'seats': 14},
                        {'id': 127, 'name': 'G', 'seats': 14},
                        {'id': 128, 'name': 'H', 'seats': 14},
                        {'id': 129, 'name': 'I', 'seats': 16},
                        {'id': 130, 'name': 'J', 'seats': 21}
                    ]
                }
            ]
        }
    ])

@app.route('/api/shows')
def shows():
    return jsonify([
        # Today's Shows
        {'id': 1, 'movie_id': 1, 'hall_id': 1, 'start_time': '2024-01-15T10:00:00', 'end_time': '2024-01-15T13:01:00', 'price': 350.0},
        {'id': 2, 'movie_id': 1, 'hall_id': 1, 'start_time': '2024-01-15T14:00:00', 'end_time': '2024-01-15T17:01:00', 'price': 400.0},
        {'id': 3, 'movie_id': 1, 'hall_id': 1, 'start_time': '2024-01-15T18:30:00', 'end_time': '2024-01-15T21:31:00', 'price': 450.0},
        
        {'id': 4, 'movie_id': 2, 'hall_id': 4, 'start_time': '2024-01-15T11:00:00', 'end_time': '2024-01-15T13:32:00', 'price': 500.0},
        {'id': 5, 'movie_id': 2, 'hall_id': 4, 'start_time': '2024-01-15T15:00:00', 'end_time': '2024-01-15T17:32:00', 'price': 550.0},
        {'id': 6, 'movie_id': 2, 'hall_id': 4, 'start_time': '2024-01-15T19:00:00', 'end_time': '2024-01-15T21:32:00', 'price': 600.0},
        
        {'id': 7, 'movie_id': 3, 'hall_id': 7, 'start_time': '2024-01-15T12:00:00', 'end_time': '2024-01-15T14:28:00', 'price': 320.0},
        {'id': 8, 'movie_id': 3, 'hall_id': 7, 'start_time': '2024-01-15T16:00:00', 'end_time': '2024-01-15T18:28:00', 'price': 380.0},
        {'id': 9, 'movie_id': 3, 'hall_id': 7, 'start_time': '2024-01-15T20:00:00', 'end_time': '2024-01-15T22:28:00', 'price': 420.0},
        
        {'id': 10, 'movie_id': 4, 'hall_id': 10, 'start_time': '2024-01-15T13:30:00', 'end_time': '2024-01-15T15:42:00', 'price': 280.0},
        {'id': 11, 'movie_id': 4, 'hall_id': 10, 'start_time': '2024-01-15T17:30:00', 'end_time': '2024-01-15T19:42:00', 'price': 320.0},
        {'id': 12, 'movie_id': 4, 'hall_id': 10, 'start_time': '2024-01-15T21:00:00', 'end_time': '2024-01-15T23:12:00', 'price': 350.0},
        
        {'id': 13, 'movie_id': 5, 'hall_id': 12, 'start_time': '2024-01-15T10:30:00', 'end_time': '2024-01-15T13:19:00', 'price': 800.0},
        {'id': 14, 'movie_id': 5, 'hall_id': 12, 'start_time': '2024-01-15T15:30:00', 'end_time': '2024-01-15T18:19:00', 'price': 900.0},
        {'id': 15, 'movie_id': 5, 'hall_id': 12, 'start_time': '2024-01-15T19:30:00', 'end_time': '2024-01-15T22:19:00', 'price': 1000.0},
        
        # Tomorrow's Shows
        {'id': 16, 'movie_id': 6, 'hall_id': 2, 'start_time': '2024-01-16T11:00:00', 'end_time': '2024-01-16T13:55:00', 'price': 300.0},
        {'id': 17, 'movie_id': 6, 'hall_id': 2, 'start_time': '2024-01-16T15:30:00', 'end_time': '2024-01-16T18:25:00', 'price': 350.0},
        {'id': 18, 'movie_id': 6, 'hall_id': 2, 'start_time': '2024-01-16T19:30:00', 'end_time': '2024-01-16T22:25:00', 'price': 400.0},
        
        {'id': 19, 'movie_id': 7, 'hall_id': 5, 'start_time': '2024-01-16T12:30:00', 'end_time': '2024-01-16T15:04:00', 'price': 380.0},
        {'id': 20, 'movie_id': 7, 'hall_id': 5, 'start_time': '2024-01-16T16:30:00', 'end_time': '2024-01-16T19:04:00', 'price': 430.0},
        {'id': 21, 'movie_id': 7, 'hall_id': 5, 'start_time': '2024-01-16T20:30:00', 'end_time': '2024-01-16T23:04:00', 'price': 480.0},
        
        {'id': 22, 'movie_id': 8, 'hall_id': 8, 'start_time': '2024-01-16T10:00:00', 'end_time': '2024-01-16T12:05:00', 'price': 250.0},
        {'id': 23, 'movie_id': 8, 'hall_id': 8, 'start_time': '2024-01-16T14:00:00', 'end_time': '2024-01-16T16:05:00', 'price': 280.0},
        {'id': 24, 'movie_id': 8, 'hall_id': 8, 'start_time': '2024-01-16T18:00:00', 'end_time': '2024-01-16T20:05:00', 'price': 320.0},
        
        {'id': 25, 'movie_id': 9, 'hall_id': 6, 'start_time': '2024-01-16T13:00:00', 'end_time': '2024-01-16T15:16:00', 'price': 340.0},
        {'id': 26, 'movie_id': 9, 'hall_id': 6, 'start_time': '2024-01-16T17:00:00', 'end_time': '2024-01-16T19:16:00', 'price': 390.0},
        {'id': 27, 'movie_id': 9, 'hall_id': 6, 'start_time': '2024-01-16T21:00:00', 'end_time': '2024-01-16T23:16:00', 'price': 440.0},
        
        {'id': 28, 'movie_id': 10, 'hall_id': 11, 'start_time': '2024-01-16T14:30:00', 'end_time': '2024-01-16T16:56:00', 'price': 310.0},
        {'id': 29, 'movie_id': 10, 'hall_id': 11, 'start_time': '2024-01-16T18:30:00', 'end_time': '2024-01-16T20:56:00', 'price': 360.0},
        {'id': 30, 'movie_id': 10, 'hall_id': 11, 'start_time': '2024-01-16T22:00:00', 'end_time': '2024-01-17T00:26:00', 'price': 400.0}
    ])

@app.route('/api/health')
def health():
    return jsonify({'status': 'healthy', 'message': 'API working'})

@app.route('/api/bookings/availability')
def booking_availability():
    show_id = request.args.get('show_id')
    if not show_id:
        return jsonify({'error': 'show_id is required'}), 400
    
    # Generate realistic seat availability (some seats booked, some available)
    import random
    
    # Get show info to determine hall
    show_hall_map = {
        '1': 1, '2': 1, '3': 1,  # Hall 1 (180 seats, rows A-J)
        '4': 4, '5': 4, '6': 4,  # Hall 4 (200 seats, rows A-J) 
        '7': 7, '8': 7, '9': 7,  # Hall 7 (170 seats, rows A-J)
        '10': 10, '11': 10, '12': 10,  # Hall 10 (190 seats, rows A-J)
        '13': 12, '14': 12, '15': 12,  # Hall 12 (80 seats, rows A-J)
    }
    
    hall_id = show_hall_map.get(show_id, 1)
    
    # Define seat layouts for each hall
    hall_layouts = {
        1: [15, 15, 18, 18, 18, 18, 18, 18, 18, 18],  # Hall 1
        4: [16, 16, 20, 20, 20, 20, 20, 20, 24, 24],  # Hall 4 (IMAX)
        7: [15, 15, 17, 17, 17, 17, 17, 17, 19, 19],  # Hall 7
        10: [17, 17, 19, 19, 19, 19, 19, 19, 21, 21], # Hall 10
        12: [6, 6, 8, 8, 8, 8, 8, 8, 10, 10]         # Hall 12 (Luxury)
    }
    
    layout = hall_layouts.get(hall_id, [15, 15, 18, 18, 18, 18, 18, 18, 18, 18])
    
    # Generate seat availability
    availability = []
    row_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    
    for row_idx, seat_count in enumerate(layout):
        row_name = row_names[row_idx]
        for seat_num in range(1, seat_count + 1):
            # Randomly make some seats booked (30% chance)
            is_booked = random.random() < 0.3
            availability.append({
                'row': row_name,
                'seat': seat_num,
                'status': 'booked' if is_booked else 'available',
                'seat_id': f"{row_name}{seat_num}"
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

@app.route('/api/analytics/overview')
def analytics_overview():
    return jsonify({
        'total_bookings': 2847,
        'total_revenue': 1245680,
        'total_theaters': 5,
        'total_movies': 10,
        'popular_movies': [
            {'title': 'Avengers: Endgame', 'bookings': 485, 'revenue': 195400},
            {'title': 'The Dark Knight', 'bookings': 412, 'revenue': 226600},
            {'title': 'Interstellar', 'bookings': 298, 'revenue': 268200},
            {'title': 'Inception', 'bookings': 356, 'revenue': 134280},
            {'title': 'Parasite', 'bookings': 267, 'revenue': 81360}
        ],
        'theater_performance': [
            {'name': 'PVR Cinemas Phoenix', 'bookings': 645, 'revenue': 287250},
            {'name': 'INOX R City', 'bookings': 598, 'revenue': 329400},
            {'name': 'Cinepolis Andheri', 'bookings': 523, 'revenue': 198740},
            {'name': 'Carnival Cinemas', 'bookings': 467, 'revenue': 156890},
            {'name': 'MovieMax Bandra', 'bookings': 614, 'revenue': 273400}
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
            {'genre': 'Sci-Fi', 'count': 3, 'revenue': 536760},
            {'genre': 'Crime', 'count': 3, 'revenue': 198450},
            {'genre': 'Thriller', 'count': 1, 'revenue': 81360},
            {'genre': 'Animation', 'count': 1, 'revenue': 7110}
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
