import { api } from './client'

export const movieAnalytics = async (movie_id, params) => (await api.get(`/analytics/movie/${movie_id}`, { params })).data.data

export const analyticsOverview = async () => (await api.get('/analytics/overview')).data.data
