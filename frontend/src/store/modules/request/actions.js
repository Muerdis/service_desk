import requests from '../../../utils/http';

async function getRequests(context) {
  const infoUrl = '/requests/';
  const infoPromise = requests.api.get(infoUrl);
  const infoResponse = await Promise.resolve(infoPromise);

  context.commit('REQUESTS', infoResponse.data.results);
}

async function changeStatus(context, info) {
  const patchUrl = `/requests/${info.id}/`;
  const data = {
    status: info.status
  };
  const patchPromise = requests.api.patch(patchUrl, data);
  await Promise.resolve(patchPromise);

  getRequests(context)
}

async function deleteRequest(context, id) {
  const deleteUrl = `/requests/${id}/`;
  const deletePromise = requests.api.delete(deleteUrl);
  await Promise.resolve(deletePromise);

  getRequests(context)
}

export default {
  getRequests,
  changeStatus,
  deleteRequest,
};
