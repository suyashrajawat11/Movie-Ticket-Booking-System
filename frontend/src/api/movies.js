import { api } from './client'

export const listMovies = async () => (await api.get('/movies')).data.data
export const createMovie = async (payload) => (await api.post('/movies', payload)).data.data
export const updateMovie = async (id, payload) => (await api.put(`/movies/${id}`, payload)).data.data
export const deleteMovie = async (id) => (await api.delete(`/movies/${id}`)).data
