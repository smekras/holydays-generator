import dicts
from datetime import datetime


class Holyday:
    def __init__(self, date=datetime.now(), religious=None, namelist=None, fast=0, secular=None, moonphase=0):
        self.date = date
        self.religious = religious
        self.namelist = namelist
        self.fast = fast
        self.secular = secular
        self.moonphase = moonphase

    def get_date(self):
        return datetime.strftime(self.date, '%Y-%m-%d')

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

    def get_secular(self):
        secular = []
        for sec in self.secular:
            secular.append(dicts.secular[sec])
        secstr = ', '.join(secular)
        return secstr
