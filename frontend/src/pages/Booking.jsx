import React, { useEffect, useState } from 'react'
import { listMovies } from '../api/movies'
import { listTheaters } from '../api/theaters'
import { listShows, getShow } from '../api/shows'
import { checkAvailability, createGroupBooking, suggestAlternates } from '../api/bookings'
import SeatMap from '../components/SeatMap'

export default function Booking() {
  const [movies, setMovies] = useState([])
  const [theaters, setTheaters] = useState([])
  const [shows, setShows] = useState([])
  const [selection, setSelection] = useState({ movie_id:'', theater_id:'', show_id:'', count:2 })
  const [availability, setAvailability] = useState(null)
  const [selectedSeats, setSelectedSeats] = useState([])
  const [suggestions, setSuggestions] = useState([])

  useEffect(() => { (async () => {
    setMovies(await listMovies())
    setTheaters(await listTheaters())
    setShows(await listShows())
  })() }, [])

  const filteredShows = shows.filter(show => {
    if (selection.movie_id && show.movie_id !== Number(selection.movie_id)) return false
    if (selection.theater_id) {
      const theater = theaters.find(t => t.id === Number(selection.theater_id))
      const hallIds = theater?.halls?.map(h => h.id) || []
      if (!hallIds.includes(show.hall_id)) return false
    }
    return true
  })

  useEffect(() => { (async () => {
    if (selection.show_id) {
      const data = await checkAvailability(selection.show_id)
      const seats = data.availability.map(s => ({
        seat_id: s.seat_id,
        row_id: s.row_number,
        seat_number: s.seat_number,
        is_aisle: false,
        is_available: s.status === 'available'
      }))
      const availableCount = seats.filter(s => s.is_available).length
      setAvailability({ 
        show_id: data.show_id,
        hall_id: data.hall_id,
        seats,
        available_seats: availableCount,
        total_seats: seats.length
      })
    } else {
      setAvailability(null)
    }
    setSelectedSeats([])
  })() }, [selection.show_id])

  const onToggleSeat = (id) => {
    setSelectedSeats(prev => {
      const newSeats = prev.includes(id) ? prev.filter(x=>x!==id) : [...prev, id]
      setSelection(sel => ({...sel, count: newSeats.length || 1}))
      return newSeats
    })
  }

  const onAutoPick = (ids) => {
    setSelectedSeats(ids)
    setSelection(sel => ({...sel, count: ids.length || 1}))
  }

  const onBook = async () => {
    if (!selection.show_id || selectedSeats.length === 0) return alert('Select seats first')
    
    try {
      const currentAvailability = await checkAvailability(selection.show_id)
      const unavailableSeats = selectedSeats.filter(seatId => {
        const seat = currentAvailability.seats.find(s => s.seat_id === seatId)
        return !seat || !seat.is_available
      })
      
      if (unavailableSeats.length > 0) {
        alert('Some selected seats are no longer available. Please refresh and select again.')
        const data = await checkAvailability(selection.show_id)
        setAvailability({ ...data, seats: data.seats.map(s=>({ ...s })) })
        setSelectedSeats([])
        return
      }
      
      const res = await createGroupBooking({ show_id: Number(selection.show_id), seat_ids: selectedSeats, user_id: 1 })
      alert(`🎉 Booking Successful!\nReference: ${res.booking_reference}\nSeats: ${selectedSeats.length}\nTotal: ₹${res.total_price}`)
      
      const data = await checkAvailability(selection.show_id)
      setAvailability({ ...data, seats: data.seats.map(s=>({ ...s })) })
      setSelectedSeats([])
    } catch (e) { 
      if (e.message.includes('Booking conflict')) {
        alert('⚠️ Booking conflict detected. Some seats may have been booked by another user. Please refresh and try again.')
        try {
          const data = await checkAvailability(selection.show_id)
          setAvailability({ ...data, seats: data.seats.map(s=>({ ...s })) })
          setSelectedSeats([])
        } catch (refreshError) {
          console.error('Failed to refresh availability:', refreshError)
        }
      } else {
        alert(e.message)
      }
    }
  }

  const onSuggest = async () => {
    if (!selection.movie_id || !selection.theater_id) return alert('Pick a movie and theater')
    const show = shows.find(s => s.id === Number(selection.show_id))
    const show_time = show ? show.start_time : new Date().toISOString().slice(0,19).replace('T',' ')
    const data = await suggestAlternates({ movie_id: selection.movie_id, theater_id: selection.theater_id, show_time, num_seats: selection.count })
    setSuggestions(data.suggested_shows)
  }

  return (
    <div>
      <h2>Booking</h2>
      <div className="card">
        <div className="grid">
          <div>
            <div className="label">Movie</div>
            <select className="input" value={selection.movie_id} onChange={e=>setSelection({...selection, movie_id:Number(e.target.value), show_id:''})}>
              <option value="">Select</option>
              {movies.map(m => <option key={m.id} value={m.id}>{m.title}</option>)}
            </select>
          </div>
          <div>
            <div className="label">Theater</div>
            <select className="input" value={selection.theater_id} onChange={e=>setSelection({...selection, theater_id:Number(e.target.value), show_id:''})}>
              <option value="">Select</option>
              {theaters.map(t => <option key={t.id} value={t.id}>{t.name}</option>)}
            </select>
          </div>
          <div>
            <div className="label">Show</div>
            <select className="input" value={selection.show_id} onChange={e=>setSelection({...selection, show_id:Number(e.target.value)})}>
              <option value="">Select</option>
              {filteredShows.map(s => {
                const movie = movies.find(m => m.id === s.movie_id)
                return (
                  <option key={s.id} value={s.id}>
                    {movie?.title || 'Unknown'} • Hall {s.hall_id} • {new Date(s.start_time).toLocaleString()}
                  </option>
                )
              })}
            </select>
          </div>
          <div>
            <div className="label">Friends (seats) count</div>
            <input className="input" type="number" min={1} value={selectedSeats.length || selection.count} readOnly style={{backgroundColor: '#2a2d3a', color: '#a9b1c6'}} />
            <div style={{fontSize: 12, color: '#a9b1c6', marginTop: 4}}>Auto-updates as you select seats</div>
          </div>
        </div>
      </div>

      {availability && (
        <div className="card">
          <div style={{display:'flex', justifyContent:'space-between', alignItems:'center'}}>
            <div>
              <div style={{fontWeight:700}}>Show #{availability.show_id} • Hall {availability.hall_id}</div>
              <div style={{fontSize:12, color:'#a9b1c6'}}>Available: {availability.available_seats} / {availability.total_seats}</div>
            </div>
            <div className="row" style={{maxWidth:500}}>
              <button className="btn secondary" onClick={async () => {
                const data = await checkAvailability(selection.show_id)
                setAvailability({ ...data, seats: data.seats.map(s=>({ ...s })) })
                setSelectedSeats([])
              }}>🔄 Refresh</button>
              <button className="btn secondary" onClick={onSuggest}>Suggest alternates</button>
              <button className="btn" onClick={onBook}>Book selected ({selectedSeats.length})</button>
            </div>
          </div>
          <div style={{marginTop:12}}>
            <SeatMap seats={availability.seats} selected={selectedSeats} onToggle={onToggleSeat} desiredCount={selection.count} onAutoPick={onAutoPick} />
          </div>
        </div>
      )}

      {suggestions.length > 0 && (
        <div className="card">
          <div style={{fontWeight:700, marginBottom:8}}>Suggested Shows</div>
          <div className="grid">
            {suggestions.map(s => (
              <div className="card" key={s.show_id}>
                <div>Show #{s.show_id}</div>
                <div style={{fontSize:12, color:'#a9b1c6'}}>{new Date(s.start_time).toLocaleString()}</div>
                <div style={{marginTop:6}}>Price: ₹{s.price}</div>
                <button className="btn" style={{marginTop:8}} onClick={()=>setSelection({...selection, show_id: s.show_id})}>Select</button>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}
