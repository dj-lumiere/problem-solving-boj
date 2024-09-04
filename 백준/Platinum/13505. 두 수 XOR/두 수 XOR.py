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


class BitArray:
    def __init__(self, bits):
        self.size = bits
        self.array = bytearray((bits + 7) // 8)

    def __len__(self):
        return self.size

    def _check_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('Index out of range')

    def set(self, index):
        self._check_index(index)
        byte_index = index // 8
        bit_index = index % 8
        self.array[byte_index] |= (1 << bit_index)

    def clear(self, index):
        self._check_index(index)
        byte_index = index // 8
        bit_index = index % 8
        self.array[byte_index] &= ~(1 << bit_index)

    def get(self, index):
        self._check_index(index)
        byte_index = index // 8
        bit_index = index % 8
        return (self.array[byte_index] >> bit_index) & 1

    def __getitem__(self, index):
        return self.get(index)

    def __setitem__(self, index, value):
        self._check_index(index)
        if value:
            self.set(index)
        else:
            self.clear(index)

    def __iter__(self):
        for i in range(self.size):
            yield self[i]

    def __eq__(self, other):
        if isinstance(other, BitArray):
            return self.array == other.array
        raise TypeError(f'Cannot compare BitArray objects to {type(other)}')

    def __hash__(self):
        return hash(sum([v << i for i, v in enumerate(reversed(self))]))

    def __str__(self):
        return str(sum([v << i for i, v in enumerate(reversed(self))]))

    def __repr__(self):
        return str(sum([v << i for i, v in enumerate(reversed(self))])) + " (" + "".join(map(str, map(int, self))) + ")"


class Trie:
    """https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/Trie.py"""

    def __init__(self, *words):
        self.root = {"_": 0}
        for word in words:
            self.add(word)

    def add(self, word):
        current = self.root
        self.root["_"] += 1
        for letter in word:
            if letter not in current:
                current[letter] = {"_": 0}
            current[letter]["_"] += 1
            current = current[letter]

    def __contains__(self, word):
        current_dict = self.root
        for letter in reversed(word):
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        return "_" in current_dict


    def prefix_count(self, word):
        current_dict = self.root
        for letter in word:
            if letter not in current_dict:
                return 0
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


def int_to_bitarray(number, size=0):
    bitarray = BitArray(max(size, number.bit_length()))
    for i in range(max(size, number.bit_length()), -1, -1):
        if number & (1 << i) != 0:
            bitarray.set(max(size, number.bit_length()) - 1 - i)
    return bitarray


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
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        numbers = [int(input()) for _ in range(n)]
        MAX_SIZE = 30
        trie = Trie(*map(lambda x: int_to_bitarray(x, size=MAX_SIZE), numbers))
        number_counter = Counter(numbers)
        answer = 0
        for x in numbers:
            try_to_find = int_to_bitarray(x, size=MAX_SIZE)
            for i, v in enumerate(try_to_find):
                try_to_find[i] = (False if v else True)
            result = BitArray(bits=MAX_SIZE)
            current_root = trie.root
            for i, v in enumerate(try_to_find):
                result_sub = 0
                if v not in current_root or not current_root[v]:
                    result_sub = (0 if v else 1)
                else:
                    result_sub = v
                result[i] = result_sub
                current_root = current_root[result_sub]
            answer = max(answer, x ^ int(str(result)))
        answers.append(f"{answer}")
print(*answers, sep="\n")
