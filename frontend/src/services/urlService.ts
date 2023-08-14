import axios from 'axios'

const url = import.meta.env.VITE_SERVER_ROOT_URL;

const apiClient = axios.create({
  baseURL: url,
  withCredentials: false,
  headers: {
    "Access-Control-Allow-Origin": "*",
  }
})

export const generateShortUrl = (url: string) => {
    return apiClient.get('/generate', { params: { url } });
}
