import Vue from 'vue';
import Vuex from 'vuex';

import base from './base';
import auth from './modules/auth';
import request from './modules/request';
import user from './modules/user';
import device from './modules/device';
import news from './modules/news';
import events from './modules/events';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    base,
    auth,
    request,
    user,
    device,
    news,
    events,
  },
});
