from flask import Blueprint, jsonify, request
from app.controllers.movie_controller import MovieController
from app.controllers.theater_controller import TheaterController
from app.controllers.booking_controller import BookingController

api_bp = Blueprint('api', __name__)

@api_bp.route('/', methods=['GET'])
def api_root():
    """API root endpoint"""
    return jsonify({
        'message': 'Movie Ticket Booking API',
        'version': '1.0.0',
        'endpoints': ['/health', '/movies', '/theaters', '/shows', '/bookings']
    })

@api_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'Movie Ticket Booking API is running',
        'version': '1.0.0'
    })

@api_bp.route('/movies', methods=['GET'])
def get_movies():
    return MovieController.get_all_movies()

@api_bp.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    return MovieController.get_movie(movie_id)

@api_bp.route('/movies', methods=['POST'])
def create_movie():
    data = request.get_json()
    return MovieController.create_movie(data)

@api_bp.route('/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    data = request.get_json()
    return MovieController.update_movie(movie_id, data)

@api_bp.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    return MovieController.delete_movie(movie_id)

@api_bp.route('/theaters', methods=['GET'])
def get_theaters():
    return TheaterController.get_all_theaters()

@api_bp.route('/theaters/<int:theater_id>', methods=['GET'])
def get_theater(theater_id):
    return TheaterController.get_theater(theater_id)

@api_bp.route('/theaters', methods=['POST'])
def create_theater():
    data = request.get_json()
    return TheaterController.create_theater(data)

@api_bp.route('/theaters/<int:theater_id>', methods=['PUT'])
def update_theater(theater_id):
    data = request.get_json()
    return TheaterController.update_theater(theater_id, data)

@api_bp.route('/theaters/<int:theater_id>', methods=['DELETE'])
def delete_theater(theater_id):
    return TheaterController.delete_theater(theater_id)

@api_bp.route('/shows', methods=['GET'])
def get_shows():
    return MovieController.get_all_shows()

@api_bp.route('/shows/<int:show_id>', methods=['GET'])
def get_show(show_id):
    return MovieController.get_show(show_id)

@api_bp.route('/shows', methods=['POST'])
def create_show():
    data = request.get_json()
    return MovieController.create_show(data)

@api_bp.route('/bookings', methods=['POST'])
def create_booking():
    data = request.get_json()
    return BookingController.create_booking(data)

@api_bp.route('/bookings/group', methods=['POST'])
def create_group_booking():
    data = request.get_json()
    return BookingController.create_group_booking(data)

@api_bp.route('/bookings/availability', methods=['GET'])
def check_availability():
    show_id = request.args.get('show_id')
    return BookingController.check_availability(show_id)

@api_bp.route('/bookings/suggest', methods=['GET'])
def suggest_alternate_shows():
    movie_id = request.args.get('movie_id')
    theater_id = request.args.get('theater_id')
    show_time = request.args.get('show_time')
    num_seats = int(request.args.get('num_seats', 1))
    
    return BookingController.suggest_alternate_shows(movie_id, theater_id, show_time, num_seats)

@api_bp.route('/analytics/movie/<int:movie_id>', methods=['GET'])
def get_movie_analytics(movie_id):
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    return BookingController.get_movie_analytics(movie_id, start_date, end_date)

@api_bp.route('/analytics/overview', methods=['GET'])
def get_analytics_overview():
    return BookingController.get_analytics_overview()
