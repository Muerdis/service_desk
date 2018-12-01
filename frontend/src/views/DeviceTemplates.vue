<template lang="pug">
  div
    base-component
    v-content
      v-container(grid-list-md)
        v-layout(row wrap)
    v-dialog(v-model="dialog" persistent max-width="800px")
      v-btn(slot="activator" fab fixed bottom right dark color="primary")
        v-icon(dark) add
      v-card
        v-card-title
          span.headline.text-center(style="width: 100%;") Добавление шаблона оборудования
        v-card-text
          v-container(grid-list-md)
            v-layout(wrap)
              v-flex(xs12)
                v-text-field(v-model="templateName" label="Название *" required)
              v-layout(wrap v-for="(param, index) in parameters")
                v-flex(xs12 sm5)
                  v-text-field(v-model="param.name" label="Характеристика")
                v-flex(xs12 sm6)
                  v-text-field(v-model="param.value" label="Значение")
                v-flex(xs12 sm1)
                  v-btn(fab dark small color="error" @click="removeParameter(index)")
                    v-icon(dark ) remove
              v-flex(xs12)
                v-btn(dark color="success" @click="addParameter") Добавить характеристику
        v-card-actions
          v-spacer
          v-btn(color="blue darken-1" flat @click="clearForm") Закрыть
          v-btn(color="blue darken-1" flat @click="createDeviceTemplate") Готово
</template>

<script>
import BaseComponent from '../components/base/BaseComponent.vue';
import RequestItem from '../components/modules/request/RequestItem.vue';

export default {
  name: 'DeviceTemplates',
  components: {
    BaseComponent,
    RequestItem,
  },
  data() {
    return {
      dialog: false,
      templateName: null,
      parameters: [],
    };
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
      this.dialog = null;
      this.templateName = null;
      this.parameters = [];
    },
    createDeviceTemplate() {
      const info = {
        name: this.templateName,
        params: this.parameters,
      };

      this.$store.dispatch('device/createDeviceTemplate', info);
      this.clearForm();
    },
  },
};
</script>

<style scoped>

</style>
