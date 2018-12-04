import requests from '../../../utils/http';

async function getUsers(context) {
  const infoUrl = '/users/';
  const infoPromise = requests.api.get(infoUrl);
  const infoResponse = await Promise.resolve(infoPromise);

  context.commit('USERS', infoResponse.data.results);
}

export default {
  getUsers,
};
