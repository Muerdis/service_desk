<template lang="pug">
  div
    navigation
    toolbar
</template>

<script>
import Toolbar from './Toolbar.vue';
import Navigation from './Navigation.vue';

export default {
  name: 'BaseComponent',
  components: {
    Toolbar,
    Navigation,
  },
};
</script>

<style scoped>

</style>
