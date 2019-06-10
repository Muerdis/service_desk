<template lang="pug">
  v-dialog(v-model="dialog" persistent max-width="800px")
    v-btn(v-if="mode === 'create'" slot="activator" fab fixed bottom right dark color="primary")
      v-icon(dark) add
    v-card
      v-card-title
        span.headline.text-center(
          v-if="mode === 'create'" style="width: 100%;"
        ) Добавление шаблона оборудования
        span.headline.text-center(
          v-if="mode === 'edit'" style="width: 100%;"
        ) Изменение шаблона оборудования
      v-card-text
        v-container(grid-list-md)
          v-layout(wrap)
            v-flex(xs12)
              v-text-field(v-model="templateName" label="Название *" required)
            v-layout(wrap v-for="(param, index) in parameters")
              v-flex(xs12 sm5)
                v-textarea(rows="1" v-model="param.name" label="Характеристика")
              v-flex(xs12 sm6)
                v-textarea(rows="1" v-model="param.value" label="Значение")
              v-flex(xs12 sm1)
                v-btn(fab dark small color="error" @click="removeParameter(index)")
                  v-icon(dark ) remove
            v-flex(xs12)
              v-btn(dark color="success" @click="addParameter") Добавить характеристику
      v-card-actions
        v-spacer
        v-btn(color="blue darken-1" flat @click="clearForm") Закрыть
        v-btn(
          v-if="mode === 'create'" color="blue darken-1"
          flat @click="createDeviceTemplate" :disabled="disableCreation"
        ) Готово
        v-btn(
          v-if="mode === 'edit'" color="blue darken-1"
          flat @click="editDeviceTemplate" :disabled="disableCreation"
        ) Сохранить изменения
</template>

<script>
export default {
  name: 'DeviceTemplateForm',
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
    templateNameInit: {
      type: String,
    },
    parametersInit: {
      type: Array,
    },
  },
  data() {
    return {
      dialog: this.dialogState,
      templateName: this.templateNameInit,
      parameters: this.parametersInit,
    };
  },
  computed: {
    disableCreation() {
      return !(this.templateName && this.parameters);
    },
  },
  methods: {
    removeParameter(index) {
      this.parameters.splice(index, 1);
    },
    addParameter() {
      this.parameters.push({
        name: null,
        value: null,
      });
    },
    clearForm() {
      this.dialog = false;
      this.templateName = null;
      this.parameters = [];
      this.$emit('closeAction');
    },
    createDeviceTemplate() {
      const info = {
        name: this.templateName,
        params: this.parameters,
      };

      this.$store.dispatch('device/createDeviceTemplate', info);
      this.clearForm();
    },
    editDeviceTemplate() {
      const info = {
        id: this.id,
        name: this.templateName,
        params: this.parameters,
      };

      this.$store.dispatch('device/editDeviceTemplate', info);
      this.clearForm();
    },
  },
};
</script>

<style scoped>

</style>
