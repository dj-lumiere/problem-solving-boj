from collections import deque, Counter
from itertools import product, chain, permutations, combinations
from string import ascii_lowercase
from sys import stdout, stderr
from time import perf_counter
from decimal import Decimal

digit_leds = [
    "### #.# #.# #.# ###",
    "..# ..# ..# ..# ..#",
    "### ..# ### #.. ###",
    "### ..# ### ..# ###",
    "#.# #.# ### ..# ..#",
    "### #.. ### ..# ###",
    "### #.. ### #.# ###",
    "### ..# ..# ..# ..#",
    "### #.# ### #.# ###",
    "### #.# ### ..# ###"
]


def match_digit(broken_led, led_digit):
    for bl, ld in zip(broken_led, led_digit):
        if bl == '#' and ld == '.':
            return False
    return True


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
    for hh in range(1, t + 1):
        led_lines = [[input() for _ in range(4)] for _ in range(5)]
        possible_digits = []
        for i in range(4):
            broken_digit = [led_lines[j][i] for j in range(5)]
            broken_digit_str = ' '.join(broken_digit)
            possible_digits.append([d for d in range(10) if match_digit(broken_digit_str, digit_leds[d])])
        answer = ""
        for h1, h2, m1, m2 in product(*possible_digits):
            if h1 * 10 + h2 < 24 and m1 * 10 + m2 < 60:
                answer = f"{h1}{h2}:{m1}{m2}"
                break
        answers.append(f"{answer}")
    print(*answers, sep="\n")
