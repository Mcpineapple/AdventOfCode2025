#!/usr/bin/env python3


with open("input") as file:
    text = file.read()[:-1]
text = text.split("\n")
for i in range(len(text)):
    text[i] = text[i].split()
for i in text:
    for j in range(len(i)):
        if i[j].isnumeric():
            i[j] = int(i[j])
        else:
            i[j] = i[j].strip()


total = 0
for j in range(len(text[0])):
    if text[len(text) - 1][j] == "*":
        func = lambda x, y: x * y
        current = 1
    else:
        func = lambda x, y: x + y
        current = 0
    for i in range(len(text) - 2, -1, -1):
        current = func(current, text[i][j])
    total += current

print("tot")
print(total)
