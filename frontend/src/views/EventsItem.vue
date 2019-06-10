<template lang="pug">
  div
    base-component
    v-content
      v-container(grid-list-md)
        v-layout(row wrap v-if="eventsItem[0]")
          v-flex(xs12)
            v-card
              v-card-title(primary-title style="padding-bottom: 0px;")
                h2 {{ eventsItem[0].title }}
                span(v-html="eventsItem[0].content")
                p.faded-text Дата проведения: с {{ eventsItem[0].from_date }} по {{ eventsItem[0].to_date }}
</template>

<script>
import { mapGetters } from 'vuex';

import BaseComponent from '../components/base/BaseComponent.vue';

export default {
  name: '',
  components: {
    BaseComponent,
  },
  computed: {
    ...mapGetters({
      events: 'events/events',
    }),
    eventsItem() {
      return this.events.filter(item => item.id.toString() === this.$route.params.id);
    },
  },
};
</script>
