from decimal import getcontext
from itertools import product
from math import floor, log10
from sys import stdout, stderr

getcontext().prec = 1000


class MapIndex:
    def __init__(self, function, iterable):
        self.function = function
        self.iterable = iterable

    def __len__(self):
        return len(self.iterable)

    def __getitem__(self, key):
        return self.function(self.iterable[key])


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    english_number = ["" for _ in range(1000)]
    one_to_nine = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    ten_to_nineteen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                       "nineteen"]
    twenty_to_ninety = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hundreds = ["", "onehundred", "twohundred", "threehundred", "fourhundred", "fivehundred", "sixhundred",
                "sevenhundred", "eighthundred", "ninehundred"]
    for i in range(1000):
        if i == 0:
            continue
        hundred_digit, ten_digit, one_digit = i // 100, i // 10 % 10, i // 1 % 10
        english = hundreds[hundred_digit]
        if ten_digit == 1:
            english += ten_to_nineteen[one_digit]
        else:
            english += twenty_to_ninety[ten_digit] + one_to_nine[one_digit]
        english_number[i] = english
    for hh in range(t):
        n = int(input())
        words = [input() for _ in range(n)]
        letter_count = sum(len(v) for v in words) - 1
        for i, v in enumerate(english_number):
            if i == 0:
                continue
            if len(v) + letter_count == i:
                words[words.index("$")] = v
                break
        answer = " ".join(words)
        answers.append(f"{answer}")
    print(*answers, sep="\n")