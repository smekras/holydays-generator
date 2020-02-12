"""
author: Stergios Mekras

email: stergios.mekras@gmail.com
"""

import calendar
import datetime


class HolyCalendar(calendar.Calendar):
    def __init__(self, year):
        super().__init__(1)
        self.year = year

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

    def last_weekday(self, month, day):
        l_day = max(week[day] for week in self.monthdayscalendar(self.year, month))
        return datetime.date(self.year, month, l_day)

    def weekday_of_month(self, number, target, month):
        days = {0: calendar.SUNDAY,
                1: calendar.MONDAY,
                2: calendar.TUESDAY,
                3: calendar.WEDNESDAY,
                4: calendar.THURSDAY,
                5: calendar.FRIDAY,
                6: calendar.SATURDAY}
        m = self.monthdatescalendar(self.year, month)
        return [day for week in m for day in week if day.weekday() == days[target] and day.month == month][number - 1]
