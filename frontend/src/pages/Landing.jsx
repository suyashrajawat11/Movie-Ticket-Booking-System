import React from 'react'
import { Link } from 'react-router-dom'

export default function Landing() {
  return (
    <div className="landing-container">
      <nav className="landing-nav">
        <div className="nav-content">
          <div className="brand">CinemaHub</div>
          <div className="nav-links">
            <Link to="/movies">Movies</Link>
            <Link to="/theaters">Theaters</Link>
            <Link to="/booking" className="nav-cta">Book Tickets</Link>
          </div>
        </div>
      </nav>

      <div className="elegant-bg">
        <div className="bg-gradient"></div>
        <div className="bg-mesh"></div>
      </div>
      
      <section className="hero-section">
        <div className="hero-container">
          <div className="hero-content">
            <div className="hero-badge">Premium Cinema Experience</div>
            
            <h1 className="hero-title">
              The Future of
              <span className="title-highlight"> Movie Booking</span>
            </h1>
            
            <p className="hero-subtitle">
              Seamlessly discover, book, and experience the latest blockbusters 
              across India's most prestigious theaters. From IMAX to Dolby Atmos, 
              every seat tells a story.
            </p>
            
            <div className="hero-actions">
              <Link to="/booking" className="btn-primary">
                <span>Start Booking</span>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                  <path d="M5 12h14m-7-7l7 7-7 7" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
              </Link>
              
              <Link to="/movies" className="btn-secondary">
                Explore Movies
              </Link>
            </div>
          </div>
          
          <div className="hero-visual">
            <div className="visual-container">
              <div className="movie-collage">
                <div className="collage-grid">
                  <div className="poster-card large">
                    <div className="poster-content">
                      <div className="poster-title">Avengers: Endgame</div>
                      <div className="poster-genre">Action • Sci-Fi</div>
                    </div>
                  </div>
                  <div className="poster-card large">
                    <div className="poster-content">
                      <div className="poster-title">Spider-Man: No Way Home</div>
                      <div className="poster-genre">Action • Adventure</div>
                    </div>
                  </div>
                  <div className="poster-card">
                    <div className="poster-content">
                      <div className="poster-title">Top Gun: Maverick</div>
                      <div className="poster-genre">Action</div>
                    </div>
                  </div>
                  <div className="poster-card">
                    <div className="poster-content">
                      <div className="poster-title">Avatar 2</div>
                      <div className="poster-genre">Sci-Fi</div>
                    </div>
                  </div>
                  <div className="poster-card">
                    <div className="poster-content">
                      <div className="poster-title">Black Panther</div>
                      <div className="poster-genre">Action</div>
                    </div>
                  </div>
                  <div className="poster-card">
                    <div className="poster-content">
                      <div className="poster-title">Inception</div>
                      <div className="poster-genre">Thriller</div>
                    </div>
                  </div>
                  <div className="poster-card">
                    <div className="poster-content">
                      <div className="poster-title">RRR</div>
                      <div className="poster-genre">Action</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="features-section">
        <div className="features-container">
          <div className="section-header">
            <h2>Why Choose CinemaHub</h2>
            <p>Experience cinema booking redefined with cutting-edge technology</p>
          </div>
          
          <div className="features-grid">
            <div className="feature-card">
              <div className="feature-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                  <rect x="2" y="3" width="20" height="14" rx="2" stroke="currentColor" strokeWidth="2"/>
                  <line x1="8" y1="21" x2="16" y2="21" stroke="currentColor" strokeWidth="2"/>
                  <line x1="12" y1="17" x2="12" y2="21" stroke="currentColor" strokeWidth="2"/>
                </svg>
              </div>
              <h3>Premium Theaters</h3>
              <p>Access to India's finest cinema chains with IMAX, Dolby Atmos, and luxury seating</p>
            </div>
            
            <div className="feature-card">
              <div className="feature-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                  <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" stroke="currentColor" strokeWidth="2"/>
                </svg>
              </div>
              <h3>Latest Releases</h3>
              <p>First-day-first-show bookings for Hollywood blockbusters and regional cinema</p>
            </div>
            
            <div className="feature-card">
              <div className="feature-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                  <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" stroke="currentColor" strokeWidth="2"/>
                </svg>
              </div>
              <h3>Smart Booking</h3>
              <p>Real-time seat selection, group bookings, and instant confirmation</p>
            </div>
          </div>
        </div>
      </section>

      <section className="stats-section">
        <div className="stats-container">
          <div className="stats-grid">
            <div className="stat-item">
              <div className="stat-number">12+</div>
              <div className="stat-label">Premium Theaters</div>
            </div>
            <div className="stat-item">
              <div className="stat-number">4.8K+</div>
              <div className="stat-label">Total Seats</div>
            </div>
            <div className="stat-item">
              <div className="stat-number">18+</div>
              <div className="stat-label">Latest Movies</div>
            </div>
            <div className="stat-item">
              <div className="stat-number">72+</div>
              <div className="stat-label">Daily Shows</div>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}
