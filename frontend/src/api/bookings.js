import { api } from './client'

export const createBooking = async (payload) => (await api.post('/bookings', payload)).data.data
export const createGroupBooking = async (payload) => (await api.post('/bookings/group', payload)).data.data
export const checkAvailability = async (show_id) => (await api.get(`/bookings/availability`, { params: { show_id } })).data.data
export const suggestAlternates = async (params) => (await api.get('/bookings/suggest', { params })).data.data
