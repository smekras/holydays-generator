"""
author: Stergios Mekras

email: stergios.mekras@gmail.com
"""

import holycalendar
from dicts import fasting as f, phases as p
from generators import religious_fixed as r, secular_fixed as s
from holyday import Holyday
from utils import moonphase, fasting

variant = "archaic"
holydays = []


def assemble_holidays(date):
    holidays = []
    for i in r[date.month][date.day]:
        holiday = r[date.month][date.day][i]["holiday"]
        holidays.append(holiday)

    return holidays


def assemble_names(date):
    names = []
    for i in r[date.month][date.day]:
        name = r[date.month][date.day][i]["names_primary"]
        for _ in name:
            names.append(_)
        name = r[date.month][date.day][i]["names_secondary"]
        for _ in name:
            names.append(_)

    return names


def assemble_secular(date):
    secular = []
    if date.day in s[date.month].keys():
        for i in s[date.month][date.day]:
            secular.append(i)

    return secular


def main():
    y = int(input("Year: "))
    cal = holycalendar.HolyCalendar(y)
    days = cal.get_all_days()
    fasts = fasting.generate_fasts(y)

    for i in days:
        if i.month < 2 and i.day < 32:
            religious = assemble_holidays(i)
            names = assemble_names(i)
            secular = assemble_secular(i)
        else:
            religious = [0]
            names = [0]
            secular = [0]
        phase, name, pos = moonphase.get_info(i)
        fast = fasts[i.month][i.day - 1]
        holydays.append(Holyday(i, religious, names, fast, secular, phase))

    for i in holydays:
        print(i.date, i.get_religious(), i.get_namelist(), f[i.fast][variant], i.get_secular(), p[i.moonphase][variant],
              sep=", ")


if __name__ == '__main__':
    main()
