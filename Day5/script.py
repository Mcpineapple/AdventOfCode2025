#!/usr/bin/env python3


def check_in_range(id, ranges):
    for bot, top in ranges:
        if bot <= id <= top:
            return True
    return False


with open("input", "r") as file:
    text = file.read()

ids_range, ids_avail = text[:-1].split("\n\n")
ids_range = ids_range.split("\n")
ids_avail = ids_avail.split("\n")

all_valid_id_ranges = []
print("hello")

for i in ids_range:
    bot, top = i.split("-")
    all_valid_id_ranges.append((int(bot), int(top)))

print("hello")
count_avail = 0

for id in ids_avail:
    if check_in_range(int(id), all_valid_id_ranges):
        count_avail += 1

print(count_avail)
