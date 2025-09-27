#!/usr/bin/env python3
"""
Mega Database Seeding Script - 12 Theaters, Hollywood Movies, Extensive Shows
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

def create_mega_theaters():
    """Create 12 theaters across major Indian cities"""
    
    theaters_data = [
        {
            'name': 'PVR Cinemas Phoenix Mills',
            'address': 'High Street Phoenix, Lower Parel',
            'city': 'Mumbai',
            'state': 'Maharashtra',
            'country': 'India',
            'pincode': '400013',
            'halls': ['IMAX Laser', 'MX4D Motion', 'Dolby Atmos 3D', 'Premium 2D']
        },
        {
            'name': 'INOX Megaplex R City',
            'address': 'R City Mall, Ghatkopar West',
            'city': 'Mumbai',
            'state': 'Maharashtra',
            'country': 'India',
            'pincode': '400086',
            'halls': ['IMAX Digital', '4DX Experience', 'RealD 3D', 'Gold Class']
        },
        {
            'name': 'Cinepolis DLF CyberHub',
            'address': 'DLF Cyber City, Sector 24',
            'city': 'Gurgaon',
            'state': 'Haryana',
            'country': 'India',
            'pincode': '122002',
            'halls': ['IMAX 70mm', 'MX4D Supreme', 'VIP 3D', 'Classic 2D']
        },
        {
            'name': 'Carnival Cinemas Nexus',
            'address': 'Nexus Mall, Koramangala',
            'city': 'Bangalore',
            'state': 'Karnataka',
            'country': 'India',
            'pincode': '560095',
            'halls': ['IMAX Enhanced', 'Motion Plus 4D', 'Dolby Vision 3D', 'Recliner 2D']
        },
        {
            'name': 'SPI Cinemas Express Avenue',
            'address': 'Express Avenue Mall, Royapettah',
            'city': 'Chennai',
            'state': 'Tamil Nadu',
            'country': 'India',
            'pincode': '600014',
            'halls': ['The Palazzo IMAX', 'Luxe Motion 4D', 'Director\'s Cut 3D', 'Elite 2D']
        },
        {
            'name': 'Miraj Cinemas Forum Mall',
            'address': 'Forum Mall, Hosur Road',
            'city': 'Bangalore',
            'state': 'Karnataka',
            'country': 'India',
            'pincode': '560068',
            'halls': ['IMAX Dome', 'MX4D Extreme', 'Premium Plus 3D', 'Comfort 2D']
        },
        {
            'name': 'PVR Select City Walk',
            'address': 'Select City Walk, Saket',
            'city': 'New Delhi',
            'state': 'Delhi',
            'country': 'India',
            'pincode': '110017',
            'halls': ['IMAX Laser GT', 'MX4D Revolution', 'Dolby Cinema 3D', 'Director\'s Cut 2D']
        },
        {
            'name': 'INOX Palladium Mall',
            'address': 'Palladium Mall, High Street Phoenix',
            'city': 'Mumbai',
            'state': 'Maharashtra',
            'country': 'India',
            'pincode': '400013',
            'halls': ['IMAX Digital Plus', '4DX Screen X', 'Insignia 3D', 'Club 2D']
        },
        {
            'name': 'Cinepolis Fun Republic',
            'address': 'Fun Republic Mall, Andheri West',
            'city': 'Mumbai',
            'state': 'Maharashtra',
            'country': 'India',
            'pincode': '400053',
            'halls': ['IMAX Xenon', 'MX4D Ultra', 'VIP Premium 3D', 'Standard 2D']
        },
        {
            'name': 'Carnival Cinemas Ameerpet',
            'address': 'Ameerpet Metro Station Complex',
            'city': 'Hyderabad',
            'state': 'Telangana',
            'country': 'India',
            'pincode': '500016',
            'halls': ['IMAX Digital 2K', 'Motion Seat 4D', 'Dolby Atmos 3D', 'Luxury 2D']
        },
        {
            'name': 'PVR Orion Mall',
            'address': 'Orion Mall, Dr. Rajkumar Road',
            'city': 'Bangalore',
            'state': 'Karnataka',
            'country': 'India',
            'pincode': '560055',
            'halls': ['IMAX Laser 4K', 'MX4D Motion Pro', 'Dolby Vision 3D', 'Gold Lounge 2D']
        },
        {
            'name': 'INOX Lulu Mall',
            'address': 'Lulu International Shopping Mall',
            'city': 'Kochi',
            'state': 'Kerala',
            'country': 'India',
            'pincode': '682025',
            'halls': ['IMAX Digital 4K', '4DX Motion', 'Premium 3D', 'Classic 2D']
        }
    ]
    
    theaters = []
    print("🏢 Creating 12 mega theaters...")
    
    for i, theater_data in enumerate(theaters_data, 1):
        # Create theater
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
        
        print(f"   📍 {i}/12: {theater.name} in {theater.city}")
        
        # Create 4 halls for this theater
        for hall_name in theater_data['halls']:
            hall = Hall(
                theater_id=theater.id,
                name=hall_name,
                total_seats=100  # 10 rows x 10 seats = 100 seats per hall
            )
            db.session.add(hall)
            db.session.flush()
            
            print(f"      🎭 {hall.name} (100 seats)")
            
            # Create 10 rows with 10 seats each
            for row_num in range(1, 11):
                row = Row(
                    hall_id=hall.id,
                    row_number=row_num,
                    seat_count=10
                )
                db.session.add(row)
                db.session.flush()
                
                # Create 10 seats for this row
                for seat_num in range(1, 11):
                    # Mark aisle seats (first 2 and last 2 in each row)
                    is_aisle = seat_num <= 2 or seat_num >= 9
                    seat = Seat(
                        row_id=row.id,
                        seat_number=seat_num,
                        is_aisle=is_aisle
                    )
                    db.session.add(seat)
        
        theaters.append(theater)
        
        # Commit every 3 theaters to avoid large transactions
        if i % 3 == 0:
            db.session.commit()
            print(f"      ✅ Committed theaters {i-2} to {i}")
    
    # Final commit
    db.session.commit()
    print(f"✅ Created {len(theaters)} theaters with 48 halls and 4,800 seats total!")
    return theaters

def create_hollywood_movies():
    """Create 18 movies - 12 existing + 6 new Hollywood blockbusters"""
    
    # Existing movies (keep them)
    existing_movies = [
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
            'description': 'A fictional story about two legendary revolutionaries and their journey away from home.',
            'duration': 187,
            'release_date': '2022-03-25',
            'genre': 'Action/Drama',
            'language': 'Telugu'
        },
        {
            'title': 'Spider-Man: No Way Home',
            'description': 'Peter Parker seeks help from Doctor Strange when his secret identity is revealed.',
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
            'description': 'A thief who steals corporate secrets through dream-sharing technology.',
            'duration': 148,
            'release_date': '2010-07-16',
            'genre': 'Sci-Fi/Thriller',
            'language': 'English'
        },
        {
            'title': 'Baahubali 2: The Conclusion',
            'description': 'Amarendra Baahubali finds his life and relationships endangered.',
            'duration': 167,
            'release_date': '2017-04-28',
            'genre': 'Action/Drama',
            'language': 'Telugu'
        },
        {
            'title': 'The Dark Knight',
            'description': 'Batman faces the Joker, a criminal mastermind who wants to plunge Gotham into anarchy.',
            'duration': 152,
            'release_date': '2008-07-18',
            'genre': 'Action/Crime',
            'language': 'English'
        },
        {
            'title': 'Zindagi Na Milegi Dobara',
            'description': 'Three friends on a bachelor trip in Spain confront their fears.',
            'duration': 155,
            'release_date': '2011-07-15',
            'genre': 'Comedy/Drama',
            'language': 'Hindi'
        },
        {
            'title': 'Dune',
            'description': 'Paul Atreides leads nomadic tribes in a revolt against the galactic emperor.',
            'duration': 155,
            'release_date': '2021-10-22',
            'genre': 'Sci-Fi/Adventure',
            'language': 'English'
        },
        {
            'title': 'Pushpa: The Rise',
            'description': 'A laborer named Pushpa makes enemies as he rises in the world of smuggling.',
            'duration': 179,
            'release_date': '2021-12-17',
            'genre': 'Action/Crime',
            'language': 'Telugu'
        },
        {
            'title': 'Interstellar',
            'description': 'A team of explorers travel through a wormhole to ensure humanity\'s survival.',
            'duration': 169,
            'release_date': '2014-11-07',
            'genre': 'Sci-Fi/Drama',
            'language': 'English'
        },
        {
            'title': '3 Idiots',
            'description': 'Two friends search for their long-lost companion while reflecting on college days.',
            'duration': 170,
            'release_date': '2009-12-25',
            'genre': 'Comedy/Drama',
            'language': 'Hindi'
        }
    ]
    
    # New Hollywood blockbusters
    new_hollywood_movies = [
        {
            'title': 'Top Gun: Maverick',
            'description': 'After thirty years, Maverick is still pushing the envelope as a top naval aviator.',
            'duration': 131,
            'release_date': '2022-05-27',
            'genre': 'Action/Drama',
            'language': 'English'
        },
        {
            'title': 'Avatar: The Way of Water',
            'description': 'Jake Sully lives with his newfound family formed on the extrasolar moon Pandora.',
            'duration': 192,
            'release_date': '2022-12-16',
            'genre': 'Sci-Fi/Adventure',
            'language': 'English'
        },
        {
            'title': 'Black Panther: Wakanda Forever',
            'description': 'The people of Wakanda fight to protect their home from intervening world powers.',
            'duration': 161,
            'release_date': '2022-11-11',
            'genre': 'Action/Adventure',
            'language': 'English'
        },
        {
            'title': 'Jurassic World Dominion',
            'description': 'Four years after the destruction of Isla Nublar, dinosaurs now live alongside humans.',
            'duration': 147,
            'release_date': '2022-06-10',
            'genre': 'Action/Adventure',
            'language': 'English'
        },
        {
            'title': 'Doctor Strange in the Multiverse of Madness',
            'description': 'Dr. Strange casts a forbidden spell that opens the doorway to the multiverse.',
            'duration': 126,
            'release_date': '2022-05-06',
            'genre': 'Action/Fantasy',
            'language': 'English'
        },
        {
            'title': 'The Batman',
            'description': 'Batman ventures into Gotham City\'s underworld when a sadistic killer leaves behind cryptic messages.',
            'duration': 176,
            'release_date': '2022-03-04',
            'genre': 'Action/Crime',
            'language': 'English'
        }
    ]
    
    all_movies = existing_movies + new_hollywood_movies
    movies = []
    
    print("\n🎬 Creating 18 movies (12 existing + 6 Hollywood blockbusters)...")
    
    for i, movie_data in enumerate(all_movies, 1):
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
        
        if i <= 12:
            print(f"   🎭 {i}/18: {movie.title} ({movie.genre}) - Existing")
        else:
            print(f"   🎬 {i}/18: {movie.title} ({movie.genre}) - NEW Hollywood!")
    
    db.session.commit()
    print(f"✅ Created {len(movies)} movies total!")
    return movies

def create_extensive_shows(theaters, movies):
    """Create 4 shows for each movie across different theaters and times"""
    
    print("\n🎪 Creating extensive show schedules...")
    print(f"   Target: 4 shows × {len(movies)} movies = {4 * len(movies)} shows")
    
    # Get all halls from all theaters
    all_halls = []
    for theater in theaters:
        all_halls.extend(theater.halls)
    
    print(f"   Available halls: {len(all_halls)} across {len(theaters)} theaters")
    
    # Define time slots for different show times
    time_slots = [
        ('09:30', '12:30'),  # Morning
        ('13:00', '16:00'),  # Afternoon  
        ('16:30', '19:30'),  # Evening
        ('20:00', '23:00'),  # Night
        ('10:00', '13:00'),  # Late Morning
        ('14:00', '17:00'),  # Late Afternoon
        ('18:00', '21:00'),  # Prime Evening
        ('21:30', '00:30'),  # Late Night
    ]
    
    # Define pricing based on hall type
    pricing_rules = {
        'IMAX': 550,
        'MX4D': 600,
        '4DX': 580,
        'Motion': 520,
        '3D': 380,
        '2D': 280,
        'Premium': 450,
        'VIP': 650,
        'Gold': 500,
        'Luxury': 480,
        'Classic': 250,
        'Standard': 220
    }
    
    shows = []
    
    # Create shows for the next 5 days
    base_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    
    for movie in movies:
        print(f"   🎬 Creating 4 shows for: {movie.title}")
        
        # Create 4 shows for this movie
        for show_num in range(4):
            # Select random day (0-4), hall, and time slot
            day_offset = random.randint(0, 4)
            hall = random.choice(all_halls)
            start_time_str, end_time_str = random.choice(time_slots)
            
            current_date = base_date + timedelta(days=day_offset)
            
            # Parse start and end times
            start_hour, start_min = map(int, start_time_str.split(':'))
            end_hour, end_min = map(int, end_time_str.split(':'))
            
            # Handle next day for late shows
            start_datetime = current_date.replace(hour=start_hour, minute=start_min)
            end_datetime = current_date.replace(hour=end_hour, minute=end_min)
            if end_hour < start_hour:  # Next day
                end_datetime += timedelta(days=1)
            
            # Calculate pricing based on hall type
            base_price = 280  # Default
            
            for hall_keyword, price in pricing_rules.items():
                if hall_keyword.lower() in hall.name.lower():
                    base_price = price
                    break
            
            # Apply time-based pricing
            if start_hour >= 18:  # Evening/night shows
                time_multiplier = 1.4
            elif start_hour >= 13:  # Afternoon shows
                time_multiplier = 1.2
            else:  # Morning shows
                time_multiplier = 1.0
            
            # Weekend pricing
            is_weekend = current_date.weekday() >= 5
            weekend_multiplier = 1.3 if is_weekend else 1.0
            
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
        
        # Commit after each movie to avoid large transactions
        db.session.commit()
    
    print(f"✅ Created {len(shows)} shows across 5 days!")
    return shows

def main():
    """Main mega seeding function"""
    print("🚀 MEGA DATABASE SEEDING STARTED!")
    print("=" * 60)
    
    # Create Flask app context
    app = create_app('development')
    
    with app.app_context():
        try:
            # Create 12 mega theaters
            theaters = create_mega_theaters()
            
            # Create 18 movies (12 existing + 6 Hollywood)
            movies = create_hollywood_movies()
            
            # Create extensive shows (4 per movie)
            shows = create_extensive_shows(theaters, movies)
            
            print("\n" + "=" * 60)
            print("🎉 MEGA SEEDING COMPLETED SUCCESSFULLY!")
            print("📊 FINAL STATISTICS:")
            print(f"   🏢 Theaters: {len(theaters)}")
            print(f"   🎭 Total Halls: {len(theaters) * 4} (4 per theater)")
            print(f"   💺 Total Seats: {len(theaters) * 4 * 100:,} (100 per hall)")
            print(f"   🎬 Movies: {len(movies)} (12 existing + 6 Hollywood)")
            print(f"   🎪 Shows: {len(shows)} (4 per movie)")
            print(f"   💰 Price Range: ₹220 - ₹850 (based on hall type & timing)")
            
            # Show some sample data
            print(f"\n🏢 Sample Theaters:")
            for theater in theaters[:4]:
                print(f"   • {theater.name} - {theater.city}")
            
            print(f"\n🎬 New Hollywood Movies Added:")
            hollywood_movies = [m for m in movies if m.language == 'English'][-6:]
            for movie in hollywood_movies:
                print(f"   • {movie.title} ({movie.duration} mins)")
                
            print(f"\n💡 USAGE TIPS:")
            print(f"   • Each theater has 4 halls with different experiences")
            print(f"   • Each hall has 10 rows × 10 seats = 100 seats")
            print(f"   • IMAX/MX4D halls have premium pricing")
            print(f"   • Evening shows cost more than morning shows")
            print(f"   • Weekend shows have 30% premium")
            
        except Exception as e:
            print(f"❌ Error during mega seeding: {str(e)}")
            db.session.rollback()
            raise
        
        print(f"\n🚀 Your MEGA movie booking system is ready!")
        print(f"   Frontend: http://localhost:5173")
        print(f"   Backend API: http://localhost:5000/api")
        print(f"   Total Capacity: {len(theaters) * 4 * 100:,} seats across India!")

if __name__ == '__main__':
    main()
