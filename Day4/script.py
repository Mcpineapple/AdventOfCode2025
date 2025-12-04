#!/usr/bin/env python3

with open("input", "r") as file:
    text = file.read()
    text = text.split("\n")
    text = text[:-1]

count_table = [[0 for j in range(len(text[0]))] for i in range(len(text))]
text.insert(0, "."*len(text[0]))
text.append("."*len(text[0]))
for i in range(len(text)):
    text[i] = "." + text[i] + "."


def conver(char):
    return 1 if char[0] == "@" else 0

for i in range(len(count_table)):
    for j in range(len(count_table[i])):
        if text[i + 1][j + 1] == "@":
            count_table[i][j] += conver([text[i+2][j+1]])
            count_table[i][j] += conver([text[i+2][j]])
            count_table[i][j] += conver([text[i+2][j+2]])

            count_table[i][j] += conver([text[i+1][j]])
            count_table[i][j] += conver([text[i+1][j+2]])

            count_table[i][j] += conver([text[i][j+2]])
            count_table[i][j] += conver([text[i][j+1]])
            count_table[i][j] += conver([text[i][j]])

count_rolls = 0

for i in range(len(count_table)):
    for j in range(len(count_table[i])):
        if text[i+1][j+1] == "@" and count_table[i][j] < 4:
            count_rolls += 1
for i in count_table:
    print(i)
