<template lang="pug">
  div
    base-component
    v-content
      v-container(grid-list-md)
        v-layout(row wrap)
          v-flex(xs12)
            v-card.news-card(v-for="item in events")
              v-card-title(primary-title)
                h2 {{ item.title }}
                span(v-html="item.preview_text")
                p.faded-text Дата проведения: с {{ item.from_date }} по {{ item.to_date }}
                router-link(:to="getRoute(item.id)") Подробнее
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
  methods: {
    getRoute(id) {
      return `/events/${id}`;
    }
  },
};
</script>

<style scoped>
 .news-card {
   margin-bottom: 20px;
 }
</style>
