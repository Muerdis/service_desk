<template lang="pug">
  div
    base-component
    v-content
      v-container(grid-list-md)
        v-layout(wrap)
          v-flex(xs6 v-for="device in devices")
            device-item(:device="device")
    device-form(
      :id="null" :dialogState="false" mode="create" :deviceNameInit="null"
    )
</template>

<script>
import { mapGetters } from 'vuex';

import BaseComponent from '../components/base/BaseComponent.vue';
import DeviceItem from '../components/modules/divice/DeviceItem.vue';
import DeviceForm from '../components/modules/divice/DeviceForm.vue';

export default {
  name: 'Devices',
  components: {
    BaseComponent,
    DeviceItem,
    DeviceForm,
  },
  mounted() {
    this.$store.dispatch('device/getDevices');
  },
  computed: {
    ...mapGetters({
      devices: 'device/devices',
    }),
  },
};
</script>

<style scoped>

</style>
