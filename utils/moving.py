"""
author: Stergios Mekras

email: stergios.mekras@gmail.com
"""

import calendar
import datetime


def add_secular_moving(year):
    secular_moving = []

    leper = weekday_of_month(0, 3, 1, year)
    secular_moving.append(leper)

    safe = weekday_of_month(2, 1, 2, year)
    if safe == datetime.datetime(year, 2, 1):
        safe = weekday_of_month(2, 2, 2, year)
    secular_moving.append(safe)

    kidney = weekday_of_month(4, 2, 3, year)
    secular_moving.append(kidney)

    return secular_moving


def last_weekday(year, month, day):
    l_day = max(week[day] for week in calendar.monthcalendar(year, month))
    return datetime.date(year, month, l_day)


def next_weekday(date, day):
    offset = day - date.weekday()
    if offset <= 0:
        offset += 7
    return date + datetime.timedelta(offset)


def weekday_of_month(target, number, month, year):
    days = {0: calendar.SUNDAY,
            1: calendar.MONDAY,
            2: calendar.TUESDAY,
            3: calendar.WEDNESDAY,
            4: calendar.THURSDAY,
            5: calendar.FRIDAY,
            6: calendar.SATURDAY}
    c = calendar.Calendar(1)
    m = c.monthdatescalendar(year, month)
    return [day for week in m for day in week if day.weekday() == days[target] and day.month == month][number - 1]
