<template lang="pug">
  div
    base-component
    v-content
      v-container(grid-list-md)
        v-layout(row wrap v-if="newsItem[0]")
          v-flex(xs12)
            v-card
              v-card-title(primary-title style="padding-bottom: 0px;")
                h2 {{ newsItem[0].title }}
                span(v-html="newsItem[0].content")
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
    newsItem() {
      return this.news.filter(item => item.id.toString() === this.$route.params.id);
    },
  },
};
</script>
