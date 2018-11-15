import requests from '../../../utils/http';

async function getRequests(context) {
  const infoUrl = '/requests/';
  const infoPromise = requests.api.get(infoUrl);
  const infoResponse = await Promise.resolve(infoPromise);

  context.commit('REQUESTS', infoResponse.data.results);
}

export default {
  getRequests,
};
