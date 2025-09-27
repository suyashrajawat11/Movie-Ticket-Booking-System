import React, { useEffect, useState } from 'react'
import { listMovies, createMovie, deleteMovie } from '../api/movies'

export default function Movies() {
  const [items, setItems] = useState([])
  const [form, setForm] = useState({ title: '', duration: 120, genre: '', language: '' })
  const [loading, setLoading] = useState(false)

  const load = async () => {
    setLoading(true)
    try {
      const data = await listMovies()
      setItems(data)
    } catch (e) { alert(e.message) }
    setLoading(false)
  }
  useEffect(() => { load() }, [])

  const onCreate = async (e) => {
    e.preventDefault()
    try {
      await createMovie(form)
      setForm({ title: '', duration: 120, genre: '', language: '' })
      load()
    } catch (e) { alert(e.message) }
  }

  return (
    <div>
      <h2>Movies</h2>
      <div className="card">
        <form onSubmit={onCreate} className="grid">
          <div>
            <div className="label">Title</div>
            <input className="input" value={form.title} onChange={e=>setForm({...form, title:e.target.value})} required />
          </div>
          <div>
            <div className="label">Duration (mins)</div>
            <input className="input" type="number" value={form.duration} onChange={e=>setForm({...form, duration:Number(e.target.value)})} required />
          </div>
          <div>
            <div className="label">Genre</div>
            <input className="input" value={form.genre} onChange={e=>setForm({...form, genre:e.target.value})} />
          </div>
          <div>
            <div className="label">Language</div>
            <input className="input" value={form.language} onChange={e=>setForm({...form, language:e.target.value})} />
          </div>
          <div className="row">
            <button className="btn" type="submit">Create</button>
          </div>
        </form>
      </div>

      <div className="grid">
        {loading ? <div>Loading...</div> : items.map(m => (
          <div className="card" key={m.id}>
            <div style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}>
              <div>
                <div style={{fontWeight:'700'}}>{m.title}</div>
                <div style={{fontSize:12, color:'#a9b1c6'}}>{m.genre} • {m.language} • {m.duration} mins</div>
              </div>
              <button className="btn secondary" onClick={async ()=>{ await deleteMovie(m.id); load() }}>Delete</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
