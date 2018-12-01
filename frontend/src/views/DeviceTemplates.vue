<template lang="pug">
  div
    base-component
    v-content
      v-container(grid-list-md)
        v-layout(row wrap)
</template>

<script>
import BaseComponent from '../components/base/BaseComponent.vue';
import RequestItem from '../components/modules/request/RequestItem.vue';

export default {
  name: 'DeviceTemplates',
  components: {
    BaseComponent,
    RequestItem,
  },
};
</script>

<style scoped>

</style>
