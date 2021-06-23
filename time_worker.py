import json
from datetime import datetime


class Shedule:
    def __init__(self, cur_datetime, squad):
        self.relax_time = False
        self.cur_datetime = cur_datetime
        self.squad = squad
        self.JSON_NAME = 'json_timetable.json'

        with open(self.JSON_NAME, encoding='utf-8') as jsload:
            self.shedule = json.load(jsload)

    def what_now(self):
        return self.what_activity()[
            0] if self.what_activity() else self.relax_time

    def what_next(self):
        return self.what_activity()[
            1] if self.what_activity() else self.relax_time

    def activity_timings(self):
        return self.what_now()[0]

    def what_activity(self):
        today = self.shedule[self.squad][str(self.cur_datetime.day)]
        res = []
        for time in today:
            t1, t2 = self._refact_two_datetimes(time)
            if t1 <= self.cur_datetime < t2 or len(res) == 1:
                res.append((time, today[time]))
            if len(res) == 2:
                return res
        return False

    def remaining_time(self):
        return self._refact_two_datetimes(self.what_now()[0])[
                   1] - self.cur_datetime if self.what_now() else self.relax_time

    def remaining_to_next(self):
        return self._refact_two_datetimes(self.what_next()[0])[
                   0] - self.cur_datetime if self.what_next() else self.relax_time

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
                           minute=int(time_str[time_str.find(':') + 1:]))


if __name__ == '__main__':
    sd = Shedule(datetime.now(), '1')
    sd.remaining_time()
