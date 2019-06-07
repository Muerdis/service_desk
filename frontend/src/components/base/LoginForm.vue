<template lang="pug">
  v-dialog(v-model="dialog" persistent max-width="300px")
    v-card
      v-card-text
        v-container
          v-layout(wrap)
            v-flex(xs12 v-if="respError")
              span.response-error Введите верные логин и пароль
            v-flex(xs12)
              v-text-field(
                ref="username" v-model="username" label="Логин *" required @change="removeRespError"
              )
            v-flex(xs12)
              v-text-field(
                ref="password" v-model="password" label="Пароль *" required type="password"
                :append-icon="showPass ? 'visibility' : 'visibility_off'"
                :type="showPass ? 'text' : 'password'" :rules="[rules.required,]"
                @change="removeRespError" @click:append="showPass = !showPass"
              )
      v-card-actions
        v-spacer
        v-btn(
          color="blue darken-1" flat @click="clearForm"
        ) Закрыть
        v-btn(
          color="blue darken-1" flat @click="authenticate"
        ) Войти
</template>

<script>
import axios from 'axios';
import Cookies from 'js-cookie';

import { mapGetters } from 'vuex';

import requests from '../../utils/http';

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
      showPass: false,
      rules: {
        required: value => !!value || 'Поле обязательно для заполнения.',
      },
      respError: false,
    };
  },
  computed: {
    ...mapGetters({
      jwt: 'auth/jwt',
      endpoints: 'auth/endpoints',
    }),
    form() {
      return {
        username: this.username,
        password: this.password,
      };
    },
  },
  methods: {
    removeRespError() {
      this.respError = false;
    },
    clearForm() {
      this.dialog = false;
      this.username = '';
      this.password = '';
      this.$emit('closeAction');
    },
    authenticate() {
      let hasErrors = false;

      Object.keys(this.form).forEach((field) => {
        if (!this.form[field]) {
          hasErrors = true;
        }

        this.$refs[field].validate(true);
      });

      if (!hasErrors) {
        const payload = {
          username: this.username,
          password: this.password,
        };
        requests.internal.post('auth/obtain_token/', payload)
          .then((response) => {
            this.$store.commit('auth/UPDATE_TOKEN', response.data.token);

            const base = {
              baseURL: 'http://139.162.128.213:8000/api/',
              headers: {
                Authorization: `JWT ${Cookies.get('csrftoken')}`,
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
          })
          .catch(() => {
            this.respError = true;
          });
      }
    },
  },
};
</script>

<style scoped>
 .response-error {
   color: #ff5252
 }
</style>
