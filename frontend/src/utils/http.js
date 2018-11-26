import axios from 'axios';

const http = axios.create();

const api = axios.create({
  headers: {
    "X-CSRFToken": 'ZajyhyQJZdsC5zBfAyCenEfqzQypoB71UDyBQTMyf63uwSG20aK8wU1RAbRZy2mH',
  },
  baseURL: 'http://localhost:8000/api/',
});

export default {
  http,
  api,
};
