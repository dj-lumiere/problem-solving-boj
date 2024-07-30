from bisect import bisect_left
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import comb, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

getcontext().prec = 1000


class SegmentTree:
    """This class is for faster range queries and updates on a list.
    This class gets a list called "members" and does the tree building process in a seperate array called "tree".
    Then, it does the query and update in fittingly named function called "query" and "updates", respectively.
    Keep in mind that when calling "query" and "update", the index uses "ZERO BASED NUMBERING" system.
    """

    def __init__(self, members: list[int]):
        # 어차피 필요한 멤버 갯수 빼고는 0으로 패딩 예정이라 깔끔하게 2의 승수가 될 수 있게 설정함
        self.member_count = len(members)
        self.tree_max_level = ceil(log2(self.member_count))
        self.tree_capacity = 1 << self.tree_max_level
        self.tree = [0 for _ in range(self.tree_capacity << 1)]
        self.build(members)

    def build(self, members: list[int]):
        for index, member in enumerate(members):
            self.tree[self.tree_capacity + index] = member
        for i in range(self.tree_capacity - 1, 0, -1):
            self.tree[i] = self.tree[2 * i + 0] + self.tree[2 * i + 1]

    def update(self, index: int, value: int):
        next_index = self.tree_capacity + index - 1
        self.tree[next_index] = value
        next_index >>= 1
        while next_index:
            self.tree[next_index] = (self.tree[next_index * 2 + 0] + self.tree[next_index * 2 + 1])
            next_index >>= 1

    def query(self, index_start: int, index_end: int) -> int:
        index_start += self.tree_capacity - 1
        index_end += self.tree_capacity - 1
        result: int = 0
        while index_start <= index_end:
            if index_start % 2 == 1:
                result += self.tree[index_start]
                index_start += 1
            if index_end % 2 == 0:
                result += self.tree[index_end]
                index_end -= 1
            index_start >>= 1
            index_end >>= 1
        return result

    def __str__(self) -> str:
        return str(self.tree[self.tree_capacity:])

    def __repr__(self) -> str:
        dfs_stack: list[tuple[int, int]] = [(0, 1)]
        result: list[str] = []
        while dfs_stack:
            level, pos = dfs_stack.pop()
            if pos >= self.tree_capacity * 2:
                continue
            indent: str = "    " * level
            if level == self.tree_max_level:
                member_index: int = pos - self.tree_capacity
                result.append(f"{indent}member{member_index + 1}[index={pos}]={self.tree[pos]}")
            elif level == 0:
                result.append(f"root[index={pos}]={self.tree[pos]}")
            else:
                if not pos % 2:
                    result.append(f"{indent}L{level}[index={pos}]={self.tree[pos]}")
                else:
                    result.append(f"{indent}R{level}[index={pos}]={self.tree[pos]}")
            dfs_stack.append((level + 1, 2 * pos + 1))
            dfs_stack.append((level + 1, 2 * pos))
        return "\n".join(result)


# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(0)]
    for hh in range(t):
        n = int(input())
        m = int(input())
        s = list(map(lambda x: ord(x) - ord("A"), input().decode()))
        alphabet_difference = [0] + [s[0]] + [(j - i) % 26 for i, j in zip(s, s[1:])] + [0]
        alphabet_set = SegmentTree(list(map(lambda x: int(bool(x)), alphabet_difference[1:-1])))
        answer_sub = []
        for _ in range(m):
            q = int(input())
            if q == 1:
                l, r = int(input()), int(input())
                result = alphabet_set.query(l, r)
                if alphabet_set.query(l, l) == 0:
                    result += 1
                answer_sub.append(result)
            if q == 2:
                l, r = int(input()), int(input())
                alphabet_difference[l] += 1
                alphabet_difference[r + 1] -= 1
                alphabet_difference[l] %= 26
                alphabet_difference[r + 1] %= 26
                if 1 <= l <= n and alphabet_difference[l] == 0:
                    alphabet_set.update(l, 0)
                elif 1 <= l <= n and alphabet_difference[l] != 0:
                    alphabet_set.update(l, 1)
                if 1 <= r + 1 <= n and alphabet_difference[r + 1] == 0:
                    alphabet_set.update(r + 1, 0)
                elif 1 <= r + 1 <= n and alphabet_difference[r + 1] != 0:
                    alphabet_set.update(r + 1, 1)
        answer = "\n".join(map(str, answer_sub))
        answers.append(f"{answer}")
    print(answers)