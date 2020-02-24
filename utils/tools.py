from dicts import holidays as h

temp = {}

for key, value in h.items():
    temp.setdefault(value, set()).add(key)

[print(key) for key, values in temp.items() if len(values) > 1]
