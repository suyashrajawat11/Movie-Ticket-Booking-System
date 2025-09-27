import React from 'react'
import { Routes, Route, useLocation } from 'react-router-dom'
import Navbar from './components/Navbar'
import Landing from './pages/Landing'
import Movies from './pages/Movies'
import Theaters from './pages/Theaters'
import Shows from './pages/Shows'
import Booking from './pages/Booking'
import Analytics from './pages/Analytics'

export default function App() {
  const location = useLocation()
  const isLandingPage = location.pathname === '/'

  return (
    <div className="app-container">
      {!isLandingPage && <Navbar />}
      <div className={isLandingPage ? '' : 'content'}>
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="/movies" element={<Movies />} />
          <Route path="/theaters" element={<Theaters />} />
          <Route path="/shows" element={<Shows />} />
          <Route path="/booking" element={<Booking />} />
          <Route path="/analytics" element={<Analytics />} />
        </Routes>
      </div>
    </div>
  )
}
