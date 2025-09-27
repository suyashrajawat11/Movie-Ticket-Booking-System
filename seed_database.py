#!/usr/bin/env python3
"""
Database Seeding Script for Movie Booking System
Creates realistic theaters, movies, and show schedules
"""

import sys
import os
from datetime import datetime, timedelta
import random

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from app.models.movie import Movie
from app.models.theater import Theater
from app.models.hall import Hall
from app.models.row import Row
from app.models.seat import Seat
from app.models.show import Show

def create_theaters():
    """Create 6 theaters with different hall configurations"""
    
    theaters_data = [
        {
            'name': 'PVR Cinemas Phoenix',
            'address': '142, Palladium Mall, High Street Phoenix',
            'city': 'Mumbai',
            'state': 'Maharashtra',
            'country': 'India',
            'pincode': '400013',
            'halls': [
                {'name': 'IMAX', 'rows': [
                    {'row_number': 1, 'seat_count': 12},
                    {'row_number': 2, 'seat_count': 14},
                    {'row_number': 3, 'seat_count': 16},
                    {'row_number': 4, 'seat_count': 18},
                    {'row_number': 5, 'seat_count': 20},
                ]},
                {'name': 'MX4D', 'rows': [
                    {'row_number': 1, 'seat_count': 8},
                    {'row_number': 2, 'seat_count': 10},
                    {'row_number': 3, 'seat_count': 12},
                    {'row_number': 4, 'seat_count': 12},
                ]},
                {'name': '3D Premium', 'rows': [
                    {'row_number': 1, 'seat_count': 10},
                    {'row_number': 2, 'seat_count': 12},
                    {'row_number': 3, 'seat_count': 14},
                    {'row_number': 4, 'seat_count': 16},
                ]},
                {'name': '2D Classic', 'rows': [
                    {'row_number': 1, 'seat_count': 8},
                    {'row_number': 2, 'seat_count': 10},
                    {'row_number': 3, 'seat_count': 12},
                ]}
            ]
        },
        {
            'name': 'INOX Megaplex',
            'address': 'R City Mall, Amrut Nagar, Ghatkopar West',
            'city': 'Mumbai',
            'state': 'Maharashtra', 
            'country': 'India',
            'pincode': '400086',
            'halls': [
                {'name': 'IMAX Laser', 'rows': [
                    {'row_number': 1, 'seat_count': 14},
                    {'row_number': 2, 'seat_count': 16},
                    {'row_number': 3, 'seat_count': 18},
                    {'row_number': 4, 'seat_count': 20},
                    {'row_number': 5, 'seat_count': 22},
                ]},
                {'name': '4DX', 'rows': [
                    {'row_number': 1, 'seat_count': 6},
                    {'row_number': 2, 'seat_count': 8},
                    {'row_number': 3, 'seat_count': 10},
                ]},
                {'name': 'Dolby Atmos 3D', 'rows': [
                    {'row_number': 1, 'seat_count': 12},
                    {'row_number': 2, 'seat_count': 14},
                    {'row_number': 3, 'seat_count': 16},
                ]},
                {'name': 'Gold Class 2D', 'rows': [
                    {'row_number': 1, 'seat_count': 6},
                    {'row_number': 2, 'seat_count': 8},
                ]}
            ]
        },
        {
            'name': 'Cinepolis DLF Mall',
            'address': 'DLF Mall of India, Sector 18',
            'city': 'Noida',
            'state': 'Uttar Pradesh',
            'country': 'India', 
            'pincode': '201301',
            'halls': [
                {'name': 'IMAX 3D', 'rows': [
                    {'row_number': 1, 'seat_count': 10},
                    {'row_number': 2, 'seat_count': 12},
                    {'row_number': 3, 'seat_count': 14},
                    {'row_number': 4, 'seat_count': 16},
                ]},
                {'name': 'MX4D Motion', 'rows': [
                    {'row_number': 1, 'seat_count': 8},
                    {'row_number': 2, 'seat_count': 10},
                    {'row_number': 3, 'seat_count': 12},
                ]},
                {'name': 'Premium 3D', 'rows': [
                    {'row_number': 1, 'seat_count': 9},
                    {'row_number': 2, 'seat_count': 12},
                    {'row_number': 3, 'seat_count': 15},
                ]},
                {'name': 'Standard 2D', 'rows': [
                    {'row_number': 1, 'seat_count': 8},
                    {'row_number': 2, 'seat_count': 10},
                    {'row_number': 3, 'seat_count': 12},
                    {'row_number': 4, 'seat_count': 14},
                ]}
            ]
        },
        {
            'name': 'Carnival Cinemas',
            'address': 'City Center Mall, Sector 12',
            'city': 'Gurgaon',
            'state': 'Haryana',
            'country': 'India',
            'pincode': '122001',
            'halls': [
                {'name': 'IMAX Digital', 'rows': [
                    {'row_number': 1, 'seat_count': 12},
                    {'row_number': 2, 'seat_count': 14},
                    {'row_number': 3, 'seat_count': 16},
                    {'row_number': 4, 'seat_count': 18},
                ]},
                {'name': 'RealD 3D', 'rows': [
                    {'row_number': 1, 'seat_count': 10},
                    {'row_number': 2, 'seat_count': 12},
                    {'row_number': 3, 'seat_count': 14},
                ]},
                {'name': 'Dolby 7.1', 'rows': [
                    {'row_number': 1, 'seat_count': 8},
                    {'row_number': 2, 'seat_count': 10},
                    {'row_number': 3, 'seat_count': 12},
                ]},
                {'name': 'Classic 2D', 'rows': [
                    {'row_number': 1, 'seat_count': 6},
                    {'row_number': 2, 'seat_count': 8},
                    {'row_number': 3, 'seat_count': 10},
                    {'row_number': 4, 'seat_count': 12},
                ]}
            ]
        },
        {
            'name': 'SPI Cinemas',
            'address': 'Express Avenue Mall, Royapettah',
            'city': 'Chennai',
            'state': 'Tamil Nadu',
            'country': 'India',
            'pincode': '600014',
            'halls': [
                {'name': 'The Palazzo IMAX', 'rows': [
                    {'row_number': 1, 'seat_count': 16},
                    {'row_number': 2, 'seat_count': 18},
                    {'row_number': 3, 'seat_count': 20},
                    {'row_number': 4, 'seat_count': 22},
                ]},
                {'name': 'Luxe 3D', 'rows': [
                    {'row_number': 1, 'seat_count': 8},
                    {'row_number': 2, 'seat_count': 10},
                    {'row_number': 3, 'seat_count': 12},
                ]},
                {'name': 'Director\'s Cut 2D', 'rows': [
                    {'row_number': 1, 'seat_count': 6},
                    {'row_number': 2, 'seat_count': 8},
                    {'row_number': 3, 'seat_count': 10},
                ]},
                {'name': 'Elite 2D', 'rows': [
                    {'row_number': 1, 'seat_count': 9},
                    {'row_number': 2, 'seat_count': 12},
                    {'row_number': 3, 'seat_count': 15},
                ]}
            ]
        },
        {
            'name': 'Miraj Cinemas',
            'address': 'Orion Mall, Dr. Rajkumar Road',
            'city': 'Bangalore',
            'state': 'Karnataka',
            'country': 'India',
            'pincode': '560055',
            'halls': [
                {'name': 'IMAX Dome', 'rows': [
                    {'row_number': 1, 'seat_count': 14},
                    {'row_number': 2, 'seat_count': 16},
                    {'row_number': 3, 'seat_count': 18},
                    {'row_number': 4, 'seat_count': 20},
                ]},
                {'name': 'MX4D Experience', 'rows': [
                    {'row_number': 1, 'seat_count': 8},
                    {'row_number': 2, 'seat_count': 10},
                ]},
                {'name': 'Premium 3D', 'rows': [
                    {'row_number': 1, 'seat_count': 10},
                    {'row_number': 2, 'seat_count': 12},
                    {'row_number': 3, 'seat_count': 14},
                ]},
                {'name': 'Comfort 2D', 'rows': [
                    {'row_number': 1, 'seat_count': 7},
                    {'row_number': 2, 'seat_count': 9},
                    {'row_number': 3, 'seat_count': 12},
                ]}
            ]
        }
    ]
    
    theaters = []
    print("🏢 Creating theaters...")
    
    for theater_data in theaters_data:
        theater = Theater(
            name=theater_data['name'],
            address=theater_data['address'],
            city=theater_data['city'],
            state=theater_data['state'],
            country=theater_data['country'],
            pincode=theater_data['pincode']
        )
        db.session.add(theater)
        db.session.flush()
        
        print(f"   📍 {theater.name} in {theater.city}")
        
        for hall_data in theater_data['halls']:
            total_seats = sum(row['seat_count'] for row in hall_data['rows'])
            hall = Hall(
                theater_id=theater.id,
                name=hall_data['name'],
                total_seats=total_seats
            )
            db.session.add(hall)
            db.session.flush()
            
            print(f"      🎭 {hall.name} ({total_seats} seats)")
            
            for row_data in hall_data['rows']:
                row = Row(
                    hall_id=hall.id,
                    row_number=row_data['row_number'],
                    seat_count=row_data['seat_count']
                )
                db.session.add(row)
                db.session.flush()
                
                for seat_num in range(1, row.seat_count + 1):
                    is_aisle = seat_num <= 2 or seat_num >= row.seat_count - 1
                    seat = Seat(
                        row_id=row.id,
                        seat_number=seat_num,
                        is_aisle=is_aisle
                    )
                    db.session.add(seat)
        
        theaters.append(theater)
    
    db.session.commit()
    print(f"✅ Created {len(theaters)} theaters with halls and seats")
    return theaters

