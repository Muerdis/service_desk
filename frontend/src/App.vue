<template lang="pug">
  v-app#inspire.main-background
    router-view
</template>

<script>
import Cookies from 'js-cookie';
import requests from './utils/http';

export default {
  name: 'App',
  mounted() {
    const csrftoken = Cookies.get('csrftoken');

    if (csrftoken) {
      requests.api.get('auth-user/')
        .then((userResponse) => {
          this.$store.commit('auth/AUTH_USER', userResponse.data);
          this.$store.commit('auth/IS_AUTHENTICATED', true);
          this.$store.dispatch('request/getRequests');
          this.$store.dispatch('news/getNews');
          this.$store.dispatch('events/getEvents');
          this.clearForm();
        });
    }
  },
};
</script>

<style>
  @import './app.css';
</style>
