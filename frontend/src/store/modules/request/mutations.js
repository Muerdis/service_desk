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

export default {
  REQUESTS,
  REQUEST_TYPES,
  REQUEST_REASONS,
};
