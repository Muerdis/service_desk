import axios from 'axios';

const http = axios.create();

const api = axios.create({
  headers: {
    Authorization: `JWT ${localStorage.getItem('token')}`,
    'Content-Type': 'application/json',
  },
  xhrFields: {
    withCredentials: true,
  },
  baseURL: 'http://localhost:8000/api/',
});

export default {
  http,
  api,
};
