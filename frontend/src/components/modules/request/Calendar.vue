<template>
  <v-layout class="white" wrap>
    <v-flex class="mb-3" xs12>
      <v-sheet height="500">
        <v-calendar
          ref="calendar"
          locale="ru-ru"
          :weekdays="[1,2,3,4,5,6,0]"
          :type="type"
          color="primary"
          v-model="start"
        >
          <template v-slot:day="{ date }">
            <template v-for="event in eventsMap[date]">
              <v-menu
                :key="event.title"
                v-model="event.open"
                full-width
                offset-x
              >
                <template v-slot:activator="{ on }">
                  <div
                    v-if="!event.time"
                    class="event-title"
                    v-on="on"
                    v-html="event.title"
                  ></div>
                </template>
                <v-card
                  color="grey lighten-4"
                  min-width="350px"
                  flat
                >
                  <v-card-title primary-title>
                    <span v-html="event.details"></span>
                  </v-card-title>
                </v-card>
              </v-menu>
            </template>
          </template>
        </v-calendar>
      </v-sheet>
    </v-flex>
    <v-flex class="text-sm-left text-xs-center" sm4 xs12>
      <v-btn @click="$refs.calendar.prev()">
        <v-icon dark left>
          keyboard_arrow_left
        </v-icon>
      </v-btn>
    </v-flex>
    <v-flex class="text-xs-center" sm4 xs12>
      <v-select v-model="type" :items="typeOptions" label="Фильтр"></v-select>
    </v-flex>
    <v-flex class="text-sm-right text-xs-center" sm4 xs12>
      <v-btn @click="$refs.calendar.next()">
        <v-icon dark right>
          keyboard_arrow_right
        </v-icon>
      </v-btn>
    </v-flex>
  </v-layout>
</template>

<script>
  export default {
    name: 'Calendar',
    props: {
      events: {
        type: Array,
      },
    },
    data: () => ({
      type: 'month',
      start: null,
      typeOptions: [
        { text: 'День', value: 'day' },
        { text: 'Неделя', value: 'week' },
        { text: 'Месяц', value: 'month' },
      ],
    }),
    computed: {
      eventsMap() {
        const map = {};
        this.events.forEach(e => (map[e.date] = map[e.date] || []).push(e));
        return map
      }
    },
  }
</script>

<style scoped>
  .event-title {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    border-radius: 2px;
    background-color: #1867c0;
    color: #ffffff;
    border: 1px solid #1867c0;
    width: 100%;
    font-size: 12px;
    padding: 3px;
    cursor: pointer;
    margin-bottom: 1px;
  }
</style>