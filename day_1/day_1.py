# https://adventofcode.com/2020/day/1
from collections import OrderedDict
from functools import reduce

target = 2020


def file_lines_as_int_list(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return [int(line.rstrip("\n")) for line in file]


expense_report = file_lines_as_int_list("day_1_input.txt")
supplements = OrderedDict(((target - x, i) for i, x in enumerate(expense_report)))


def find_two():
    for i, el in enumerate(expense_report):
        if el in supplements and supplements[el] != i:
            return el, expense_report[supplements[el]]


def find_three():
    for i, el in enumerate(expense_report):
        s = set()
        curr_sum = target - el
        for j in range(i + 1, len(expense_report)):
            if curr_sum - expense_report[j] in s:
                return el, expense_report[j], curr_sum - expense_report[j]
            s.add(expense_report[j])


two = find_two()
print(f"two: {two}; multiplied: {reduce((lambda x, y: x * y), two)}")
three = find_three()
print(f"two: {three}; multiplied: {reduce((lambda x, y: x * y), three)}")
