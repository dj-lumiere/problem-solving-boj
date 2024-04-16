import os
from itertools import product

# with open(0, 'rb') as f:
with (open(0, 'rb') as f):
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    for h in range(t):
        a = [int(input()) for _ in range(4)]
        b = [int(input()) for _ in range(4)]
        found_answer = False
        for c in product(range(1, 11), repeat=4):
            a_vs_b = sum(i > j for i, j in product(a, b)) > sum(i < j for i, j in product(a, b))
            b_vs_a = sum(i > j for i, j in product(a, b)) < sum(i < j for i, j in product(a, b))
            b_vs_c = sum(i > j for i, j in product(b, c)) > sum(i < j for i, j in product(b, c))
            c_vs_b = sum(i > j for i, j in product(b, c)) < sum(i < j for i, j in product(b, c))
            c_vs_a = sum(i > j for i, j in product(c, a)) > sum(i < j for i, j in product(c, a))
            a_vs_c = sum(i > j for i, j in product(c, a)) < sum(i < j for i, j in product(c, a))
            if (a_vs_b and b_vs_c and c_vs_a) or (a_vs_c and c_vs_b and b_vs_a) or (b_vs_a and a_vs_c and c_vs_b) or (
                    b_vs_c and c_vs_a and a_vs_b) or (c_vs_a and a_vs_b and b_vs_c) or (c_vs_b and b_vs_a and a_vs_c):
                found_answer = True
                break
        answer = "yes" if found_answer else "no"
        answers[h] = f"{answer}"
    print(answers)