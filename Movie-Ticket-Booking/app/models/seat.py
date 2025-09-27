from app import db

class Seat(db.Model):
    __tablename__ = 'seats'
    
    id = db.Column(db.Integer, primary_key=True)
    row_id = db.Column(db.Integer, db.ForeignKey('rows.id'), nullable=False)
    seat_number = db.Column(db.Integer, nullable=False)  # Seat number in the row
    is_aisle = db.Column(db.Boolean, default=False)  # Mark if it's an aisle seat
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    bookings = db.relationship('Booking', backref='seat', lazy=True, cascade='all, delete-orphan')
    
    __table_args__ = (
        db.UniqueConstraint('row_id', 'seat_number', name='uix_row_seat'),
    )
    
    def __repr__(self):
        return f'<Seat {self.seat_number} (Row ID: {self.row_id})>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'row_id': self.row_id,
            'seat_number': self.seat_number,
            'is_aisle': self.is_aisle,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
