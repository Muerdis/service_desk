<template lang="pug">
  v-toolbar.no-transition(color="grey darken-3" dark app)
    v-toolbar-side-icon(@click.stop="changeDrawerState")
    v-toolbar-title Service desk
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'Toolbar',
  computed: {
    ...mapGetters({
      drawer: 'base/drawer',
    }),
  },
  methods: {
    changeDrawerState() {
      this.$store.commit('base/DRAWER', !this.drawer);
    },
  },
};
</script>

<style scoped>
.no-transition {
  transition: none;
}
</style>
