<template lang="pug">
  div
    base-component
    v-content
      v-container(grid-list-md)
        v-layout(row wrap)
          v-flex(xs12)
            v-card
              v-card-title(primary-title style="padding-bottom: 0px;")
                span(v-for="item in news" v-html="item.content")
</template>

<script>
import { mapGetters } from 'vuex';

import BaseComponent from '../components/base/BaseComponent.vue';
import RequestCountCard from '../components/modules/request/RequestCountCard.vue';

export default {
  name: '',
  components: {
    BaseComponent,
    RequestCountCard,
  },
  computed: {
    ...mapGetters({
      news: 'news/news',
    }),
  },
};
</script>