def create_movies():
    """Create 12 popular movies with different genres"""
    
    movies_data = [
        {
            'title': 'Avengers: Endgame',
            'description': 'The Avengers assemble once more to reverse Thanos\' actions and restore balance to the universe.',
            'duration': 181,
            'release_date': '2019-04-26',
            'genre': 'Action/Sci-Fi',
            'language': 'English'
        },
        {
            'title': 'RRR',
            'description': 'A fictional story about two legendary revolutionaries and their journey away from home before they started fighting for their country.',
            'duration': 187,
            'release_date': '2022-03-25',
            'genre': 'Action/Drama',
            'language': 'Telugu'
        },
        {
            'title': 'Spider-Man: No Way Home',
            'description': 'Peter Parker seeks help from Doctor Strange when his secret identity is revealed, but a spell goes wrong.',
            'duration': 148,
            'release_date': '2021-12-17',
            'genre': 'Action/Adventure',
            'language': 'English'
        },
        {
            'title': 'Dangal',
            'description': 'Former wrestler Mahavir Singh Phogat trains his daughters to become world-class wrestlers.',
            'duration': 161,
            'release_date': '2016-12-23',
            'genre': 'Biography/Drama',
            'language': 'Hindi'
        },
        {
            'title': 'Inception',
            'description': 'A thief who steals corporate secrets through dream-sharing technology is given the inverse task of planting an idea.',
            'duration': 148,
            'release_date': '2010-07-16',
            'genre': 'Sci-Fi/Thriller',
            'language': 'English'
        },
        {
            'title': 'Baahubali 2: The Conclusion',
            'description': 'Amarendra Baahubali, the heir apparent to the throne of Mahishmati, finds his life and relationships endangered.',
            'duration': 167,
            'release_date': '2017-04-28',
            'genre': 'Action/Drama',
            'language': 'Telugu'
        },
        {
            'title': 'The Dark Knight',
            'description': 'Batman faces the Joker, a criminal mastermind who wants to plunge Gotham City into anarchy.',
            'duration': 152,
            'release_date': '2008-07-18',
            'genre': 'Action/Crime',
            'language': 'English'
        },
        {
            'title': 'Zindagi Na Milegi Dobara',
            'description': 'Three friends on a bachelor trip in Spain confront their fears and discover themselves.',
            'duration': 155,
            'release_date': '2011-07-15',
            'genre': 'Comedy/Drama',
            'language': 'Hindi'
        },
        {
            'title': 'Dune',
            'description': 'Paul Atreides leads nomadic tribes in a revolt against the galactic emperor and his father\'s evil nemesis.',
            'duration': 155,
            'release_date': '2021-10-22',
            'genre': 'Sci-Fi/Adventure',
            'language': 'English'
        },
        {
            'title': 'Pushpa: The Rise',
            'description': 'A laborer named Pushpa makes enemies as he rises in the world of red sandalwood smuggling.',
            'duration': 179,
            'release_date': '2021-12-17',
            'genre': 'Action/Crime',
            'language': 'Telugu'
        },
        {
            'title': 'Interstellar',
            'description': 'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.',
            'duration': 169,
            'release_date': '2014-11-07',
            'genre': 'Sci-Fi/Drama',
            'language': 'English'
        },
        {
            'title': '3 Idiots',
            'description': 'Two friends search for their long-lost companion while reflecting on their college days.',
            'duration': 170,
            'release_date': '2009-12-25',
            'genre': 'Comedy/Drama',
            'language': 'Hindi'
        }
    ]
    
    movies = []
    print("\n🎬 Creating movies...")
    
    for movie_data in movies_data:
        movie = Movie(
            title=movie_data['title'],
            description=movie_data['description'],
            duration=movie_data['duration'],
            release_date=datetime.strptime(movie_data['release_date'], '%Y-%m-%d').date(),
            genre=movie_data['genre'],
            language=movie_data['language']
        )
        db.session.add(movie)
        movies.append(movie)
        print(f"   🎭 {movie.title} ({movie.genre}, {movie.duration} mins)")
    
    db.session.commit()
    print(f"✅ Created {len(movies)} movies")
    return movies

