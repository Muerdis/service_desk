<template lang="pug">
  div
    base-component
    v-content
      v-container(grid-list-md)
        v-layout(row wrap)
          v-flex(xs12)
            v-card
              v-card-title(primary-title style="padding-bottom: 0px;")
                span(v-for="item in events" v-html="item.content")
</template>

<script>
import { mapGetters } from 'vuex';

import BaseComponent from '../components/base/BaseComponent.vue';

export default {
  name: 'Events',
  components: {
    BaseComponent,
  },
  computed: {
    ...mapGetters({
      events: 'events/events',
    }),
  },
};
</script>
