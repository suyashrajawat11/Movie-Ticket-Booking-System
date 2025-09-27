import React, { useEffect, useState } from 'react'
import { listMovies } from '../api/movies'
import { movieAnalytics, analyticsOverview } from '../api/analytics'

export default function Analytics() {
  const [movies, setMovies] = useState([])
  const [movieId, setMovieId] = useState('')
  const [range, setRange] = useState({ start_date: '', end_date: '' })
  const [data, setData] = useState(null)
  const [overview, setOverview] = useState(null)

  useEffect(()=>{ 
    (async()=>{
      setMovies(await listMovies())
      setOverview(await analyticsOverview())
    })() 
  }, [])

  const load = async () => {
    if (!movieId) return
    const res = await movieAnalytics(movieId, { ...range })
    setData(res)
  }

  return (
    <div>
      <h2>Analytics</h2>
      
      {overview && (
        <div className="card">
          <div style={{fontWeight:700, marginBottom:12}}>📊 Overview</div>
          <div className="grid" style={{gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))'}}>
            <div className="card">
              <div style={{fontSize:24, fontWeight:700, color:'#4CAF50'}}>{overview.total_bookings}</div>
              <div style={{fontSize:14, color:'#a9b1c6'}}>Total Bookings</div>
            </div>
            <div className="card">
              <div style={{fontSize:24, fontWeight:700, color:'#2196F3'}}>₹{overview.total_revenue.toLocaleString()}</div>
              <div style={{fontSize:14, color:'#a9b1c6'}}>Total Revenue</div>
            </div>
          </div>
          
          {overview.movies && overview.movies.length > 0 && (
            <div style={{marginTop:16}}>
              <div style={{fontWeight:600, marginBottom:8}}>🎬 Movies Performance</div>
              <div className="grid">
                {overview.movies.map((movie, i) => (
                  <div key={i} className="card">
                    <div style={{fontWeight:600}}>{movie.movie}</div>
                    <div style={{fontSize:12, color:'#a9b1c6'}}>
                      {movie.bookings} tickets • ₹{movie.revenue.toLocaleString()}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      )}
      
      <div className="card">
        <div style={{fontWeight:700, marginBottom:12}}>🔍 Detailed Movie Analytics</div>
        <div className="grid">
          <div>
            <div className="label">Movie</div>
            <select className="input" value={movieId} onChange={e=>setMovieId(Number(e.target.value))}>
              <option value="">Select</option>
              {movies.map(m => <option key={m.id} value={m.id}>{m.title}</option>)}
            </select>
          </div>
          <div>
            <div className="label">Start date (YYYY-MM-DD)</div>
            <input className="input" placeholder="2025-01-01" value={range.start_date} onChange={e=>setRange({...range, start_date:e.target.value})} />
          </div>
          <div>
            <div className="label">End date (YYYY-MM-DD)</div>
            <input className="input" placeholder="2025-12-31" value={range.end_date} onChange={e=>setRange({...range, end_date:e.target.value})} />
          </div>
          <div>
            <button className="btn" onClick={load}>Load</button>
          </div>
        </div>
      </div>

      {data && (
        <div className="card">
          <div style={{fontWeight:700, marginBottom:8}}>Summary</div>
          <div>Total tickets sold: {data.total_tickets_sold}</div>
          <div>Total revenue: ₹{data.total_revenue}</div>
          <div style={{marginTop:10, fontWeight:700}}>Daily</div>
          <div className="grid">
            {data.daily_analytics.map(d => (
              <div key={d.date} className="card">
                <div style={{fontWeight:600}}>{new Date(d.date).toLocaleDateString()}</div>
                <div>Tickets: {d.tickets_sold}</div>
                <div>Revenue: ₹{d.revenue}</div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}
