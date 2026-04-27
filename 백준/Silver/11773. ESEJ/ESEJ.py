import os
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
        a, b = int(input()), int(input())
        possible_letters = "abcdefghijklmno"
        word_list = ["".join(i) for i in product(possible_letters, repeat=2)] + ["".join(i) for i in
                                                                                 product(possible_letters, repeat=1)] + [
                        "".join(i) for i in product(possible_letters, repeat=3)] + ["".join(i) for i in
                                                                                    product(possible_letters, repeat=4)] + [
                        "".join(i) for i in product(possible_letters, repeat=5)]
        answer = " ".join(word_list[:b])
        answers[h] = f"{answer}"
    print(answers)