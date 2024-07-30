from sys import stdin
from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta

getcontext().prec = 1000

class Trie:
    """https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/Trie.py"""

    def __init__(self, *words):
        self.root = {}
        for word in words:
            self.add(word)

    def add(self, word):
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict["_"] = True

    def __contains__(self, word):
        current_dict = self.root
        for letter in word:
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        return True

    def __delitem__(self, word):
        current_dict = self.root
        nodes = [current_dict]
        for letter in word:
            current_dict = current_dict[letter]
            nodes.append(current_dict)
        del current_dict["_"]
        for i, (v, node) in enumerate(zip(reversed(word), reversed(nodes[:-1]))):
            if not node[v]:
                del node[v]

    def __str__(self, current_dict=None, level=0):
        if current_dict is None:
            current_dict = self.root

        indent = " " * (level + 1) * 2
        child_repr = ""
        if current_dict:
            for i, (key, child) in enumerate(sorted(current_dict.items())):
                if key == "_":
                    continue
                child_repr += (f"{indent}child{level + 1}={key}{self.__str__(child, level + 1) if child else chr(10)}")
        else:
            child_repr = f""

        if level == 0:
            return f"root\n{child_repr}"
        else:
            return f"\n{child_repr}"

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="": write(1, (sep.join(map(str, args)) + end).encode())
    eprint = lambda *args, sep=" ", end="\n": write(2, (sep.join(map(str, args)) + end).encode())
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    for hh in range(t):
        n = int(input())
        m = int(input())
        words = [input().decode() for _ in range(n)]
        find = [input().decode() for _ in range(m)]
        answer = 0
        my_trie = Trie(*words)
        for word in find:
            if word in my_trie:
                answer += 1
        answers.append(f"{answer}")
    print(*answers)