def create_shows(theaters, movies):
    """Create interesting show schedules across different days and times"""
    
    print("\n🎪 Creating show schedules...")
    
    # Get all halls from all theaters
    all_halls = []
    for theater in theaters:
        all_halls.extend(theater.halls)
    
    # Define time slots for different types of shows
    time_slots = [
        ('09:00', '12:00'),  # Morning
        ('12:30', '15:30'),  # Afternoon  
        ('16:00', '19:00'),  # Evening
        ('19:30', '22:30'),  # Night
        ('23:00', '02:00'),  # Late night
    ]
    
    # Define pricing based on hall type and time
    pricing_rules = {
        'IMAX': {'base': 450, 'premium_multiplier': 1.5},
        'MX4D': {'base': 500, 'premium_multiplier': 1.4}, 
        '4DX': {'base': 480, 'premium_multiplier': 1.4},
        '3D': {'base': 320, 'premium_multiplier': 1.3},
        '2D': {'base': 250, 'premium_multiplier': 1.2},
    }
    
    shows = []
    
    # Create shows for the next 7 days
    base_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    
    for day_offset in range(7):
        current_date = base_date + timedelta(days=day_offset)
        day_name = current_date.strftime('%A')
        
        print(f"   📅 {day_name} ({current_date.strftime('%Y-%m-%d')})")
        
        # Weekend vs weekday pricing
        is_weekend = current_date.weekday() >= 5
        weekend_multiplier = 1.2 if is_weekend else 1.0
        
        for hall in all_halls:
            # Each hall gets 3-4 shows per day
            num_shows = random.randint(3, 4)
            selected_slots = random.sample(time_slots, num_shows)
            
            for i, (start_time, end_time) in enumerate(selected_slots):
                # Select a random movie for this show
                movie = random.choice(movies)
                
                # Parse start and end times
                start_hour, start_min = map(int, start_time.split(':'))
                end_hour, end_min = map(int, end_time.split(':'))
                
                # Handle next day for late shows
                start_datetime = current_date.replace(hour=start_hour, minute=start_min)
                end_datetime = current_date.replace(hour=end_hour, minute=end_min)
                if end_hour < start_hour:  # Next day
                    end_datetime += timedelta(days=1)
                
                # Calculate pricing based on hall type
                hall_type = None
                base_price = 250  # Default
                
                for hall_keyword, pricing in pricing_rules.items():
                    if hall_keyword.lower() in hall.name.lower():
                        hall_type = hall_keyword
                        base_price = pricing['base']
                        break
                
                # Apply time-based pricing (evening/night shows cost more)
                if start_hour >= 19:  # Evening/night shows
                    time_multiplier = 1.3
                elif start_hour >= 16:  # Late afternoon
                    time_multiplier = 1.1
                else:
                    time_multiplier = 1.0
                
                final_price = base_price * time_multiplier * weekend_multiplier
                
                # Create the show
                show = Show(
                    movie_id=movie.id,
                    hall_id=hall.id,
                    start_time=start_datetime,
                    end_time=end_datetime,
                    price=round(final_price, 2)
                )
                db.session.add(show)
                shows.append(show)
        
        # Commit shows for each day
        db.session.commit()
        print(f"      ✅ Created shows for {day_name}")
    
    print(f"✅ Created {len(shows)} shows across 7 days")
    return shows

