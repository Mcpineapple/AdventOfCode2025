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

ids_range.sort()
for i in ids_range:
    bot, top = i.split("-")
    bot = int(bot)
    top = int(top)

    add = True
    for j in all_valid_id_ranges:
        if bot in range(j[0], j[1] + 1) and top in range(j[0], j[1] + 1):
            add = False
        elif bot in range(j[0], j[1] + 1):
            j[1] = top
            add = False
        elif top in range(j[0], j[1] + 1):
            j[0] = bot
            add = False
    if add:
        all_valid_id_ranges.append([bot, top])


while True:
    all_valid_id_ranges_2 = []
    for i in all_valid_id_ranges:
        bot = i[0]
        top = i[1]

        add = True
        for j in all_valid_id_ranges_2:
            if bot == j[0] and top == j[1]:
                continue
            if bot in range(j[0], j[1] + 1) and top in range(j[0], j[1] + 1):
                add = False
            elif bot in range(j[0], j[1] + 1):
                j[1] = top
                add = False
            elif top in range(j[0], j[1] + 1):
                j[0] = bot
                add = False
        if add:
            all_valid_id_ranges_2.append([bot, top])
    if len(all_valid_id_ranges) == len(all_valid_id_ranges_2):
        break
    else:
        all_valid_id_ranges = all_valid_id_ranges_2


def func(x):
    return x[1] - x[0] + 1


summed = map(func, all_valid_id_ranges)
print(sum(summed))


# for id in ids_avail:
#     if check_in_range(int(id), all_valid_id_ranges):
#         count_avail += 1

# print(count_avail)
