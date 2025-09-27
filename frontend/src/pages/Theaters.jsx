import React, { useEffect, useState } from 'react'
import { listTheaters, createTheater } from '../api/theaters'

export default function Theaters() {
  const [items, setItems] = useState([])
  const [theater, setTheater] = useState({ name: '', address: '', city: '', country: '', halls: [] })
  const [hallDraft, setHallDraft] = useState({ name: '', total_seats: 0, rows: [] })
  const [rowDraft, setRowDraft] = useState({ row_number: 1, seat_count: 6 })

  const load = async () => {
    const data = await listTheaters()
    setItems(data)
  }
  useEffect(()=>{ load() }, [])

  const addRow = () => {
    if (rowDraft.seat_count < 6) return alert('Row must have at least 6 seats')
    setHallDraft({ ...hallDraft, rows: [...hallDraft.rows, rowDraft] })
    setRowDraft({ row_number: rowDraft.row_number + 1, seat_count: 6 })
  }

  const addHall = () => {
    setTheater({ ...theater, halls: [...theater.halls, hallDraft] })
    setHallDraft({ name: '', total_seats: 0, rows: [] })
  }

  const onCreate = async () => {
    try {
      const totalSeats = theater.halls.reduce((acc, h) => acc + (h.rows?.reduce((a,r)=>a+r.seat_count,0) || 0), 0)
      const payload = {
        ...theater,
        halls: theater.halls.map(h => ({ ...h, total_seats: h.rows?.reduce((a,r)=>a+r.seat_count,0) || 0 }))
      }
      const newTheater = await createTheater(payload)
      console.log('Theater created:', newTheater)
      setTheater({ name: '', address: '', city: '', country: '', halls: [] })
      await load()
      alert('Theater created successfully!')
    } catch (e) { 
      console.error('Error creating theater:', e)
      alert('Error creating theater: ' + e.message) 
    }
  }

  return (
    <div>
      <h2>Theaters</h2>
      <div className="card">
        <div className="grid">
          <input className="input" placeholder="Name" value={theater.name} onChange={e=>setTheater({...theater, name:e.target.value})} />
          <input className="input" placeholder="Address" value={theater.address} onChange={e=>setTheater({...theater, address:e.target.value})} />
          <input className="input" placeholder="City" value={theater.city} onChange={e=>setTheater({...theater, city:e.target.value})} />
          <input className="input" placeholder="Country" value={theater.country} onChange={e=>setTheater({...theater, country:e.target.value})} />
        </div>
        <div className="card" style={{marginTop:12}}>
          <div style={{fontWeight:600, marginBottom:8}}>Add Hall</div>
          <div className="grid">
            <input className="input" placeholder="Hall name" value={hallDraft.name} onChange={e=>setHallDraft({...hallDraft, name:e.target.value})} />
          </div>
          <div className="row" style={{marginTop:10}}>
            <div>
              <div className="label">Row number</div>
              <input className="input" type="number" value={rowDraft.row_number} onChange={e=>setRowDraft({...rowDraft, row_number:Number(e.target.value)})} />
            </div>
            <div>
              <div className="label">Seat count</div>
              <input className="input" type="number" value={rowDraft.seat_count} onChange={e=>setRowDraft({...rowDraft, seat_count:Number(e.target.value)})} />
            </div>
            <button className="btn secondary" onClick={addRow}>Add Row</button>
          </div>
          <div style={{marginTop:8}}>
            {hallDraft.rows.map((r, idx) => (
              <div key={idx} style={{fontSize:13, color:'#a9b1c6'}}>Row {r.row_number}: {r.seat_count} seats</div>
            ))}
          </div>
          <div style={{marginTop:10}}>
            <button className="btn" onClick={addHall}>Add Hall to Theater</button>
          </div>
        </div>
        <div style={{marginTop:12}}>
          <button className="btn" onClick={onCreate}>Create Theater</button>
        </div>
      </div>

      <div className="grid">
        {items.map(t => (
          <div className="card" key={t.id}>
            <div style={{fontWeight:700}}>{t.name}</div>
            <div style={{fontSize:12, color:'#a9b1c6'}}>{t.address}, {t.city}, {t.country}</div>
            <div style={{marginTop:8}}>
              {t.halls?.map(h => (
                <div key={h.id} style={{marginBottom:6}}>
                  <div style={{fontWeight:600}}>{h.name}</div>
                  {h.rows?.map(r => (
                    <div key={r.id} style={{fontSize:12, color:'#a9b1c6'}}>Row {r.row_number}: {r.seat_count} seats</div>
                  ))}
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
