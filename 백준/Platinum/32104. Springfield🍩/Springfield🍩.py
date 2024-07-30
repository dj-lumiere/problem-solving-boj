import __pypy__
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

getcontext().prec = 1000

from bisect import bisect_left as lower_bound
from bisect import bisect_right as upper_bound

"""from https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/SortedList.py"""


class FenwickTree:
    def __init__(self, x):
        bit = self.bit = list(x)
        size = self.size = len(bit)
        for i in range(size):
            j = i | (i + 1)
            if j < size:
                bit[j] += bit[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < self.size:
            self.bit[idx] += x
            idx |= idx + 1

    def __call__(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def find_kth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(self.size.bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < self.size and self.bit[right_idx] <= k:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1, k


class SortedList:
    block_size = 700

    def __init__(self, iterable=()):
        self.macro = []
        self.micros = [[]]
        self.micro_size = [0]
        self.fenwick = FenwickTree([0])
        self.size = 0
        for item in iterable:
            self.insert(item)

    def insert(self, x):
        i = lower_bound(self.macro, x)
        j = upper_bound(self.micros[i], x)
        self.micros[i].insert(j, x)
        self.size += 1
        self.micro_size[i] += 1
        self.fenwick.update(i, 1)
        if len(self.micros[i]) >= self.block_size:
            self.micros[i:i + 1] = self.micros[i][:self.block_size >> 1], self.micros[i][self.block_size >> 1:]
            self.micro_size[i:i + 1] = self.block_size >> 1, self.block_size >> 1
            self.fenwick = FenwickTree(self.micro_size)
            self.macro.insert(i, self.micros[i + 1][0])

    def pop(self, k=-1):
        i, j = self._find_kth(k)
        self.size -= 1
        self.micro_size[i] -= 1
        self.fenwick.update(i, -1)
        return self.micros[i].pop(j)

    def __getitem__(self, k):
        i, j = self._find_kth(k)
        return self.micros[i][j]

    def count(self, x):
        return self.upper_bound(x) - self.lower_bound(x)

    def __contains__(self, x):
        return self.count(x) > 0

    def lower_bound(self, x):
        i = lower_bound(self.macro, x)
        return self.fenwick(i) + lower_bound(self.micros[i], x)

    def upper_bound(self, x):
        i = upper_bound(self.macro, x)
        return self.fenwick(i) + upper_bound(self.micros[i], x)

    def _find_kth(self, k):
        return self.fenwick.find_kth(k + self.size if k < 0 else k)

    def __len__(self):
        return self.size

    def __iter__(self):
        return (x for micro in self.micros for x in micro)

    def __repr__(self):
        return str(list(self))


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
        q = int(input())
        answers = __pypy__.newlist_hint(q)
        dough_flavors = [SortedList() for _ in range(n + 1)]
        dough_flavor_count = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            a, b = int(input()), int(input()) + 1
            dough_flavors[i].insert((a, b))
            dough_flavor_count[i] = b - a
        for _ in range(q):
            i = int(input())
            if i == 1:
                j, k = int(input()), int(input())
                this, other = dough_flavors[j], dough_flavors[k]
                this_idx, other_idx = j, k
                should_be_swapped = False
                if len(this) < len(other):
                    this, other = dough_flavors[k], dough_flavors[j]
                    this_idx, other_idx = k, j
                    should_be_swapped = True
                for a, b in other:
                    x = this.lower_bound((a, -INF))
                    if x > 0 and this[x - 1][1] >= a:
                        x -= 1
                    while 0 <= x < len(this) and this[x][0] <= b:
                        dough_flavor_count[this_idx] -= this[x][1] - this[x][0]
                        a = min(a, this[x][0])
                        b = max(b, this[x][1])
                        this.pop(x)
                    this.insert((a, b))
                    dough_flavor_count[this_idx] += b - a
                other = SortedList()
                dough_flavor_count[other_idx] = 0
                if should_be_swapped:
                    dough_flavors[j], dough_flavors[k] = dough_flavors[k], dough_flavors[j]
                    dough_flavor_count[j], dough_flavor_count[k] = dough_flavor_count[k], dough_flavor_count[j]
            if i == 2:
                a = int(input())
                answers.append(dough_flavor_count[a])
    print(*answers)
