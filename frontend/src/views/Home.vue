<template lang="pug">
  div
    base-component
    v-content
      v-container(grid-list-md)
        v-layout(row wrap)
          v-flex(xs3 text-xs-center)
            request-count-card(
              color="red darken-1"
              title="Входящие заявки"
              count="5"
              icon="arrow_downward")
          v-flex(xs3 text-xs-center)
            request-count-card(
              color="orange lighten-1"
              title="В работе"
              count="3"
              icon="update")
          v-flex(xs3 text-xs-center)
            request-count-card(
              color="light-blue lighten-1"
              title="Исходящие заявки"
              count="4"
              icon="arrow_upward")
          v-flex(xs3 text-xs-center)
            request-count-card(
              color="green lighten-1"
              title="Выполнено"
              count="2"
              icon="done")
          v-flex(xs6)
            v-card(dark color="white")
              v-icon(style="font-size: 50px;" light) info
          v-flex(xs6)
            v-card(dark color="white")
              v-card-text.px-0 6
</template>

<script>
import BaseComponent from '../components/base/BaseComponent.vue';
import RequestCountCard from '../components/modules/request/RequestCountCard.vue';

export default {
  name: '',
  components: {
    BaseComponent,
    RequestCountCard,
  },
};
</script>
