import React from 'react'
import { NavLink, Link } from 'react-router-dom'

export default function Navbar() {
  return (
    <nav className="navbar">
      <Link to="/" className="nav-brand">🎬 Movie Booking</Link>
      <div className="nav-links">
        <NavLink to="/movies" className={({isActive}) => isActive ? 'active' : ''}>Movies</NavLink>
        <NavLink to="/theaters" className={({isActive}) => isActive ? 'active' : ''}>Theaters</NavLink>
        <NavLink to="/shows" className={({isActive}) => isActive ? 'active' : ''}>Shows</NavLink>
        <NavLink to="/booking" className={({isActive}) => isActive ? 'active' : ''}>Booking</NavLink>
        <NavLink to="/analytics" className={({isActive}) => isActive ? 'active' : ''}>Analytics</NavLink>
      </div>
    </nav>
  )
}
