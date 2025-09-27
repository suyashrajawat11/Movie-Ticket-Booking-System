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
                {'id': 1, 'name': 'Screen 1', 'total_seats': 180, 'type': 'Premium'},
                {'id': 2, 'name': 'Screen 2', 'total_seats': 150, 'type': 'Standard'},
                {'id': 3, 'name': 'Screen 3', 'total_seats': 120, 'type': 'Standard'}
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
                {'id': 4, 'name': 'Screen A', 'total_seats': 200, 'type': 'IMAX'},
                {'id': 5, 'name': 'Screen B', 'total_seats': 160, 'type': 'Premium'},
                {'id': 6, 'name': 'Screen C', 'total_seats': 140, 'type': 'Standard'}
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
                {'id': 7, 'name': 'Audi 1', 'total_seats': 170, 'type': 'Premium'},
                {'id': 8, 'name': 'Audi 2', 'total_seats': 130, 'type': 'Standard'},
                {'id': 9, 'name': 'Audi 3', 'total_seats': 110, 'type': 'Standard'}
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
                {'id': 10, 'name': 'Hall 1', 'total_seats': 190, 'type': 'Premium'},
                {'id': 11, 'name': 'Hall 2', 'total_seats': 155, 'type': 'Standard'}
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
                {'id': 12, 'name': 'Gold Class', 'total_seats': 80, 'type': 'Luxury'},
                {'id': 13, 'name': 'Silver Screen', 'total_seats': 145, 'type': 'Standard'}
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
