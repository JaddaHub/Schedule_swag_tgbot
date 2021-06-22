from datetime import datetime
import json


class Shedule:
    def __init__(self, datetime):
        self.datetime = datetime

        with open('timetable.json', 'r') as json_file:
            self.shedule = json.load(json_file)


    def what_now(self):
        now = datetime.now()
        try:
            today = self.shedule[datetime.today()]
            for hour in today.keys():
                if hour <= now.hour:
                    return today[hour]

        except KeyError:
            return 0


    def what_next(self):
        now = datetime.now()
        has_now = False
        try:
            today = self.shedule[datetime.today()]
            for hour in today.keys():
                if hour <= now.hour and has_now:
                    return today[hour]
                elif not has_now:
                    has_now = True

        except KeyError:
            return 0


if __name__ == '__main__':
    dt = datetime(1231, 11, 23, 21, 34, 45)
    shed = Shedule(dt)
    shed.what_now()
