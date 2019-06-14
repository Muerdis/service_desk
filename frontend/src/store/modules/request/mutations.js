const REQUESTS = (state, requests) => {
  const st = state;
  st.requests = requests;
};

const REQUEST_TYPES = (state, requestTypes) => {
  const st = state;
  st.requestTypes = requestTypes;
};

const REQUEST_REASONS = (state, requestReasons) => {
  const st = state;
  st.requestReasons = requestReasons;
};

const RESERVATIONS = (state, reservations) => {
  const st = state;
  st.reservations = reservations;
};

const MAINTENANCES = (state, maintenances) => {
  const st = state;
  st.maintenances = maintenances;
};

export default {
  REQUESTS,
  REQUEST_TYPES,
  REQUEST_REASONS,
  RESERVATIONS,
  MAINTENANCES,
};
