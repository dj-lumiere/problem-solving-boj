import os
import re
from collections import Counter

with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    for i in range(t):
        a1 = int(input())
        a1_patterns = [int(input()) for _ in range(a1)]
        a1_counter = Counter(a1_patterns)
        b1 = int(input())
        b1_patterns = [int(input()) for _ in range(b1)]
        b1_counter = Counter(b1_patterns)
        winner = ""
        if a1_counter[4] != b1_counter[4]:
            winner = "A" if a1_counter[4]>b1_counter[4] else "B"
        elif a1_counter[3] != b1_counter[3]:
            winner = "A" if a1_counter[3] > b1_counter[3] else "B"
        elif a1_counter[2] != b1_counter[2]:
            winner = "A" if a1_counter[2] > b1_counter[2] else "B"
        elif a1_counter[1] != b1_counter[1]:
            winner = "A" if a1_counter[1] > b1_counter[1] else "B"
        else:
            winner = "D"
        answers[i] = winner
    print(answers)