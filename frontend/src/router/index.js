import Vue from 'vue';
import Router from 'vue-router';
import Home from '../views/Home.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/agile',
      name: 'agile',
      component: () => import('../views/Agile.vue'),
    },
    {
      path: '/incoming-requests',
      name: 'incoming-requests',
      component: () => import('../views/IncomingRequests.vue'),
    },
    {
      path: '/outgoing-requests',
      name: 'outgoing-requests',
      component: () => import('../views/OutgoingRequests.vue'),
    },
    {
      path: '/in-work-requests',
      name: 'in-work-requests',
      component: () => import('../views/InWorkRequests.vue'),
    },
    {
      path: '/completed-requests',
      name: 'completed-requests',
      component: () => import('../views/CompletedRequests.vue'),
    },
    {
      path: '/device-templates',
      name: 'device-templates',
      component: () => import('../views/DeviceTemplates.vue'),
    },
    {
      path: '/devices',
      name: 'devices',
      component: () => import('../views/Devices.vue'),
    },
    {
      path: '/events-calendar',
      name: 'eventsCal',
      component: () => import('../views/EventsCal.vue'),
    },
    {
      path: '/usings-calendar',
      name: 'usingsCal',
      component: () => import('../views/UsingsCal.vue'),
    },
    {
      path: '/service-calendar',
      name: 'serviceCal',
      component: () => import('../views/ServiceCal.vue'),
    },
  ],
});
