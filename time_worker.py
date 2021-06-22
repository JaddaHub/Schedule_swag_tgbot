import json
from datetime import datetime
from datetime import timedelta


class Shedule:
    def __init__(self, cur_datetime, squad):
        self.cur_datetime = cur_datetime
        self.squad = squad
        self.JSON_NAME = 'json_timetable.json'

        with open(self.JSON_NAME, encoding='utf-8') as jsload:
            self.shedule = json.load(jsload)

        self.activity = self.what_activity()

    def what_now(self):
        return self.activity

    def what_next(self):
        return self.activity[1]

    def activity_timings(self):
        return tuple([i[0] for i in self.what_activity()])

    def what_activity(self):
        for timing in self.shedule[self.squad][str(self.cur_datetime.day)]:
            print(timing)

    def remaining_time(self):
        t1 = self._refact_time_to_datetime(self.activity[1][0])
        t2 = self.cur_datetime
        return timedelta(t2 - t1)

    def show_shedule(self):
        return [timing for timing in
                self.shedule[self.squad][str(self.cur_datetime.day)]]

    def _refact_time_to_datetime(self, time_str):
        time_str = time_str.split('-')[0]
        res = self.cur_datetime
        return res.replace(hour=int(time_str[:time_str.find(':')]),
                           minute=int(time_str[time_str.find(':') + 1]))


if __name__ == '__main__':
    # print(datetime.now().day)
    sd = Shedule(datetime.now(), '1')

    print(sd.what_now())
    print(sd.what_next())
