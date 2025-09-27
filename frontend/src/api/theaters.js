import { api } from './client'

export const listTheaters = async () => (await api.get('/theaters')).data
export const createTheater = async (payload) => (await api.post('/theaters', payload)).data
export const updateTheater = async (id, payload) => (await api.put(`/theaters/${id}`, payload)).data
export const deleteTheater = async (id) => (await api.delete(`/theaters/${id}`)).data
