#!/usr/bin/env python3

with open("input", "r") as file:
    text = file.read()
    text = text.split("\n")

text = text[:-1]
dial = [0]
index = 50


for i in range(99):
    dial += [dial[-1] + 1]
count = 0

for shift in text :
    for i in range(int(shift[1:])):
        if shift[0] == 'R':
            index += 1
        if shift[0] == 'L':
            index -= 1
        if index == -1:
            index = 99
        if index == 100:
            index = 0

        if dial[index] == 0:
            count += 1
