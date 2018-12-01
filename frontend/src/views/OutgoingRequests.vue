<template lang="pug">
  div
    base-component
    v-content
      v-container(grid-list-md)
        v-layout(row wrap)
          request-item(v-for="request in requestsCreated" :request="request" mode="outgoing")
    v-dialog(v-model="dialog" persistent max-width="600px")
      v-btn(slot="activator" fab fixed bottom right dark color="green")
        v-icon(dark) add
      v-card
        v-card-title
          span.headline Создание заявки
        v-card-text
          v-container(grid-list-md)
            v-layout(wrap)
              v-flex(xs12)
                v-text-field(label="Заголовок *" required)
              v-flex(xs12)
                v-textarea(
                  label="Описание *" required
                  hint="Опишите проблему как можно более подробно"
                )
              v-flex(xs12 sm6)
                v-select(
                  :items="['Техническое обеспечение проведеня мероприятия']"
                  label="Причина*"
                  required
                )
        v-card-actions
          v-spacer
          v-btn(color="blue darken-1" flat @click.native="dialog = false") Закрыть
          v-btn(color="blue darken-1" flat @click.native="dialog = false") Готово
</template>

<script>
import { mapGetters } from 'vuex';

import BaseComponent from '../components/base/BaseComponent.vue';
import RequestItem from '../components/modules/request/RequestItem.vue';

export default {
  name: 'OutgoingRequests',
  components: {
    BaseComponent,
    RequestItem,
  },
  data() {
    return {
      dialog: false,
    };
  },
  computed: {
    ...mapGetters({
      requests: 'request/requests',
      user: 'user/user',
    }),
    requestsCreated() {
      return this.requests.filter(request => request.created_user === this.user.id);
    },
  },
};
</script>

<style scoped>

</style>
