import Cookies from 'js-cookie';

const AUTH_USER = (state, authUser) => {
  const st = state;
  st.authUser = authUser;
};

const IS_AUTHENTICATED = (state, isAuthenticated) => {
  const st = state;
  st.isAuthenticated = isAuthenticated;
};

const UPDATE_TOKEN = (state, newToken) => {
  Cookies.set('csrftoken', newToken);
};

const REMOVE_TOKEN = () => {
  Cookies.remove('csrftoken');
};

export default {
  AUTH_USER,
  IS_AUTHENTICATED,
  UPDATE_TOKEN,
  REMOVE_TOKEN,
};
