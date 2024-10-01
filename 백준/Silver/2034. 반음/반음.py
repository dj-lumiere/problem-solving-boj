from collections import deque
from itertools import product
from sys import stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(1, t + 1):
        notes = ['A', "_", 'B', 'C', "_", 'D', "_", 'E', 'F', "_", 'G', "_", ]
        n = int(input())
        steps = [int(input()) for _ in range(n)]
        for index, start_note in enumerate(notes):
            if start_note == "_":
                continue
            current_note_index = index
            valid = True
            for step in steps:
                next_note_index = (current_note_index + step) % 12
                current_note_index = next_note_index
                if notes[next_note_index] == "_":
                    valid = False
                    break
            if valid:
                answers.append(f"{start_note} {notes[current_note_index]}")
    print(*answers, sep="\n")