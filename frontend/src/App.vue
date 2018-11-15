<template lang="pug">
  v-app#inspire
    router-view
</template>

<script>

export default {
  name: 'App',
  mounted() {
    this.$store.dispatch('user/getUserInfo');
  },
};
</script>
