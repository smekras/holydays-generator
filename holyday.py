"""
author: Stergios Mekras

email: stergios.mekras@gmail.com
"""

from datetime import datetime

import dicts


class Holyday:
    def __init__(self, date=datetime.now(), religious=None, namelist=None, fast=0, off=None, secular=None, moonphase=0):
        self.date = date
        self.religious = religious
        self.namelist = namelist
        self.fast = fast
        self.off = off
        self.secular = secular
        self.moonphase = moonphase

    def get_date(self):
        return int(datetime.strftime(self.date, '%Y%m%d'))

    def get_religious(self):
        holidays = []
        for rel in self.religious:
            holidays.append(dicts.holidays[rel])
        relstr = ', '.join(holidays)
        return relstr

    def get_namelist(self):
        names = []
        for name in self.namelist:
            names.append(dicts.names[name])
        namestr = ', '.join(names)
        return namestr

    def get_fast(self):
        return dicts.fasting[self.fast]

    def get_off_days(self):
        off_list = []

        if len(self.off) == 0:
            off_list.append("")
        else:
            for _ in self.off:
                off_list.append(str(_))

        off_desc = ','.join(off_list)

        return off_desc

    def get_secular(self):
        secular = []
        for sec in self.secular:
            secular.append(dicts.secular[sec])
        secstr = ', '.join(secular)

        return secstr
