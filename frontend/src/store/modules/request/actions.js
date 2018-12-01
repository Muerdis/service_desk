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
    status: info.status,
  };
  const patchPromise = requests.api.patch(patchUrl, data);
  await Promise.resolve(patchPromise);

  getRequests(context);
}

async function deleteRequest(context, id) {
  const deleteUrl = `/requests/${id}/`;
  const deletePromise = requests.api.delete(deleteUrl);
  await Promise.resolve(deletePromise);

  getRequests(context);
}

async function getRequestTypes(context) {
  const infoUrl = '/request-types/';
  const infoPromise = requests.api.get(infoUrl);
  const infoResponse = await Promise.resolve(infoPromise);

  context.commit('REQUEST_TYPES', infoResponse.data.results);
}

async function getRequestReasons(context) {
  const infoUrl = '/request-reasons/';
  const infoPromise = requests.api.get(infoUrl);
  const infoResponse = await Promise.resolve(infoPromise);

  context.commit('REQUEST_REASONS', infoResponse.data.results);
}

async function createRequest(context, info) {
  const createUrl = '/requests/';
  const createPromise = requests.api.post(createUrl, info);
  await Promise.resolve(createPromise);

  getRequests(context);
}

export default {
  getRequests,
  changeStatus,
  deleteRequest,
  getRequestTypes,
  getRequestReasons,
  createRequest,
};
