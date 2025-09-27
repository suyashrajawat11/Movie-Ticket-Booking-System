from app import db
from datetime import datetime, time

class Show(db.Model):
    __tablename__ = 'shows'
    
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    hall_id = db.Column(db.Integer, db.ForeignKey('halls.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    bookings = db.relationship('Booking', backref='show', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Show {self.movie_id} at {self.start_time} (Hall: {self.hall_id})>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'movie_id': self.movie_id,
            'hall_id': self.hall_id,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat(),
            'price': float(self.price) if self.price else None,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
