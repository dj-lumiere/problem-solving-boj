from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import comb, cos, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
from heapq import heapify, heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta

getcontext().prec = 1000

from bisect import bisect_left as lower_bound
from bisect import bisect_right as upper_bound


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


def is_inbound(pos_x, pos_y, size_x, size_y):
    return 0 <= pos_x < size_x and 0 <= pos_y < size_y


# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens) if tokens else ""
    print = lambda *args, sep="\n", end="": write(1, (sep.join(map(str, args)) + end).encode())
    eprint = lambda *args, sep=" ", end="\n": write(2, (sep.join(map(str, args)) + end).encode())
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    DELTA = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    DELTA2 = [(0, 1), (0, -1), (1, 0), (1, -1)]
    for hh in range(t):
        n = int(input())
        grid = [[int(input()) for _ in range(n)] for _ in range(n)]
        min_diff = INF
        for x, y, d1, d2 in product(range(1, n + 1), repeat=4):
            current_zone = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
            person_count = [0 for _ in range(5)]
            if not (d1 >= 1 and d2 >= 1 and 1 <= x < x + d1 + d2 <= n and 1 <= y - d1 < y < y + d2 <= n):
                continue
            queue = deque()
            for i in range(d1 + 1):
                nx, ny = x + i, y - i
                if not is_inbound(ny - 1, nx - 1, n, n):
                    continue
                current_zone[nx][ny] = 4
            for i in range(d2 + 1):
                nx, ny = x + i, y + i
                if not is_inbound(ny - 1, nx - 1, n, n):
                    continue
                current_zone[nx][ny] = 4
            for i in range(d2 + 1):
                nx, ny = x + d1 + i, y - d1 + i
                if not is_inbound(ny - 1, nx - 1, n, n):
                    continue
                current_zone[nx][ny] = 4
            for i in range(d1 + 1):
                nx, ny = x + d2 + i, y + d2 - i
                if not is_inbound(ny - 1, nx - 1, n, n):
                    continue
                current_zone[nx][ny] = 4
            for r in range(1, x+d1):
                for c in range(1, y+1):
                    if current_zone[r][c] == 4:
                        break
                    current_zone[r][c] = 0
            for r in range(1, x + d2 + 1):
                for c in reversed(range(y + 1, n + 1)):
                    if current_zone[r][c] == 4:
                        break
                    current_zone[r][c] = 1
            for r in range(x + d1, n + 1):
                for c in range(1, y - d1 + d2):
                    if current_zone[r][c] == 4:
                        break
                    current_zone[r][c] = 2
            for r in range(x + d2 + 1, n + 1):
                for c in reversed(range(y - d1 + d2, n + 1)):
                    if current_zone[r][c] == 4:
                        break
                    current_zone[r][c] = 3
            for r, c in product(range(1, n + 1), repeat=2):
                if current_zone[r][c] == -1:
                    current_zone[r][c] = 4
            for r, c in product(range(1, n + 1), repeat=2):
                person_count[current_zone[r][c]-1] += grid[r-1][c-1]
            min_diff = min(min_diff, max(person_count)-min(person_count))
        answer = f"{min_diff}"
        answers.append(answer)
    print(*answers)