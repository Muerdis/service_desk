import axios from 'axios';
import Cookies from 'js-cookie';

const http = axios.create();
const internal = axios.create({
  baseURL: 'http://localhost:8000/',
});
const api = axios.create({
  headers: {
    Authorization: `JWT ${Cookies.get('csrftoken')}`,
    'Content-Type': 'application/json',
  },
  xhrFields: {
    withCredentials: true,
  },
  baseURL: 'http://localhost:8000/api/',
});

export default {
  http,
  internal,
  api,
};
