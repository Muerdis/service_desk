<template lang="pug">
  div
    base-component
    v-content
      v-container(grid-list-md)
        v-layout(row wrap)
          requests-column(
            color="red darken-1"
            title="Входящие заявки"
            :requests="requestsNew")
          requests-column(
            color="orange lighten-1"
            title="В работе"
            :requests="requestsInWork")
          requests-column(
            color="light-blue lighten-1"
            title="Исходящие заявки"
            :requests="requestsCreated")
          requests-column(
            color="green lighten-1"
            title="Выполнено"
            :requests="requestsClosed")
</template>

<script>
import { mapGetters } from 'vuex';

import BaseComponent from '../components/base/BaseComponent.vue';
import RequestsColumn from '../components/modules/request/RequestsColumn.vue';

export default {
  name: 'Requests',
  components: {
    BaseComponent,
    RequestsColumn,
  },
  computed: {
    ...mapGetters({
      requests: 'request/requests',
      user: 'user/user',
    }),
    requestsNew() {
      return this.requests.filter(request => request.status === 1);
    },
    requestsInWork() {
      return this.requests.filter(request => request.status === 2);
    },
    requestsClosed() {
      return this.requests.filter(request => request.status === 3);
    },
    requestsCreated() {
      return this.requests.filter(request => request.created_user === this.user.id);
    },
  },
  mounted() {
    this.$store.dispatch('request/getRequests');
  },
};
</script>

<style scoped>

</style>
