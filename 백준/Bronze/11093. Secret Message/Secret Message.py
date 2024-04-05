import os
from itertools import permutations
from fractions import Fraction
from math import ceil

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    for a in range(t):
        word = input().decode()
        next_square = ceil(len(word)**.5)
        word += "*" * (next_square**2-len(word))
        word_grid = [[word[i*next_square+j] for j in range(next_square)] for i in range(next_square)]
        word_grid_rotate = [[word_grid[next_square-j-1][i] for j in range(next_square)] for i in range(next_square)]
        crypted_word = []
        for i1 in range(next_square):
            for i2 in range(next_square):
                if word_grid_rotate[i1][i2] == "*":
                    continue
                crypted_word.append(word_grid_rotate[i1][i2])
        answers[a] = "".join(crypted_word)
    print(answers)