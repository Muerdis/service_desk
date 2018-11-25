<template lang="pug">
  div
    base-component
    v-content
      v-container(grid-list-md)
        v-layout(row wrap)
          v-flex(xs3 text-xs-center)
            request-count-card(
              color="red darken-1"
              title="Входящие заявки"
              :count="`${requestsNew.length}`"
              link="/incoming-requests"
              icon="arrow_downward")
          v-flex(xs3 text-xs-center)
            request-count-card(
              color="light-blue lighten-1"
              title="Исходящие заявки"
              :count="`${requestsCreated.length}`"
              link="/outgoing-requests"
              icon="arrow_upward")
          v-flex(xs3 text-xs-center)
            request-count-card(
              color="orange lighten-1"
              title="В работе"
              :count="`${requestsInWork.length}`"
              link="/in-work-requests"
              icon="update")
          v-flex(xs3 text-xs-center)
            request-count-card(
              color="green lighten-1"
              title="Выполнено"
              :count="`${requestsClosed.length}`"
              link="/completed-requests"
              icon="done")
          v-flex(xs6)
            v-card(dark color="white")
              v-icon(style="font-size: 50px;" light) info
          v-flex(xs6)
            v-card(dark color="white")
              v-card-text.px-0 6
</template>

<script>
import { mapGetters } from 'vuex';

import BaseComponent from '../components/base/BaseComponent.vue';
import RequestCountCard from '../components/modules/request/RequestCountCard.vue';

export default {
  name: '',
  components: {
    BaseComponent,
    RequestCountCard,
  },
  computed: {
    ...mapGetters({
      requests: 'request/requests',
      user: 'user/user',
    }),
    requestsNew() {
      return this.requests.filter(
        request => request.status === 1 && request.assigned_user === this.user.id,
      );
    },
    requestsInWork() {
      return this.requests.filter(
        request => request.status === 2 && request.assigned_user === this.user.id,
      );
    },
    requestsClosed() {
      return this.requests.filter(
        request => request.status === 3 && request.assigned_user === this.user.id,
      );
    },
    requestsCreated() {
      return this.requests.filter(request => request.created_user === this.user.id);
    },
  },
};
</script>
