"""
author: Stergios Mekras

email: stergios.mekras@gmail.com
"""

from calendar import Calendar


class HolyCalendar(Calendar):
    def __init__(self, year):
        super().__init__()
        self.year = year

    def get_all_days(self):
        days = []
        for line in self.yeardatescalendar(self.year):
            for month in line:
                for week in month:
                    for date in week:
                        if date.year == self.year:
                            days.append(date)
        return days
