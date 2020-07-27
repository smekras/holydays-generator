import csv
import json
from dicts import holidays as h

temp = {}


def check_doubles():
    for key, value in h.items():
        temp.setdefault(value, set()).add(key)

    [print(key) for key, values in temp.items() if len(values) > 1]


def csv_to_json(csv_file, json_file):
    data = []

    with open(csv_file) as f:
        for row in csv.DictReader(f):
            data.append(row)

    json_data = json.dumps(data)

    with open(json_file, "w+") as f:
        f.write(json_data)
    # json.dump(json_data, json_file)


csv_to_json('../files/2020.csv', '../files/2020.json')
