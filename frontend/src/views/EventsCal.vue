<template lang="pug">
	div
		base-component
		v-content
			v-container(grid-list-md)
				calendar(:events="eventsDates")
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
      eventsDates: 'events/eventsDates',
    }),
  },
};
</script>

<style scoped>

</style>
