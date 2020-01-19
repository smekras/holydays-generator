"""
Stergios Mekras

stergios.mekras@gmail.com
"""
import calendar

import holycalendar


year = int(input("year: "))

cal = holycalendar.HolyCalendar(year)


def get_all_days(year):
    days = []
    for line in cal.yeardatescalendar(year):
        for month in line:
            for week in month:
                for date in week:
                    if date.year == year:
                        days.append(date)
    return days


holidays = get_all_days(year)
for _ in holidays:
    print(_, _.weekday())

_ = 6
fast = {1: [0, 0, 0, 0, 5, 0, 2, _, _, _, _, _, _, _, _, 3, 3, 3, _, 3, _, 3, _, _, 3, _, 3, _, _, 3, _, _],
        2: [_, 2, _, _, _, _, _, 3, _, 3, 3, _, _, _, _, _, 3, _, _, _, _, _, _, 3, _, _, _, _, _, _],
        3: [_, _, _, _, _, _, _, _, 3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2, 3, _, _, _, _, _, _],
        4: [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3, _, 3, _, _, _, _, 3, _],
        5: [_, 3, _, _, _, _, _, 3, _, _, _, _, _, _, 3, _, _, _, _, _, 3, _, _, _, 3, _, _, _, _, _, _, _],
        6: [3, 3, _, _, _, _, _, 3, _, _, 3, _, _, _, _, _, 3, _, _, 3, _, 3, _, 2, 3, 3, 3, _, 2, 3, _],
        7: [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
        8: [4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 4, 4, 0, _, _, _, _, _, _, _, _, _, _, _, _, _, 5, _, 3, _],
        9: [3, _, _, _, _, 3, _, 2, 3, _, _, _, 3, 5, _, _, _, _, _, 3, _, _, 3, _, _, 3, _, _, _, _, _],
        10: [_, _, _, _, _, 3, _, _, _, _, _, _, _, _, _, _, _, 3, _, _, _, _, 3, _, _, 3, _, 4, _, _, _, _],
        11: [3, _, _, _, _, _, _, 3, _, _, _, 3, 3, 2, 3, _, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, _],
        12: [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, _, _, _, _, _, _, _, _]}

for h in holidays:
    if h.weekday() == calendar.TUESDAY:
        pass
        # print(h, fast[h.month][h.day])