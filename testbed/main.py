import csv
from holyday import HolyDay, Secular

h1 = HolyDay(2, [1], [2, 3], 0)
h2 = HolyDay(1, [0], [0], 1)
h3 = HolyDay(0, [2], [1], 2)

s1 = Secular(1, [2], 2)
s2 = Secular(0, [1], 0)
s3 = Secular(2, [0], 1)

holidays = [h1, h2, h3]
days = [s1, s2, s3]

with open("holydays.csv", "w+") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    for h in holidays:
        for i in range(len(days)):
            if h.date == days[i].date:
                date = h.get_date()
                rel = h.get_religious()
                names = h.get_namelist()
                sec = days[i].get_secular()
                fast = h.get_fast()
                moon = days[i].get_moonphase()

                csv_writer.writerow([date, rel, names, sec, fast, moon])

with open("holydays.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(' '.join(row))
