#!/usr/bin/env python3
"""
Show Seeding Script - Creates show schedules for theaters and movies
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
from app.models.show import Show

def create_shows():
    """Create show schedules for the next 3 days (faster than 7 days)"""
    
    print("🎪 Creating show schedules...")
    
    # Get all movies and halls
    movies = Movie.query.all()
    halls = Hall.query.all()
    
    if not movies:
        print("❌ No movies found! Run seed_movies.py first")
        return []
        
    if not halls:
        print("❌ No halls found! Run seed_theaters.py first")
        return []
    
    print(f"   Found {len(movies)} movies and {len(halls)} halls")
    
    # Define time slots for shows
    time_slots = [
        ('10:00', '13:00'),  # Morning
        ('14:00', '17:00'),  # Afternoon  
        ('18:00', '21:00'),  # Evening
        ('21:30', '00:30'),  # Night
    ]
    
    # Define pricing based on hall type
    pricing_rules = {
        'IMAX': 450,
        'MX4D': 500,
        '4DX': 480,
        '3D': 320,
        '2D': 250,
    }
    
    shows = []
    
    base_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    
    for day_offset in range(3):
        current_date = base_date + timedelta(days=day_offset)
        day_name = current_date.strftime('%A')
        
        print(f"   📅 {day_name} ({current_date.strftime('%Y-%m-%d')})")
        
        is_weekend = current_date.weekday() >= 5
        weekend_multiplier = 1.2 if is_weekend else 1.0
        
        for hall in halls:
            selected_slots = random.sample(time_slots, 2)
            
            for start_time, end_time in selected_slots:
                movie = random.choice(movies)
                
                start_hour, start_min = map(int, start_time.split(':'))
                end_hour, end_min = map(int, end_time.split(':'))
                
                # Handle next day for late shows
                start_datetime = current_date.replace(hour=start_hour, minute=start_min)
                end_datetime = current_date.replace(hour=end_hour, minute=end_min)
                if end_hour < start_hour:  # Next day
                    end_datetime += timedelta(days=1)
                
                # Calculate pricing based on hall type
                base_price = 250  # Default
                
                for hall_keyword, price in pricing_rules.items():
                    if hall_keyword.lower() in hall.name.lower():
                        base_price = price
                        break
                
                # Apply time-based pricing (evening/night shows cost more)
                if start_hour >= 18:  # Evening/night shows
                    time_multiplier = 1.3
                else:
                    time_multiplier = 1.0
                
                final_price = base_price * time_multiplier * weekend_multiplier
                
                show = Show(
                    movie_id=movie.id,
                    hall_id=hall.id,
                    start_time=start_datetime,
                    end_time=end_datetime,
                    price=round(final_price, 2)
                )
                db.session.add(show)
                shows.append(show)
        
        # Commit shows for each day to avoid large transactions
        db.session.commit()
        print(f"      ✅ Created shows for {day_name}")
    
    print(f"✅ Created {len(shows)} shows across 3 days")
    return shows

def main():
    """Main function"""
    print("🎪 Creating show schedules...")
    
    app = create_app('development')
    
    with app.app_context():
        try:
            shows = create_shows()
            
            print(f"\n✅ Show seeding completed!")
            print(f"📊 Created {len(shows)} shows")
            
            # Show some sample data
            if shows:
                print(f"\n🎪 Sample shows:")
                for show in shows[:5]:
                    movie = Movie.query.get(show.movie_id)
                    hall = Hall.query.get(show.hall_id)
                    theater = Theater.query.get(hall.theater_id) if hall else None
                    print(f"   • {movie.title if movie else 'Unknown'} at {theater.name if theater else 'Unknown'} - {hall.name if hall else 'Unknown'}")
                    print(f"     {show.start_time.strftime('%Y-%m-%d %H:%M')} - ₹{show.price}")
                
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            db.session.rollback()
            raise

if __name__ == '__main__':
    main()
