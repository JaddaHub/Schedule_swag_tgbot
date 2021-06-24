import json
from datetime import datetime


class Shedule:
    def __init__(self, cur_datetime, squad):
        self.cur_datetime = cur_datetime
        self.squad = squad
        self.JSON_NAME = 'json_timetable.json'

        with open(self.JSON_NAME, encoding='utf-8') as jsload:
            self.shedule = json.load(jsload)

    def what_activity(self):
        today = self.shedule[self.squad][str(self.cur_datetime.day)]
        for time in today:
            t1, t2 = self._refact_two_datetimes(time)
            if t1 <= self.cur_datetime < t2:
                return time, today[time]
        return False

    def what_next_activity(self):
        today = self.shedule[self.squad][str(self.cur_datetime.day)]
        for time in today:
            t = self._refact_two_datetimes(time)[0]
            if t > self.cur_datetime:
                return time, today[time]

    def what_now(self):
        return self.what_activity() if self.what_activity() else False

    def what_next(self):
        return self.what_next_activity()

    def remaining_time(self):
        now = self.what_now()
        return self._refact_two_datetimes(now[0])[1] - self.cur_datetime if now \
            else self._refact_two_datetimes(self.what_next()[0])[0] \
                 - self.cur_datetime

    def remaining_to_next(self):
        return self._refact_two_datetimes(self.what_next()[0])[
                   0] - self.cur_datetime

    def show_shedule(self):
        return self.shedule[self.squad][str(self.cur_datetime.day)]

    def _refact_two_datetimes(self, time):
        return self._refact_time_to_datetime(
            time[:time.find('-')]), self._refact_time_to_datetime(
            time[time.find('-') + 1:])

    def _refact_time_to_datetime(self, time_str):
        time_str = time_str.split('-')[0]
        res = self.cur_datetime
        return res.replace(hour=int(time_str[:time_str.find(':')]),
                           minute=int(time_str[time_str.find(':') + 1:]),
                           second=0)
