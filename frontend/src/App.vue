<template lang="pug">
  v-app#inspire.main-background
    router-view
</template>

<script>
export default {
  name: 'App',
  mounted() {
    this.$store.dispatch('request/getRequests');
  },
};
</script>

<style>
  @import './app.css';
</style>
