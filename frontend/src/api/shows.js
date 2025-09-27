import { api } from './client'

export const listShows = async () => (await api.get('/shows')).data
export const getShow = async (id) => (await api.get(`/shows/${id}`)).data
export const createShow = async (payload) => (await api.post('/shows', payload)).data
