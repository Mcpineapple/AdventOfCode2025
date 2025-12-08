#!/usr/bin/env python3

with open("testinput", "r") as file:
    text = file.read()

ids_range, ids_avail = text[:-1].split("\n\n")
ids_range = ids_range.split("\n")
ids_avail = ids_avail.split("\n")

all_valid_ids = []
for i in ids_range:
    bot, top = i.split("-")
    for j in range(int(bot), int(top) + 1):
        all_valid_ids.append(j)

count_avail = 0
for id in ids_avail:
    if int(id) in all_valid_ids:
        count_avail += 1
