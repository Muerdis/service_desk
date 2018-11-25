<template lang="pug">
  v-card(dark :color="color")
    v-layout
      v-flex(xs12)
        v-flex(xs12)
          v-layout
            v-flex(xs9 style="margin: auto;")
              h2 {{ title }}
            v-flex(xs3)
              v-icon(style="font-size: 50px;") {{ icon }}
        span.display-2 {{ count }}
    v-divider
    v-card-actions.pa-3
      v-btn(flat dark style="width: 100%" :to="link")
        v-flex(xs11)
          span Подробнее
        v-flex(xs1)
          v-icon(style="font-size: 30px;") chevron_right
</template>

<script>
export default {
  name: 'RequestCountCard',
  props: {
    color: {
      type: String,
    },
    title: {
      type: String,
    },
    count: {
      type: String,
    },
    link: {
      type: String,
    },
    icon: {
      type: String,
    },
  },
};
</script>

<style scoped>

</style>
