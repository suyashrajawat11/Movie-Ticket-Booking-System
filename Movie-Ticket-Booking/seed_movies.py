#!/usr/bin/env python3
"""
Movie Seeding Script - Creates popular movies
"""

import sys
import os
from datetime import datetime

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from app.models.movie import Movie

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
    
    movies = []
    print("🎬 Creating movies...")
    
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

def main():
    """Main function"""
    print("🎬 Creating movies...")
    
    app = create_app('development')
    
    with app.app_context():
        try:
            movies = create_movies()
            
            print(f"\n✅ Movie seeding completed!")
            print(f"📊 Created {len(movies)} movies across various genres")
            
            # Show sample movies
            print(f"\n🎬 Sample movies:")
            for movie in movies[:5]:
                print(f"   • {movie.title} ({movie.genre}) - {movie.duration} mins")
                
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            db.session.rollback()
            raise

if __name__ == '__main__':
    main()
