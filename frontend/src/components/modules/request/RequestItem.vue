<template lang="pug">
  v-flex(xs12)
    v-card
      v-card-title(primary-title style="padding-bottom: 0px;")
        span.title(style="margin-bottom: 10px;") {{ request.title }}
        p Тип: {{ request.reason_type_name }}
        p Причина: {{ request.reason_name }}
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
        v-btn(@click="changeStatus(3)" color="success")
          v-flex
            span Завершить
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
  methods: {
    changeStatus(status) {
      const info = {
        id: this.request.id,
        status,
      };

      this.$store.dispatch('request/changeStatus', info);
    },
    deleteRequest() {
      this.$store.dispatch('request/deleteRequest', this.request.id);
    }
  }
};
</script>

<style scoped>

</style>
