<template lang="pug">
  v-card(dark :color="color")
    v-layout
      v-flex(xs9)
        h2 {{ title }}
        span.display-3 {{ count }}
      v-flex(xs3)
        v-icon(style="font-size: 50px;") {{ icon }}
    v-divider
    v-card-actions.pa-3
      span.title(style="text-align: center; width: 100%;") Просмотр
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
    icon: {
      type: String,
    },
  },
};
</script>

<style scoped>

</style>
