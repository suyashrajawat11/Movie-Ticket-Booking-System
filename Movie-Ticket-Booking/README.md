# Movie Ticket Booking API

A RESTful API for booking movie tickets with support for group bookings, seat selection, and analytics.

## Features

- CRUD operations for movies, theaters, and shows
- Book single or multiple seats together
- Check seat availability in real-time
- Suggest alternative shows if requested seats are not available together
- Analytics for movie performance
- Concurrent booking prevention

## Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd movie-ticket-booking-api
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. **Run the application**
   ```bash
   flask run
   ```

## API Endpoints

### Movies
- `GET /api/movies` - Get all movies
- `GET /api/movies/<int:movie_id>` - Get a specific movie
- `POST /api/movies` - Create a new movie
- `PUT /api/movies/<int:movie_id>` - Update a movie
- `DELETE /api/movies/<int:movie_id>` - Delete a movie

### Theaters
- `GET /api/theaters` - Get all theaters
- `GET /api/theaters/<int:theater_id>` - Get a specific theater
- `POST /api/theaters` - Create a new theater with halls and seats
- `PUT /api/theaters/<int:theater_id>` - Update a theater
- `DELETE /api/theaters/<int:theater_id>` - Delete a theater

### Shows
- `GET /api/shows` - Get all shows
- `GET /api/shows/<int:show_id>` - Get a specific show
- `POST /api/shows` - Create a new show

### Bookings
- `POST /api/bookings` - Create a new booking (single seat)
- `POST /api/bookings/group` - Create a group booking (multiple seats)
- `GET /api/bookings/availability?show_id=<show_id>` - Check seat availability for a show
- `GET /api/bookings/suggest?movie_id=<movie_id>&theater_id=<theater_id>&show_time=<show_time>&num_seats=<num_seats>` - Suggest alternative shows with available seats

### Analytics
- `GET /api/analytics/movie/<int:movie_id>?start_date=<start_date>&end_date=<end_date>` - Get analytics for a movie

## Database Schema

The database consists of the following tables:

1. **movies** - Stores movie information
2. **theaters** - Stores theater information
3. **halls** - Stores hall information within theaters
4. **rows** - Stores row information within halls
5. **seats** - Stores seat information within rows
6. **shows** - Stores show information (movie, hall, timing, price)
7. **bookings** - Stores booking information (show, seat, user, status)

## Concurrency Handling

The API uses database-level locking to prevent double-booking of seats. When a booking request is made, the system checks seat availability within a transaction to ensure data consistency.

## Error Handling

The API returns appropriate HTTP status codes and JSON error messages for different scenarios:
- 400 Bad Request - Invalid input data
- 401 Unauthorized - Authentication required
- 403 Forbidden - Insufficient permissions
- 404 Not Found - Resource not found
- 409 Conflict - Resource conflict (e.g., seat already booked)
- 500 Internal Server Error - Server error

## Testing

To run the test suite:

```bash
python -m pytest tests/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
