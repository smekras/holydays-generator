"""
author: Stergios Mekras

email: stergios.mekras@gmail.com
"""

import csv

import holycalendar as h
from dicts import months
from generators import religious_fixed as r, religious_moving as e, secular_fixed as s, secular_moving as m
from holyday import Holyday
from utils import fasting, moonphase

variant = "archaic"
holydays = []


def assemble_holidays(date, easter):
    holidays = []
    for i in r[date.month][date.day]:
        holiday = r[date.month][date.day][i]["holiday"]
        holidays.append(holiday)

    if date in easter.values():
        mov_rel = [key for key, value in easter.items() if value == date]
        for _ in mov_rel:
            holidays.append(_)
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

    return set(names)


def assemble_secular(date, moving):
    secular = []
    if date.day in s[date.month].keys():
        for i in s[date.month][date.day]["holiday"]:
            secular.append(i)

    if date in moving.values():
        mov_sec = [key for key, value in moving.items() if value == date]
        for _ in mov_sec:
            secular.append(_)

    return secular


def main():
    y = int(input("Year: "))
    cal = h.HolyCalendar(y)
    days = cal.get_all_days()
    fasts = fasting.generate_fasts(y)
    moving = cal.get_secular_moving(m)
    easter = cal.get_religious_moving(e)

    for i in days:
        if i.month > 2 or (i.month == 2 and i.day > 10):
            religious = [0]
            names = [0]
            secular = [0]
        else:
            religious = assemble_holidays(i, easter)
            names = assemble_names(i)
            secular = assemble_secular(i, moving)

        phase, name, pos = moonphase.get_info(i)
        fast = fasts[i.month][i.day - 1]
        holydays.append(Holyday(i, religious, names, fast, secular, phase))

    with open("files/%s.csv" % y, "w+") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in holydays:
            date = i.get_date()
            day = str(date)[-2:]
            if day == "01":
                full_date = str(date)[:-2] + "00"
                index = int(str(date)[4:6])
                month = months[index]["name"]
                link = months[index]["link"]
                csv_writer.writerow([full_date, month, "", "", "", "", "", link])
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
