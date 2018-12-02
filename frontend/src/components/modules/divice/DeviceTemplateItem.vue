<template lang="pug">
  v-flex(xs12)
    v-card
      v-card-title(primary-title style="padding-bottom: 0px;")
        span.title(style="margin-bottom: 10px;") {{ deviceTemplate.name }}
        hr
        p.headline Характеристики:
        p.subheading(v-for="param in deviceTemplate.params") {{ param.name }}: {{ param.value }}
      v-card-actions
        v-btn(@click="" color="success")
          v-flex
            span Редактировать
        v-btn(color="error")
          v-flex
            span Удалить
</template>

<script>
export default {
  name: 'DeviceTemplateItem',
  props: {
    deviceTemplate: {
      type: Object,
    },
  },
  methods: {},
};
</script>

<style scoped>

</style>
