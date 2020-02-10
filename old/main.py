"""
Stergios Mekras

stergios.mekras@gmail.com
"""

import csv
import datetime

from utils.easter import easter


def main():
    year = int(input("Year: "))
    m = calculate_moving(year)
    [print(date) for date in m]
    c = next_weekday(datetime.datetime.now(), 6)
    print("next Saturday is:", c.strftime("%Y-%m-%d"))
    l_day = last_weekday(year, 12, 1)
    print("last Saturday is:", l_day)
    x = weekday_of_month(0, 3, 1, year)
    print("3rd Sunday of January: ", x)
    holiday_list = [[x.strftime("%Y-%m-%d"), "Saint Whatever", "All Names", "Something stupid", 4, 6, "nada"],
                    [l_day.strftime("%Y-%m-%d"), "Another Saint", "Another name", "Another bullshit", 3, 5, "no link"]]
    write_csv("2019.csv", holiday_list)


def calculate_moving(year):
    moving = []
    offsets = [-70, -63, -59, -57, -56, -49, -48, -43, -42, -35. - 8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6,
               7, 14, 21, 39, 48, 49, 50, 56]
    e = easter(year, 2)
    for offset in offsets:
        date = e + datetime.timedelta(offset)
        moving.append(date)
    return moving


def write_csv(filename, final_list):
    with open(filename, 'w') as csv_file:
        fields = ["Date", "Religious Holidays", "Names", "Secular Holidays", "Fasting", "Moon Phase", "Info"]
        writer = csv.DictWriter(csv_file, fields)
        # writer.writeheader()
        for entry in final_list:
            writer.writerow({fields[0]: entry[0],
                             fields[1]: entry[1],
                             fields[2]: entry[2],
                             fields[3]: entry[3],
                             fields[4]: entry[4],
                             fields[5]: entry[5],
                             fields[6]: entry[6]})
        print(final_list)


main()
