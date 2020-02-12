"""
author: Stergios Mekras

email: stergios.mekras@gmail.com
"""

import datetime


class Moving:
    def __init__(self, date, secular):
        self.date = date
        self.secular = secular

    def get_date(self):
        return self.date

    def get_secular(self):
        return self.secular


def add_secular_moving(year):
    secular_moving = []

    leper_date = weekday_of_month(0, 3, 1, year)
    leper = Moving(leper_date, 2)
    secular_moving.append(leper)

    safe_date = weekday_of_month(2, 1, 2, year)
    if safe_date == datetime.datetime(year, 2, 1):
        safe_date = weekday_of_month(2, 2, 2, year)
    safe = Moving(safe_date, 8)
    secular_moving.append(safe)

    kidney_date = weekday_of_month(4, 2, 3, year)
    kidney = Moving(kidney_date, 8)
    secular_moving.append(kidney)

    cannabis_date = weekday_of_month(6, 1, 5, year)
    cannabis = Moving(cannabis_date, 9)
    secular_moving.append(cannabis)

    laughter_date = weekday_of_month(0, 1, 5, year)
    laughter = Moving(laughter_date, 10)
    secular_moving.append(laughter)

    mother_date = weekday_of_month(0, 2, 5, year)
    mother = Moving(mother_date, 11)
    secular_moving.append(mother)

    father_date = weekday_of_month(0, 3, 6, year)
    father = Moving(father_date, 12)
    secular_moving.append(father)

    coop_date = weekday_of_month(0, 1, 7, year)
    coop = Moving(coop_date, 13)
    secular_moving.append(coop)

    admin_date = last_weekday(year, 6, 5)
    admin = Moving(admin_date, 14)
    secular_moving.append(admin)

    beer_date = weekday_of_month(5, 1, 8, year)
    beer = Moving(beer_date, 15)
    secular_moving.append(beer)

    coast_date = weekday_of_month(6, 3, 9, year)
    coast = Moving(coast_date, 16)
    secular_moving.append(coast)

    heart_date = last_weekday(year, 9, 0)
    heart = Moving(heart_date, 17)
    secular_moving.append(heart)

    birds1_date = weekday_of_month(6, 1, 10, year)
    birds2_date = next_weekday(birds1_date, 0)
    birds1 = Moving(birds1_date, 18)
    birds2 = Moving(birds2_date, 18)
    secular_moving.append(birds1)
    secular_moving.append(birds2)

    home_date = weekday_of_month(1, 1, 10, year)
    home = Moving(home_date, 19)
    secular_moving.append(home)

    architecture_date = weekday_of_month(1, 1, 10, year)
    architecture = Moving(architecture_date, 20)
    secular_moving.append(architecture)

    vision_date = weekday_of_month(4, 2, 10, year)
    vision = Moving(vision_date, 21)
    secular_moving.append(vision)

    eggs_date = weekday_of_month(5, 2, 10, year)
    eggs = Moving(eggs_date, 22)
    secular_moving.append(eggs)

    host_date = weekday_of_month(6, 2, 10, year)
    host = Moving(host_date, 23)
    secular_moving.append(host)

    expression_date = last_weekday(year, 10, 6)
    expression = Moving(expression_date, 24)
    secular_moving.append(expression)

    philosophy_date = weekday_of_month(4, 3, 11, year)
    philosophy = Moving(philosophy_date, 25)
    secular_moving.append(philosophy)

    crashes_date = weekday_of_month(0, 3, 11, year)
    crashes = Moving(crashes_date, 26)
    secular_moving.append(crashes)

    boycott_date = weekday_of_month(5, 4, 11, year)
    boycott = Moving(boycott_date, 27)
    secular_moving.append(boycott)

    return secular_moving
