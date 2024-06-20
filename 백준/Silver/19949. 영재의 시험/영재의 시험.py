from os import write
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    for hh in range(t):
        correct = [int(input()) for _ in range(10)]
        answer = sum((sum(i == j for i, j in zip(my_answer, correct)) >= 5 and not any(i == j == k for i, j, k in zip(my_answer, my_answer[1:], my_answer[2:])) for my_answer in product(range(1,6),repeat=10)))
        answers.append(f"{answer}")
    print(answers)