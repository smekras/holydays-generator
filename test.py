import dicts
from utils import fasting


def populate_holiday(year):
    for day in fasting.fixed_fast[1]:
        print(dicts.fasting[day][1])


y = int(input("Enter year: "))

fasting.generate_fasts(y)
populate_holiday(y)
