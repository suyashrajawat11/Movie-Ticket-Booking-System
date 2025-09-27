from app import db
from datetime import datetime

class Booking(db.Model):
    __tablename__ = 'bookings'
    
    id = db.Column(db.Integer, primary_key=True)
    show_id = db.Column(db.Integer, db.ForeignKey('shows.id'), nullable=False)
    seat_id = db.Column(db.Integer, db.ForeignKey('seats.id'), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)  # In a real app, this would be a foreign key to a users table
    booking_reference = db.Column(db.String(50), unique=True, nullable=False)
    booking_time = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='confirmed')  # confirmed, cancelled, expired
    price_paid = db.Column(db.Numeric(10, 2), nullable=False)
    
    def __repr__(self):
        return f'<Booking {self.booking_reference} (Show: {self.show_id}, Seat: {self.seat_id})>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'show_id': self.show_id,
            'seat_id': self.seat_id,
            'user_id': self.user_id,
            'booking_reference': self.booking_reference,
            'booking_time': self.booking_time.isoformat(),
            'status': self.status,
            'price_paid': float(self.price_paid) if self.price_paid else None
        }
