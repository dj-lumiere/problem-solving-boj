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
    for h in range(t):
        n = int(input())
        correct_answer = input().decode()
        adrian_pattern = ["A", "B", "C"] * 34
        bruno_pattern = ["B", "A", "B", "C"] * 25
        goran_pattern = ["C", "C", "A", "A", "B", "B"] * 17
        adrian_score = sum(i == j for i, j in zip(correct_answer, adrian_pattern))
        bruno_score = sum(i == j for i, j in zip(correct_answer, bruno_pattern))
        goran_score = sum(i == j for i, j in zip(correct_answer, goran_pattern))
        max_score = max(adrian_score, bruno_score, goran_score)
        max_scorer = []
        if adrian_score == max_score:
            max_scorer.append("Adrian")
        if bruno_score == max_score:
            max_scorer.append("Bruno")
        if goran_score == max_score:
            max_scorer.append("Goran")
        answer = f"{max_score}\n" + "\n".join(max_scorer)
        answers[h] = answer
    print(answers)