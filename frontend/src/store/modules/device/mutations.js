const DEVICE_TEMPLATES = (state, deviceTemplates) => {
  const st = state;
  st.deviceTemplates = deviceTemplates;
};

const DEVICES = (state, devices) => {
  const st = state;
  st.devices = devices;
};

export default {
  DEVICE_TEMPLATES,
  DEVICES,
};
