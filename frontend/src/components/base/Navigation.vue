<template lang="pug">
  v-navigation-drawer(v-model="drawer" fixed app width="250")
    v-avatar(:tile="false" size="200"  color="grey lighten-4" style="margin-left: 25px;")
      img(src="@/assets/logo.png" alt="avatar")
    v-list(dense)
      v-list-tile(to="/")
        v-list-tile-action
          v-icon home
        v-list-tile-content
          v-list-tile-title Главная
      v-list-tile(@click="")
        v-list-tile-action
          v-icon vertical_split
        v-list-tile-content
          v-list-tile-title Новости
      v-list-group(
        v-for="item in items" v-model="item.active"
        :key="item.title" :prepend-icon="item.action" no-action
      )
        v-list-tile(slot="activator")
          v-list-tile-content
            v-list-tile-title {{ item.title }}
        v-list-tile(v-for="subItem in item.items" :key="subItem.title" :to="subItem.to")
          v-list-tile-content
            v-list-tile-title {{ subItem.title }}
          v-list-tile-action
            v-icon {{ subItem.action }}
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'Navigation',
  data() {
    return {
      items: [
        {
          action: 'description',
          title: 'Заявки',
          active: true,
          items: [
            { title: 'Agile доска', to: '/agile' },
            { title: 'Входящие', to: '/incoming-requests' },
            { title: 'Исходящие', to: '/outgoing-requests' },
            { title: 'В работе', to: '/in-work-requests' },
            { title: 'Выполнено', to: '/completed-requests' },
          ],
        },
      ],
    };
  },
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
