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
        v-dialog(v-model="deviceDialog" persistent max-width="700px")
          v-btn.request-action(slot="activator" color="info")
            v-flex
              span Бронирование
          v-card
            v-card-title
              span.headline.text-center(style="width: 100%;") Бронирование
            v-card-text
              v-container(grid-list-md)
                v-layout(wrap)
                  v-flex(xs12)
                    v-autocomplete(
                      :multiple="true"
                      v-model="selectedDevices"
                      :items="devices"
                      item-value="id"
                      item-text="name"
                      label="Единицы оборудования"
                    )
                  v-flex(xs12 sm6)
                    v-date-picker(
                      :allowed-dates="allowedFromDates"
                      v-model="dateFrom"
                      locale="ru-ru"
                      first-day-of-week="1"
                    )
                  v-flex.hidden-xs-only(xs12 sm6)
                    v-date-picker(
                      :allowed-dates="allowedToDates"
                      v-model="dateTo"
                      locale="ru-ru"
                      first-day-of-week="1"
                    )
              v-spacer
                v-btn(color="blue darken-1" flat @click="createReservations" :disabled="disableReservation") Готово
                v-btn(color="blue darken-1" flat @click="clearDeviceForm" right) Закрыть
</template>

<script>
import { mapGetters } from 'vuex';

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
      selectedDevices: [],
      dateFrom: new Date().toISOString().substr(0, 10),
      dateTo: new Date().toISOString().substr(0, 10)
    };
  },
  mounted() {
    this.$store.dispatch('device/getDevices');
  },
  computed: {
    ...mapGetters({
      devices: 'device/devices',
    }),
    disableReservation() {
      return !(this.selectedDevices.length !== 0 && this.dateFrom && this.dateTo);
    },
  },
  methods: {
    clearDeviceForm() {
      this.selectedDevices = [];
      this.deviceDialog = false;
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
    createReservations() {
      const state = this;
      this.selectedDevices.forEach(function(device) {
        const info = {
          request: state.request.id,
          from_date: state.dateFrom,
          to_date: state.dateTo,
          device: device,
        };

        state.$store.dispatch('request/createReservation', info);
      });

      state.changeStatus(3);
      this.selectedDevices = [];
      this.deviceDialog = false;
    },
    allowedFromDates: function (val) {
      let isReserved = false;
      const state = this;
      this.selectedDevices.forEach((el) => {
        const device = this.devices.filter(item => item.id === el);
        if (device) {
          device[0].res_dates.forEach((date) => {
            if (val >= date[0] && val <= date[1]) {
              isReserved = true;
              state.dateFrom = null;
            }
          });
        }
      });
      return !isReserved && val <= this.dateTo;
    },
    allowedToDates(val) {
      let isReserved = false;
      const state = this;
      this.selectedDevices.forEach((el) => {
        const device = this.devices.filter(item => item.id === el);
        if (device) {
          device[0].res_dates.forEach((date) => {
            if (val >= date[0] && val <= date[1]) {
              isReserved = true;
              state.dateTo = null;
            }
          });
        }
      });
      return !isReserved && val >= this.dateFrom;
    },
  },
};
</script>

<style scoped>
  .request-action {
    margin-right: 10px;
  }
</style>
