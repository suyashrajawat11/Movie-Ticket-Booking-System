import React, { useMemo } from 'react'

export default function SeatMap({ seats, selected, onToggle, desiredCount = 0, onAutoPick }) {
  const grouped = useMemo(() => {
    const byRow = {}
    seats.forEach(s => {
      if (!byRow[s.row_id]) byRow[s.row_id] = []
      byRow[s.row_id].push(s)
    })
    Object.values(byRow).forEach(arr => arr.sort((a,b) => a.seat_number - b.seat_number))
    return byRow
  }, [seats])

  const tryAutoPick = () => {
    if (!desiredCount || desiredCount <= 0) return
    for (const rowId of Object.keys(grouped)) {
      const rowSeats = grouped[rowId]
      let streak = []
      for (const seat of rowSeats) {
        if (seat.is_available && !selected.includes(seat.seat_id)) {
          streak.push(seat)
          if (streak.length === desiredCount) {
            onAutoPick(streak.map(s => s.seat_id))
            return
          }
        } else {
          streak = []
        }
      }
    }
    alert('Could not find consecutive seats in this show. Try suggestions.')
  }

  return (
    <div>
      <div className="legend" style={{marginBottom: 10}}>
        <span><span className="dot" style={{background:'#1a224b', border:'1px solid #5060aa'}}></span>Available</span>
        <span><span className="dot" style={{background:'#5a6bff'}}></span>Selected</span>
        <span><span className="dot" style={{background:'#7a1a1a'}}></span>Booked</span>
        <span><span className="dot" style={{background:'#1a224b', border:'1px solid #e0a200'}}></span>Aisle</span>
      </div>
      <div className="seatmap">
        {Object.keys(grouped).sort((a,b)=>Number(a)-Number(b)).map(rowId => (
          <div key={rowId} className="seat-row">
            {grouped[rowId].map(seat => {
              const cls = [
                'seat',
                seat.is_aisle ? 'aisle' : '',
                selected.includes(seat.seat_id) ? 'selected' : '',
                seat.is_available ? '' : 'booked'
              ].join(' ')
              return (
                <div
                  key={seat.seat_id}
                  className={cls}
                  title={`Row ${rowId}, Seat ${seat.seat_number}`}
                  onClick={() => seat.is_available && onToggle(seat.seat_id)}
                >{seat.seat_number}</div>
              )
            })}
          </div>
        ))}
      </div>
      {desiredCount > 0 && (
        <div style={{marginTop: 10}}>
          <button className="btn secondary" onClick={tryAutoPick}>Auto-pick {desiredCount} seats together</button>
        </div>
      )}
    </div>
  )
}
