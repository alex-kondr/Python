import re


def generator_numbers(string=""):
    split_str = string.split()

    for item in split_str:
        temp = re.search(r"\d+", item)
        yield int(temp.group()) if temp else 0


def sum_profit(string):

    sum = 0

    for number in generator_numbers(string):
        sum += number

    return sum

"a".normalize()
