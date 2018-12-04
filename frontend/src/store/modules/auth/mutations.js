const AUTH_USER = (state, authUser) => {
  const st = state;
  st.authUser = authUser;
};

const IS_AUTHENTICATED = (state, isAuthenticated) => {
  const st = state;
  st.isAuthenticated = isAuthenticated;
};

const UPDATE_TOKEN = (state, newToken) => {
  const st = state;
  localStorage.setItem('token', newToken);
  st.jwt = newToken;
};

const REMOVE_TOKEN = (state) => {
  const st = state;
  localStorage.removeItem('token');
  st.jwt = null;
};

export default {
  AUTH_USER,
  IS_AUTHENTICATED,
  UPDATE_TOKEN,
  REMOVE_TOKEN,
};
