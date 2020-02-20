"""
author: Stergios Mekras

email: stergios.mekras@gmail.com
"""

import calendar
import datetime

from utils import easter


class HolyCalendar(calendar.Calendar):
    def __init__(self, year):
        super().__init__(1)
        self.year = year
        self.pasxa = easter.easter(self.year, 2)
        self.days = {0: calendar.SUNDAY,
                     1: calendar.MONDAY,
                     2: calendar.TUESDAY,
                     3: calendar.WEDNESDAY,
                     4: calendar.THURSDAY,
                     5: calendar.FRIDAY,
                     6: calendar.SATURDAY}

    def get_all_days(self):
        days = []
        for line in self.yeardatescalendar(self.year):
            for month in line:
                for week in month:
                    for date in week:
                        if date.year == self.year:
                            days.append(date)

        days = list(dict.fromkeys(days))
        return days

    def get_religious_moving(self, e):
        moving = {}

        for k in e.keys():
            v = e[k]["date"]
            if k in [336, 337]:
                date = self.next_weekday(v[1], v[2], v[0])
            elif k in [338, 339] and self.pasxa < datetime.date(self.year, 4, 23):
                date = datetime.date(self.year, v[1], v[2])
            elif k == 350:
                date = self.weekday_of_month(v[0], v[1], v[2])
            else:
                date = self.pasxa + datetime.timedelta(v[0])
            moving[k] = date
        return moving

    def get_secular_moving(self, m):
        moving = {}

        for k in m.keys():
            v = m[k]
            last_key = list(m.keys())[-1]

            if k == 1008:
                if calendar.isleap(self.year):
                    date = datetime.date(self.year, 2, 29)
                else:
                    date = datetime.date(self.year, 2, 28)
            elif k == 1012:
                date = self.last_day_before(v[0], v[1], v[2])
            elif k == 1014:
                if calendar.isleap(self.year):
                    date = datetime.date(self.year, 3, 28)
                else:
                    date = datetime.date(self.year, 3, 29)
            elif k in [1029, 1031]:
                if calendar.isleap(self.year):
                    date = datetime.date(self.year, 6, 20)
                else:
                    date = datetime.date(self.year, 6, 21)
            elif k == 1055:
                date = self.next_weekday(v[0], v[1], v[2])
            else:
                if len(v) > 2:
                    date = self.weekday_of_month(v[0], v[1], v[2])
                    if date.month == 2 and date.day == 1:
                        date += datetime.timedelta(1)
                    if k in [1009, 1048]:
                        for i in range(1, 7):
                            date2 = date + datetime.timedelta(i)
                            moving[last_key + i] = date2
                    if k == 1024:
                        date2 = self.weekday_of_month(v[0], v[1], v[3])
                        moving[last_key + 1] = date2
                    if k == 1042:
                        for i in range[1, 3]:
                            date2 = date + datetime.timedelta(i)
                            moving[last_key + i] = date2
                    if k == 1045:
                        date2 = date + datetime.timedelta(1)
                        moving[last_key + 1] = date2
                elif len(v) == 1:
                    date = self.pasxa + datetime.timedelta(v[0])
                else:
                    date = self.last_weekday(v[0], v[1])
            moving[k] = date

        return moving

    def last_weekday(self, day, month):
        l_day = max(week[day - 1] for week in calendar.monthcalendar(self.year, month))
        return datetime.date(self.year, month, l_day)

    def last_day_before(self, month, day, target):
        target_date = datetime.date(self.year, month, day)

        while target_date.weekday() != self.days[target]:
            target_date -= datetime.timedelta(1)

        return target_date

    def next_weekday(self, day, month, target):
        start = datetime.date(self.year, month, day)
        offset = target - start.weekday()
        if offset <= 0:
            offset += 7
        return start + datetime.timedelta(offset - 1)

    def weekday_of_month(self, number, target, month):
        m = self.monthdatescalendar(self.year, month)
        w = [day for week in m for day in week if day.weekday() == self.days[target] and day.month == month][number - 1]
        return w
