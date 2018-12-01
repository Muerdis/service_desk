const USER = (state, user) => {
  const st = state;
  st.user = user;
};

const USERS = (state, users) => {
  const st = state;
  st.users = users;
};

export default {
  USER,
  USERS,
};
