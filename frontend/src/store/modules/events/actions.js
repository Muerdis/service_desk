import requests from '../../../utils/http';

async function getEvents(context) {
  const infoUrl = '/events/';
  const infoPromise = requests.api.get(infoUrl);
  const infoResponse = await Promise.resolve(infoPromise);

  context.commit('EVENTS', infoResponse.data.results);
}

export default {
  getEvents,
};
