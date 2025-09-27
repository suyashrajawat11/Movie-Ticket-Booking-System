from app import db

class BaseModel(db.Model):
    """Base model class that includes CRUD operations"""
    __abstract__ = True

    def save(self):
        """Save the current instance to the database"""
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        """Delete the current instance from the database"""
        db.session.delete(self)
        db.session.commit()
        return self

    @classmethod
    def get_by_id(cls, id):
        """Get a record by ID"""
        return cls.query.get_or_404(id)

    @classmethod
    def get_all(cls):
        """Get all records"""
        return cls.query.all()

    def update(self, **kwargs):
        """Update the current instance with the provided fields"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        db.session.commit()
        return self
