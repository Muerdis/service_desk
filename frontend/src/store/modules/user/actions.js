import requests from '../../../utils/http';

async function getUserInfo(context) {
  const infoUrl = '/user-info/';
  const infoPromise = requests.api.get(infoUrl);
  const infoResponse = await Promise.resolve(infoPromise);

  context.commit('USER', infoResponse.data);
}

export default {
  getUserInfo,
};
