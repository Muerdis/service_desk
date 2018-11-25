<template lang="pug">
  v-card
    v-layout
      v-flex(xs1)
      v-flex(xs10)
        v-form(v-model="valid")
          v-text-field(v-model="name" :rules="nameRules" :counter="10" label="Name" required)
          v-text-field(v-model="email" :rules="emailRules" label="E-mail" required)
      v-flex(xs1)
</template>

<script>
export default {
  name: 'RequestCard',
  data() {
    return {
      valid: false,
      name: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => v.length <= 10 || 'Name must be less than 10 characters',
      ],
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid',
      ],
    };
  },
};
</script>

<style scoped>

</style>
