import Vue from 'vue';
import Vuex from 'vuex';

import base from './base';
import request from './modules/request';
import user from './modules/user';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    base,
    request,
    user,
  },
});
