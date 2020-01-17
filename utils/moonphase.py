"""
moonphase.py - Calculate Lunar Phase
Author: Sean B. Palmer, inamidst.com
Cf. http://en.wikipedia.org/wiki/Lunar_phase#Lunar_phase_calculation
"""

import datetime
import decimal
import math
from dicts import phases

dec = decimal.Decimal


def position(day=None):
    if day is None:
        day = datetime.datetime.now()
    else:
        day = datetime.datetime.combine(day, datetime.datetime.min.time())
    diff = day - datetime.datetime(2001, 1, 1)
    days = dec(diff.days) + (dec(diff.seconds) / dec(86400))
    lunations = dec("0.20439731") + (days * dec("0.03386319269"))

    return lunations % dec(1)


def get_phase(pos):
    index = (pos * dec(8)) + dec("0.5")
    index = math.floor(index)
    return index & 7, phases[index & 7]


def get_info(date):
    pos = position(date)
    phase, name = get_phase(pos)
    roundedpos = round(float(pos), 3)
    return phase, name, roundedpos
