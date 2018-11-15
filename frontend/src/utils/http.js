import axios from 'axios';

const http = axios.create();

const api = axios.create({
  baseURL: 'http://localhost:8000/api/',
});

export default {
  http,
  api,
};
