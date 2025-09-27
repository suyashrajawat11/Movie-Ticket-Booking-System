from app import db
from datetime import datetime

class Hall(db.Model):
    __tablename__ = 'halls'
    
    id = db.Column(db.Integer, primary_key=True)
    theater_id = db.Column(db.Integer, db.ForeignKey('theaters.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    total_seats = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    rows = db.relationship('Row', backref='hall', lazy=True, cascade='all, delete-orphan')
    shows = db.relationship('Show', backref='hall', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Hall {self.name} (Theater ID: {self.theater_id})>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'theater_id': self.theater_id,
            'name': self.name,
            'total_seats': self.total_seats,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'rows': [row.to_dict() for row in self.rows]
        }
