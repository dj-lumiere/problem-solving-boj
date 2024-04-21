import os
import re
from collections import Counter
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
    MOD = 10 ** 9 + 7
    for h in range(t):
        n = int(input())
        y_size1, x_size1 = int(input()), int(input())
        matrix1 = [[int(input()) for _ in range(x_size1)] for _ in range(y_size1)]
        can_be_multiplied = True
        for _ in range(n - 1):
            y_size2, x_size2 = int(input()), int(input())
            matrix2 = [[int(input()) for _ in range(x_size2)] for _ in range(y_size2)]
            eprint(matrix2)
            if x_size1 != y_size2:
                can_be_multiplied = False
                break
            new_matrix = [[0 for _ in range(x_size2)] for _ in range(y_size1)]
            for i in range(y_size1):
                for j in range(x_size2):
                    for k in range(x_size1):
                        new_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
                        new_matrix[i][j] %= MOD
            matrix1 = new_matrix
            y_size1, x_size1 = y_size1, x_size2
        if can_be_multiplied:
            answer = sum(sum(j for j in i) for i in matrix1) % MOD
        else:
            answer = -1
        answers[h] = f"{answer}"
    print(answers)