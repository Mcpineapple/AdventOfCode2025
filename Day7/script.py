#!/usr/bin/env python3

with open("input") as file:
    text = file.read().splitlines()

col_set = set()
col_set.add(text[0].find("S"))
splits = 0
for i in range(1, len(text)):
    col_set_2 = set()
    for rayon in col_set:
        if text[i][rayon] == "^":
            splits += 1

            col_set_2.add(rayon - 1)
            col_set_2.add(rayon + 1)
        else:
            col_set_2.add(rayon)
    col_set = col_set_2
