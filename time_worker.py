import json
from datetime import datetime, timedelta
from config import json_name


class Shedule:
    def __init__(self, cur_datetime, squad):
        self.cur_datetime = cur_datetime
        self.squad = squad
        self.JSON_NAME = json_name

        with open(self.JSON_NAME, encoding='utf-8', mode='r') as jsload:
            self.shedule = json.load(jsload)

    def what_activity(self):
        try:
            today = self.shedule[self.squad][str(self.cur_datetime.day)]
        except KeyError:
            return

        for time in today:
            t1, t2 = self._refact_two_datetimes(time)
            if t1 <= self.cur_datetime < t2:
                return time, today[time]
        else:
            if t1 - timedelta(days=1) <= self.cur_datetime < t2:
                return time, today[time]

        return False

    def what_next_activity(self):
        try:
            today = self.shedule[self.squad][str(self.cur_datetime.day)]
        except KeyError:
            return

        for time in today:
            t = self._refact_two_datetimes(time)[0]
            if t > self.cur_datetime:
                return time, today[time]
        return False

    def what_now(self):
        return self.what_activity() if self.what_activity() else False

    def what_next(self):
        return self.what_next_activity() if self.what_next_activity() else False

    def remaining_time(self):
        now = self.what_now()
        if now:
            return self._refact_two_datetimes(now[0])[1] - self.cur_datetime
        elif self.what_next():
            return self._refact_two_datetimes(self.what_next()[0])[0] - self.cur_datetime
        return False

    def remaining_to_next(self):
        return self._refact_two_datetimes(self.what_next()[0])[
                   0] - self.cur_datetime if self.what_next() else False

    def show_shedule(self):
        try:
            return self.shedule[self.squad][str(self.cur_datetime.day)]
        except KeyError:
            return

    def show_shedule_tomorrow(self):
        try:
            return self.shedule[self.squad][
                str((self.cur_datetime + timedelta(days=1)).day)]
        except KeyError:
            return

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


if __name__ == '__main__':
    dt = datetime.now()
    sh = Shedule(dt, '1')
    print(sh.remaining_time())
