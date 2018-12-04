<template lang="pug">
  v-dialog(v-model="dialog" persistent max-width="300px")
    v-card
      v-card-text
        v-container
          v-layout(wrap)
            v-flex(xs12)
              v-text-field(v-model="username" label="Логин *" required)
            v-flex(xs12)
              v-text-field(v-model="password" label="Пароль *" required type="password")
      v-card-actions
        v-spacer
        v-btn(
          color="blue darken-1" flat @click="authenticate"
        ) Войти
</template>

<script>
import axios from 'axios';

import { mapGetters } from 'vuex';

export default {
  name: 'LoginForm',
  props: {
    dialogState: {
      type: Boolean,
    },
  },
  data() {
    return {
      dialog: this.dialogState,
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
    clearForm() {
      this.dialog = false;
      this.username = '';
      this.password = '';
      this.$emit('closeAction');
    },
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
              this.$store.dispatch('request/getRequests');
              this.clearForm();
            });
        });
    },
  },
};
</script>

<style scoped>

</style>
