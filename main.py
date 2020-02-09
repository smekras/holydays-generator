"""
author: Stergios Mekras

email: stergios.mekras@gmail.com
"""

import csv

import holycalendar
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

    for i in r[date.month][date.day]:
        name = r[date.month][date.day][i]["names_secondary"]
        for _ in name:
            names.append(_)

    if not names:
        for i in r[date.month][date.day]:
            name = r[date.month][date.day][i]["names_unofficial"]
            for _ in name:
                names.append(_)

    return names


def assemble_secular(date):
    secular = []
    if date.day in s[date.month].keys():
        for i in s[date.month][date.day]["holiday"]:
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

    with open("files/%s.csv" % y, "w+") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in holydays:
            date = i.get_date()
            rel = i.get_religious()
            names = i.get_namelist()
            gap = ""
            sec = i.get_secular()
            fast = i.fast  # fast = f[i.fast][variant]
            moon = i.moonphase  # moon = p[i.moonphase][variant]
            link = s[i.date.month][i.date.day]["link"]
            csv_writer.writerow([date, rel, names, gap, sec, fast, moon, link])


if __name__ == '__main__':
    main()
