<template lang="pug">
  div
    base-component
    v-content
      v-container(grid-list-md)
        v-layout(row wrap)
          request-item(v-for="request in requestsCreated" :request="request" mode="outgoing")
    v-dialog(v-model="dialog" persistent max-width="600px")
      v-btn(slot="activator" fab fixed bottom right dark color="primary")
        v-icon(dark) add
      v-card
        v-card-title
          span.headline.text-center(style="width: 100%;") Создание заявки
        v-card-text
          v-container(grid-list-md)
            v-layout(wrap)
              v-flex(xs12)
                v-text-field(v-model="title" label="Заголовок *" required)
              v-flex(xs12)
                v-textarea(
                  v-model="text"
                  label="Описание *" required
                  rows="2"
                  hint="Опишите проблему как можно более подробно"
                )
              v-flex(xs12 sm6)
                v-autocomplete(
                  @change="requestReason = null"
                  v-model="requestType"
                  :items="requestTypes"
                  item-text="name"
                  item-value="id"
                  label="Тип заявки *"
                  required
                )
              v-flex(xs12 sm6)
                v-autocomplete(
                  v-model="requestReason"
                  :items="allowedReasons"
                  item-value="id"
                  item-text="text"
                  label="Причина *"
                  required
                )
              v-flex(xs12)
                v-autocomplete(
                  v-model="assignedUser"
                  :items="users"
                  item-value="id"
                  item-text="full_name"
                  label="Ответственный *"
                  required
                )
              v-flex(xs12)
                v-autocomplete(
                  :multiple="true"
                  v-model="selectedDeviceTemplates"
                  :items="deviceTemplates"
                  item-value="id"
                  item-text="name"
                  label="Необходимое оборудование"
                )
                  template(slot="item" slot-scope="data")
                    v-tooltip(right)
                      span(slot="activator") {{ data.item.name }}
                      v-flex
                        p Характеристики
                        p(v-for="param in data.item.params") {{ param.name }}: {{ param.value }}
          v-spacer
          v-btn(color="blue darken-1" flat @click="clearForm") Закрыть
          v-btn(color="blue darken-1" flat @click="createRequest") Готово
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
      title: null,
      text: null,
      requestType: null,
      requestReason: null,
      assignedUser: null,
      selectedDeviceTemplates: [],
    };
  },
  mounted() {
    this.$store.dispatch('request/getRequestTypes');
    this.$store.dispatch('request/getRequestReasons');
    this.$store.dispatch('user/getUsers');
    this.$store.dispatch('device/getDeviceTemplates');
  },
  computed: {
    ...mapGetters({
      requests: 'request/requests',
      requestTypes: 'request/requestTypes',
      requestReasons: 'request/requestReasons',
      user: 'auth/authUser',
      users: 'user/users',
      deviceTemplates: 'device/deviceTemplates',
    }),
    requestsCreated() {
      return this.requests.filter(request => request.created_user === this.user.id);
    },
    allowedReasons() {
      return this.requestReasons.filter(
        requestReason => requestReason.request_type === this.requestType,
      );
    },
  },
  methods: {
    clearForm() {
      this.dialog = false;
      this.title = null;
      this.text = null;
      this.requestType = null;
      this.requestReason = null;
      this.assignedUser = null;
    },
    createRequest() {
      const info = {
        title: this.title,
        text: this.text,
        request_reason: this.requestReason,
        assigned_user: this.assignedUser,
        created_user: this.user.id,
        device_templates: this.selectedDeviceTemplates,
      };

      this.$store.dispatch('request/createRequest', info);
      this.clearForm();
    },
  },
};
</script>

<style scoped>

</style>
