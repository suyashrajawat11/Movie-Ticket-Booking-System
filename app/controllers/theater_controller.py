from flask import jsonify
from app.models.theater import Theater
from app.models.hall import Hall
from app.models.row import Row
from app.models.seat import Seat
from app.models.booking import Booking
from app import db
from datetime import datetime

class TheaterController:
    @staticmethod
    def get_all_theaters():
        try:
            theaters = Theater.query.all()
            return jsonify({
                'status': 'success',
                'data': [theater.to_dict() for theater in theaters]
            }), 200
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 500

    @staticmethod
    def get_theater(theater_id):
        try:
            theater = Theater.query.get_or_404(theater_id)
            return jsonify({
                'status': 'success',
                'data': theater.to_dict()
            }), 200
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 500

    @staticmethod
    def create_theater(data):
        try:
            # Create theater
            theater = Theater(
                name=data['name'],
                address=data['address'],
                city=data['city'],
                state=data.get('state'),
                country=data['country'],
                pincode=data.get('pincode')
            )
            db.session.add(theater)
            db.session.flush()  # To get the theater.id
            
            # Create halls
            for hall_data in data.get('halls', []):
                hall = Hall(
                    theater_id=theater.id,
                    name=hall_data['name'],
                    total_seats=hall_data['total_seats']
                )
                db.session.add(hall)
                db.session.flush()
                
                # Create rows and seats for each hall
                for row_data in hall_data.get('rows', []):
                    row = Row(
                        hall_id=hall.id,
                        row_number=row_data['row_number'],
                        seat_count=row_data['seat_count']
                    )
                    db.session.add(row)
                    db.session.flush()
                    
                    # Create seats for the row
                    for seat_num in range(1, row.seat_count + 1):
                        is_aisle = seat_num in [1, 2, row.seat_count - 1, row.seat_count]  # Mark aisle seats
                        seat = Seat(
                            row_id=row.id,
                            seat_number=seat_num,
                            is_aisle=is_aisle
                        )
                        db.session.add(seat)
            
            db.session.commit()
            return jsonify({
                'status': 'success',
                'data': theater.to_dict()
            }), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 400

    @staticmethod
    def update_theater(theater_id, data):
        try:
            theater = Theater.query.get_or_404(theater_id)
            
            if 'name' in data:
                theater.name = data['name']
            if 'address' in data:
                theater.address = data['address']
            if 'city' in data:
                theater.city = data['city']
            if 'state' in data:
                theater.state = data['state']
            if 'country' in data:
                theater.country = data['country']
            if 'pincode' in data:
                theater.pincode = data['pincode']
                
            db.session.commit()
            return jsonify({
                'status': 'success',
                'data': theater.to_dict()
            }), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 400

    @staticmethod
    def delete_theater(theater_id):
        try:
            theater = Theater.query.get_or_404(theater_id)
            db.session.delete(theater)
            db.session.commit()
            return jsonify({
                'status': 'success',
                'message': 'Theater deleted successfully'
            }), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 500
