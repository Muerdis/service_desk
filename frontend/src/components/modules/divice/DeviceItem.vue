<template lang="pug">
  v-flex(xs12)
    v-card
      v-card-title(primary-title style="padding-bottom: 0px;")
        span.title(style="margin-bottom: 10px;") {{ device.name }}
        hr
        p Инвентарный номер: {{ device.inventory_number }}
      v-card-actions
        v-btn(@click="dialogState = true" color="success")
          v-flex
            span Редактировать
        v-btn(@click="deleteDevice" color="error")
          v-flex
            span Удалить
    device-form(
      @closeAction="closeAction"
      v-if="dialogState"
      :id="device.id"
      :dialogState="dialogState" mode="edit"
      :deviceNameInit="device.name"
      :deviceNumInit="device.inventory_number"
      :deviceTemplateInit="device.device_template"
    )
</template>

<script>
import DeviceForm from './DeviceForm.vue';

export default {
  name: 'DeviceItem',
  data() {
    return {
      dialogState: false,
    };
  },
  props: {
    device: {
      type: Object,
    },
  },
  components: {
    DeviceForm,
  },
  methods: {
    deleteDevice() {
      this.$store.dispatch('device/deleteDevice', this.device.id);
    },
    closeAction() {
      this.dialogState = false;
    },
  },
};
</script>

<style scoped>

</style>
