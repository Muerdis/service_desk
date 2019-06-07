<template lang="pug">
  div
    base-component
    v-content
      v-container(grid-list-md)
        v-layout.white(wrap)
          v-flex.mb-3(xs12)
            v-sheet(height="500")
              v-calendar(
                ref="calendar"
                v-model="start"
                locale="ru-ru"
                :weekdays="[1,2,3,4,5,6,0]"
                :type="type"
                color="primary"
              )
          v-flex.text-sm-left.text-xs-center(sm4 xs12)
            v-btn(@click="$refs.calendar.prev()")
              v-icon(dark left) keyboard_arrow_left
          v-flex.text-xs-center(sm4 xs12)
            v-select(
              v-model="type"
              :items="typeOptions"
              label="Фильтр"
            )
          v-flex.text-sm-right.text-xs-center(sm4 xs12)
            v-btn(@click="$refs.calendar.next()")
              v-icon(dark right) keyboard_arrow_right
</template>

<script>

import BaseComponent from '../components/base/BaseComponent.vue';

export default {
  name: 'EventsCal',
  components: {
    BaseComponent,
  },
  data: () => ({
    type: 'month',
    start: '2019-06-07',
    typeOptions: [
      { text: 'День', value: 'day' },
      { text: '4 Дня', value: '4day' },
      { text: 'Неделя', value: 'week' },
      { text: 'Месяц', value: 'month' },
    ],
  }),
};
</script>

<style scoped>

</style>
