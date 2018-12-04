<template lang="pug">
  div
    base-component
    v-content
      v-container(grid-list-md)
        v-layout(row wrap)
          request-item(v-for="request in requestsClosed" :request="request" mode="completed")
</template>

<script>
import { mapGetters } from 'vuex';

import BaseComponent from '../components/base/BaseComponent.vue';
import RequestItem from '../components/modules/request/RequestItem.vue';

export default {
  name: 'CompletedRequests',
  components: {
    BaseComponent,
    RequestItem,
  },
  computed: {
    ...mapGetters({
      requests: 'request/requests',
      user: 'auth/authUser',
    }),
    requestsClosed() {
      return this.requests.filter(
        request => request.status === 3 && request.assigned_user === this.user.id,
      );
    },
  },
};
</script>

<style scoped>

</style>
