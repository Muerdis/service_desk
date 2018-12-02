import requests from '../../../utils/http';

async function getDeviceTemplates(context) {
  const infoUrl = '/device-templates/';
  const infoPromise = requests.api.get(infoUrl);
  const infoResponse = await Promise.resolve(infoPromise);

  context.commit('DEVICE_TEMPLATES', infoResponse.data.results);
}

async function createDeviceTemplate(context, info) {
  const createUrl = '/device-templates/';
  const createPromise = requests.api.post(createUrl, info);
  await Promise.resolve(createPromise);

  getDeviceTemplates(context);
}

async function deleteDeviceTemplate(context, id) {
  const deleteUrl = `/device-templates/${id}/`;
  const deletePromise = requests.api.delete(deleteUrl);
  await Promise.resolve(deletePromise);

  getDeviceTemplates(context);
}

async function editDeviceTemplate(context, info) {
  const patchUrl = `/device-templates/${info.id}/`;
  const patchPromise = requests.api.patch(patchUrl, info);
  await Promise.resolve(patchPromise);

  getDeviceTemplates(context);
}

export default {
  getDeviceTemplates,
  createDeviceTemplate,
  deleteDeviceTemplate,
  editDeviceTemplate,
};
