import json
from datetime import datetime
from datetime import timedelta


# cur_time
# отряд

# расписание на день
# what_next
# оставшееся время
# что сейчас


class Shedule:
    def __init__(self, cur_datetime, squad, json_file):
        self.cur_datetime = cur_datetime
        self.squad = squad
        self.shedule = json_file

        self.activity = self.what_activity()

    def what_now(self):
        return self.activity[0]

    def what_next(self):
        return self.activity[1]

    def what_activity(self):
        has_now = False
        res = []
        try:
            today = self.shedule[self.cur_datetime.today()]
            for hour in today[0].keys():
                ref_hour = self._refact_time_to_datetime(hour)
                if ref_hour <= self.cur_datetime and has_now:
                    res.extend((hour, self.shedule[hour]))
                elif not has_now:
                    has_now = True
                    res.extend((hour, self.shedule[hour]))
        except KeyError:
            return None
        finally:
            return res

    def remaining_time(self):
        t1 = self._refact_time_to_datetime(self.activity[1][0])
        t2 = self.cur_datetime
        return timedelta(t2 - t1)

    def show_shedule(self):
        return self.shedule[self.cur_datetime.date][0]

    def _refact_time_to_datetime(self, time_str):
        return int(time_str[:time_str.find(':')]) * 60 + int(
            time_str[time_str.find(':') + 1:])
