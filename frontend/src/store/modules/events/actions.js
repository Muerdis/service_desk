import Moment from 'moment';
import { extendMoment } from 'moment-range';

import requests from '../../../utils/http';

const moment = extendMoment(Moment);

async function getEvents(context) {
  const infoUrl = '/events/';
  const infoPromise = requests.api.get(infoUrl);
  const infoResponse = await Promise.resolve(infoPromise);

  let eventsDates = [];
  infoResponse.data.results.forEach((item) => {
    const dateFrom = new Date(item.from_date);
    const dateTo = new Date(item.to_date);
    const range = moment().range(dateFrom, dateTo);

    for (let day of range.by('day')) {
      eventsDates.push({
        title: item.title,
        details: item.preview_text,
        open: false,
        date: day.format('YYYY-MM-DD'),
      });
    }
  });

  context.commit('EVENTS', infoResponse.data.results);
  context.commit('EVENTS_DATES', eventsDates);
}

export default {
  getEvents,
};
