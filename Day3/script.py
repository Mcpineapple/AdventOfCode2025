#!/usr/bin/env python3

with open("input", "r") as file:
    text = file.read()
    text = text[:-1]
    text = text.split("\n")

total_voltage = 0

for bank in text:
    index_first_batt = 0
    value_first_batt = "-1"
    for battery_index in range(len(bank) - 1):
        if int(bank[battery_index]) > int(value_first_batt):
            index_first_batt = battery_index
            value_first_batt = bank[battery_index]
    value_second_batt = "-1"
    for battery_index in range(index_first_batt + 1, len(bank)):
        if int(bank[battery_index]) > int(value_second_batt):
           value_second_batt = bank[battery_index]
    total_voltage += int(value_first_batt + value_second_batt)
    print(  int(value_first_batt + value_second_batt))
print(total_voltage)
