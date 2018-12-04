<template lang="pug">
  v-toolbar.no-transition(color="grey darken-3" dark app)
    v-toolbar-side-icon(@click.stop="changeDrawerState")
    v-toolbar-title Service desk
    login-form(v-if="dialogState" @closeAction="closeAction" :dialogState="dialogState")
    v-spacer
    v-btn(v-if="isAuthenticated" color="info" @click="logout") Выйти
    v-btn(v-else color="info" @click="dialogState = true") Войти
</template>

<script>
import { mapGetters } from 'vuex';

import LoginForm from './LoginForm.vue';

export default {
  name: 'Toolbar',
  components: {
    LoginForm,
  },
  data() {
    return {
      dialogState: false,
    };
  },
  computed: {
    ...mapGetters({
      drawer: 'base/drawer',
      isAuthenticated: 'auth/isAuthenticated',
    }),
  },
  methods: {
    changeDrawerState() {
      this.$store.commit('base/DRAWER', !this.drawer);
    },
    closeAction() {
      this.dialogState = false;
    },
    logout() {
      this.$store.commit('auth/REMOVE_TOKEN');
      this.$store.commit('auth/AUTH_USER', null);
      this.$store.commit('auth/IS_AUTHENTICATED', false);
      this.$router.push({ name: 'home' });
    },
  },
};
</script>

<style scoped>
.no-transition {
  transition: none;
}
</style>
