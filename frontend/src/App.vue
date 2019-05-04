<template lang="pug">
  v-app#inspire.main-background
    router-view
</template>

<script>
import requests from './utils/http';
import Cookies from 'js-cookie';

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
          this.clearForm();
        });
    }
  },
};
</script>

<style>
  @import './app.css';
</style>
