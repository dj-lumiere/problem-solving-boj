from math import pi
from string import ascii_uppercase
from sys import stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split("\n"))
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = int(input())
    answers = []
    letter_position = {v: i for i, v in enumerate(ascii_uppercase)}
    letter_position[" "] = 26
    letter_position["'"] = 27
    circumference = 60 * pi
    for hh in range(t):
        letters = list(map(lambda x: letter_position[x], input()))
        eprint(letters)
        letter_left = [j - i for i, j in zip(letters, letters[1:])]
        for i, v in enumerate(letter_left):
            if v < 0:
                letter_left[i] += 28
        letter_right = [i - j for i, j in zip(letters, letters[1:])]
        for i, v in enumerate(letter_right):
            if v < 0:
                letter_right[i] += 28
        distance = 0
        for i, j in zip(letter_left, letter_right):
            distance += min(i, j) * circumference / 28
        answer = distance / 15 + len(letters)
        answers.append(f"{answer}")
    print(*answers, sep="\n")
