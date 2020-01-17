"""
Stergios Mekras

stergios.mekras@gmail.com
"""

import calendar
import datetime
from utils import easter

_ = 6

fixed_fast = {1: [0, 0, 0, 0, 4, 0, 2, _, _, _, _, _, _, _, _, 3, 3, 3, _, 3, _, 3, _, _, 3, _, 3, _, _, 3, _],
              2: [_, 2, _, _, _, _, _, 3, _, 3, 3, _, _, _, _, _, 3, _, _, _, _, _, _, 3, _, _, _, _, _, _, _],
              3: [_, _, _, _, _, _, _, _, 3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2, 3, _, _, _, _, _, _],
              4: [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3, _, 3, _, _, _, _, 3, _],
              5: [_, 3, _, _, _, _, _, 3, _, _, _, _, _, _, 3, _, _, _, _, _, 3, _, _, _, 3, _, _, _, _, _, _, _],
              6: [3, 3, _, _, _, _, _, 3, _, _, 3, _, _, _, _, _, 3, _, _, 3, _, 3, _, 2, 3, 3, 3, _, 2, 3, _],
              7: [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
              8: [4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 4, 4, 0, _, _, _, _, _, _, _, _, _, _, _, _, _, 4, _, 3],
              9: [3, _, _, _, _, 3, _, 2, 3, _, _, _, 3, 4, _, _, _, _, _, 3, _, _, 3, _, _, 3, _, _, _, _, _],
              10: [_, _, _, _, _, 3, _, _, _, _, _, _, _, _, _, _, _, 3, _, _, _, _, 3, _, _, 3, _, 4, _, _, _],
              11: [3, _, _, _, _, _, _, 3, _, _, _, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, _],
              12: [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, _, _, _, _, _, _, _]}

easter_fast = {-70: 0, -69: 0, -68: 0, -67: 0, -66: 0, -65: 0, -64: 0, -63: 0, -62: 0, -61: 0, -60: 4, -59: 0, -58: 4,
               -57: 0, -56: 0, -55: 1, -54: 1, -53: 1, -52: 1, -51: 1, -50: 1, -49: 1, -48: 4, -47: 4, -46: 4, -45: 4,
               -44: 4, -43: 3, -42: 3, -41: 4, -40: 4, -39: 4, -38: 4, -37: 4, -36: 3, -35: 3, -34: 4, -33: 4, -32: 4,
               -31: 4, -30: 4, -29: 3, -28: 3, -27: 4, -26: 4, -25: 4, -24: 4, -23: 0, -22: 3, -21: 3, -20: 4, -19: 4,
               -18: 4, -17: 4, -16: 4, -15: 3, -14: 3, -13: 4, -12: 4, -11: 4, -10: 4, -9: 4, -8: 3, -7: 2, -6: 4,
               -5: 4, -3: 4, -2: 4, -1: 4, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 14: 0, 21: 0, 24: 2, 28: 0, 35: 0,
               38: 2, 39: 0, 42: 0, 48: 0, 49: 0, 50: 0, 51: 0, 52: 0, 53: 0, 54: 0, 55: 0, 56: 0, 57: 2, 58: 2, 59: 4,
               60: 2, 61: 4, 62: 2, 63: 0, 64: 2, 65: 2, 66: 4, 67: 2, 68: 4, 69: 2, 70: 2}


def add_moving(year):
    e = easter.easter(year, 2)
    for _ in easter_fast.keys():
        target = e + datetime.timedelta(_)
        fixed_fast[target.month][target.day - 1] = easter_fast[_]


def fix_wed_fri(year):
    exception_dates = ["11-15", "11-26", "11-27", "11-28", "11-29", "12-1", "12-2", "12-3", "12-7", "12-8", "12-10",
                       "12-11", "12-13", "12-14", "12-15", "12-16", "12-18", "12-19", "12-21", "12-22", "12-23"]
    exceptions = []

    for _ in exception_dates:
        ex = datetime.datetime.strptime(str(year) + "-" + _, "%Y-%m-%d")
        exceptions.append(ex)

    to_zero = []
    e = easter.easter(year, 2)
    wed = calendar.WEDNESDAY
    fri = calendar.FRIDAY

    for _ in range((datetime.date(year, 1, 4) - datetime.date(year, 1, 1)).days):
        target = datetime.date(year, 1, 1) + datetime.timedelta(_)
        to_zero.append(target)

    for _ in range((datetime.date(year, 12, 31) - datetime.date(year, 12, 25)).days + 1):
        target = datetime.date(year, 12, 25) + datetime.timedelta(_)
        to_zero.append(target)

    for _ in range(-79, -71):
        target = e + datetime.timedelta(_)
        to_zero.append(target)

    start_date = e + datetime.timedelta(71)
    end_date = datetime.date(year, 6, 28)
    if start_date <= end_date:
        for _ in range((start_date - end_date).days + 1):
            exceptions.append(_)

    _ = datetime.datetime(year, 1, 1)
    end = datetime.datetime(year, 12, 31)
    while _ < end:
        _ += datetime.timedelta(1)

        if _ not in exceptions:
            if _.weekday() in (wed, fri):
                fixed_fast[_.month][_.day - 1] = 4

    if datetime.date(year, 8, 15) in (wed, fri):
        fixed_fast[8][14] = 2

    for _ in to_zero:
        if _.weekday() in (wed, fri):
            fixed_fast[_.month][_.day - 1] = 0


def fix_weekend(year):
    to_two = [datetime.date(year, 11, 21), datetime.date(year, 11, 22), datetime.date(year, 11, 23),
              datetime.date(year, 11, 24), datetime.date(year, 11, 26), datetime.date(year, 11, 27),
              datetime.date(year, 11, 28), datetime.date(year, 11, 29), datetime.date(year, 12, 1),
              datetime.date(year, 12, 2), datetime.date(year, 12, 3), datetime.date(year, 12, 7),
              datetime.date(year, 12, 8), datetime.date(year, 12, 10), datetime.date(year, 12, 11),
              datetime.date(year, 12, 13), datetime.date(year, 12, 14), datetime.date(year, 12, 15),
              datetime.date(year, 12, 16)]
    to_three = [datetime.date(year, 1, 5), datetime.date(year, 8, 29), datetime.date(year, 9, 14),
                datetime.date(year, 12, 24)]
    sat = calendar.SATURDAY
    sun = calendar.SUNDAY

    for _ in to_two:
        if _.weekday() in (sat, sun):
            fixed_fast[_.month][_.day - 1] = 2

    for _ in to_three:
        if _.weekday() in (sat, sun):
            fixed_fast[_.month][_.day - 1] = 3


def generate_fasts(year):
    fix_wed_fri(year)
    fix_weekend(year)
    add_moving(year)
    for i in fixed_fast.keys():
        fixed_fast[i] = [x if x != 6 else 0 for x in fixed_fast[i]]
    return fixed_fast
