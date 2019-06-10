<template lang="pug">
  v-dialog(v-model="dialog" persistent max-width="800px")
    v-btn(v-if="mode === 'create'" slot="activator" fab fixed bottom right dark color="primary")
      v-icon(dark) add
    v-card
      v-card-title
        span.headline.text-center(
          v-if="mode === 'create'" style="width: 100%;"
        ) Добавление оборудования
        span.headline.text-center(
          v-if="mode === 'edit'" style="width: 100%;"
        ) Изменение оборудования
      v-card-text
        v-container(grid-list-md)
          v-layout(wrap)
            v-flex(xs12)
              v-text-field(v-model="deviceName" label="Название *" required)
            v-flex(xs12)
              v-text-field(v-model="deviceNum" label="Инвентарный номер *" required)
            v-flex(xs12)
                v-autocomplete(
                  v-model="deviceTemplate"
                  :items="deviceTemplates"
                  item-value="id"
                  item-text="name"
                  label="Шаблон оборудования *"
                  required
                )
      v-card-actions
        v-spacer
        v-btn(color="blue darken-1" flat @click="clearForm") Закрыть
        v-btn(
          v-if="mode === 'create'" color="blue darken-1"
          flat @click="createDevice" :disabled="disableCreation"
        ) Готово
        v-btn(
          v-if="mode === 'edit'" color="blue darken-1"
          flat @click="editDevice" :disabled="disableCreation"
        ) Сохранить изменения
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'DeviceForm',
  props: {
    dialogState: {
      type: Boolean,
    },
    mode: {
      type: String,
    },
    id: {
      type: Number,
    },
    deviceNameInit: {
      type: String,
    },
    deviceNumInit: {
      type: String,
    },
    deviceTemplateInit: {
      type: Number,
    },
  },
  data() {
    return {
      dialog: this.dialogState,
      deviceName: this.deviceNameInit,
      deviceNum: this.deviceNumInit,
      deviceTemplate: this.deviceTemplateInit,
    };
  },
  mounted() {
    this.$store.dispatch('device/getDeviceTemplates');
  },
  computed: {
    ...mapGetters({
      deviceTemplates: 'device/deviceTemplates',
    }),
    disableCreation() {
      return !(this.deviceName && this.deviceNum && this.deviceTemplate);
    },
  },
  methods: {
    clearForm() {
      this.dialog = false;
      this.deviceName = null;
      this.deviceNum = null;
      this.deviceTemplate = null;
      this.$emit('closeAction');
    },
    createDevice() {
      const info = {
        name: this.deviceName,
        inventory_number: this.deviceNum,
        device_template: this.deviceTemplate,
      };

      this.$store.dispatch('device/createDevice', info);
      this.clearForm();
    },
    editDevice() {
      const info = {
        id: this.id,
        name: this.deviceName,
        inventory_number: this.deviceNum,
        device_template: this.deviceTemplate,
      };

      this.$store.dispatch('device/editDevice', info);
      this.clearForm();
    },
  },
};
</script>

<style scoped>

</style>
