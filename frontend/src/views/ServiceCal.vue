<template lang="pug">
  div
    base-component
    v-content
      v-container(grid-list-md)
        calendar(:events="maintenances")
</template>

<script>
import { mapGetters } from 'vuex';

import BaseComponent from '../components/base/BaseComponent.vue';
import Calendar from '../components/modules/request/Calendar.vue';

export default {
  name: 'EventsCal',
  components: {
    BaseComponent,
    Calendar,
  },
  computed: {
    ...mapGetters({
      maintenances: 'request/maintenances',
    }),
  },
};
</script>

<style scoped>

</style>
