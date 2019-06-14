import actions from './actions';
import getters from './getters';
import mutations from './mutations';

const state = {
  requests: [],
  requestTypes: [],
  requestReasons: [],
  reservations: [],
  maintenances: [],
};

export default {
  namespaced: true,
  state,
  actions,
  getters,
  mutations,
};
