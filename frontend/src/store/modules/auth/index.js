import actions from './actions';
import getters from './getters';
import mutations from './mutations';

const state = {
  authUser: {},
  isAuthenticated: false,
  jwt: localStorage.getItem('token'),
  endpoints: {
    // TODO: Remove hardcoding of dev endpoints
    obtainJWT: 'http://127.0.0.1:8000/auth/obtain_token/',
    refreshJWT: 'http://127.0.0.1:8000/auth/refresh_token/',
    baseUrl: 'http://127.0.0.1:8000/api/',
  },
};

export default {
  namespaced: true,
  state,
  actions,
  getters,
  mutations,
};