def main():
    """Main seeding function"""
    print("🌱 Starting database seeding...")
    print("=" * 50)
    
    # Create Flask app context
    app = create_app('development')
    
    with app.app_context():
        try:
            # Create theaters with halls and seats
            theaters = create_theaters()
            
            # Create movies
            movies = create_movies()
            
            # Create shows
            shows = create_shows(theaters, movies)
            
            print("\n" + "=" * 50)
            print("🎉 Database seeding completed successfully!")
            print(f"📊 Summary:")
            print(f"   🏢 Theaters: {len(theaters)}")
            print(f"   🎭 Total Halls: {sum(len(t.halls) for t in theaters)}")
            print(f"   🎬 Movies: {len(movies)}")
            print(f"   🎪 Shows: {len(shows)}")
            print(f"   💺 Total Seats: {sum(h.total_seats for t in theaters for h in t.halls)}")
            
            # Show some sample data
            print(f"\n📋 Sample theaters:")
            for theater in theaters[:3]:
                print(f"   • {theater.name} - {theater.city}")
                for hall in theater.halls[:2]:
                    print(f"     └─ {hall.name} ({hall.total_seats} seats)")
            
            print(f"\n🎬 Sample movies:")
            for movie in movies[:5]:
                print(f"   • {movie.title} ({movie.genre}) - {movie.duration} mins")
                
        except Exception as e:
            print(f"❌ Error during seeding: {str(e)}")
            db.session.rollback()
            raise
        
        print("\n🚀 Your movie booking system is ready to use!")
        print("   Frontend: http://localhost:5173")
        print("   Backend API: http://localhost:5000/api")

if __name__ == '__main__':
    main()
