from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit, stdout, stderr
from random import randint, shuffle
from collections import deque, Counter
from math import log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop, heapify
from itertools import combinations, pairwise, permutations, combinations_with_replacement, product, zip_longest, chain, groupby
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

getcontext().prec = 1000


class SegmentTree:
    def __init__(self, member: list[int], default=0, identity=0, index_start=0):
        self.size = len(member)
        self.default = default
        self.identity = identity
        self.log_size = ceil(log2(self.size))
        self.tree_capacity = 1 << self.log_size
        self.index_start = index_start
        self.tree = [self.default] * (2 * self.tree_capacity)
        self.lazy = [self.identity] * (2 * self.tree_capacity)
        self.lazy_multiplier = [0] * (2 * self.tree_capacity)
        self.index_offset = self.tree_capacity - self.index_start
        self.build_tree(member)

    def __str__(self, level: int = 0, pos: int = 1) -> str:
        indent: str = "    " * level
        left_string: str = (
            f"    {indent}L{level + 1}={self.__str__(level=level + 1, pos=2 * pos)}" if 2 * pos < len(self.tree) else "")
        right_string: str = (
            f"    {indent}R{level + 1}={self.__str__(level=level + 1, pos=2 * pos + 1)}" if 2 * pos + 1 < len(self.tree) else "")
        if level == 0:
            return f"root={self.tree[pos]} ({self.lazy[pos]})\n{left_string}\n{right_string}"
        elif level == self.log_size:
            return f"{self.tree[pos]} ({self.lazy[pos]})"
        else:
            return f"{self.tree[pos]} ({self.lazy[pos]})\n{left_string}\n{right_string}"

    def build_tree(self, member: list[int]):
        for i, v in enumerate(member, start=self.tree_capacity):
            self.tree[i] = v
            self.lazy_multiplier[i] = 1
        for i in range(self.tree_capacity - 1, 0, -1):
            self.pull(i)

    def point_update(self, index, value):
        index += self.index_offset
        for level in range(self.log_size, 0, -1):
            self.push(index >> level)
        self.apply_update(index, value)
        for level in range(1, self.log_size + 1):
            self.pull(index >> level)

    def range_update(self, left, right, value):
        left += self.index_offset
        right += self.index_offset
        for level in range(self.log_size, 0, -1):
            if ((left >> level) << level) != left:
                self.push(left >> level)
            if (((right + 1) >> level) << level) != right + 1:
                self.push(right >> level)
        L, R = left, right
        while L <= R:
            if L % 2 == 1:
                self.apply_update(L, value)
                L += 1
            if R % 2 == 0:
                self.apply_update(R, value)
                R -= 1
            L >>= 1
            R >>= 1
        for level in range(1, self.log_size + 1):
            if ((left >> level) << level) != left:
                self.pull(left >> level)
            if (((right + 1) >> level) << level) != right + 1:
                self.pull(right >> level)

    def point_query(self, index):
        index += self.index_offset
        for level in range(self.log_size, 0, -1):
            self.push(index >> level)
        return self.tree[index]

    def range_query(self, left, right):
        left_result = self.default
        right_result = self.default
        left += self.index_offset
        right += self.index_offset
        for level in range(self.log_size, 0, -1):
            if ((left >> level) << level) != left:
                self.push(left >> level)
            if (((right + 1) >> level) << level) != right + 1:
                self.push(right >> level)
        while left <= right:
            if left % 2 == 1:
                left_result = self.merge_nodes(left_result, self.tree[left])
                left += 1
            if right % 2 == 0:
                right_result = self.merge_nodes(self.tree[right], right_result)
                right -= 1
            left >>= 1
            right >>= 1
        return self.merge_nodes(left_result, right_result)

    def apply_update(self, index, value):
        self.tree[index] = self.update_node(value, self.tree[index], self.lazy_multiplier[index])
        if index < self.tree_capacity:
            self.lazy[index] = self.compose_lazies(value, self.lazy[index])

    def push(self, index):
        self.apply_update(2 * index, self.lazy[index])
        self.apply_update(2 * index + 1, self.lazy[index])
        self.lazy[index] = self.identity

    def pull(self, index):
        self.tree[index] = self.merge_nodes(self.tree[2 * index], self.tree[2 * index + 1])
        self.lazy_multiplier[index] = (self.lazy_multiplier[2 * index] + self.lazy_multiplier[2 * index + 1])

    def merge_nodes(self, left, right):
        # Change this part for various operations
        return left + right

    def update_node(self, lazy_value, node_value, lazy_multiplier):
        # Change this part for various operations
        return node_value + lazy_value * lazy_multiplier

    def compose_lazies(self, lazy_value1, lazy_value2):
        # Change this part for various operations
        return lazy_value1 + lazy_value2


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 998244353
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        occupied_seats = SegmentTree(member=[0] * 1000002)
        for _ in range(n):
            s, e = int(input()), int(input())
            occupied_seats.range_update(s, e, 1)
        q = int(input())
        for _ in range(q):
            x = int(input())
            answer = occupied_seats.point_query(x)
            answers.append(f"{answer}")
print(*answers, sep="\n")