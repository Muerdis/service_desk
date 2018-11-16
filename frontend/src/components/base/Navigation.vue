<template lang="pug">
  v-navigation-drawer(v-model="drawer" fixed app width="250")
    v-avatar(:tile="false" size="200"  color="grey lighten-4" style="margin-left: 25px;")
      img(src="@/assets/logo.png" alt="avatar")
    v-list(dense)
      v-list-tile(to="/")
        v-list-tile-action
          v-icon(style="font-size: 40px;") home
        v-list-tile-content
          v-list-tile-title.title Главная
      v-list-tile(to="/requests")
        v-list-tile-action
          v-icon(style="font-size: 40px;") description
        v-list-tile-content
          v-list-tile-title.title Заявки
      v-list-tile(@click="")
        v-list-tile-action
          v-icon(style="font-size: 40px;") vertical_split
        v-list-tile-content
          v-list-tile-title.title Новости
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'Navigation',
  computed: {
    ...mapGetters({
      stDrawer: 'base/drawer',
    }),
    drawer: {
      get() {
        return this.stDrawer;
      },
      set(value) {
        this.$store.commit('base/DRAWER', value);
      },
    },
  },
};
</script>

<style scoped>

</style>
