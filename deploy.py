#!/usr/bin/env python3
"""
Deployment script for Movie Ticket Booking System
Initializes database and seeds data for production
"""

import os
from app import create_app, db

def deploy():
    """Run deployment tasks."""
    
    # Use production config
    app = create_app('production')
    
    with app.app_context():
        # Create database tables
        db.create_all()
        
        # Import and run seeders
        try:
            from seed_movies import create_movies
            from seed_theaters import create_theaters  
            from seed_shows import create_shows
            
            print("🎬 Seeding movies...")
            movies = create_movies()
            
            print("🏢 Seeding theaters...")
            theaters = create_theaters()
            
            print("🎭 Seeding shows...")
            shows = create_shows(movies, [hall for theater in theaters for hall in theater.halls])
            
            db.session.commit()
            print("✅ Database seeded successfully!")
            
        except Exception as e:
            print(f"⚠️ Seeding failed: {e}")
            print("Database tables created, but no seed data.")

if __name__ == '__main__':
    deploy()
