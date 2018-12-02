<template lang="pug">
  v-flex(xs12)
    v-card
      v-card-title(primary-title style="padding-bottom: 0px;")
        span.title(style="margin-bottom: 10px;") {{ deviceTemplate.name }}
        hr
        p.headline Характеристики:
        p.subheading(v-for="param in deviceTemplate.params") {{ param.name }}: {{ param.value }}
      v-card-actions
        v-btn(@click="dialogState = true" color="success")
          v-flex
            span Редактировать
        v-btn(@click="deleteDeviceTemplate" color="error")
          v-flex
            span Удалить
    device-template-form(
      @closeAction="closeAction"
      v-if="dialogState"
      :id="deviceTemplate.id"
      :dialogState="dialogState" mode="edit"
      :templateNameInit="deviceTemplate.name"
      :parametersInit="deviceTemplate.params"
    )
</template>

<script>
import DeviceTemplateForm from './DeviceTemplateForm.vue';

export default {
  name: 'DeviceTemplateItem',
  data() {
    return {
      dialogState: false,
    };
  },
  props: {
    deviceTemplate: {
      type: Object,
    },
  },
  components: {
    DeviceTemplateForm,
  },
  methods: {
    deleteDeviceTemplate() {
      this.$store.dispatch('device/deleteDeviceTemplate', this.deviceTemplate.id);
    },
    closeAction() {
      this.dialogState = false;
    },
  },
};
</script>

<style scoped>

</style>
