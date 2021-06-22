from datetime import datetime
import csv


def readcsv():
    with open('template.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
    return reader


SHEDULE = readcsv()


class Shedule:
    def __init__(self, datetime):
        self.datetime = datetime

    def what_now(self):
        print(self.datetime)


if __name__ == '__main__':
    dt = datetime(1231, 11, 23, 21, 34, 45)
    shed = Shedule(dt)
    shed.what_now()
