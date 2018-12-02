<template lang="pug">
  div
    base-component
    v-content
      v-container(grid-list-md)
        v-layout(wrap)
          v-flex(xs6 v-for="deviceTemplate in deviceTemplates")
            device-template-item(:deviceTemplate="deviceTemplate")
    device-template-form(
      :id="null" :dialogState="false" mode="create" :templateNameInit="null" :parametersInit="[]"
    )
</template>

<script>
import { mapGetters } from 'vuex';

import BaseComponent from '../components/base/BaseComponent.vue';
import DeviceTemplateItem from '../components/modules/divice/DeviceTemplateItem.vue';
import DeviceTemplateForm from '../components/modules/divice/DeviceTemplateForm.vue';

export default {
  name: 'DeviceTemplates',
  components: {
    BaseComponent,
    DeviceTemplateItem,
    DeviceTemplateForm,
  },
  mounted() {
    this.$store.dispatch('device/getDeviceTemplates');
  },
  computed: {
    ...mapGetters({
      deviceTemplates: 'device/deviceTemplates',
    }),
  },
};
</script>

<style scoped>

</style>
