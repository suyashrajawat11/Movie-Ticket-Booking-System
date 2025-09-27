from flask import jsonify
from app.models.booking import Booking
from app.models.show import Show
from app.models.seat import Seat
from app.models.row import Row
from app import db
from datetime import datetime, timedelta
import random
import string
import time
from sqlalchemy.exc import IntegrityError

class BookingController:
    @staticmethod
    def create_booking(data):
        """Create a new booking for a single seat"""
        try:
            show_id = data['show_id']
            seat_id = data['seat_id']
            user_id = data['user_id']
            
            # Check if seat is already booked for this show
            existing_booking = Booking.query.filter_by(
                show_id=show_id,
                seat_id=seat_id,
                status='confirmed'
            ).first()
            
            if existing_booking:
                return jsonify({
                    'status': 'error',
                    'message': 'Seat is already booked for this show'
                }), 400
            
            # Get show details for price
            show = Show.query.get_or_404(show_id)
            
            # Generate a unique booking reference with timestamp
            timestamp = str(int(time.time() * 1000))[-6:]  # Last 6 digits of timestamp
            random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
            booking_ref = f"{timestamp}{random_part}"
            
            # Create booking
            booking = Booking(
                show_id=show_id,
                seat_id=seat_id,
                user_id=user_id,
                booking_reference=booking_ref,
                status='confirmed',
                price_paid=show.price
            )
            
            db.session.add(booking)
            db.session.flush()  # Flush to check for constraint violations
            db.session.commit()
            
            return jsonify({
                'status': 'success',
                'data': {
                    'booking_reference': booking_ref,
                    'booking_id': booking.id,
                    'show_id': show_id,
                    'seat_id': seat_id,
                    'price_paid': float(show.price) if show.price else None,
                    'booking_time': booking.booking_time.isoformat()
                }
            }), 201
            
        except IntegrityError as e:
            db.session.rollback()
            return jsonify({
                'status': 'error',
                'message': 'Booking conflict - seat may already be booked or booking reference collision. Please try again.'
            }), 409
        except Exception as e:
            db.session.rollback()
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 400

    @staticmethod
    def create_group_booking(data):
        """Create a booking for multiple seats together"""
        try:
            show_id = data['show_id']
            seat_ids = data['seat_ids']  # List of seat IDs to book together
            user_id = data['user_id']
            
            if not isinstance(seat_ids, list) or len(seat_ids) == 0:
                return jsonify({
                    'status': 'error',
                    'message': 'At least one seat must be selected'
                }), 400
            
            # Check if all seats are available
            show = Show.query.get_or_404(show_id)
            
            # Get all seats in the same row to check for adjacency
            first_seat = Seat.query.get(seat_ids[0])
            row_id = first_seat.row_id
            
            # Verify all seats are in the same row
            for seat_id in seat_ids:
                seat = Seat.query.get(seat_id)
                if seat.row_id != row_id:
                    return jsonify({
                        'status': 'error',
                        'message': 'All seats must be in the same row for group booking'
                    }), 400
            
            # Check if any of the seats are already booked
            existing_bookings = Booking.query.filter(
                Booking.show_id == show_id,
                Booking.seat_id.in_(seat_ids),
                Booking.status == 'confirmed'
            ).all()
            
            if existing_bookings:
                booked_seats = [str(b.seat_id) for b in existing_bookings]
                return jsonify({
                    'status': 'error',
                    'message': f'Some seats are already booked: {", ".join(booked_seats)}'
                }), 400
            
            # Check if seats are adjacent
            seat_numbers = [s.seat_number for s in Seat.query.filter(Seat.id.in_(seat_ids)).all()]
            seat_numbers_sorted = sorted(seat_numbers)
            
            # Check if seats are consecutive
            if not all(seat_numbers_sorted[i] + 1 == seat_numbers_sorted[i + 1] 
                      for i in range(len(seat_numbers_sorted) - 1)):
                return jsonify({
                    'status': 'error',
                    'message': 'Selected seats are not adjacent. Please select adjacent seats.'
                }), 400
            
            # Generate a unique booking reference for the group with timestamp
            timestamp = str(int(time.time() * 1000))[-6:]  # Last 6 digits of timestamp
            random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
            base_booking_ref = f"{timestamp}{random_part}"
            bookings = []
            
            # Create bookings for each seat with unique references
            for i, seat_id in enumerate(seat_ids):
                # Each seat gets a unique booking reference with sequence number
                booking_ref = f"{base_booking_ref}S{i+1:02d}"  # S01, S02, etc.
                booking = Booking(
                    show_id=show_id,
                    seat_id=seat_id,
                    user_id=user_id,
                    booking_reference=booking_ref,
                    status='confirmed',
                    price_paid=show.price
                )
                db.session.add(booking)
                bookings.append(booking)
            
            db.session.flush()  # Flush to check for constraint violations
            db.session.commit()
            
            return jsonify({
                'status': 'success',
                'data': {
                    'booking_reference': base_booking_ref,
                    'booking_references': [b.booking_reference for b in bookings],
                    'booking_ids': [b.id for b in bookings],
                    'show_id': show_id,
                    'seat_ids': seat_ids,
                    'total_price': float(show.price * len(seat_ids)) if show.price else None,
                    'booking_time': bookings[0].booking_time.isoformat() if bookings else None
                }
            }), 201
            
        except IntegrityError as e:
            db.session.rollback()
            return jsonify({
                'status': 'error',
                'message': 'Booking conflict - some seats may already be booked or booking reference collision. Please try again.'
            }), 409
        except Exception as e:
            db.session.rollback()
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 400

    @staticmethod
    def check_availability(show_id):
        """Check seat availability for a show"""
        try:
            show = Show.query.get_or_404(show_id)
            hall = show.hall
            
            # Get all seats in the hall
            all_seats = Seat.query.join(Row).filter(Row.hall_id == hall.id).all()
            
            # Get all booked seats for this show
            booked_seats = Booking.query.filter(
                Booking.show_id == show_id,
                Booking.status == 'confirmed'
            ).all()
            
            booked_seat_ids = {b.seat_id for b in booked_seats}
            
            # Prepare seat availability data
            seats_availability = []
            for seat in all_seats:
                seats_availability.append({
                    'seat_id': seat.id,
                    'row_id': seat.row_id,
                    'seat_number': seat.seat_number,
                    'is_aisle': seat.is_aisle,
                    'is_available': seat.id not in booked_seat_ids
                })
            
            return jsonify({
                'status': 'success',
                'data': {
                    'show_id': show_id,
                    'hall_id': hall.id,
                    'total_seats': len(all_seats),
                    'available_seats': len(all_seats) - len(booked_seat_ids),
                    'seats': seats_availability
                }
            }), 200
            
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 500

    @staticmethod
    def suggest_alternate_shows(movie_id, theater_id, show_time, num_seats):
        """Suggest alternative shows where the requested number of seats are available together"""
        try:
            show_time = datetime.strptime(show_time, '%Y-%m-%d %H:%M:%S')
            
            # Find shows for the same movie at the same theater around the same time
            time_window_start = show_time - timedelta(hours=3)
            time_window_end = show_time + timedelta(hours=3)
            
            shows = Show.query.filter(
                Show.movie_id == movie_id,
                Show.start_time.between(time_window_start, time_window_end)
            ).all()
            
            suggested_shows = []
            
            for show in shows:
                # Check availability for this show
                availability = BookingController._check_consecutive_seats_availability(show.id, num_seats)
                
                if availability['available']:
                    suggested_shows.append({
                        'show_id': show.id,
                        'start_time': show.start_time.isoformat(),
                        'end_time': show.end_time.isoformat(),
                        'price': float(show.price) if show.price else None,
                        'available_seats': availability['available_seats'],
                        'suggested_seats': availability['suggested_seats']
                    })
            
            return jsonify({
                'status': 'success',
                'data': {
                    'original_show_time': show_time.isoformat(),
                    'requested_seats': num_seats,
                    'suggested_shows': suggested_shows
                }
            }), 200
            
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 500

    @staticmethod
    def _check_consecutive_seats_availability(show_id, num_seats):
        """Helper method to check if consecutive seats are available"""
        show = Show.query.get_or_404(show_id)
        hall = show.hall
        
        # Get all rows in the hall
        rows = Row.query.filter_by(hall_id=hall.id).order_by(Row.row_number).all()
        
        for row in rows:
            # Get all seats in this row
            seats = Seat.query.filter_by(row_id=row.id).order_by(Seat.seat_number).all()
            
            # Get booked seats for this show
            booked_seats = {b.seat_id for b in Booking.query.filter(
                Booking.show_id == show_id,
                Booking.status == 'confirmed',
                Booking.seat_id.in_([s.id for s in seats])
            ).all()}
            
            # Find consecutive available seats
            available_seats = []
            consecutive_count = 0
            
            for seat in seats:
                if seat.id not in booked_seats:
                    consecutive_count += 1
                    available_seats.append(seat.id)
                    
                    if consecutive_count >= num_seats:
                        # Found enough consecutive seats
                        return {
                            'available': True,
                            'available_seats': len(seats) - len(booked_seats),
                            'suggested_seats': available_seats[-num_seats:]
                        }
                else:
                    consecutive_count = 0
                    available_seats = []
        
        return {
            'available': False,
            'available_seats': 0,
            'suggested_seats': []
        }

    @staticmethod
    def get_movie_analytics(movie_id, start_date=None, end_date=None):
        """Get analytics for a movie (tickets sold, revenue)"""
        try:
            # Base query
            query = db.session.query(
                db.func.count(Booking.id).label('tickets_sold'),
                db.func.sum(Booking.price_paid).label('total_revenue'),
                db.func.date(Show.start_time).label('show_date')
            ).join(
                Show, Show.id == Booking.show_id
            ).filter(
                Show.movie_id == movie_id,
                Booking.status == 'confirmed'
            )
            
            # Apply date filters if provided
            if start_date:
                start_date = datetime.strptime(start_date, '%Y-%m-%d')
                query = query.filter(db.func.date(Show.start_time) >= start_date)
                
            if end_date:
                end_date = datetime.strptime(end_date, '%Y-%m-%d')
                query = query.filter(db.func.date(Show.start_time) <= end_date)
            
            # Group by show date
            query = query.group_by('show_date').order_by('show_date')
            
            results = query.all()
            
            # Format results
            analytics = []
            total_tickets = 0
            total_revenue = 0
            
            for result in results:
                total_tickets += result.tickets_sold
                total_revenue += float(result.total_revenue) if result.total_revenue else 0
                
                analytics.append({
                    'date': result.show_date.isoformat(),
                    'tickets_sold': result.tickets_sold,
                    'revenue': float(result.total_revenue) if result.total_revenue else 0
                })
            
            return jsonify({
                'status': 'success',
                'data': {
                    'movie_id': movie_id,
                    'period': {
                        'start_date': start_date.isoformat() if start_date else None,
                        'end_date': end_date.isoformat() if end_date else None
                    },
                    'total_tickets_sold': total_tickets,
                    'total_revenue': total_revenue,
                    'daily_analytics': analytics
                }
            }), 200
            
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 500

    @staticmethod
    def get_analytics_overview():
        """Get overall analytics overview"""
        try:
            from app.models.movie import Movie
            
            # Get total bookings count
            total_bookings = Booking.query.filter_by(status='confirmed').count()
            
            # Get total revenue
            total_revenue_result = db.session.query(
                db.func.sum(Booking.price_paid)
            ).filter_by(status='confirmed').scalar()
            
            total_revenue = float(total_revenue_result) if total_revenue_result else 0
            
            # Get bookings by movie
            movie_stats = db.session.query(
                Movie.title,
                db.func.count(Booking.id).label('bookings'),
                db.func.sum(Booking.price_paid).label('revenue')
            ).join(
                Show, Show.movie_id == Movie.id
            ).join(
                Booking, Booking.show_id == Show.id
            ).filter(
                Booking.status == 'confirmed'
            ).group_by(Movie.id, Movie.title).all()
            
            movies_data = []
            for stat in movie_stats:
                movies_data.append({
                    'movie': stat.title,
                    'bookings': stat.bookings,
                    'revenue': float(stat.revenue) if stat.revenue else 0
                })
            
            return jsonify({
                'status': 'success',
                'data': {
                    'total_bookings': total_bookings,
                    'total_revenue': total_revenue,
                    'movies': movies_data
                }
            }), 200
            
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 500
