#!/usr/bin/env python3
"""
Theater Seeding Script - Creates theaters, halls, rows, and seats
"""

import sys
import os

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from app.models.theater import Theater
from app.models.hall import Hall
from app.models.row import Row
from app.models.seat import Seat

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
                ]},
                {'name': 'MX4D', 'rows': [
                    {'row_number': 1, 'seat_count': 8},
                    {'row_number': 2, 'seat_count': 10},
                ]},
                {'name': '3D Premium', 'rows': [
                    {'row_number': 1, 'seat_count': 10},
                    {'row_number': 2, 'seat_count': 12},
                ]},
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
                ]},
                {'name': '4DX', 'rows': [
                    {'row_number': 1, 'seat_count': 6},
                    {'row_number': 2, 'seat_count': 8},
                ]},
                {'name': 'Dolby Atmos 3D', 'rows': [
                    {'row_number': 1, 'seat_count': 12},
                    {'row_number': 2, 'seat_count': 14},
                ]},
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
                ]},
                {'name': 'Premium 3D', 'rows': [
                    {'row_number': 1, 'seat_count': 9},
                    {'row_number': 2, 'seat_count': 12},
                ]},
            ]
        },
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

def main():
    """Main function"""
    print("🏢 Creating theaters, halls, and seats...")
    
    app = create_app('development')
    
    with app.app_context():
        try:
            theaters = create_theaters()
            
            print(f"\n✅ Theater seeding completed!")
            print(f"📊 Created:")
            print(f"   🏢 Theaters: {len(theaters)}")
            print(f"   🎭 Total Halls: {sum(len(t.halls) for t in theaters)}")
            print(f"   💺 Total Seats: {sum(h.total_seats for t in theaters for h in t.halls)}")
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            db.session.rollback()
            raise

if __name__ == '__main__':
    main()
