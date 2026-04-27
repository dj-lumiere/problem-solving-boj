import os
from collections import Counter
from itertools import combinations, permutations, product
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
    for h in range(t):
        n, k = int(input()), int(input())
        changes = [[int(input()), input().decode()] for _ in range(k)]
        result = ["?" for _ in range(n)]
        current_position = 0
        no_answer = False
        for i, j in changes:
            current_position -= i
            current_position %= n
            if result[current_position] == "?" or result[current_position] == j:
                result[current_position] = j
            else:
                no_answer = True
                break
        letter_count = Counter(result)
        for letter, count in letter_count.items():
            if letter != "?" and count > 1:
                no_answer = True
        result = result[current_position:] + result[:current_position]
        answer = "".join(result) if not no_answer else "!"
        answers[h] = f"{answer}"
    print(answers)