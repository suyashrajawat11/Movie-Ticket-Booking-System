from app import create_app, db
from app.models.movie import Movie
from app.models.theater import Theater
from app.models.hall import Hall
from app.models.row import Row
from app.models.seat import Seat
from app.models.show import Show
from datetime import datetime, timedelta

app = create_app('development')

with app.app_context():
    print("🌱 Quick seeding...")
    
    # Create 1 theater
    theater = Theater(name='PVR Phoenix', address='Mumbai Mall', city='Mumbai', country='India')
    db.session.add(theater)
    db.session.flush()
    
    # Create 2 halls
    hall1 = Hall(theater_id=theater.id, name='IMAX', total_seats=20)
    hall2 = Hall(theater_id=theater.id, name='3D', total_seats=16)
    db.session.add_all([hall1, hall2])
    db.session.flush()
    
    # Create rows and seats for hall1
    for row_num in range(1, 3):
        row = Row(hall_id=hall1.id, row_number=row_num, seat_count=10)
        db.session.add(row)
        db.session.flush()
        for seat_num in range(1, 11):
            seat = Seat(row_id=row.id, seat_number=seat_num, is_aisle=(seat_num <= 2 or seat_num >= 9))
            db.session.add(seat)
    
    # Create rows and seats for hall2
    for row_num in range(1, 3):
        row = Row(hall_id=hall2.id, row_number=row_num, seat_count=8)
        db.session.add(row)
        db.session.flush()
        for seat_num in range(1, 9):
            seat = Seat(row_id=row.id, seat_number=seat_num, is_aisle=(seat_num <= 2 or seat_num >= 7))
            db.session.add(seat)
    
    # Create 3 movies
    movies = [
        Movie(title='Avengers: Endgame', duration=181, genre='Action', language='English'),
        Movie(title='RRR', duration=187, genre='Action', language='Telugu'),
        Movie(title='Inception', duration=148, genre='Sci-Fi', language='English')
    ]
    db.session.add_all(movies)
    db.session.flush()
    
    # Create shows for today and tomorrow
    base_time = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0)
    
    for day in range(2):
        for hall in [hall1, hall2]:
            for hour_offset in [0, 4, 8]:  # 10am, 2pm, 6pm
                show_time = base_time + timedelta(days=day, hours=hour_offset)
                end_time = show_time + timedelta(hours=3)
                
                show = Show(
                    movie_id=movies[day % len(movies)].id,
                    hall_id=hall.id,
                    start_time=show_time,
                    end_time=end_time,
                    price=300
                )
                db.session.add(show)
    
    db.session.commit()
    print("✅ Quick seeding completed!")
    print("🏢 1 theater, 2 halls, 36 seats, 3 movies, 12 shows created")
