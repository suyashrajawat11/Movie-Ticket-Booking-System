from app import create_app, db
from app.models.movie import Movie
from app.models.theater import Theater
from app.models.hall import Hall
from app.models.row import Row
from app.models.seat import Seat
from app.models.show import Show
from app.models.booking import Booking

app = create_app()

with app.app_context():
    # Create all database tables
    db.create_all()
    print("Database tables created successfully!")
