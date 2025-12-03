#!/usr/bin/env python3

with open("input", "r") as file:
    text = file.read()
    text = text[:-1]
text = text.split(",")
ids = []
for two_id in text:
    begin,end = two_id.split("-")[0], two_id.split("-")[1]
    for i in range(int(begin), int(end) + 1):
        ids.append(str(i))

value = 0
for iden in ids:
    if iden[0] == '0':
        value += int(iden)
        continue
    for i in range(len(iden)):
        if (iden.count(iden[0:i]) * len(iden[0:i]) == len(iden)) :
            print(iden)
            value += int(iden)
            break
print(value)
