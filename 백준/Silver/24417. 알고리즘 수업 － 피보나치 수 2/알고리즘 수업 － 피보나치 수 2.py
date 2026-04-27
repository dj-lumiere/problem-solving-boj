import os
from collections import Counter, deque
from itertools import product
from array import array
from functools import reduce

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    matrix = [[1, 1], [1, 0]]
    for h in range(t):
        n = int(input())
        matrix_pow_n = [[1, 0], [0, 1]]
        matrix_pow_2 = [[1, 1], [1, 0]]
        for i in range(n.bit_length()):
            if n & (1 << i) != 0:
                new_matrix = [[0, 0], [0, 0]]
                for i in range(2):
                    for j in range(2):
                        for k in range(2):
                            new_matrix[i][j] += matrix_pow_n[i][k] * matrix_pow_2[k][j]
                        new_matrix[i][j] %= 10 ** 9 + 7
                matrix_pow_n = new_matrix
            new_matrix = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        new_matrix[i][j] += matrix_pow_2[i][k] * matrix_pow_2[k][j]
                        new_matrix[i][j] %= 10 ** 9 + 7
            matrix_pow_2 = new_matrix
        answer = f"{matrix_pow_n[1][0]} {n - 2}"
        answers[h] = f"{answer}"
    print(answers)