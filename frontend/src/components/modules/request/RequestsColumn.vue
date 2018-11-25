<template lang="pug">
  v-flex(xs3)
    v-layout(row wrap)
      v-flex(xs12)
        v-card(dark :color="color")
          v-card-title(primary-title)
            .headline(style="text-align: center; width: 100%;") {{ title }}
      v-flex(xs12 v-for="request in requests" :key="request.id")
        v-card
          v-card-title(primary-title)
            span.title(
              style="text-align: center; width: 100%; margin-bottom: 10px;"
            ) {{ request.title }}
            p Тип: {{ request.reason_type_name }}
            p Причина: {{ request.reason_name }}
            p {{ request.text.slice(0, 80) }}...
            p.faded-text {{ request.created_user_name }}
            p.faded-text {{ request.date_created }}
</template>

<script>
export default {
  name: 'RequestsColumn',
  props: {
    color: {
      type: String,
    },
    title: {
      type: String,
    },
    requests: {
      type: Array,
    },
  },
};
</script>

<style scoped>

</style>
