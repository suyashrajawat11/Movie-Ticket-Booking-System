import React, { useEffect, useState } from 'react'
import { listMovies } from '../api/movies'
import { listTheaters } from '../api/theaters'
import { createShow, listShows } from '../api/shows'

export default function Shows() {
  const [movies, setMovies] = useState([])
  const [theaters, setTheaters] = useState([])
  const [shows, setShows] = useState([])
  const [form, setForm] = useState({ movie_id: '', hall_id: '', start_time: '', end_time: '', price: 200 })

  const load = async () => {
    setMovies(await listMovies())
    setTheaters(await listTheaters())
    setShows(await listShows())
  }
  useEffect(()=>{ load() }, [])

  const halls = theaters.flatMap(t => t.halls || [])

  const onCreate = async (e) => {
    e.preventDefault()
    try {
      await createShow(form)
      setForm({ movie_id: '', hall_id: '', start_time: '', end_time: '', price: 200 })
      setShows(await listShows())
    } catch (e) { alert(e.message) }
  }

  return (
    <div>
      <h2>Shows</h2>
      <div className="card">
        <form onSubmit={onCreate} className="grid">
          <div>
            <div className="label">Movie</div>
            <select className="input" value={form.movie_id} onChange={e=>setForm({...form, movie_id:Number(e.target.value)})} required>
              <option value="">Select movie</option>
              {movies.map(m => <option key={m.id} value={m.id}>{m.title}</option>)}
            </select>
          </div>
          <div>
            <div className="label">Hall</div>
            <select className="input" value={form.hall_id} onChange={e=>setForm({...form, hall_id:Number(e.target.value)})} required>
              <option value="">Select hall</option>
              {halls.map(h => <option key={h.id} value={h.id}>{h.name} (theater {h.theater_id || ''})</option>)}
            </select>
          </div>
          <div>
            <div className="label">Start Time (YYYY-MM-DD HH:MM:SS)</div>
            <input className="input" placeholder="2025-09-27 18:00:00" value={form.start_time} onChange={e=>setForm({...form, start_time:e.target.value})} required />
          </div>
          <div>
            <div className="label">End Time (YYYY-MM-DD HH:MM:SS)</div>
            <input className="input" placeholder="2025-09-27 21:00:00" value={form.end_time} onChange={e=>setForm({...form, end_time:e.target.value})} required />
          </div>
          <div>
            <div className="label">Price</div>
            <input className="input" type="number" value={form.price} onChange={e=>setForm({...form, price:Number(e.target.value)})} required />
          </div>
          <div>
            <button className="btn" type="submit">Create Show</button>
          </div>
        </form>
      </div>

      <div className="grid">
        {shows.map(s => {
          const movie = movies.find(m => m.id === s.movie_id)
          const hall = halls.find(h => h.id === s.hall_id)
          return (
            <div className="card" key={s.id}>
              <div style={{fontWeight:700}}>{movie?.title || 'Unknown Movie'}</div>
              <div style={{fontSize:12, color:'#a9b1c6'}}>Show #{s.id} • {hall?.name || `Hall ${s.hall_id}`} • {new Date(s.start_time).toLocaleString()} - {new Date(s.end_time).toLocaleString()}</div>
              <div style={{marginTop:6}}>Price: ₹{s.price}</div>
            </div>
          )
        })}
      </div>
    </div>
  )
}
