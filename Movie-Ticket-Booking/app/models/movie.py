from app import db
from datetime import datetime

class Movie(db.Model):
    __tablename__ = 'movies'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    duration = db.Column(db.Integer, nullable=False)  # in minutes
    release_date = db.Column(db.Date)
    genre = db.Column(db.String(100))
    language = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    shows = db.relationship('Show', backref='movie', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Movie {self.title}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'duration': self.duration,
            'release_date': self.release_date.isoformat() if self.release_date else None,
            'genre': self.genre,
            'language': self.language,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
