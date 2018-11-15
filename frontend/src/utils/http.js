import axios from 'axios';

const http = axios.create();

const api = axios.create({
  baseURL: '/api/',
});

export default {
  http,
  api,
};
