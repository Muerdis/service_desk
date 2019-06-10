<template lang="pug">
  div
    base-component
    v-content
      v-container(grid-list-md)
        v-layout(row wrap)
          v-flex(xs12)
            v-card.news-card(v-for="item in news")
              v-card-title(primary-title)
                h2 {{ item.title }}
                span(v-html="item.preview_text")
                router-link(:to="getRoute(item.id)") Подробнее
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
      news: 'news/news',
    }),
  },
  methods: {
    getRoute(id) {
      return `/news/${id}`;
    }
  },
};
</script>

<style scoped>
 .news-card {
   margin-bottom: 20px;
 }
</style>
