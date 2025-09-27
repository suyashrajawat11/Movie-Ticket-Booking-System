from flask import jsonify, request
from app.models.movie import Movie
from app.models.show import Show
from app import db
from datetime import datetime

class MovieController:
    @staticmethod
    def get_all_movies():
        try:
            movies = Movie.query.all()
            return jsonify({
                'status': 'success',
                'data': [movie.to_dict() for movie in movies]
            }), 200
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 500

    @staticmethod
    def get_movie(movie_id):
        try:
            movie = Movie.query.get_or_404(movie_id)
            return jsonify({
                'status': 'success',
                'data': movie.to_dict()
            }), 200
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 500

    @staticmethod
    def create_movie(data):
        try:
            movie = Movie(
                title=data['title'],
                description=data.get('description'),
                duration=data['duration'],
                release_date=datetime.strptime(data['release_date'], '%Y-%m-%d').date() if 'release_date' in data else None,
                genre=data.get('genre'),
                language=data.get('language')
            )
            db.session.add(movie)
            db.session.commit()
            return jsonify({
                'status': 'success',
                'data': movie.to_dict()
            }), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 400

    @staticmethod
    def update_movie(movie_id, data):
        try:
            movie = Movie.query.get_or_404(movie_id)
            
            if 'title' in data:
                movie.title = data['title']
            if 'description' in data:
                movie.description = data['description']
            if 'duration' in data:
                movie.duration = data['duration']
            if 'release_date' in data:
                movie.release_date = datetime.strptime(data['release_date'], '%Y-%m-%d').date()
            if 'genre' in data:
                movie.genre = data['genre']
            if 'language' in data:
                movie.language = data['language']
                
            db.session.commit()
            return jsonify({
                'status': 'success',
                'data': movie.to_dict()
            }), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 400

    @staticmethod
    def delete_movie(movie_id):
        try:
            movie = Movie.query.get_or_404(movie_id)
            db.session.delete(movie)
            db.session.commit()
            return jsonify({
                'status': 'success',
                'message': 'Movie deleted successfully'
            }), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 500

    @staticmethod
    def get_all_shows():
        try:
            shows = Show.query.all()
            return jsonify({
                'status': 'success',
                'data': [show.to_dict() for show in shows]
            }), 200
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 500

    @staticmethod
    def get_show(show_id):
        try:
            show = Show.query.get_or_404(show_id)
            return jsonify({
                'status': 'success',
                'data': show.to_dict()
            }), 200
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 500

    @staticmethod
    def create_show(data):
        try:
            show = Show(
                movie_id=data['movie_id'],
                hall_id=data['hall_id'],
                start_time=datetime.strptime(data['start_time'], '%Y-%m-%d %H:%M:%S'),
                end_time=datetime.strptime(data['end_time'], '%Y-%m-%d %H:%M:%S'),
                price=data['price']
            )
            db.session.add(show)
            db.session.commit()
            return jsonify({
                'status': 'success',
                'data': show.to_dict()
            }), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 400
