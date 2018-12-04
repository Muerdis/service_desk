const authUser = state => state.authUser;
const isAuthenticated = state => state.isAuthenticated;
const jwt = state => state.jwt;
const endpoints = state => state.endpoints;

export default {
  authUser,
  isAuthenticated,
  jwt,
  endpoints,
};
