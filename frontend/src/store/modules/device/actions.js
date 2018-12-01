import requests from '../../../utils/http';

async function createDeviceTemplate(context, info) {
  const createUrl = '/device-templates/';
  const createPromise = requests.api.post(createUrl, info);
  await Promise.resolve(createPromise);
}

export default {
  createDeviceTemplate,
};
