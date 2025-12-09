#!/usr/bin/env python3
import math

with open("input") as file:
    text = file.readlines()


ops = text[-1].split()

tot = 0
op_num = 0
nums = []
for col in range(len(text[0])):
    num = ""

    for line in range(len(text) - 1):
        if text[line][col].isdigit():
            num += text[line][col]

    if col == len(text[0]) - 1:
        if num.isnumeric():
            nums.append(int(num))
        num = ""
    if num == "":
        if ops[op_num] == "*":
            tot += math.prod(nums)
        else:
            tot += sum(nums)
        nums = []
        op_num += 1
    else:
        nums.append(int(num))
print("result : ", tot)
