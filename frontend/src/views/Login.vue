<template lang="html">
  <form class="login form">
    <div class="field">
      <label for="id_username">Username</label>
      <input
        v-model="username"
        type="text"
        placeholder="Username"
        autofocus="autofocus"
        maxlength="150"
        id="id_username">
    </div>
    <div class="field">
      <label for="id_password">Password</label>
      <input
        v-model="password"
        type="password"
        placeholder="Password"
        id="id_password">
    </div>
    <button
      @click.prevent="authenticate"
      class="button primary"
      type="submit">
      Log In
    </button>
  </form>
</template>

<script>
import axios from 'axios';

import { mapGetters } from 'vuex';

export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
    };
  },
  computed: {
    ...mapGetters({
      jwt: 'auth/jwt',
      endpoints: 'auth/endpoints',
    }),
  },
  methods: {
    authenticate() {
      const payload = {
        username: this.username,
        password: this.password,
      };
      axios.post(this.endpoints.obtainJWT, payload)
        .then((response) => {
          this.$store.commit('auth/UPDATE_TOKEN', response.data.token);

          const base = {
            baseURL: this.endpoints.baseUrl,
            headers: {
              Authorization: `JWT ${this.jwt}`,
              'Content-Type': 'application/json',
            },
            xhrFields: {
              withCredentials: true,
            },
          };

          const axiosInstance = axios.create(base);

          axiosInstance({
            url: 'auth-user/',
            method: 'get',
            params: {},
          })
            .then((userResponse) => {
              this.$store.commit('auth/AUTH_USER', userResponse.data);
              this.$store.commit('auth/IS_AUTHENTICATED', true);
              this.$router.push({ name: 'home' });
            });
        });
    },
  },
};
</script>

<style scoped>

</style>
