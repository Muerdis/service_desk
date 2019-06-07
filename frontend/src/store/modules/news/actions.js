import requests from '../../../utils/http';

async function getNews(context) {
  const infoUrl = '/news/';
  const infoPromise = requests.api.get(infoUrl);
  const infoResponse = await Promise.resolve(infoPromise);

  context.commit('NEWS', infoResponse.data.results);
}

export default {
  getNews,
};
