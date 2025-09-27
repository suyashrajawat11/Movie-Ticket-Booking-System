from app import db
from datetime import datetime

class Row(db.Model):
    __tablename__ = 'rows'
    
    id = db.Column(db.Integer, primary_key=True)
    hall_id = db.Column(db.Integer, db.ForeignKey('halls.id'), nullable=False)
    row_number = db.Column(db.Integer, nullable=False)
    seat_count = db.Column(db.Integer, nullable=False)  # Total seats in this row
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    seats = db.relationship('Seat', backref='row', lazy=True, cascade='all, delete-orphan')
    
    __table_args__ = (
        db.UniqueConstraint('hall_id', 'row_number', name='uix_hall_row'),
    )
    
    def __repr__(self):
        return f'<Row {self.row_number} (Hall ID: {self.hall_id})>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'hall_id': self.hall_id,
            'row_number': self.row_number,
            'seat_count': self.seat_count,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
