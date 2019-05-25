<template lang="pug">
  v-flex(xs12)
    v-card
      v-card-title(primary-title style="padding-bottom: 0px;")
        span.title(style="margin-bottom: 10px;") Заявка №{{ request.id }}: {{ request.title }}
        p Тип: {{ request.reason_type_name }}
        p Причина: {{ request.reason_name }}
        p Назначена на: {{ request.assigned_user_name }}
        span Необходимое оборудование:&nbsp;
        span(v-for="name in request.device_templates_names") {{ name }},&nbsp;
        hr
        p {{ request.text }}
        p.faded-text {{ request.created_user_name }}
        p.faded-text {{ request.date_created }}
      v-card-actions(v-if="mode === 'incoming'")
        v-btn(@click="changeStatus(2)" color="success")
          v-flex
            span Взять в работу
        v-btn(@click="changeStatus(3)" color="error")
          v-flex
            span Отклонить
      v-card-actions(v-if="mode === 'outgoing'")
        v-btn(@click="deleteRequest" color="error")
          v-flex
            span Удалить
      v-card-actions(v-if="mode === 'in-work'")
        v-btn.request-action(@click="changeStatus(3)" color="success")
          v-flex
            span Завершить
        v-dialog(v-model="deviceDialog" persistent max-width="600px")
          v-btn.request-action(slot="activator" color="info")
            v-flex
              span Оборудование
          v-card
            v-card-title
              span.headline.text-center(style="width: 100%;") Оборудование
            v-card-text
              v-container(grid-list-md)
                v-layout(wrap)
                  v-flex(xs12)
                    v-autocomplete(
                      :multiple="true"
                      v-model="selectedDevices"
                      :items="[]"
                      item-value="id"
                      item-text="name"
                      label="Прикрепленное оборудование"
                    )
              v-spacer
                v-btn(color="blue darken-1" flat @click="clearDeviceForm") Закрыть
        v-dialog(v-model="dateDialog" persistent max-width="600px")
          v-btn(slot="activator" color="info")
            v-flex
              span Сроки
          v-card
            v-card-title
              span.headline.text-center(style="width: 100%;") Сроки
            v-card-text
              v-container(grid-list-md)
                v-layout(wrap)
                  v-flex(xs12)
                    span afsdfsdfsdf
              v-spacer
                v-btn(color="blue darken-1" flat @click="clearDateForm") Закрыть
</template>

<script>
export default {
  name: 'RequestItem',
  props: {
    request: {
      type: Object,
    },
    mode: {
      type: String,
    },
  },
  data() {
    return {
      deviceDialog: false,
      dateDialog: false,
      selectedDevices: [],
    };
  },
  methods: {
    clearDeviceForm() {
      this.deviceDialog = false;
    },
    clearDateForm() {
      this.dateDialog = false;
    },
    changeStatus(status) {
      const info = {
        id: this.request.id,
        status,
      };
      this.$store.dispatch('request/changeStatus', info);
    },
    deleteRequest() {
      this.$store.dispatch('request/deleteRequest', this.request.id);
    },
  },
};
</script>

<style scoped>
  .request-action {
    margin-right: 10px;
  }
</style>
