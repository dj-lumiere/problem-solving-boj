from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit, stdout, stderr
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import cos, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
from heapq import heapify, heappush, heappop
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
        self.root = {"_": 0}
        for word in words:
            self.add(*word)

    def add(self, *letters):
        current = self.root
        self.root["_"] += 1
        for i in letters:
            if i not in current:
                current[i] = {"_": 0}
            current[i]["_"] += 1
            current = current[i]

    def __contains__(self, word):
        current_dict = self.root
        for letter in word:
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        return "_" in current_dict

    def prefix_count(self, word):
        current_dict = self.root
        for letter in word:
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        if "_" not in current_dict:
            return 0
        return current_dict["_"]

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

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = int(input())
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        words = [input() for _ in range(n)]
        my_trie = Trie(*words)
        answer = "NO" if any(my_trie.prefix_count(word)!= 1 for word in words) else "YES"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
