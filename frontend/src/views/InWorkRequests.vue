<template lang="pug">
  div
    base-component
    v-content
      v-container(grid-list-md)
        v-layout(row wrap)
          request-item(v-for="request in requestsInWork" :request="request" mode="in-work")
</template>

<script>
import { mapGetters } from 'vuex';

import BaseComponent from '../components/base/BaseComponent.vue';
import RequestItem from '../components/modules/request/RequestItem.vue';

export default {
  name: 'InWorkRequests',
  components: {
    BaseComponent,
    RequestItem,
  },
  computed: {
    ...mapGetters({
      requests: 'request/requests',
      user: 'auth/authUser',
    }),
    requestsInWork() {
      return this.requests.filter(
        request => request.status === 2 && request.assigned_user === this.user.id,
      );
    },
  },
};
</script>

<style scoped>

</style>
