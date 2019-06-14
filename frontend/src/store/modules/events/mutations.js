const EVENTS = (state, events) => {
  const st = state;
  st.events = events;
};

const EVENTS_DATES = (state, eventsDates) => {
  const st = state;
  st.eventsDates = eventsDates;
};

export default {
  EVENTS,
  EVENTS_DATES,
};
